from storages.backends.s3boto3 import S3Boto3Storage,S3StaticStorage

#StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
StaticRootS3BotoStorage = lambda: S3StaticStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media')