# Generated by Django 4.0.2 on 2022-03-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techmelaApp', '0004_auto_20210330_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('1', 'Software'), ('2', 'Hardware'), ('3', 'Research Corner')], default=1, max_length=50),
        ),
    ]
