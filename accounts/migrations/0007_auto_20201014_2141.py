# Generated by Django 3.0.8 on 2020-10-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='download.jpg', null=True, upload_to=''),
        ),
    ]
