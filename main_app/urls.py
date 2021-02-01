from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"visuals", views.VisualView, 'visuals')
router.register(r"user", views.UserView, 'user')
print(type(router.urls))

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('', views.index, name="index"),
    # path('about/', views.about, name="about"),
    path('login/', views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
    # path('users/', views.get_users, name="users"),
    # path('users/<str:username>/', views.profile, name="profile"),
    # path('systems/', views.get_system_list, name='systems'),
    path('api/', include(router.urls)),
    # path('systems/<str:system_name>', views.get_system, name='get_system'),
    # path('submissions/', views.get_submissions, name='submissions'),
    # path('submissions/create', views.CreateSubmissions.as_view(), name='create_submissions'),
    # path('submissions/<str:username>/update', views.UpdateSubmissions.as_view(), name='update_submissions'),
    # path('submissions/delete/<int:pk>', views.DeleteSubmissions.as_view(), name='delete_submissions')

    # path('database/', views.database, name="database")
]
