# Generated by Django 2.1.2 on 2018-11-18 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pirates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tesouro',
            old_name='valor',
            new_name='preco',
        ),
    ]
