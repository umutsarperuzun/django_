from django.urls import path
from . import views # Import the views module from the current package

urlpatterns = [
    path("",views.index,name="index" ),
    path("<int:num1>/" , views.course_number_view,name="course_number_view"),
    path("<str:item>/",views.course,name="course"),
    path("<int:x>/<int:y>/",views.multiply,name="multiply"),
    

]
