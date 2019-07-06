from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def PoliciesView(request):
    return Response({'hi': 'hello'}, content_type='application/json', status=200)
