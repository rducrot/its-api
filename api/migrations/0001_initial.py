# Generated by Django 4.1.4 on 2022-12-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=4096)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('AU', 'Author'), ('CO', 'Contributor')], max_length=5)),
                ('role', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=4096)),
                ('tag', models.CharField(choices=[('BU', 'Bug'), ('UP', 'Upgrade'), ('TA', 'Task')], max_length=5)),
                ('priority', models.CharField(choices=[('LO', 'Low'), ('ME', 'Medium'), ('HI', 'High')], max_length=5)),
                ('status', models.CharField(choices=[('NE', 'New'), ('PR', 'Processing'), ('SO', 'Solved')], max_length=5)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=4096)),
                ('type', models.CharField(choices=[('BE', 'Back End'), ('FE', 'Front End'), ('IO', 'Ios'), ('AN', 'Android')], max_length=5)),
            ],
        ),
    ]