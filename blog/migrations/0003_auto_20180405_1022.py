# Generated by Django 2.0.3 on 2018-04-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180402_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=500, verbose_name='文章摘要'),
        ),
    ]
