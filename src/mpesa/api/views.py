
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from mpesa.models import LNMOnline
from mpesa.api.serializers import LNMOnlineSerializer

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
        """

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be merchant request id")

        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        print(checkout_request_id, "this should be check out request id")

        result_code = request.data["Body"]["stkCallback"]["ResultDesc"]
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


        from mpesa.models import LNMOnline

        mpesa_model = LNMOnline.objects.create(
             CheckoutRequestID = checkout_request_id,
             MerchantRequestID = merchant_request_id,
             PhoneNumber = phone_number,
             ResultCode = result_code,
             Amount = amount,
             MpesaReceiptNumber = mpesa_receipt_number,
             TransactionDate = transaction_date
        )
        mpesa_model.save()