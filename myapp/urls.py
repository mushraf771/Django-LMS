from django.urls import path,include
from myapp import views
from .views import SignupView, UserProfileView,PasswordResetView , PasswordResetSendEmailView, UserChangePassword, LoginView
from rest_framework import urls
urlpatterns = [
   path('', views.base,name='base'),
   path('signup/', views.SignUp.as_view(), name='signup'),
   # path('signup/', SignupView.as_view(), name='signup'),
   # path('loginuser/', LoginView.as_view(), name='login'),
   # path('profile/', UserProfileView().as_view(), name='profile'),
   # path('changepassword/', UserChangePassword.as_view(), name='changepassword'),
   # path('password-reset/<uid>/<token>/', PasswordResetView().as_view(), name='passwordreset'),
   # path('password-reset-email/', PasswordResetSendEmailView.as_view(),
   #       name='password-reset-email'),
   # path('api-auth/', include('rest_framework.urls'))
]
 