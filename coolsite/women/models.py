from django.db import models
from django.urls import reverse

class Women(models.Model):
    title=models.CharField(max_length=255,verbose_name='Ady')
    content=models.TextField(blank=True,verbose_name='Tekst')
    photo=models.ImageField(upload_to="photos/%Y/%m/%d",verbose_name='Surat')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Doran wagty')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Uytgan wagty')
    is_published=models.BooleanField(default=True,verbose_name='Publikasiya')
    cat=models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name='Kategoriya')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id':self.id})

    class Meta:
        verbose_name='Pornstar'
        verbose_name_plural='PornStars'
        ordering=['-time_create','title']

class Category(models.Model):
    name=models.CharField(max_length=100,db_index=True,verbose_name='Ady')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_id':self.id})

    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural='Kategoriyalar'
        ordering=['id']