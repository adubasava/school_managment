# Generated by Django 5.0 on 2023-12-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_group_stud_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='stud_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='stud_min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
