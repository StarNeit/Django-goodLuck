from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Test Project - Good Luck</h1>
    <a href="/goodLuck/">Start!</a><br>    
    """
    return HttpResponse(html)