from django.urls import path
from . import views

app_name='gamelog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('login/',views.LoginView.as_view(),name='login'),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
    path(
        'post/',
        views.CreateGamelogView.as_view(),
        name='post'),
    path(
        'post_done/',
        views.PostSuccessView.as_view(),
        name='post_done'),
    path(
        'content/',
        views.ContentView.as_view(),
        name='content'
    ),
    path('content/<int:Category>',
         views.CategoryView.as_view(),
         name='games_cat'
         ),
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'
         ),
    path('game-detail/<int:pk>',
         views.DetailView.as_view(),
         name='game_detail'),
    path('mypage/',
         views.MypageView.as_view(),
         name='mypage'),
    path('game-detail/<int:pk>/delete',
         views.GameDeleteView.as_view(),
         name='game_delete'),
]
