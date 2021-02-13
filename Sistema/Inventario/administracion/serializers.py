from .models import ProductoModel

#rest
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel
        fields = "__all__"
    def update(self):
        self.instance.productoNombre = self.validated_data.get("productoNombre",self.instance.productoNombre)
        self.instance.productoStock = self.validated_data.get("productoStock",self.instance.productoStock)
        self.instance.productoDescripcion = self.validated_data.get("productoDescripcion",self.instance.productoDescripcion)
        self.instance.productoImagen=self.validated_data.get("productoImagen",self.instance.productoImagen)
        self.instance.productoEstado=self.validated_data.get("productoEstado",self.instance.productoEstado)
        self.instance.productoMedida =self.validated_data.get("productoMedida",self.instance.productoMedida)
        self.instance.categoriaId = self.validated_data.get("categoriaId",self.instance.categoriaId)
        self.instance.save()
        return self.instance

    def delete(self):
        self.instance.productoEstado = False
        self.instance.save()
        return self.instance