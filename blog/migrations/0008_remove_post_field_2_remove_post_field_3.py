# Generated by Django 4.2.10 on 2024-03-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_field_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]
