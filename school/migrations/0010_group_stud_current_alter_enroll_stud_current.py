# Generated by Django 5.0 on 2023-12-27 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_remove_enroll_group_enroll_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='stud_current',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='stud_current',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_number', to='school.course'),
        ),
    ]