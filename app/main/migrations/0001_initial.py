# Generated by Django 3.0.7 on 2020-06-06 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetectionCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_relevant', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('threat', models.ManyToManyField(to='main.Threat')),
            ],
            options={
                'verbose_name': 'Обнаруженная угроза',
                'verbose_name_plural': 'Обнаруженные угрозы',
            },
        ),
    ]