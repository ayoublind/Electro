# Generated by Django 2.1.dev20180215012401 on 2018-05-10 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180510_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('informations', models.CharField(max_length=800)),
                ('logo', models.ImageField(default='marques/no_image_available.jpg', upload_to='marques/')),
            ],
        ),
    ]
