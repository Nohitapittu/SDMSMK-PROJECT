# Generated by Django 4.2.7 on 2023-12-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0022_rename_upload_resume_teacherjob_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentform',
            old_name='address',
            new_name='enter_address',
        ),
        migrations.RenameField(
            model_name='studentform',
            old_name='date_of_birth',
            new_name='enter_dob',
        ),
        migrations.RenameField(
            model_name='studentform',
            old_name='email',
            new_name='enter_email',
        ),
        migrations.RenameField(
            model_name='studentform',
            old_name='contact_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='studentform',
            old_name='gender',
            new_name='select_gender',
        ),
        migrations.RenameField(
            model_name='studentform',
            old_name='grade',
            new_name='select_grade',
        ),
    ]
