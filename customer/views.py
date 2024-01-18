from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions, status
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes



class CreateCustomer(generics.CreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListCustomer(generics.ListAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        currentUser = self.request.user
        return Customer.objects.filter(user=currentUser)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if customer.user_id == request.user.id:
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

        

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if customer.user == request.user:
            customer.delete()
            return Response({'success': 'Customer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
