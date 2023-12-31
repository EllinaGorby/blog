# Generated by Django 3.2.12 on 2023-11-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('anons', models.TextField()),
                ('full_text', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='article_images')),
                ('articleCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articles.articlecategory')),
            ],
        ),
    ]
