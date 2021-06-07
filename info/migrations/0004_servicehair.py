# Generated by Django 3.2.4 on 2021-06-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_company_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicehair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
