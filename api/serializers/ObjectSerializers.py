from rest_framework import serializers

from api.models import Object


class AllObjectSerializer(serializers.ModelSerializer):
    """Добавление, Изменение и Вывод объектов"""

    class Meta:
        model = Object
        fields = [
            'id',  # идентификация
            'name',  # название
            'quantity',  # кол-во
            'distance',  # расстояние
            'created',  # дата создания
            'updated',  # дата обновления
        ]
