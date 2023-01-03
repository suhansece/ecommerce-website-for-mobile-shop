# Generated by Django 4.1.4 on 2023-01-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/')),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=255)),
            ],
        ),
    ]
