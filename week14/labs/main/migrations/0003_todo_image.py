# Generated by Django 2.2 on 2020-04-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_list_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='todo'),
        ),
    ]
