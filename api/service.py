from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class PartialUpdateService(GenericAPIView):
    """Сервис обновления (patch)"""

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer, *args, **kwargs)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer, *args, **kwargs):
        serializer.save()


class PartialUpdateServiceView(PartialUpdateService):
    """Generic сервис обновления (patch)"""

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)