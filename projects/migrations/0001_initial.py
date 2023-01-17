# Generated by Django 4.1.2 on 2023-01-17 02:44

from django.db import migrations, models
import django.db.models.deletion
import projects.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', projects.fields.CaseInsensitiveCharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('project_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('demo_link', models.CharField(blank=True, max_length=3000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=3000, null=True)),
                ('review_total', models.IntegerField(blank=True, default=0, null=True)),
                ('review_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('tags', models.ManyToManyField(blank=True, to='projects.tag')),
            ],
            options={
                'ordering': ['-review_ratio', '-review_total', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('very_good', 'Positive Review'), ('good', 'Negative Review')], max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'unique_together': {('owner', 'project')},
            },
        ),
    ]
