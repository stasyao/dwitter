# Generated by Django 3.2.5 on 2022-01-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='dwitter.Profile', verbose_name='на кого подписан'),
        ),
    ]
