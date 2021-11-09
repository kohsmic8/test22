from django.http.response import HttpResponse
from django.shortcuts import render
from .models import 아이디


def 홈페이지(request):
    드실분 = 아이디.objects.all()
    context = {
        "메뉴" : "레몬에이드",
        "가격" : "5200원",
        "손님" : 드실분,
    }
    return render(request, "2step.html", context)

# Create your views here.
