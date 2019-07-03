
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import Service



# Create your views here.
def index(request):
   services = Service.objects.all()

   paginator = Paginator(services, 3)
   page = request.GET.get('page')
   paged_services = paginator.get_page(page)
   context = {
      'services': paged_services
   }
   return render(request, 'services/services.html', context)

def singleService(request, service_id):
   service = get_object_or_404(Service, pk=service_id)
   context = {
      'service': service
   }
   return render(request, 'services/singleService.html', context)

def search(request):
    return render(request, 'services/search.html')