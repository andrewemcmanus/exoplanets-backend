from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
    path('users/', views.get_users, name="users"),
    path('users/<username>/', views.profile, name="profile"),
    path('systems/', views.get_system_list, name='systems'),
    path('submissions/', views.get_submissions, name='submissions'),
    path('submissions/create', views.CreateSubmissions.as_view(), name='create_submissions'),
    path('submissions/<username>/update', views.UpdateSubmissions.as_view(), name='update_submissions'),
    path('submissions/delete/<int:pk>', views.DeleteSubmissions.as_view(), name='delete_submissions')

    # path('database/', views.database, name="database")
]
