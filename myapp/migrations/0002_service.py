# Generated by Django 4.0.5 on 2022-07-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='services/')),
                ('cover', models.ImageField(upload_to='services/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='services/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='services/')),
            ],
        ),
    ]
