# Generated by Django 3.2.2 on 2021-05-10 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blog_confession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confession',
            old_name='img',
            new_name='conf_img',
        ),
    ]
