# Generated by Django 4.1 on 2022-09-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('date_added', models.DateField()),
                ('bugs_count', models.IntegerField()),
            ],
        ),
    ]
