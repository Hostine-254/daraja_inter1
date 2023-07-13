import keys

import base64


def generate_password(formatted_time):

    data_to_encode = keys.business_ShortCode + keys.lipa_na_mpesa_passkey + formatted_time
    encode_string = base64.b64encode(data_to_encode.encode())
    #print(encode_string) b'MTc0Mzc5MjAyMzA2MjAyMzQ4MTE='

    decoded_password = encode_string.decode("utf-8")
    #print(decoded_password)
    return decoded_password