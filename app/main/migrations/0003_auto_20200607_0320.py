# Generated by Django 3.0.7 on 2020-06-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200607_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threat',
            old_name='name',
            new_name='en_name',
        ),
        migrations.AddField(
            model_name='threat',
            name='ru_name',
            field=models.CharField(default='Угроза', max_length=50),
            preserve_default=False,
        ),
    ]
