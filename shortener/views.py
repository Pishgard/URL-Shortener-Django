from django.shortcuts import render, get_object_or_404, redirect
from .models import Url
from django.contrib import messages


def index(requst):
    if requst.method == 'POST':
        url = requst.POST["url"]
        slug = requst.POST["slug"]

        try:
            Url.objects.get(slug=slug)
            messages.error(requst, 'لینک کوتاه شده نمیتواند تکراری باشد')
            return render(requst, 'index.html')
        except Url.DoesNotExist:
            pass

        new_url = Url(url=url, slug=slug)
        new_url.save()
        messages.success(requst, 'لینک شما ساخته شد.')
        return render(requst, 'index.html')

    return render(requst, 'index.html')


def list(requst):
    list = Url.objects.all()
    return render(requst, 'list.html', {'list': list})


def url_redirect(requst, slug):
    url = get_object_or_404(Url, slug=slug)
    url.visit += 1
    url.save()

    return redirect(url.url)