# Generated by Django 2.2.4 on 2020-12-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_auto_20201209_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
