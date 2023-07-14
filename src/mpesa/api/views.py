
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

        transaction_data = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        print(transaction_data, "this should be the transaction date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        print(phone_number, "this is the senders phone number")