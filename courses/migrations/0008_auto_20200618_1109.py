# Generated by Django 3.0.7 on 2020-06-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200618_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='description2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='GiftCard',
        ),
    ]
