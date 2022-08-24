from django.shortcuts import render


def index(request):
    """A view to render the welcome page"""
    return render(request, 'welcome/index.html')
