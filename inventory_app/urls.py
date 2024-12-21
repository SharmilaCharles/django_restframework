from django.urls import path
from .views import *

urlpatterns = [
    path('products/', Productview.as_view()),
    path('products/<int:id>/', ProductViewbyID.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', CategoryViewByID.as_view()),

]