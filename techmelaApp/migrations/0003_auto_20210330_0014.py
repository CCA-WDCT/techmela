# Generated by Django 3.1.7 on 2021-03-29 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techmelaApp', '0002_auto_20210330_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='status',
            new_name='category',
        ),
    ]
