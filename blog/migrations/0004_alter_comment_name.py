# Generated by Django 4.2.7 on 2023-11-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
