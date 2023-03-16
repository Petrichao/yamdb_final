# Generated by Django 3.2 on 2023-02-05 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre_title',
            new_name='GenreTitle',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
