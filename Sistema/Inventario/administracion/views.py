from django.shortcuts import render
from .models import ProductoModel
from .serializers import ProductoSerializer
#REST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ProductosView(ListCreateAPIView): 
    #consulta a la base de datos para efectuar está vista 
    queryset=ProductoModel.objects.all() # SELECT * FROM
    # es la forma en la cual vamos a decorar el resultado, para mostrar al cliente
    serializer_class= ProductoSerializer
    def get(self, request):
        respuesta = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        }, status=status.HTTP_200_OK)

    def post(self,request):
        producto = self.get_serializer(data=request.data)
        if producto.is_valid():
            producto.save()
            return Response({
                "ok":True,
                "content":producto.data,
                "message":"Se creo exitosamente el producto"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":producto.errors,
                "message":"Hubo un error al guardar el producto"
            }, status.HTTP_400_BAD_REQUEST)

class ProductoView(RetrieveUpdateDestroyAPIView):
    queryset= ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    def get(self, request, id):
        respuesta = self.get_serializer(self.get_queryset().filter(productoId=id).first())
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":None
        })
    def put(self, request, id):
        producto = self.get_queryset().filter(productoId=id).first()
        respuesta = self.get_serializer(producto, data=request.data)
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response({
                "ok":True,
                "content":self.serializer_class(resultado).data,
                "message": "Se actulizo exitosamente el producto"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ok":False,
                "content":respuesta.errors,
                "message":"hubo un error al actualizar el producto"
            }, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        producto = self.get_queryset().filter(productoId=id).first()
        respuesta = self.get_serializer(producto)
        respuesta.delete()
        return Response({
            "ok":True,
            "content":respuesta.data,
            "message":"Se elimino el producto exitosamente"
        })



