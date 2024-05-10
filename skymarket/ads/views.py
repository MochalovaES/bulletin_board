from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsAdmin, IsOwner
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    """Пагинация для объявлений"""
    page_size = 4
    page_query_param = "page"


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class_class = AdFilter
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        """Создавать и просматривать может любой авторизованный пользователь, а редактировать
        и удалять только владелец или админ"""
        permission_classes = []
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Автоматическое сохранение владельца при создании объекта"""
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получает отзывы для определенного объявления"""
        return self.queryset.filter(ad=self.kwargs['ad_pk'])

    def get_permissions(self):
        """Создавать и просматривать может любой авторизованный пользователь, а редактировать
        и удалять только владелец или админ"""
        permission_classes = []
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Автоматическое сохранение владельца отзыва в определенном объявлении"""
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.ad = Ad.objects.get(pk=self.kwargs['ad_pk'])
        new_comment.save()
