from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='Input Field'),
    path('image_generate',views.image_generate,name='image_generate')

]