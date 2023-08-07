
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from mpesa.models import LNMOnline,netview,C2BPayments
from mpesa.api.serializers import LNMOnlineSerializer,NetPostSerializer,C2BPaymentSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request,):
        print(request.data, "this is the request.data")

    
        """
        {'Body':{
            'stkCallback':{ 
          
                'MerchantRequestID': '18761-17185781-1', 
                'CheckoutRequestID': 'ws_CO_14072023144007940722888543', 
                'ResultCode': 0, 
                'ResultDesc': 'The service request is processed successfully.', 
                'CallbackMetadata': {
                            'Item':         [
                                            {'Name': 'Amount', 'Value': 1.0}, 
                                            {'Name': 'MpesaReceiptNumber', 'Value': 'RGE3IES9TF'}, 
                                            {'Name': 'Balance'}, 
                                            {'Name': 'TransactionDate', 'Value': 20230714143845}, 
                                            {'Name': 'PhoneNumber', 'Value': 254722888543}
                                        ]
                                    }
                            }  
                }
             
        }


        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be merchant request id")

        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        print(checkout_request_id, "this should be check out request id")

        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        print(result_code, "this should be the result code")
        
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        print(amount, "this should be the amount")
        
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        print(mpesa_receipt_number, "this should be the receipt number")

        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        print(transaction_date, "this should be the transaction date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        print(phone_number, "this is the senders phone number")

        from datetime import datetime

        str_transaction_date = str(transaction_date)
        print(str_transaction_date, "this should be a str_transaction_data")

        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        print(transaction_datetime, "this should be a transaction_datetime")

        import pytz
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(aware_transaction_datetime, "this should be an aware_transaction_datetime")

        from samples.mob_message import mobitech
        from samples.voucher_retrival import get_Voucher

        voucher_detail = get_Voucher(amount)
        mobitech(voucher_detail,phone_number)


        from mpesa.models import LNMOnline


        mpesa_model = LNMOnline.objects.create(
            CheckoutRequestID = checkout_request_id,
            MerchantRequestID = merchant_request_id,
            PhoneNumber = phone_number,
            ResultCode = result_code,
            Amount = amount,
            MpesaReceiptNumber = mpesa_receipt_number,
            TransactionDate = aware_transaction_datetime
        )
        mpesa_model.save()

        

        return Response({"OurResultDesc": "YEEY!!! It worked!"})
"""

class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    #def create(self, request,):
       
    #    print(request.data, "this is the request.data in validation")


    #    return Response({"OurResultDesc": "YEEY!!! It worked!"})
    


class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    def create(self, request,):
       
        print(request.data, "this is the request.data in Confirmation")


        return Response({"ResultDesc": 0})
        

          

class NetPostAPIView(CreateAPIView):
    

    queryset = netview.objects.all()
    serializer_class = NetPostSerializer
    permission_classes = [AllowAny]

    def create(self, request,):
        from django.http import HttpResponse

        print(request.data, "this is the net-request.data")

        payee_amount = request.data["form_values"]
        payee_number = request.data["phone_number"]
        print(type(payee_amount))
        print(type(payee_number))
        payee_amount_converted = int(payee_amount)
        print(type(payee_amount_converted))
        print('This is the requested payee amount: ',payee_amount)
        print("This is the requested payee number: ",payee_number)

        payee_number = payee_number.lstrip('0')
        payee_number_converted = '254' + payee_number

        print("This is the converted number: ",payee_number_converted)
        print("This is the payee amount converted:",type(payee_amount_converted))
        print("This is the payee number converted",type(payee_number_converted))
        
        from samples.payments import lipa_na_mpesa


        lipa_na_mpesa(payee_number_converted, payee_amount_converted)
        

        return HttpResponse(status=204)
        
        #{'form_values': ['100'], 'phone_number': ['0722888543']}
        