from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
# Create your views here.

#for main splsh page
def index(request):
    return render(request, 'game/index.html')

#to get name of user
def get_name(request):
    return render(request, 'game/name.html')

#for first question
def que_one(request):
    name = request.POST.get('name')
    return render(request, 'game/question_one.html',{'name':name})

#for second question
def que_two(request):
    name = request.POST.get('name')
    ans_que_one = request.POST.get('que1')
    return render(request, 'game/question_two.html',{'name':name, 'ans_que_one':ans_que_one})

#for saveing an data and show summary
def summary(request):
    name = request.POST.get('name')
    ans_que_one = request.POST.get('ans_que_one')
    ans_que_two = request.POST.getlist('que2')
    ans_que_two_str = ','.join(ans_que_two)

    Game.objects.create(
    name = name,
    que_one = ans_que_one,
    que_two = ans_que_two_str,
    )

    return render(request, 'game/summary.html',{'name':name, 'ans_que_one':ans_que_one,'ans_que_two':ans_que_two_str})

#to show history
def history(request):
    obj = Game.objects.all()
    return render(request, 'game/history.html',{'obj':obj})
    