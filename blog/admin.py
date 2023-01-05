from django.contrib import admin
from blog.models import Postingan, Kategori

class PostAdmin(admin.ModelAdmin):
    pass

class KategoriAdmin(admin.ModelAdmin):
    pass

admin.site.register(Postingan, PostAdmin)
admin.site.register(Kategori, KategoriAdmin)