# Generated by Django 2.1.1 on 2018-09-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180903_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
