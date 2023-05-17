from django.contrib import admin
from .models import Amphibian, Arthropod, Lizard, Snake, Venom, Prey, Biotop, LifeCommunity, Turtle, ReproductionPeriod

@admin.register(Venom)
class VenomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name", "effects"]})
    ]
    list_display = ("name",)

@admin.register(Prey)
class PreyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]})
    ]
    list_display = ("name",)

@admin.register(Biotop)
class BiotopAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]})
    ]
    list_display = ("name",)

@admin.register(LifeCommunity)
class LifeCommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]})
    ]
    list_display = ("name",)

@admin.register(ReproductionPeriod)
class ReproductionPeriodCommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]})
    ]
    list_display = ("name",)

@admin.register(Amphibian)
class AmphibianAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            # Set the last_owner field to the current user when creating a new instance
            obj.last_owner = request.user
        else:
            # If the instance is being updated, don't change the last_owner field
            pass
        super().save_model(request, obj, form, change)
    fieldsets = [
        (None, {"fields": ["genus", "species"]}),
        ('Description physique', {'fields': ["juvenil_size", "adult_size", "image_egg", "image_larve", "image"]}),
        ('Biologie', {'fields': ["life_expectancy", "main_mores", "main_behavior", "activity_period", "reproduction", "reproduction_period", "volume_call", "preys"]}),
        ('Environement', {'fields': ["distribution", "biotops"]}),
        ('Protection', {'fields': ['is_cites', 'bern_convention_annex']}),
        ('En captivité', {'fields': ['vivarium_size', 'day_temperature', 'night_temperature', 'humidity', 'difficulty_care', 'bite_dangerosity', 'life_community']}),
        ('Divers', {'fields': ['more_informations']})
    ]

    exclude = ("last_update", "last_owner")

    list_display = ["genus", "species", "last_owner"]
    list_filter = ["genus"]
    search_fields = ("genus", "species", "description", "mores", "distribution", "protection")

@admin.register(Arthropod)
class ArthropodAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            # Set the last_owner field to the current user when creating a new instance
            obj.last_owner = request.user
        else:
            # If the instance is being updated, don't change the last_owner field
            pass
        super().save_model(request, obj, form, change)

    fieldsets = [
        (None, {"fields": ["genus", "species"]}),
        ('Description physique', {'fields': ["juvenil_size", "adult_size", "image"]}),
        ('Biologie', {'fields': ["life_expectancy","main_mores", "main_behavior", "activity_period", "reproduction", "reproduction_period", "preys"]}),
        ('Environement', {'fields': ["distribution", "biotops"]}),
        ('Protection', {'fields': ['is_cites', 'bern_convention_annex']}),
        ('Toxicologie', {'fields': ['toxicity_level', 'venoms']}),
        ('En captivité', {'fields': ['vivarium_size', 'day_temperature', 'night_temperature', 'humidity', 'difficulty_care', 'bite_dangerosity', 'life_community']}),
        ('Divers', {'fields': ['more_informations']})
    ]

    exclude = ("last_update", "last_owner")

    list_display = ["genus", "species", "last_owner"]
    list_filter = ["genus"]
    search_fields = ("genus", "species", "description", "mores", "distribution", "protection")


@admin.register(Lizard)
class LizardAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            # Set the last_owner field to the current user when creating a new instance
            obj.last_owner = request.user
        else:
            # If the instance is being updated, don't change the last_owner field
            pass
        super().save_model(request, obj, form, change)

    fieldsets = [
        (None, {"fields": ["genus", "species"]}),
        ('Description physique', {'fields': ["juvenil_size", "adult_size", "image"]}),
        ('Biologie', {'fields': ["life_expectancy","main_mores", "main_behavior", "activity_period", "reproduction", "reproduction_period", "preys"]}),
        ('Environement', {'fields': ["distribution", "biotops"]}),
        ('Protection', {'fields': ['is_cites', 'bern_convention_annex']}),
        ('En captivité', {'fields': ['vivarium_size', 'day_temperature', 'night_temperature', 'humidity', 'difficulty_care', 'bite_dangerosity', 'life_community']}),
        ('Divers', {'fields': ['more_informations']})
    ]

    exclude = ("last_update", "last_owner")

    list_display = ["genus", "species", "last_owner"]
    list_filter = ["genus"]
    search_fields = ("genus", "species", "description", "mores", "distribution", "protection")

@admin.register(Snake)
class SnakeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            # Set the last_owner field to the current user when creating a new instance
            obj.last_owner = request.user
        else:
            # If the instance is being updated, don't change the last_owner field
            pass
        super().save_model(request, obj, form, change)

    fieldsets = [
        (None, {"fields": ["genus", "species"]}),
        ('Description physique', {'fields': ["dentition","juvenil_size", "adult_size", "image"]}),
        ('Biologie', {'fields': ["life_expectancy", "main_mores", "main_behavior", "activity_period", "reproduction", "reproduction_period", "preys"]}),
        ('Environement', {'fields': ["distribution", "biotops"]}),
        ('Protection', {'fields': ['is_cites', 'bern_convention_annex']}),
        ('Toxicologie', {'fields': ['toxicity_level', 'venoms']}),
        ('En captivité', {'fields': ['vivarium_size', 'day_temperature', 'night_temperature', 'humidity', 'difficulty_care', 'bite_dangerosity', 'life_community']}),
        ('Divers', {'fields': ['more_informations']})
    ]

    exclude = ("last_update", "last_owner")

    list_display = ["genus", "species", "last_owner"]
    list_filter = ["genus"]
    search_fields = ("genus", "species", "description", "mores", "distribution", "protection")

@admin.register(Turtle)
class turtleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            # Set the last_owner field to the current user when creating a new instance
            obj.last_owner = request.user
        else:
            # If the instance is being updated, don't change the last_owner field
            pass
        super().save_model(request, obj, form, change)

    fieldsets = [
        (None, {"fields": ["genus", "species"]}),
        ('Description physique', {'fields': ["juvenil_size", "adult_size", "image"]}),
        ('Biologie', {'fields': ["life_expectancy","main_mores", "main_behavior", "activity_period", "reproduction", "reproduction_period", 'type_of_turtle', "preys"]}),
        ('Environement', {'fields': ["distribution", "biotops"]}),
        ('Protection', {'fields': ['is_cites', 'bern_convention_annex']}),
        ('En captivité', {'fields': ['vivarium_size', 'day_temperature', 'night_temperature', 'humidity', 'difficulty_care', 'bite_dangerosity', 'life_community']}),
        ('Divers', {'fields': ['more_informations']})
    ]

    exclude = ("last_update", "last_owner")

    list_display = ["genus", "species", "last_owner"]
    list_filter = ["genus", 'type_of_turtle']
    search_fields = ("genus", "species", "description", "mores", "distribution", "protection")