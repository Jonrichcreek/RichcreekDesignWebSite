from django.shortcuts import render
from django.http import HttpResponse

from portfolio.models import Portfolio
# Create your views here.
def index(request):
    portfolio = Portfolio.objects.order_by('-pub_date').filter(publish=True)[:6]

    context = {
        'portfolio': portfolio
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')