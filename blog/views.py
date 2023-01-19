from .forms import FormKomentar
from django.shortcuts import render
from blog.models import Postingan, Komentar

def blog_index(request):
    postingan = Postingan.objects.all().order_by('tgl_buat')
    konteks = {
        'postingan' : postingan
    }

    return render(request, "base.html", konteks)

def kategori_blog(request, kategori):
    Postingan = Postingan.object.filter(
        categories__nama__contains=kategori
    ).order_by(
        'tgl_buat'
    )
    konteks = {
        "kategori" : kategori,
        "Postingan" : Postingan
    }

    return render(request, "kategori_blog.html", konteks)

def detil_blog(request, pk):
    Postingan = Postingan.objects.get(pk=pk)

    form = FormKomentar()
    if request.method == 'POST':
        form = FormKomentar(request.POST)
        if form.is_valid():
            Komentar = Komentar(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                Postingan = Postingan
            )
            Komentar.save()


    Komentar = Komentar.objects.filter(Postingan=Postingan)
    konteks = {
        "Postingan" : Postingan,
        "komentar" : Komentar,
        "form"  : form,
    }

    return render(request, "detil_blog.html", konteks)