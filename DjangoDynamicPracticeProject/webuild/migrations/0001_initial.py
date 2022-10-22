# Generated by Django 4.1.1 on 2022-10-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('add', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]