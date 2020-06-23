# Generated by Django 3.0.7 on 2020-06-23 08:43

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
            name='Link',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wrote_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostOfFreeSeminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('vote_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostOfRecruitSeminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('tag_kind', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostOfRequestSeminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('tag_kind', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('profile_url', models.URLField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommends', to='seminar.Link')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.CharField(max_length=200)),
                ('comment_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='seminar.Link')),
            ],
        ),
    ]
