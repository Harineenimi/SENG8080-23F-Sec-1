# Generated by Django 4.1.7 on 2023-02-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allAppData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_scraper_order', models.CharField(blank=True, max_length=200, null=True)),
                ('web_scraper_order_start_url', models.TextField(blank=True, null=True)),
                ('app_link_txt', models.CharField(blank=True, max_length=500, null=True)),
                ('app_link_href', models.TextField(blank=True, null=True)),
                ('app_name', models.CharField(blank=True, max_length=500, null=True)),
                ('app_category', models.CharField(blank=True, max_length=200, null=True)),
                ('app_rating', models.CharField(blank=True, max_length=200, null=True)),
                ('app_rating_count', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_downloads', models.CharField(blank=True, max_length=200, null=True)),
                ('developer_email', models.CharField(blank=True, max_length=200, null=True)),
                ('last_update', models.CharField(blank=True, max_length=200, null=True)),
                ('privacy_policy', models.CharField(blank=True, max_length=500, null=True)),
                ('contains_ads', models.CharField(blank=True, max_length=200, null=True)),
                ('in_app_purchase', models.CharField(blank=True, max_length=200, null=True)),
                ('rated_for', models.CharField(blank=True, max_length=200, null=True)),
                ('reviews', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
