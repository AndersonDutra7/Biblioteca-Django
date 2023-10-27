# Generated by Django 4.2.6 on 2023-10-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('book_cover', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('qtd', models.IntegerField()),
                ('in_stock', models.BooleanField(default=False)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_biblioteca.genders')),
            ],
        ),
    ]
