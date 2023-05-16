from django.urls import path
from .views import AdsList, AdsDetail, AdsCreateView, AdsUpdateView, AdsDeleteView, AdsOwnList

app_name = "ads"
urlpatterns = [
    path("", AdsList, name="ads-list"),
    path("ajouter", AdsCreateView.as_view(), name="ads-new"),
    path("mes-annonces", AdsOwnList, name="ads-own-list"),
    path("<int:pk>", AdsDetail, name="ads-detail"),
    path("<int:pk>/editer", AdsUpdateView.as_view(), name="ads-edit"),
    path("<int:pk>/supprimer", AdsDeleteView.as_view(), name="ads-delete"),
]