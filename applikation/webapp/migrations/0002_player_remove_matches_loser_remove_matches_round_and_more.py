# Generated by Django 4.2.6 on 2023-10-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('federation_code', models.CharField(max_length=5)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (3, 'Other')])),
                ('nationality', models.CharField(max_length=5)),
                ('plays_beach', models.BooleanField()),
                ('plays_volley', models.BooleanField()),
                ('team_name', models.CharField(max_length=100)),
                ('no', models.IntegerField(unique=True)),
                ('version', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.RemoveField(
            model_name='matches',
            name='loser',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='round',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='rounds',
            name='loser',
        ),
        migrations.RemoveField(
            model_name='rounds',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='rounds',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='member1',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='member2',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='city',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='court',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='loser',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='matches',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='round',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='winner',
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
        migrations.DeleteModel(
            name='Courts',
        ),
        migrations.DeleteModel(
            name='Matches',
        ),
        migrations.DeleteModel(
            name='Players',
        ),
        migrations.DeleteModel(
            name='Rounds',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
