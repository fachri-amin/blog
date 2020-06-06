# Generated by Django 2.2.4 on 2019-10-23 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('kategori', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('penulis', models.CharField(max_length=100)),
                ('published', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('slug', models.CharField(blank=True, editable=False, max_length=255)),
            ],
        ),
    ]