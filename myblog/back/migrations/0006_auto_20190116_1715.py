# Generated by Django 2.1.5 on 2019-01-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_auto_20190115_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='a_colum',
            new_name='a_column',
        ),
    ]
