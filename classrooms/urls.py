from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from classes import views
# from api.views import ListAPIView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('classrooms/', views.classroom_list, name='classroom-list'),
#     path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

#     path('classrooms/create', views.classroom_create, name='classroom-create'),
#     path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
#     path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

#     path('list/', ListView.as_view(), name='list'),
#     path('detail/<int:object_id>/', DetailView.as_view(), name='detail'),
#     path('delete/int:object_id>/', DeleteView.as_view(), name='delete'),
#     path('create/', CreateView.as_view(), name='create'),
# ]

# if settings.DEBUG:
# 	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
