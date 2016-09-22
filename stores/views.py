from django.shortcuts import render



from .models import Store

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})

from django.http import Http404

def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'stores/store_detail.html', {'store': store})

from django.forms.models import modelform_factory
from django.shortcuts import redirect, render

def store_create(request):
    StoreForm = modelform_factory(Store, fields=('name', 'notes',))
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm()
    return render(request, 'stores/store_create.html', {'form': form})

def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    StoreForm = modelform_factory(Store, fields=('name', 'notes'))
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store)
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })