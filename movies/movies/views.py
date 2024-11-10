from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1669,
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'year': 1600,
        },
        {
            'id': 5,
            'title': 'Meg',
            'year': 2000,
        }
        ],

    'books': [
        {
            'id': 1,
            'title': 'book1',
            'year': 1669,
        },
        {
            'id': 2,
            'title': 'book2',
            'year': 1600,
        },
        {
            'id': 3,
            'title': 'book3',
            'year': 2000,
        }
        ]
    }

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")
