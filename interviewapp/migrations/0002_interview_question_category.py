# Generated by Django 5.1.3 on 2024-11-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview_question',
            name='category',
            field=models.CharField(default='python', max_length=100),
        ),
    ]
