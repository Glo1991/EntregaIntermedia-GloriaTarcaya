# Generated by Django 3.2.16 on 2022-12-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
