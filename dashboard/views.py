from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from records.models import financial_records


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary(request):

    if request.user.role == 'viewer':
        return Response({'error': 'Not allowed'}, status=403)

    income = financial_records.objects.filter(type='income').aggregate(Sum('amount'))
    expense = financial_records.objects.filter(type='expense').aggregate(Sum('amount'))

    return Response({
        'total_income': income['amount__sum'] or 0,
        'total_expense': expense['amount__sum'] or 0,
        'net_balance': (income['amount__sum'] or 0) - (expense['amount__sum'] or 0)
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_summary(request):
    data = financial_records.objects.values('category').annotate(total=Sum('amount'))
    return Response(data)