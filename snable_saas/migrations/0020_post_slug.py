# Generated by Django 4.0.4 on 2022-05-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snable_saas', '0019_delete_blogcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
