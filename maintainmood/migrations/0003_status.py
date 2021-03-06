# Generated by Django 2.1.3 on 2019-02-20 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0001_initial'),
        ('maintainmood', '0002_auto_20190220_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('parent_mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintainmood.Mood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SignUp.RegisteredUser')),
            ],
        ),
    ]
