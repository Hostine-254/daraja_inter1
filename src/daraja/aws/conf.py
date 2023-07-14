import datetime

#from decouple import config

AWS_ACCESS_KEY_ID = "AKIAUAGJXVIYEA7JDMNA"
AWS_SECRET_ACCESS_KEY = "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"

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = "daraja.aws.utils.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "daraja.aws.utils.StaticRootS3BotoStorage"

AWS_S3_OBJESCT_PARAMETERS = {
    'CachedControl': 'max-age=86400'
}

AWS_LOCATION = 'static' #added line


AWS_STORAGE_BUCKET_NAME = "daraja-internet"
S3DIRECT_REGION = "eu-west-1"

S3_URL = "//%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "//%s.s3.amazonaws.com/media/" % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    #"Expires": expires,
    #"Cache-Control": "max-age=%d" % (int(two_months.total_seconds()),),
    'Access-Control-Allow-Origin': '*'
}