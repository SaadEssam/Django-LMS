# Generated by Django 3.2.7 on 2021-09-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('متاح', 'متاح'), ('مستأجر', 'مستأجر'), ('مباع', 'مباع')], max_length=50, null=True),
        ),
    ]
