# Generated by Django 3.0.6 on 2020-06-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_comment_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
    ]