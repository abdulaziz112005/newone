
# Generated by Django 3.1.4 on 2021-01-06 10:28

# Generated by Django 3.1.4 on 2021-01-06 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news')),
                ('views_count', models.IntegerField(blank=True, default=0)),
                ('is_actual', models.BooleanField(default=False)),
                ('is_columnist', models.BooleanField(default=False)),
                ('is_dephoto', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('tags', models.ManyToManyField(to='news.Tags')),
            ],
        ),
    ]
