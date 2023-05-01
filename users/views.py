from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET'])
def main(request):
    res = {
        'test':True
    }
    return Response(res, status.HTTP_200_OK)