from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from interview import views

router = DefaultRouter()
router.register('categories', views.CategoryApiView)


schema_view = get_schema_view(
    openapi.Info(
        title="Crib for exams",
        default_version='v-0.01-alpha',
        description="API для со шпаргалками",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ulanoviman3@gmail.com"),
        license=openapi.License(name="No Licence"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/questions/', views.QuestionAnswerApiView.as_view({
        'get': 'list',
        'post': 'create'})),
    path('api/questions/<int:pk>/', views.QuestionAnswerDetailApiView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'})),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),
]
