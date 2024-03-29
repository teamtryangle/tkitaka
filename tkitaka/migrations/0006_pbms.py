# Generated by Django 2.2.5 on 2019-09-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkitaka', '0005_auto_20190925_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='PBMS',
            fields=[
                ('_PBMSID', models.AutoField(primary_key=True, serialize=False, verbose_name='PBMS번호')),
                ('accommondation', models.CharField(max_length=1, verbose_name='숙박')),
                ('meal', models.CharField(max_length=1, verbose_name='식사')),
                ('sTransportation', models.CharField(max_length=1, verbose_name='근거리 이동')),
                ('lTransportation', models.CharField(max_length=1, verbose_name='장거리 이동')),
                ('expense', models.CharField(max_length=1, verbose_name='경비')),
                ('preplan', models.CharField(max_length=1, verbose_name='사전계획')),
                ('spending', models.CharField(max_length=1, verbose_name='지출')),
                ('flight', models.CharField(max_length=1, verbose_name='항공')),
                ('guide', models.CharField(max_length=1, verbose_name='가이드')),
                ('smoking', models.CharField(max_length=1, verbose_name='흡연')),
                ('memberID', models.CharField(max_length=1, verbose_name='식사')),
            ],
        ),
    ]
