#Importaciones
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#Decoradores
@permission_classes((IsAuthenticated,))
