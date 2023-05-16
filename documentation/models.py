from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.urls import reverse
from django.template.defaultfilters import slugify

def documentation_directory_path(instance, filename):
    return "medias/uploads/documentation/{0}/{1}".format(instance.slug, filename)

class Documentation(models.Model):
    CATEGORIES = (
        ('A', 'Amphibiens'),
        ('R', 'Arthropodes'),
        ('L', 'Lézards'),
        ('S', 'Serpents'),
        ('T', 'Tortues')
    )
    category = models.CharField(max_length=1, choices=CATEGORIES)
    title = models.CharField(max_length=256, verbose_name="Title", help_text="Choisissez un titre pertinent")
    banner = ImageField(upload_to=documentation_directory_path, help_text="Choisissez une image pertinente")
    content = models.TextField()
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True,auto_created=True)
    updated_at = models.DateField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name="last_modifier", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            _slug = self.title
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("documentation-detail", kwargs={"category": str, "slug": self.slug})

    class Meta:
        verbose_name = 'Documentation'
        verbose_name_plural = 'Documentations'