from django.urls import path
from .views import show_index, show_todays_revision, show_all_revisions, update_revision, delete_revision, handle_login, handle_register, handle_logout

urlpatterns = [
    path("", show_index, name="homepage"),
    path("revisions/", show_todays_revision, name="show_todays_revision"),
    path("all-revisions/", show_all_revisions, name="all_revision"),
    path("update/<int:pk>/", update_revision, name="update"),
    path("delete/<int:pk>/", delete_revision, name="delete"),
    path('login/', handle_login, name='login'),
    path('register/', handle_register, name='register'),
    path('logout/', handle_logout, name='logout'),
]