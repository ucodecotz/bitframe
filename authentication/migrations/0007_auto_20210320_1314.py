# Generated by Django 3.1.7 on 2021-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20210309_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image_url',
            field=models.ImageField(null=True, upload_to='user_profile_pic'),
        ),
    ]
