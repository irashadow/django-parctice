from django.shortcuts import render



from .models import Store

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

from django.http import Http404

def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'store_detail.html', {'store': store})