
from rest_framework.generics import CreateAPIView

from mpesa.models import LNMOnline
from mpesa.api.serializers import LNMOnlineSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    #permission_classes = [IsAdminUser]

    def create(self, request,):
        print(request.data, "this is the request.data")