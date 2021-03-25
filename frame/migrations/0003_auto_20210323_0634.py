# Generated by Django 3.1.7 on 2021-03-23 06:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0002_frame_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frame',
            old_name='type',
            new_name='frame_type',
        ),
        migrations.AlterField(
            model_name='frame',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='frame',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
