# Generated by Django 3.2.3 on 2021-06-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
