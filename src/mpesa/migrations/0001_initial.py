# Generated by Django 4.2.3 on 2023-07-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckoutRequestID', models.CharField(max_length=50)),
                ('MerchantRequestID', models.CharField(max_length=30)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('ResultCode', models.IntegerField()),
                ('Amount', models.FloatField(blank=True)),
                ('MpesaReceiptNumber', models.CharField(max_length=20)),
                ('TransactionDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='netview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
