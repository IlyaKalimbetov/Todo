from rest_framework import viewsets 


from .serializers import  TodoSerializers
from apps.info.models import InfoTodo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = InfoTodo.objects.all()
    serializer_class = TodoSerializers
