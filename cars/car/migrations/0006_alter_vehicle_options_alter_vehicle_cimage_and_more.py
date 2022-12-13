# Generated by Django 4.1.4 on 2022-12-11 11:14

import cars.core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0005_vehicle_publication_date_alter_vehicle_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ('-publication_date', 'manufacturer', 'model')},
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='cimage',
            field=models.ImageField(upload_to='cars', validators=[cars.core.validators.validate_file_max_size_2mb], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]