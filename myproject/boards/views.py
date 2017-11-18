from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
# Create your views here.
from .models import Board
#import models

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})