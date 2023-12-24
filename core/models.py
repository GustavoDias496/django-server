# models.py

from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

def upload_image(instance, filename):
    return f"{instance.id}_{filename}"

class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'category'

class Finalist(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    votes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'finalist'

class Episodes(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'episodes'

class Services(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=upload_image, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'services'

class Post(models.Model):
    typeRedeSocial = {
        ('insta', 'Instragram'),
        ('face', 'Facebook'),
        ('linkedln', 'Linkedln'),
        ('github', 'Github'),
        ('twitter', 'Twitter')
    }
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    # Titulo do post.
    titulo = models.CharField(max_length=300)
    # Slug será a Url do post.
    slug = models.SlugField(max_length=300, unique=True, auto_created=titulo)
    # Autor do post.

    author = models.CharField(max_length=200)
    iconTypeRedeSocial = models.CharField(
        max_length=10, choices=typeRedeSocial)
    linkRedeSocial = models.CharField(max_length=300)

    imagem_capa = models.CharField(max_length=300)

    resumo = models.CharField(max_length=500)
    # Texto do post
    texto = RichTextField(blank=False)
    # Data de criação do post
    created = models.DateTimeField(auto_now_add=True)
    # Data de atualização do post.
    update = models.DateTimeField(auto_now=True)
    #
    aprovado = models.BooleanField()

    def previewCapa(self):
        return mark_safe('<img src="' + self.imagem_capa + '"height="auto" width="100%">')

    previewCapa.short_description = "Preview da capa:"
    previewCapa.allow_tags = True

    class Meta:
        verbose_name = u'Postagem'
        verbose_name_plural = u'Postagens'
        permissions = (('check_approved', 'Check approved'),)

    def __str__(self):
        return self.titulo