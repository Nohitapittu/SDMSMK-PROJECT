# Generated by Django 5.0 on 2023-12-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0054_alter_teacher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
