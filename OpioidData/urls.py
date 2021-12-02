from django.urls import path
from .views import searchDrugsPageView, addPageView, deletePageView, updatePageView, editPageView, trendsPageView, allPrescriberPageView, allDrugsPageView, singlePrescriberPageView, singleDrugPageView, indexPageView

urlpatterns = [
    path("drugsearch/<str:name>", searchDrugsPageView, name="drugsearch"),
    path("add/", addPageView, name="add"),
    path("delete/<int:npi>/", deletePageView, name='delete'),
    path("update/", updatePageView, name="update"),
    path("edit/<int:npi>/", editPageView, name="edit"),
    path("trends/", trendsPageView, name="trends"),
    path("prescribers/", allPrescriberPageView, name="prescribers"),
    path("drugs/", allDrugsPageView, name="drugs"),
    path("prescriber/", singlePrescriberPageView, name="prescriber"),
    path("drug/", singleDrugPageView, name="drug"),
    path("", indexPageView, name="index"),
]