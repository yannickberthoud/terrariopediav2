from django.urls import path
from .views import DocumentationList, DocumentationDetail, DocumentationCreateView, DocumentationUpdateView

app_name = "documentation"
urlpatterns = [
    path("ajouter/", DocumentationCreateView.as_view(), name="documentation-new"),
    path("<str:category>/", DocumentationList, name="documentation-list"),
    path("<str:category>/<slug:slug>", DocumentationDetail, name="documentation-detail"),
    path("<str:category>/<slug:slug>/editer", DocumentationUpdateView.as_view(), name="documentation-edit")
]