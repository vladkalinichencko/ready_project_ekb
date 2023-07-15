# Generated by Django 3.2.9 on 2021-11-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('duration', models.DateTimeField()),
                ('author', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
