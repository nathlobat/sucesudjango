# Generated by Django 2.0.7 on 2018-07-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucesuview', '0004_auto_20180725_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiretoriaAtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='images/diretoria/%Y-%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(upload_to='images/eventos/%Y-%m/%d'),
        ),
    ]