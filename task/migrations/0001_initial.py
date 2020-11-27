# Generated by Django 2.1.7 on 2019-02-16 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registeruser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, unique=True)),
                ('lastname', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('mobile1', models.CharField(max_length=50)),
                ('mobile2', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='login_id', to='task.Login')),
            ],
        ),
    ]
