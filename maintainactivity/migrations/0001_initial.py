# Generated by Django 2.1.3 on 2019-03-05 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SignUp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('time_posted', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SignUp.RegisteredUser')),
            ],
        ),
    ]
