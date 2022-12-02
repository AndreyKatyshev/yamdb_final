from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class Mixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    pass
