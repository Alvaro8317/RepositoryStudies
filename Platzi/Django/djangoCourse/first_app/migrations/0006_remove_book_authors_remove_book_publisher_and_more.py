# Generated by Django 5.1.2 on 2024-10-28 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]