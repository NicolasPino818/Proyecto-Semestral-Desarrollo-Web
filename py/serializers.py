#Serializers
#Hombre y Mujer (Adolescente y Adulto)
from rest_framework import serializers
from core.models import ropa-hombre

class ropa-hombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ropa-hombre
        fields = ['Talla', 'Marca', 'Categoria']

from rest_framework import serializers
from core.models import ropa-mujer

class ropa-mujerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ropa-mujer
        fields = ['Talla', 'Marca', 'Categoria']        

#Niño y Niña        
from rest_framework import serializers
from core.models import ropa-nino

class ropa-ninoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ropa-nino
        fields = ['Talla', 'Marca', 'Categoria']        
        
from rest_framework import serializers
from core.models import ropa-nina

class ropa-ninaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ropa-nina
        fields = ['Talla', 'Marca', 'Categoria']        
        
