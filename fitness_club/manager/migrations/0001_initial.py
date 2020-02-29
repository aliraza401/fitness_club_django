# Generated by Django 3.0.3 on 2020-02-27 10:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=255)),
                ('height', models.FloatField(max_length=255)),
                ('weight', models.FloatField(max_length=255)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('username', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=55)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(max_length=255)),
                ('month', models.CharField(max_length=255)),
                ('date_paid', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee', to='manager.Member')),
            ],
        ),
    ]