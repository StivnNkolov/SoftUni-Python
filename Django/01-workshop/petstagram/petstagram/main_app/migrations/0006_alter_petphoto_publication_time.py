# Generated by Django 4.0.2 on 2022-02-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_pet_type_alter_petphoto_publication_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='publication_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
