# Generated by Django 4.0.4 on 2022-05-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroomgmt', '0006_alter_club_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clas',
            name='istaken',
        ),
    ]