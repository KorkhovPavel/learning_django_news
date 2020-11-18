# Generated by Django 3.0.2 on 2020-11-18 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201116_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.Category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
