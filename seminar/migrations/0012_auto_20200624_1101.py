# Generated by Django 3.0.7 on 2020-06-24 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0011_auto_20200624_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='ref_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommends', to='seminar.Link'),
        ),
    ]