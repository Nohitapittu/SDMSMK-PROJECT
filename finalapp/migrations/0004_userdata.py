# Generated by Django 4.2.7 on 2023-11-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_student_teacher_delete_staf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
