from django.shortcuts import render, redirect
from .models import URL

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        new_url = URL.objects.create(original_url=long_url)
        return render(request, 'success.html', {'short_url': new_url.code})
    return render(request, 'shorten.html')

def redirect_url(request, code):
    url_obj = URL.objects.get(code=code)
    return redirect(url_obj.original_url)
