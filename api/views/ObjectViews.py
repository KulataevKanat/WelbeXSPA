from rest_framework import generics, filters
from api.models import Object
from api.pagination_settings import ObjectPagination
from api.serializers import ObjectSerializers


class CreateObjectView(generics.CreateAPIView):
    """Добавление объекта"""

    serializer_class = ObjectSerializers.AllObjectSerializer


class DeleteObjectByIdView(generics.DestroyAPIView):
    """Удаление объекта по идентификации"""

    queryset = Object.objects.all()


class UpdateObjectByIdView(generics.CreateAPIView):
    """Обновление объекта по идентификации"""

    queryset = Object.objects.all()
    serializer_class = ObjectSerializers.AllObjectSerializer


class GetObjectView(generics.ListAPIView):
    """Вывод объектов"""

    queryset = Object.objects.all()
    serializer_class = ObjectSerializers.AllObjectSerializer
    pagination_class = ObjectPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'quantity', 'distance']
    page_size = 2


class FindObjectByIdView(generics.RetrieveAPIView):
    """Поиск объекта по идентификации"""

    queryset = Object.objects.all()
    serializer_class = ObjectSerializers.AllObjectSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'quantity', 'distance']
