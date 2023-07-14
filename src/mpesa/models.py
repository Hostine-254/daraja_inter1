from django.db import models

# Create your models here.

class LNMOnline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50)
    MerchantRequestID = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=11)
    ResultCode = models.IntegerField()
    Amount = models.FloatField()
    MpesaReceiptNumber = models.CharField(max_length=20)
    TransactionDate = models.DateTimeField()

