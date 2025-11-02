from django.urls import path
from . import views

app_name="library"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>", views.book, name="book"),
    path("student/<str:tup_id>", views.student, name="student")
]