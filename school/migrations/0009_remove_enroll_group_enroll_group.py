# Generated by Django 5.0 on 2023-12-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_enroll_group_alter_enroll_course_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='group',
        ),
        migrations.AddField(
            model_name='enroll',
            name='group',
            field=models.ManyToManyField(blank=True, to='school.group'),
        ),
    ]
