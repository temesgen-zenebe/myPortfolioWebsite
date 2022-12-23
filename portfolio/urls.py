from django.urls import path
from .views import *
from portfolio.views import Home 
from django.urls import path
#from portfolio import views as contact_views



app_name = 'portfolio'
urlpatterns = [
    
    path('', ProjectListView.as_view(), name="project-list"),
    path('<int:detail_id>', DetailView.as_view(), name="detail"),
    path('<int:detail_id>', ProjectListDetailView.as_view(), name="detail"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', Home.as_view(), name='home'),   
    
]
