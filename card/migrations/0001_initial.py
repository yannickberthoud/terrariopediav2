# Generated by Django 4.2.1 on 2023-05-16 07:36

import card.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biotop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Biotope',
                'verbose_name_plural': 'Biotopes',
            },
        ),
        migrations.CreateModel(
            name='LifeCommunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Vie en communauté',
                'verbose_name_plural': 'Vies en communauté',
            },
        ),
        migrations.CreateModel(
            name='Prey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Proie',
                'verbose_name_plural': 'Proies',
            },
        ),
        migrations.CreateModel(
            name='Venom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('effects', models.TextField()),
            ],
            options={
                'verbose_name': 'Venin',
                'verbose_name_plural': 'Venins',
            },
        ),
        migrations.CreateModel(
            name='Turtle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(help_text='Exemple: Thamnophis', max_length=64, verbose_name='Genre')),
                ('species', models.CharField(help_text='Exemple : sirtalis similis', max_length=128, verbose_name='Espèce (sous-espèce)')),
                ('is_cites', models.BooleanField()),
                ('bern_convention_annex', models.PositiveSmallIntegerField(blank=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne", null=True)),
                ('juvenil_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des juvéniles')),
                ('adult_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des adultes')),
                ('life_expectancy', models.CharField(default=15, help_text='Exemple: 15 - 20 ans', max_length=100, verbose_name='Espérance de vie')),
                ('main_mores', models.CharField(choices=[('F', 'Fouisseur'), ('T', 'Terrestre'), ('A', '(Semi-)Arboricole')], max_length=1, verbose_name='Moeurs principale')),
                ('activity_period', models.CharField(choices=[('N', 'Nocturne'), ('D', 'Diurne'), ('A', 'Aube/Crépusculaire')], max_length=1, verbose_name="Période d'activité principale")),
                ('main_behavior', models.CharField(choices=[('P', 'Placide'), ('F', 'Fuyard'), ('D', 'Démonstratif'), ('I', 'Irascible')], max_length=1, verbose_name='Tempérament')),
                ('distribution', models.CharField(max_length=1024)),
                ('vivarium_size', models.CharField(help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5", max_length=128, verbose_name='Taille du terrarium')),
                ('slug', models.SlugField(unique=True)),
                ('more_informations', models.TextField(help_text='Informations complémentaires importantes', verbose_name='Informations complémentaires')),
                ('bite_dangerosity', models.CharField(choices=[('I', 'Inofensif'), ('P', 'Pouvant entraîner des dommages'), ('D', 'Dangereux'), ('E', 'Extrêmement dangereux')], max_length=1, verbose_name='Dangerosité de la morsure')),
                ('difficulty_care', models.CharField(choices=[('N', 'Pour éleveur débutant (premières espèces)'), ('B', 'Pour éleveur ayant déjà une base'), ('E', 'Pour éleveur expérimenté'), ('X', 'Pour éleveur très expérimenté')], max_length=1, verbose_name='Difficulté de maintien')),
                ('day_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de jour')),
                ('night_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de nuit')),
                ('humidity', models.CharField(help_text='format: 50% - 80%', max_length=64, verbose_name='humidité')),
                ('last_update', models.DateField(auto_now=True)),
                ('type_of_turtle', models.CharField(choices=[('A', 'Eau douce'), ('S', 'Eau saumâtre'), ('M', 'Eau marine'), ('T', 'Terrestre')], max_length=1, verbose_name="Type d'activité")),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=card.models.turtle_directory_path, verbose_name='Image des adultes')),
                ('biotops', models.ManyToManyField(to='card.biotop', verbose_name='Biotopes')),
                ('last_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('life_community', models.ManyToManyField(to='card.lifecommunity', verbose_name='Peut vivre en communauté')),
                ('preys', models.ManyToManyField(to='card.prey', verbose_name='Proies')),
            ],
            options={
                'verbose_name': 'Tortue',
                'verbose_name_plural': 'Tortues',
            },
        ),
        migrations.CreateModel(
            name='Snake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(help_text='Exemple: Thamnophis', max_length=64, verbose_name='Genre')),
                ('species', models.CharField(help_text='Exemple : sirtalis similis', max_length=128, verbose_name='Espèce (sous-espèce)')),
                ('is_cites', models.BooleanField()),
                ('bern_convention_annex', models.PositiveSmallIntegerField(blank=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne", null=True)),
                ('juvenil_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des juvéniles')),
                ('adult_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des adultes')),
                ('life_expectancy', models.CharField(default=15, help_text='Exemple: 15 - 20 ans', max_length=100, verbose_name='Espérance de vie')),
                ('main_mores', models.CharField(choices=[('F', 'Fouisseur'), ('T', 'Terrestre'), ('A', '(Semi-)Arboricole')], max_length=1, verbose_name='Moeurs principale')),
                ('activity_period', models.CharField(choices=[('N', 'Nocturne'), ('D', 'Diurne'), ('A', 'Aube/Crépusculaire')], max_length=1, verbose_name="Période d'activité principale")),
                ('main_behavior', models.CharField(choices=[('P', 'Placide'), ('F', 'Fuyard'), ('D', 'Démonstratif'), ('I', 'Irascible')], max_length=1, verbose_name='Tempérament')),
                ('distribution', models.CharField(max_length=1024)),
                ('vivarium_size', models.CharField(help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5", max_length=128, verbose_name='Taille du terrarium')),
                ('slug', models.SlugField(unique=True)),
                ('more_informations', models.TextField(help_text='Informations complémentaires importantes', verbose_name='Informations complémentaires')),
                ('bite_dangerosity', models.CharField(choices=[('I', 'Inofensif'), ('P', 'Pouvant entraîner des dommages'), ('D', 'Dangereux'), ('E', 'Extrêmement dangereux')], max_length=1, verbose_name='Dangerosité de la morsure')),
                ('difficulty_care', models.CharField(choices=[('N', 'Pour éleveur débutant (premières espèces)'), ('B', 'Pour éleveur ayant déjà une base'), ('E', 'Pour éleveur expérimenté'), ('X', 'Pour éleveur très expérimenté')], max_length=1, verbose_name='Difficulté de maintien')),
                ('day_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de jour')),
                ('night_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de nuit')),
                ('humidity', models.CharField(help_text='format: 50% - 80%', max_length=64, verbose_name='humidité')),
                ('last_update', models.DateField(auto_now=True)),
                ('toxicity_level', models.CharField(blank=True, choices=[('N', 'Non venimeux'), ('F', 'Faible toxicité'), ('A', 'Nécessite une surveillance active'), ('H', 'Hospitalisation immédiate recommandée'), ('I', 'Hospitalisation immédiate (risque de décès)')], max_length=1, verbose_name='Niveau de toxicité')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=card.models.snake_directory_path)),
                ('biotops', models.ManyToManyField(to='card.biotop', verbose_name='Biotopes')),
                ('last_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('life_community', models.ManyToManyField(to='card.lifecommunity', verbose_name='Peut vivre en communauté')),
                ('preys', models.ManyToManyField(to='card.prey', verbose_name='Proies')),
                ('venoms', models.ManyToManyField(to='card.venom', verbose_name='Venins')),
            ],
            options={
                'verbose_name': 'Serpent',
                'verbose_name_plural': 'Serpents',
            },
        ),
        migrations.CreateModel(
            name='Lizard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(help_text='Exemple: Thamnophis', max_length=64, verbose_name='Genre')),
                ('species', models.CharField(help_text='Exemple : sirtalis similis', max_length=128, verbose_name='Espèce (sous-espèce)')),
                ('is_cites', models.BooleanField()),
                ('bern_convention_annex', models.PositiveSmallIntegerField(blank=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne", null=True)),
                ('juvenil_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des juvéniles')),
                ('adult_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des adultes')),
                ('life_expectancy', models.CharField(default=15, help_text='Exemple: 15 - 20 ans', max_length=100, verbose_name='Espérance de vie')),
                ('main_mores', models.CharField(choices=[('F', 'Fouisseur'), ('T', 'Terrestre'), ('A', '(Semi-)Arboricole')], max_length=1, verbose_name='Moeurs principale')),
                ('activity_period', models.CharField(choices=[('N', 'Nocturne'), ('D', 'Diurne'), ('A', 'Aube/Crépusculaire')], max_length=1, verbose_name="Période d'activité principale")),
                ('main_behavior', models.CharField(choices=[('P', 'Placide'), ('F', 'Fuyard'), ('D', 'Démonstratif'), ('I', 'Irascible')], max_length=1, verbose_name='Tempérament')),
                ('distribution', models.CharField(max_length=1024)),
                ('vivarium_size', models.CharField(help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5", max_length=128, verbose_name='Taille du terrarium')),
                ('slug', models.SlugField(unique=True)),
                ('more_informations', models.TextField(help_text='Informations complémentaires importantes', verbose_name='Informations complémentaires')),
                ('bite_dangerosity', models.CharField(choices=[('I', 'Inofensif'), ('P', 'Pouvant entraîner des dommages'), ('D', 'Dangereux'), ('E', 'Extrêmement dangereux')], max_length=1, verbose_name='Dangerosité de la morsure')),
                ('difficulty_care', models.CharField(choices=[('N', 'Pour éleveur débutant (premières espèces)'), ('B', 'Pour éleveur ayant déjà une base'), ('E', 'Pour éleveur expérimenté'), ('X', 'Pour éleveur très expérimenté')], max_length=1, verbose_name='Difficulté de maintien')),
                ('day_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de jour')),
                ('night_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de nuit')),
                ('humidity', models.CharField(help_text='format: 50% - 80%', max_length=64, verbose_name='humidité')),
                ('last_update', models.DateField(auto_now=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=card.models.lizard_directory_path, verbose_name='Image des adultes')),
                ('biotops', models.ManyToManyField(to='card.biotop', verbose_name='Biotopes')),
                ('last_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('life_community', models.ManyToManyField(to='card.lifecommunity', verbose_name='Peut vivre en communauté')),
                ('preys', models.ManyToManyField(to='card.prey', verbose_name='Proies')),
            ],
            options={
                'verbose_name': 'Lézard',
                'verbose_name_plural': 'Lézards',
            },
        ),
        migrations.CreateModel(
            name='Arthropod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(help_text='Exemple: Thamnophis', max_length=64, verbose_name='Genre')),
                ('species', models.CharField(help_text='Exemple : sirtalis similis', max_length=128, verbose_name='Espèce (sous-espèce)')),
                ('is_cites', models.BooleanField()),
                ('bern_convention_annex', models.PositiveSmallIntegerField(blank=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne", null=True)),
                ('juvenil_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des juvéniles')),
                ('adult_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des adultes')),
                ('life_expectancy', models.CharField(default=15, help_text='Exemple: 15 - 20 ans', max_length=100, verbose_name='Espérance de vie')),
                ('main_mores', models.CharField(choices=[('F', 'Fouisseur'), ('T', 'Terrestre'), ('A', '(Semi-)Arboricole')], max_length=1, verbose_name='Moeurs principale')),
                ('activity_period', models.CharField(choices=[('N', 'Nocturne'), ('D', 'Diurne'), ('A', 'Aube/Crépusculaire')], max_length=1, verbose_name="Période d'activité principale")),
                ('main_behavior', models.CharField(choices=[('P', 'Placide'), ('F', 'Fuyard'), ('D', 'Démonstratif'), ('I', 'Irascible')], max_length=1, verbose_name='Tempérament')),
                ('distribution', models.CharField(max_length=1024)),
                ('vivarium_size', models.CharField(help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5", max_length=128, verbose_name='Taille du terrarium')),
                ('slug', models.SlugField(unique=True)),
                ('more_informations', models.TextField(help_text='Informations complémentaires importantes', verbose_name='Informations complémentaires')),
                ('bite_dangerosity', models.CharField(choices=[('I', 'Inofensif'), ('P', 'Pouvant entraîner des dommages'), ('D', 'Dangereux'), ('E', 'Extrêmement dangereux')], max_length=1, verbose_name='Dangerosité de la morsure')),
                ('difficulty_care', models.CharField(choices=[('N', 'Pour éleveur débutant (premières espèces)'), ('B', 'Pour éleveur ayant déjà une base'), ('E', 'Pour éleveur expérimenté'), ('X', 'Pour éleveur très expérimenté')], max_length=1, verbose_name='Difficulté de maintien')),
                ('day_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de jour')),
                ('night_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de nuit')),
                ('humidity', models.CharField(help_text='format: 50% - 80%', max_length=64, verbose_name='humidité')),
                ('last_update', models.DateField(auto_now=True)),
                ('toxicity_level', models.CharField(blank=True, choices=[('N', 'Non venimeux'), ('F', 'Faible toxicité'), ('A', 'Nécessite une surveillance active'), ('H', 'Hospitalisation immédiate recommandée'), ('I', 'Hospitalisation immédiate (risque de décès)')], max_length=1, verbose_name='Niveau de toxicité')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=card.models.arthropod_directory_path)),
                ('biotops', models.ManyToManyField(to='card.biotop', verbose_name='Biotopes')),
                ('last_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('life_community', models.ManyToManyField(to='card.lifecommunity', verbose_name='Peut vivre en communauté')),
                ('preys', models.ManyToManyField(to='card.prey', verbose_name='Proies')),
                ('venoms', models.ManyToManyField(to='card.venom', verbose_name='Venins')),
            ],
            options={
                'verbose_name': 'Arthropode',
                'verbose_name_plural': 'Arthropodes',
            },
        ),
        migrations.CreateModel(
            name='Amphibian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(help_text='Exemple: Thamnophis', max_length=64, verbose_name='Genre')),
                ('species', models.CharField(help_text='Exemple : sirtalis similis', max_length=128, verbose_name='Espèce (sous-espèce)')),
                ('is_cites', models.BooleanField()),
                ('bern_convention_annex', models.PositiveSmallIntegerField(blank=True, default=0, help_text="Laissez vide si l'espèce ne figure pas dans la Convention de Berne", null=True)),
                ('juvenil_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des juvéniles')),
                ('adult_size', models.CharField(help_text='Exemple: 80 - 90 cm', max_length=32, verbose_name='Taille des adultes')),
                ('life_expectancy', models.CharField(default=15, help_text='Exemple: 15 - 20 ans', max_length=100, verbose_name='Espérance de vie')),
                ('main_mores', models.CharField(choices=[('F', 'Fouisseur'), ('T', 'Terrestre'), ('A', '(Semi-)Arboricole')], max_length=1, verbose_name='Moeurs principale')),
                ('activity_period', models.CharField(choices=[('N', 'Nocturne'), ('D', 'Diurne'), ('A', 'Aube/Crépusculaire')], max_length=1, verbose_name="Période d'activité principale")),
                ('main_behavior', models.CharField(choices=[('P', 'Placide'), ('F', 'Fuyard'), ('D', 'Démonstratif'), ('I', 'Irascible')], max_length=1, verbose_name='Tempérament')),
                ('distribution', models.CharField(max_length=1024)),
                ('vivarium_size', models.CharField(help_text="Exemple: Lxlxh - bassin: Lxlxl. Dimension en cm. Possibilité de mettre multiplicateur de l'animal selon l'OPAN: 1x0.55x0.5", max_length=128, verbose_name='Taille du terrarium')),
                ('slug', models.SlugField(unique=True)),
                ('more_informations', models.TextField(help_text='Informations complémentaires importantes', verbose_name='Informations complémentaires')),
                ('bite_dangerosity', models.CharField(choices=[('I', 'Inofensif'), ('P', 'Pouvant entraîner des dommages'), ('D', 'Dangereux'), ('E', 'Extrêmement dangereux')], max_length=1, verbose_name='Dangerosité de la morsure')),
                ('difficulty_care', models.CharField(choices=[('N', 'Pour éleveur débutant (premières espèces)'), ('B', 'Pour éleveur ayant déjà une base'), ('E', 'Pour éleveur expérimenté'), ('X', 'Pour éleveur très expérimenté')], max_length=1, verbose_name='Difficulté de maintien')),
                ('day_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de jour')),
                ('night_temperature', models.CharField(help_text='format : 18°C - 22°C', max_length=64, verbose_name='Température de nuit')),
                ('humidity', models.CharField(help_text='format: 50% - 80%', max_length=64, verbose_name='humidité')),
                ('last_update', models.DateField(auto_now=True)),
                ('image_egg', sorl.thumbnail.fields.ImageField(blank=True, upload_to=card.models.amphibian_directory_path, verbose_name="Image d'une ponte")),
                ('image_larve', sorl.thumbnail.fields.ImageField(blank=True, upload_to=card.models.amphibian_directory_path, verbose_name='Image des larves')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=card.models.amphibian_directory_path, verbose_name='Image des adultes')),
                ('volume_call', models.CharField(choices=[('A', 'Aphone'), ('D', 'Discret'), ('B', 'Bruyant')], help_text='Volume sonnor du chant', max_length=1)),
                ('biotops', models.ManyToManyField(to='card.biotop', verbose_name='Biotopes')),
                ('last_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('life_community', models.ManyToManyField(to='card.lifecommunity', verbose_name='Peut vivre en communauté')),
                ('preys', models.ManyToManyField(to='card.prey', verbose_name='Proies')),
            ],
            options={
                'verbose_name': 'Amphibien',
                'verbose_name_plural': 'Amphibiens',
            },
        ),
    ]