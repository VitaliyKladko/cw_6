from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)    # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'me']:
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        author = self.request.user.id
        serializer.save(author_id=author)

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs.get("ad_pk"))

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
