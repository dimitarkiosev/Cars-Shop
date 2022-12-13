from django.contrib.auth.decorators import login_required
from django.urls import path, include
from cars.accounts.views import SignInView, SignUpView, SignOutView, \
    AccountDetailsView, AccountEditView, AccountDeleteView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', AccountDetailsView.as_view(), name='details user'),
        path('edit/', login_required(AccountEditView.as_view()), name='edit user'),
        path('delete/', login_required(AccountDeleteView.as_view()), name='delete user'),
    ])),
)

from .signals import *