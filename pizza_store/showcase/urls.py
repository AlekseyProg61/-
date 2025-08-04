from django.urls import include, path
from django import views
from . import views


app_name = "showcase"
urlpatterns = [
    path('',views.ShowcaseView.as_view(),name="index")
]
