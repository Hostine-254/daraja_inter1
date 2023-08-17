from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from mpesa.api.views import LNMCallbackUrlAPIView,NetPostAPIView,VoucherAPIView,CustomLoginView,delete_form

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
    path('netview/', NetPostAPIView.as_view(), name="netview-post"),
    path('vouchers/', VoucherAPIView.as_view(), name="voucher-upload"),
    path('vouchers-delete/', delete_form, name="vouchers-delete"),

]
