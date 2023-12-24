from django.contrib import admin
from .models import Category, Finalist, Episodes, Services, Post
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Category)
admin.site.register(Finalist)
admin.site.register(Episodes)
admin.site.register(Services)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("titulo", )
    list_display = ("titulo", "slug", "author", "created", "update")
    list_filter = ("author",)
    fields = ["titulo", "slug", 'imagem_capa', 'previewCapa', "author",
              "linkRedeSocial", "iconTypeRedeSocial", "resumo", "texto", 'aprovado']
    prepopulated_fields = {"slug": ("titulo",)}
    readonly_fields = ('previewCapa',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if list(request.user.get_all_permissions()).count('Aplicativos.check_approved') < 1:
            form.base_fields['aprovado'].disabled = True
            return form
        else:
            return form