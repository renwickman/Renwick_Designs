# Generated by Django 2.2 on 2020-02-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renwick_Designs_app', '0003_auto_20200225_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='consultation',
            field=models.DateTimeField(null=True),
        ),
    ]