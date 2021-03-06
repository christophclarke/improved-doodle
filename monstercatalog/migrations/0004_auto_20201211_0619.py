# Generated by Django 3.1.4 on 2020-12-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monstercatalog', '0003_auto_20201210_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='monster',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
