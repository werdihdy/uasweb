# Generated by Django 4.2.7 on 2023-12-04 22:15

import ckeditor.fields
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('handoyo', '0002_kategori_banner_satu_profil_keterangan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='banner_satu',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]