from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
def api(request):
    data= [
        {'users': 'GET'}
    ]
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    data = UserSerializer(users,many=True)
    return Response(data.data)


@api_view(['GET'])
def getUser(request,pk):
    users = User.objects.get(id=pk)
    data = UserSerializer(users,many=False)
    return Response(data.data)