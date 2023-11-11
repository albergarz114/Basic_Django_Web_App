from django.urls import path
from .views import storePageView

urlpatterns = [
    path("", storePageView, name= "store_page"),
    
]