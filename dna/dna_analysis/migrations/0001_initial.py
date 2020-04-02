# Generated by Django 2.2.7 on 2020-03-31 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dna_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dna', models.TextField()),
                ('url', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
