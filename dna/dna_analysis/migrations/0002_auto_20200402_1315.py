# Generated by Django 2.2.7 on 2020-04-02 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dna_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dna_profile',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='dna_profile',
            name='url',
        ),
    ]