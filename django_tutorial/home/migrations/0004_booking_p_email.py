# Generated by Django 4.2.3 on 2023-07-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='p_email',
            field=models.EmailField(default='rafnazcm@gmail.com', max_length=254),
        ),
    ]
