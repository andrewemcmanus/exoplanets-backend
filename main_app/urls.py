from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('', views.index, name="index"),
    path('about/', views.about, name="about")
    path('login/', views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
]
