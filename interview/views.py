from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionDetailSerializer


class PostPagePagination(PageNumberPagination):
    page_size = 3


class CategoryApiView(viewsets.ModelViewSet):
    """
        API для создания, получения, изменения и удаления категорий
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerApiView(viewsets.ModelViewSet):
    """
        API для создания, получения вопросов
    """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'question']
    ordering_fields = ['importance', ]
    pagination_class = PostPagePagination


class QuestionAnswerDetailApiView(viewsets.ModelViewSet):
    """
        API для детального просмотра и редактирвания
    """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionDetailSerializer
