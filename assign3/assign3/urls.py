
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi',views.StudentCrud,basename='student_crud')
router.register('studentapi/<int:pk>/',views.StudentCrud,basename='student_crud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
