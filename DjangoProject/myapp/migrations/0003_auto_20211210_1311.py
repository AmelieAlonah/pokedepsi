# Generated by Django 3.2.9 on 2021-12-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_teampokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampokemon',
            name='pokemon1',
            field=models.CharField(choices=[('Pikachu', 'Evoli'), ('Pikachutete', 'Evolitete'), ('Pikachueazrezr', 'Evoliazrr')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teampokemon',
            name='pokemon2',
            field=models.CharField(choices=[('Pikachu', 'Evoli'), ('Pikachutete', 'Evolitete'), ('Pikachueazrezr', 'Evoliazrr')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teampokemon',
            name='pokemon3',
            field=models.CharField(choices=[('Pikachu', 'Evoli'), ('Pikachutete', 'Evolitete'), ('Pikachueazrezr', 'Evoliazrr')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teampokemon',
            name='pokemon4',
            field=models.CharField(choices=[('Pikachu', 'Evoli'), ('Pikachutete', 'Evolitete'), ('Pikachueazrezr', 'Evoliazrr')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teampokemon',
            name='pokemon5',
            field=models.CharField(choices=[('Pikachu', 'Evoli'), ('Pikachutete', 'Evolitete'), ('Pikachueazrezr', 'Evoliazrr')], max_length=200, null=True),
        ),
    ]