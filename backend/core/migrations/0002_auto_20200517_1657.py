# Generated by Django 3.0.6 on 2020-05-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='basophils',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Basófilos'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='eosinophils',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Eosinófilos'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='hematocrit',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Hematócrito'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='hemoglobin',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Hemoglobina'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='leukocytes',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Leucócitos'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='lymphocytes',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Linfócitos'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='mch',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='MCH'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='mchc',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='MCHC'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='mcv',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='MCV'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='monocytes',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Monócitos'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='mpv',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='MPV'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='platelets',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='Plaquetas'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='rbc',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='RBC'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='rdw',
            field=models.DecimalField(decimal_places=30, max_digits=50, null=True, verbose_name='RDW'),
        ),
    ]
