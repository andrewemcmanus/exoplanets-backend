from django.urls import path
froom . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view')
    path('signup/', views.signup, name='signup')
]
