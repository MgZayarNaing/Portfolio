# Generated by Django 4.2.1 on 2023-12-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='img1',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='img2',
            new_name='second',
        ),
    ]
