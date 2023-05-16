from django.urls import path

from .views import AmphibianList, AmphibianDetail, AmphibianCreateView, AmphibianUpdateView, \
    ArthropodList, ArthropodDetail, ArthropodCreateView, ArthropodUpdateView, \
    LizardList, LizardDetail, LizardCreateView, LizardUpdateView, \
    SnakeList, SnakeDetail, SnakeCreateView, SnakeUpdateView, \
    TurtleList, TurtleDetail, TurtleCreateView, TurtleUpdateView

app_name = "card"
urlpatterns = [
    path("amphibiens/", AmphibianList, name="amphibian-list"),
    path("amphibiens/ajouter", AmphibianCreateView.as_view(), name="amphibian-new"),
    path("amphibiens/<slug:slug>/editer", AmphibianUpdateView.as_view(), name="amphibian-edit"),
    path("amphibiens/<slug:slug>", AmphibianDetail, name="amphibian-detail"),

    path("arthropodes/", ArthropodList, name="arthropod-list"),
    path("arthropodes/ajouter", ArthropodCreateView.as_view(), name="arthropod-new"),
    path("arthropodes/<slug:slug>/editer", ArthropodUpdateView.as_view(), name="arthropod-edit"),
    path("arthropodes/<slug:slug>", ArthropodDetail, name="arthropod-detail"),

    path("lezards/", LizardList, name="lizard-list"),
    path("lezards/ajouter", LizardCreateView.as_view(), name="lizard-new"),
    path("lezards/<slug:slug>/editer", LizardUpdateView.as_view(), name="lizard-edit"),
    path("lezards/<slug:slug>", LizardDetail, name="lizard-detail"),

    path("serpents/", SnakeList, name="snake-list"),
    path("serpents/ajouter", SnakeCreateView.as_view(), name="snake-new"),
    path("serpents/<slug:slug>/editer", SnakeUpdateView.as_view(), name="snake-edit"),
    path("serpents/<slug:slug>", SnakeDetail, name="snake-detail"),

    path("tortues/", TurtleList, name="turtle-list"),
    path("tortues/ajouter", TurtleCreateView.as_view(), name="turtle-new"),
    path("tortues/<slug:slug>/editer", TurtleUpdateView.as_view(), name="turtle-edit"),
    path("tortues/<slug:slug>", TurtleDetail, name="turtle-detail"),
]
