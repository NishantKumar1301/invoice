# Generated by Django 5.0.2 on 2024-02-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='question',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]