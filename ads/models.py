from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from sorl.thumbnail import ImageField

def ads_directory_path(instance, filename):
    return 'medias/uploads/images/ads/{0}/{1}'.format(instance.owner.username, filename)

class Ads(models.Model):
    TYPE_OF_ADS = (
        ('R', 'Recherche'),
        ('V', 'Vends')
    )
    CATEGORIES = (
        ('A', 'Amphibiens'),
        ('R', 'Arthropodes'),
        ('L', 'Lézards'),
        ('S', 'Serpents'),
        ('M', 'Matériels et terrarium')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, verbose_name="Catégorie", choices=CATEGORIES)
    type_of_ads = models.CharField(max_length=1, verbose_name='Type d\'annonce', choices=TYPE_OF_ADS)
    image = ImageField(upload_to=ads_directory_path, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Petite annonce de {self.owner} publié le {self.created_at}"

    def get_absolute_url(self):
        return reverse("ads-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Petite annonce'
        verbose_name_plural = 'Petites annonces'