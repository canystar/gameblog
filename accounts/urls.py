from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='accounts'
urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
    path('loginpage/',
         auth_views.LoginView.as_view(template_name='loginpage.html'),
         name='loginpage'
         ),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'
         ),
]
