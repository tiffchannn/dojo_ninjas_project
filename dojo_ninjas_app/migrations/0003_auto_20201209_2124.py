# Generated by Django 2.2.4 on 2020-12-09 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_auto_20201209_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
        ),
    ]
