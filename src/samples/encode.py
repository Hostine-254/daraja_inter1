#from samples.keys import *

import base64


def generate_password(formatted_time):
    business_ShortCode = "174379"
    lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

    data_to_encode = business_ShortCode + lipa_na_mpesa_passkey + formatted_time
    encode_string = base64.b64encode(data_to_encode.encode())
    #print(encode_string) b'MTc0Mzc5MjAyMzA2MjAyMzQ4MTE='

    decoded_password = encode_string.decode("utf-8")
    #print(decoded_password)
    return decoded_password