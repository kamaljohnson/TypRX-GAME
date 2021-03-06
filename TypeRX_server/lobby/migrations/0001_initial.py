# Generated by Django 2.0.7 on 2018-07-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('global_rank', models.IntegerField(unique=True)),
                ('matches_won', models.IntegerField(default=0)),
                ('type_speed', models.IntegerField(default=0)),
                ('letters_typed', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('LI', 'Log In'), ('L', 'Lobby'), ('P', 'Playing'), ('O', 'Offline')], max_length=10)),
                ('local_rank', models.IntegerField(null=True)),
            ],
        ),
    ]
