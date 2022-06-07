from django import views
from django.urls import path
from .views import IndexView, PostView
from . import views

urlpatterns = [
    path('home/',IndexView.as_view(), name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/',views.logar, name='logar'),
    path('post/',views.cadastrar_post, name='cadastrar_post'),
    # path('post/<int:id>',PostView.as_view(), name='mostrar_post')
    path('post/view/',views.post_view, name='mostrar_post'),
    path('post/view/<id>',views.detail_post),
    path('post/view/<id>/delete',views.delete_post),
    path('post/view/<id>/editar',views.editar_post, name='editar_post'),
    path('user/',views.user_view, name='mostrar_user'),
    path('user/<id>/delete', views.delete_user),
    path('user/<id>', views.detail_user ),
    path('teste', views.test ),
]