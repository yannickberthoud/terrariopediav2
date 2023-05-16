from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

from sorl.thumbnail import ImageField

class Prey(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Proie"
        verbose_name_plural = "Proies"

class Biotop(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Biotope"
        verbose_name_plural = "Biotopes"

class LifeCommunity(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Vie en communauté"
        verbose_name_plural = "Vies en communauté"

class Card(models.Model):
    BITE_DANGEROSITY_CHOICES = (
        ('I', 'Inofensif'),
        ('P', 'Pouvant entraîner des dommages'),
        ('D', 'Dangereux'),
        ('E', 'Extrêmement dangereux')
    )
    DIFFICULTY_LEVEL_CHOICE = (
        ('N', 'Pour éleveur débutant (premières espèces)'),
        ('B', 'Pour éleveur ayant déjà une base'),
        ('E', 'Pour éleveur expérimenté'),
        ('X', 'Pour éleveur très expérimenté')
    )
    MORES_CHOICES = (
        ('F', 'Fouisseur'),
        ('T', 'Terrestre'),
        ('A', '(Semi-)Arboricole')
    )
    ACTIVITY_PERIOD_CHOICES = (
        ('N', 'Nocturne'),
        ('D', 'Diurne'),
        ('A', 'Aube/Crépusculaire')
    )
    BEHAVIOR_CHOICES = (
        ('P', 'Placide'),
        ('F', 'Fuyard'),
        ('D', 'Démonstratif'),
        ('I', 'Irascible')
    )
    genus = models.CharField(max_length=64, verbose_name="Genre", help_text="Exemple: Thamnophis")
    species = models.CharField(max_length=128, verbose_name="Espèce (sous-espèce)", help_text="Exemple : sirtalis similis")
    is_cites = models.BooleanField()
    bern_convention_annex = models.PositiveSmallIntegerField(blank=True, null=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne")
    juvenil_size = models.CharField(max_length=32, verbose_name="Taille des juvéniles", help_text="Exemple: 80 - 90 cm")
    adult_size = models.CharField(max_length=32, verbose_name="Taille des adultes", help_text="Exemple: 80 - 90 cm")
    life_expectancy = models.CharField(max_length=100, verbose_name="Espérance de vie", help_text="Exemple: 15 - 20 ans", default=15)
    main_mores = models.CharField(max_length=1, verbose_name="Moeurs principale", choices=MORES_CHOICES)
    activity_period = models.CharField(max_length=1, verbose_name="Période d'activité principale", choices=ACTIVITY_PERIOD_CHOICES)
    preys = models.ManyToManyField(Prey, verbose_name="Proies")
    main_behavior = models.CharField(max_length=1, verbose_name="Tempérament", choices=BEHAVIOR_CHOICES)
    distribution = models.CharField(max_length=1024)
    biotops = models.ManyToManyField(Biotop, verbose_name="Biotopes")
    vivarium_size = models.CharField(max_length=128, verbose_name="Taille du terrarium", help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5")
    slug = models.SlugField(unique=True)
    more_informations = models.TextField(verbose_name="Informations complémentaires", help_text="Informations complémentaires importantes")
    bite_dangerosity = models.CharField(max_length=1, verbose_name="Dangerosité de la morsure",
                                        choices=BITE_DANGEROSITY_CHOICES)
    difficulty_care = models.CharField(max_length=1, verbose_name="Difficulté de maintien",
                                       choices=DIFFICULTY_LEVEL_CHOICE)
    day_temperature = models.CharField(max_length=64, verbose_name="Température de jour", help_text="format : 18°C - 22°C")
    night_temperature = models.CharField(max_length=64, verbose_name="Température de nuit",
                                       help_text="format : 18°C - 22°C")
    humidity = models.CharField(max_length=64, verbose_name="humidité", help_text="format: 50% - 80%")
    life_community = models.ManyToManyField(LifeCommunity, verbose_name='Peut vivre en communauté')
    last_update = models.DateField(auto_now=True)
    last_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name = "Fiche d'élevage"
        verbose_name_plural = "Fiches d'élevage"

class Venom(models.Model):
    name = models.CharField(max_length=64)
    effects = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Venin"
        verbose_name_plural = "Venins"

class VenomousCard(Card):
    TOXICITY_LEVEL_CHOICES = (
        ('N', 'Non venimeux'),
        ('F', 'Faible toxicité'),
        ('A', 'Nécessite une surveillance active'),
        ('H', 'Hospitalisation immédiate recommandée'),
        ('I', 'Hospitalisation immédiate (risque de décès)')
    )
    toxicity_level = models.CharField(max_length=1, blank=True, verbose_name="Niveau de toxicité",
                                      choices=TOXICITY_LEVEL_CHOICES)
    venoms = models.ManyToManyField(Venom, verbose_name="Venins")

    class Meta:
        abstract = True

def snake_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "medias/uploads/snake/{0}/{1}/{2}".format(instance.genus, instance.species, filename)

class Snake(VenomousCard):
    image = ImageField(upload_to=snake_directory_path)

    class Meta:
        verbose_name = "Serpent"
        verbose_name_plural = "Serpents"

    def get_absolute_url(self):
        return reverse("snake_detail", kwargs={"slug": self.slug})

    def get_scientific_name(self):
        return f"{self.genus} {self.species}"

    def __str__(self):
        return self.get_scientific_name()

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

def arthropod_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "medias/uploads/arthropod/{0}/{1}/{2}".format(instance.genus, instance.species, filename)

class Arthropod(VenomousCard):
    image = ImageField(upload_to=arthropod_directory_path)

    class Meta:
        verbose_name = "Arthropode"
        verbose_name_plural = "Arthropodes"

    def get_absolute_url(self):
        return reverse("snake_detail", kwargs={"slug": self.slug})

    def get_scientific_name(self):
        return f"{self.genus} {self.species}"

    def __str__(self):
        return self.get_scientific_name()

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)


def amphibian_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "medias/uploads/amphibian/{0}/{1}/{2}".format(instance.genus, instance.species, filename)


class Amphibian(Card):
    VOLUME_CALL_CHOICES = (
        ('A', 'Aphone'),
        ('D', 'Discret'),
        ('B', 'Bruyant')
    )
    image_egg = ImageField(upload_to=amphibian_directory_path, blank=True, verbose_name="Image d'une ponte")
    image_larve = ImageField(upload_to=amphibian_directory_path, blank=True, verbose_name="Image des larves")
    image = ImageField(upload_to=amphibian_directory_path, verbose_name="Image des adultes")
    volume_call = models.CharField(max_length=1, help_text="Volume sonnor du chant", choices=VOLUME_CALL_CHOICES)

    class Meta:
        verbose_name = "Amphibien"
        verbose_name_plural = "Amphibiens"

    def get_absolute_url(self):
        return reverse("amphibian_detail", kwargs={"slug": self.slug})

    def get_scientific_name(self):
        return f"{self.genus} {self.species}"

    def __str__(self):
        return self.get_scientific_name()

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)


def lizard_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "medias/uploads/lizard/{0}/{1}/{2}".format(instance.genus, instance.species, filename)


class Lizard(Card):
    image = ImageField(upload_to=lizard_directory_path, verbose_name="Image des adultes")

    class Meta:
        verbose_name = "Lézard"
        verbose_name_plural = "Lézards"

    def get_absolute_url(self):
        return reverse("lizard_detail", kwargs={"slug": self.slug})

    def get_scientific_name(self):
        return f"{self.genus} {self.species}"

    def __str__(self):
        return self.get_scientific_name()

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)

def turtle_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "medias/uploads/turtle/{0}/{1}/{2}".format(instance.genus, instance.species, filename)

class Turtle(Card):
    CATEGORIES = (
        ('A', 'Eau douce'),
        ('S', 'Eau saumâtre'),
        ('M', 'Eau marine'),
        ('T', 'Terrestre')
    )
    type_of_turtle = models.CharField(max_length=1, verbose_name="Type d'activité", choices=CATEGORIES)
    image = ImageField(upload_to=turtle_directory_path, verbose_name="Image des adultes")

    class Meta:
        verbose_name = "Tortue"
        verbose_name_plural = "Tortues"

    def get_absolute_url(self):
        return reverse("turtle_detail", kwargs={"slug": self.slug})

    def get_scientific_name(self):
        return f"{self.genus} {self.species}"

    def __str__(self):
        return self.get_scientific_name()

    def save(self, *args, **kwargs):
        self.genus = self.genus.capitalize()
        self.species = self.species.lower()
        if not self.slug:
            _slug = self.get_scientific_name()
            self.slug = slugify(_slug)
        return super().save(*args, **kwargs)