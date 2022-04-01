# Generated by Django 4.0.2 on 2022-02-20 08:13

from django.db import migrations, models
import petstagram.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='mediafiles/', validators=[petstagram.validators.validators.validate_image_size]),
        ),
    ]