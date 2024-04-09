# Generated by Django 4.2.3 on 2024-03-27 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus_or_resv', '0002_bus_bus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Srcdst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('dest', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='bus',
            name='dest',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='source',
        ),
        migrations.AddField(
            model_name='bus',
            name='srcdst',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bus_or_resv.srcdst'),
            preserve_default=False,
        ),
    ]