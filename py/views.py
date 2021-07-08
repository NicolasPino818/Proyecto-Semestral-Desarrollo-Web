#Api de los objetos
@api_view(['GET', 'PUT', 'DELETE'])
def ropa-hombre(request, pk):
  try:
     ropa-hombre = ropa-hombre.objects.get(talla=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
        serializer = Ropa-HombreSerializer(Ropa-Hombre)
        return Response(serializer.data)
  
  elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = Ropa-HombreSerializer(Ropa-Hombre, data=data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      ropa-hombre.delete()
      return Responde(status=status.HTTP_204_NO_CONTENT)
   else:
      return response(status=status.HTTP_401_UNAUTHORIZED)
  
 def ropa-mujer(request, pk):
  try:
     ropa-mujer = ropa-mujer.objects.get(talla=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
        serializer = Ropa-MujerSerializer(Ropa-Mujer)
        return Response(serializer.data)
  
  elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = Ropa-MujerSerializer(Ropa-Mujer, data=data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      ropa-mujer.delete()
      return Responde(status=status.HTTP_204_NO_CONTENT)
   else:
      return response(status=status.HTTP_401_UNAUTHORIZED) 
 

def ropa-nina(request, pk):
  try:
     ropa-hombre = ropa-nina.objects.get(talla=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
        serializer = Ropa-NinaSerializer(Ropa-Nina)
        return Response(serializer.data)
  
  elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = Ropa-NinaSerializer(Ropa-Nina, data=data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      ropa-nina.delete()
      return Responde(status=status.HTTP_204_NO_CONTENT)
   else:
      return response(status=status.HTTP_401_UNAUTHORIZED)

def ropa-nino(request, pk):
  try:
     ropa-nino = ropa-nino.objects.get(talla=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
        serializer = Ropa-HombreSerializer(Ropa-Nino)
        return Response(serializer.data)
  
  elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = Ropa-NinoSerializer(Ropa-Nino, data=data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      ropa-nino.delete()
      return Responde(status=status.HTTP_204_NO_CONTENT)
   else:
      return response(status=status.HTTP_401_UNAUTHORIZED)
    
#Importaciones
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#Decoradores
@permission_classes((IsAuthenticated,))
