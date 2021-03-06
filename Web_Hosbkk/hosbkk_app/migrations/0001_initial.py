# Generated by Django 3.0 on 2020-07-10 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('h_type', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_subgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('modified_user_id', models.CharField(max_length=255)),
                ('assigned_user_id', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('resolution', models.TextField()),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('hospitals_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosbkk_app.Hospitals')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosbkk_app.Project')),
                ('project_subgroup_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosbkk_app.Project_subgroup')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosbkk_app.Service')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hosbkk_app.Status')),
            ],
        ),
    ]
