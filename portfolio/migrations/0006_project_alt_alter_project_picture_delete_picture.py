# Generated by Django 4.1.4 on 2022-12-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_description_demoimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='projectLogo/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
