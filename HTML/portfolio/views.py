from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Portfolio

# Create your views here.
def index(request):
   portfolio = Portfolio.objects.all()
   paginator = Paginator(portfolio, 3)
   page = request.GET.get('page')
   paged_portfolio = paginator.get_page(page)
   context = {
      'portfolio': paged_portfolio
   }
   return render(request, 'portfolio/gallery-image.html', context)

def gallery_single(request, portfolio_id):
   portfolio_sig = get_object_or_404(Portfolio, pk=portfolio_id)
   context = {
      'portfolio_sig': portfolio_sig
   }
   return render(request, 'portfolio/gallery_single.html', context)

def search(request):
    return render(request, 'portfolio/search.html')