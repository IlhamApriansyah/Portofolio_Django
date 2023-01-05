from django.shortcuts import render
from blog.models import Postingan, Komentar

def blog_index(request):
    Postingan = Postingan.objects.all().order_by('dibuat')
    konteks = {
        'postingan' : Postingan
    }

    return render(request, "blog_index.html", konteks)

def blog_kategori(request, kategori):
    Postingan = Postingan.object.filter(
        categories__nama__contains=kategori
    ).order_by(
        'dibuat'
    )
    konteks = {
        "kategori" : kategori,
        "postingan" : Postingan
    }

    return render(request, "kategori_blog.html", konteks)