from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.

def newbook(request):
    book1 = Book(name="Huckleberry Finn", pagenumber=22, genre="folklore", publishdate="1989-09-23")
    book1.save()
    return HttpResponse("Book1 saved!")

def getAllBooks(request):
