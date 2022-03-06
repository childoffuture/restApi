# Generated by Django 4.0.2 on 2022-02-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_added_delete_perevaltest_delete_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pereval_added',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_parent', models.BigIntegerField()),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pereval_areas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('img', models.BinaryField()),
            ],
            options={
                'db_table': 'pereval_images',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Added',
        ),
    ]
