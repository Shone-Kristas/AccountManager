# Generated by Django 5.0.6 on 2024-06-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='residential_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
