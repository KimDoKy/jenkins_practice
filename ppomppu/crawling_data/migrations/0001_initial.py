# Generated by Django 2.1.5 on 2019-01-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('category', models.CharField(max_length=10)),
                ('write_date', models.CharField(max_length=10)),
                ('detail_link', models.URLField()),
                ('prod_image', models.URLField(blank=True, null=True)),
                ('crawling_data', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]