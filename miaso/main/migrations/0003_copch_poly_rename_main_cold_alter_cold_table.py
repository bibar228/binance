# Generated by Django 4.2 on 2023-05-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_images_main_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Main',
            new_name='Cold',
        ),
        migrations.AlterModelTable(
            name='cold',
            table=None,
        ),
    ]
