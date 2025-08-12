from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ExpenseListView, SignUpView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]