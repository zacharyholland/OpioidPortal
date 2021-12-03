from django.urls import path
from .views import notOpioidDrugsPageView, opioidDrugsPageView, searchDrugsPageView, addPageView, deletePageView, updatePageView, editPageView, trendsPageView, allPrescriberPageView, allDrugsPageView, singlePrescriberPageView, singleDrugPageView, indexPageView

urlpatterns = [
    path("notopioiddrugs/", notOpioidDrugsPageView, name="notopioiddrugs"),
    path("opioiddrugs/", opioidDrugsPageView, name="opioiddrugs"),
    path("searchdrugs/", searchDrugsPageView, name="searchdrugs"),
    path("add/", addPageView, name="add"),
    path("delete/<int:npi>/", deletePageView, name='delete'),
    path("update/", updatePageView, name="update"),
    path("edit/<int:npi>/", editPageView, name="edit"),
    path("trends/", trendsPageView, name="trends"),
    path("prescribers/", allPrescriberPageView, name="prescribers"),
    path("drugs/", allDrugsPageView, name="drugs"),
    path("prescriber/<int:npi>", singlePrescriberPageView, name="prescriber"),
    path("drug/", singleDrugPageView, name="drug"),
    path("", indexPageView, name="index"),
]