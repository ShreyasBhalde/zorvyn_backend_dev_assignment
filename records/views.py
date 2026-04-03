from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import financial_records
from .serializers import RecordSerializer
from users.serializers import register_request_serializer
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema

# CREATE
@swagger_auto_schema(method='post', request_body=RecordSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_record(request):
    if request.user.role != 'admin':
        return Response({'error': 'Not allowed'}, status=403)

    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# LIST
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_records(request):
    # Base queryset (exclude soft deleted)
    records = financial_records.objects.filter(is_deleted=False).order_by('-date')

    filters_applied = []

    #Category filter
    category = request.GET.get('category')
    if category:
        records = records.filter(category__icontains=category)
        filters_applied.append(f"category='{category}'")

    #Date range filter
    start = request.GET.get('start_date')
    end = request.GET.get('end_date')
    if start and end:
        records = records.filter(date__range=[start, end])
        filters_applied.append(f"date between {start} and {end}")

    #Search (category + notes)
    search = request.GET.get('search')
    if search:
        records = records.filter(
            Q(category__icontains=search) |
            Q(notes__icontains=search)
        )
        filters_applied.append(f"search='{search}'")

    #Pagination
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        return Response({"message": "Invalid page number"}, status=400)

    limit = 5
    start_index = (page - 1) * limit
    end_index = start_index + limit

    total_records = records.count()
    paginated_records = records[start_index:end_index]

    serializer = RecordSerializer(paginated_records, many=True)

    # Message
    if filters_applied:
        message = f"Filtered results for: {', '.join(filters_applied)}"
    else:
        message = "All records fetched successfully"

    return Response({
        "message": message,
        "total_records": total_records,
        "page": page,
        "page_size": limit,
        "total_pages": (total_records + limit - 1) // limit,
        "data": serializer.data
    })


# UPDATE
@swagger_auto_schema(method='put', request_body=RecordSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_record(request, pk):
    if request.user.role != 'admin':
        return Response({'error': 'Not allowed'}, status=403)

    try:
        record = financial_records.objects.get(pk=pk)
    except financial_records.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = RecordSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_record(request, pk):
    if request.user.role != 'admin':
        return Response({'error': 'Not allowed'}, status=403)

    record = financial_records.objects.filter(pk=pk).first()
    if not record:
        return Response({'error': 'Not found'}, status=404)

    record.is_deleted = True
    record.save()

    return Response({'message': 'Record soft deleted'})