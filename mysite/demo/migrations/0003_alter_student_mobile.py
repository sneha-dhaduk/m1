# Generated by Django 5.0 on 2023-12-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_rename_course_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='MOBILE',
            field=models.BigIntegerField(),
        ),
    ]