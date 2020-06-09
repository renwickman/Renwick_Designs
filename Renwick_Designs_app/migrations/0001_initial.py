# Generated by Django 2.2 on 2020-02-25 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('city', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=3)),
                ('zip_code', models.IntegerField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renwick_Designs_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=60)),
                ('consultation', models.DateTimeField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('project', models.CharField(max_length=60)),
                ('guests', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renwick_Designs_app.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renwick_Designs_app.User')),
            ],
        ),
    ]