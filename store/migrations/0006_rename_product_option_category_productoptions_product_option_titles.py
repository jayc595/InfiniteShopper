# Generated by Django 4.2.6 on 2023-10-23 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productoptiontitle_alter_productoptions_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productoptions',
            old_name='product_option_category',
            new_name='product_option_titles',
        ),
    ]