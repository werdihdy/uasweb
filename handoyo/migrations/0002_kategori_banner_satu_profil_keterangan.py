# Generated by Django 4.2.7 on 2023-11-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handoyo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='banner_satu',
            field=models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AddField(
            model_name='profil',
            name='keterangan',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
