from django.urls import path
from . import views # Import the views module from the current package

urlpatterns = [
    path("",views.index,name="index" ),
]
