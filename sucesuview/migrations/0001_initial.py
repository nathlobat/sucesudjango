# Generated by Django 2.0.7 on 2018-07-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_evento', models.CharField(max_length=200)),
                ('sobre_evento', models.TextField()),
                ('local_evento', models.CharField(max_length=200)),
                ('data_evento', models.DateTimeField()),
                ('imagem_evento', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]