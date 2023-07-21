from django.contrib import admin
from django.urls import path,include

from mpesa.api.views import LNMCallbackUrlAPIView,NetPostAPIView

urlpatterns = [
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
    path('netview/', NetPostAPIView.as_view(), name="netview-post"),

]
