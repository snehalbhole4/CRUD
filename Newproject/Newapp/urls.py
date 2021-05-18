from django.urls import path
from . import views

urlpatterns = [
    path('rv/', views.retrieve_view),
    path('cv/', views.createview),
    path('update/<id>/', views.update_view,name='update'),
    path('delete/<id>/', views.delete_view,name='delete'),
    path('del/', views.del_view),
    path('upd/', views.update_success),


]

