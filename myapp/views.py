
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Group
from .serializers import GroupSerializer
from django.http.response import HttpResponseRedirect

@api_view(['GET'])
def get_groups(request):
    groups=Group.objects.all()
    ser=GroupSerializer(groups,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)




