from django.shortcuts import render
from django.http import HttpResponse

course_dictionary = {
    "python":"Python Course Page",
    "java" : "Java Course Page",
    "kotlin" : "Kotlin Course Page",
    "swift" : "Swift Course Page"
}
def index(request):
    return HttpResponse("This is first Django project,first index")


def course(request,item):
    return HttpResponse(course_dictionary.get(item,"Not found"))
