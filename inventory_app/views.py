from itertools import product
from multiprocessing.dummy import freeze_support
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Products
from .serializers import Products_Serializers, Category_Serializers
from inventory_app import serializers

class Productview (APIView):

    # def get(self,request):
    #     all_data = Products.objects.all()  
    #     products_data = [] 
    #     for product in all_data:
    #         single_product = {
    #             'id' : product.id,
    #             'product_name' : product.product_name,  
    #             'code' : product.code,
    #             'price': product.price
    #         }
    #         products_data.append(single_product)
    #     return Response(products_data)
    
    def get(self,request):
        all_data = Products.objects.all() 
        serialized_products = Products_Serializers(all_data,many = True).data
        return Response(serialized_products)
    
    # def post(self, request):
    #     new_data = Products(product_name = request.data['product_name'],
    #                         code = request.data['code'],
    #                         price = request.data['price'])
    #     new_data.save()
    #     return Response("Data saved")
    
    def post(self, request):
        
        new_product = Products_Serializers(data= request.data)
        if new_product.is_valid():
            new_product.save()
            return Response("Data saved")
        
        else: 
            return Response(new_product.errors)
    



class ProductViewbyID(APIView):
    # def get(self,request,id):
    #     product = Products.objects.get(id = id)
    #     # print(product)
    #     single_product = {
    #             'id' : product.id,
    #             'product_name' : product.product_name,  
    #             'code' : product.code,
    #             'price': product.price
    #         }
    #     return Response(single_product)

    def get(self,request,id):
        product = Products.objects.get(id = id)
        serialized_product = Products_Serializers(product).data
        return Response(serialized_product)
    
    def patch(self,request,id):
        # product = Products.objects.filter(id = id)
        # # print(request.data)
        # product.update(product_name = request.data['product_name'],
        #                     code = request.data['code'],
        #                     price = request.data['price'])
        # return Response("Get Updated")

        product = Products.objects.get(id = id)
        new_data = Products_Serializers(product, data = request.data, partial=True)
        if new_data.is_valid():
            new_data.save() 
        return Response("Updated")
    
    def delete(self,request,id):
        product=Products.objects.get(id =id)
        product.delete()
        return Response("Deleted")
    

class CategoryView(APIView):

    def get(self,request):
        all_category = Category.objects.all()
        category_serializers = Category_Serializers(all_category, many =True).data
        return Response (category_serializers)
    
    def post(self, request):
        new_category = Category_Serializers(data = request.data)
        if new_category.is_valid():
            new_category.save()

            return Response ("Category Saved")  
        else: 
            return Response(new_category.errors)
    
class CategoryViewByID(APIView):
    def delete(self,request,id):
        category_delete = Category.objects.get(id = id)
        category_delete.delete()
        return Response("Deleted")