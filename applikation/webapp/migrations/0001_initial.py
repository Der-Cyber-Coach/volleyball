# Generated by Django 4.2.6 on 2023-10-08 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Courts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date played')),
                ('time', models.DateTimeField(null=True, verbose_name='time played')),
                ('roundNumber', models.IntegerField(default=2)),
            ],
            options={
                'verbose_name_plural': 'Courts',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='date played')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(default='None', max_length=200)),
                ('birthdate', models.DateTimeField(null=True, verbose_name='date of birth')),
                ('age', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True, verbose_name='date played')),
                ('roundNumber', models.IntegerField(default=2)),
            ],
            options={
                'verbose_name_plural': 'Rounds',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member1', to='webapp.players')),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member2', to='webapp.players')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True, verbose_name='date played')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_city', to='webapp.cities')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_court', to='webapp.courts')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_loser', to='webapp.teams')),
                ('matches', models.ManyToManyField(to='webapp.matches')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_round', to='webapp.rounds')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_winner', to='webapp.teams')),
            ],
            options={
                'verbose_name_plural': 'Tournaments',
            },
        ),
        migrations.AddField(
            model_name='rounds',
            name='loser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_loser', to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='rounds',
            name='teams',
            field=models.ManyToManyField(to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='rounds',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_winner', to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='loser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_loser', to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_round', to='webapp.rounds'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_team1', to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_team2', to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_winner', to='webapp.teams'),
        ),
    ]
