# Generated by Django 4.1.2 on 2022-10-27 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.reporter')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]