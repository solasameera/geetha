from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import geetha
from geetha_app1.models import Geetha


# Create your views here.
class GeethsAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):

        geetha = Geetha()
        geetha.name = request.data['name']
        geetha.address = request.data['address']
        geetha.save()
        return Response({'status': 'data saved'})
    def get(self,request):
       geetha = Geetha.objects.all().values()
       return Response(list(geetha))


    def put(self, request):
         geetha = Geetha.objects.all().values()
         return Response(list(geetha))
    def patch(self,request):
        geetha = Geetha.objects.all().values()
        return Response(list(geetha))
    def delete(self,request):
        geetha = Geetha.objects.all().values()
        return Response(list(geetha))




