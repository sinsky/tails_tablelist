from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    return render(request,"index.html")