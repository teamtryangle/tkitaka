# Generated by Django 2.2.5 on 2019-09-25 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tkitaka', '0006_pbms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbms',
            name='memberID',
            field=models.OneToOneField(max_length=1, on_delete=django.db.models.deletion.CASCADE, to='tkitaka.Member', verbose_name='회원번호'),
        ),
    ]