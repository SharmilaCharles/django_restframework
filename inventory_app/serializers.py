from rest_framework import serializers
from .models import *

class Products_Serializers(serializers.ModelSerializer):

    class Meta: 
        model = Products
        fields  = '__all__'

class Category_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

        

