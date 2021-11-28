from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'HEAD'])
@authentication_classes(())
def ping(request):
    return Response({"message": "Todo API running..."}, status=status.HTTP_200_OK)
