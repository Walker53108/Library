# Generated by Django 3.1.5 on 2021-02-27 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20210227_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_books',
            name='bid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='index.all_books'),
        ),
        migrations.AlterField(
            model_name='issued_books',
            name='bid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='index.all_books'),
        ),
    ]
