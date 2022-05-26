# Generated by Django 4.0.4 on 2022-05-25 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lophoc', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monhoc', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiangDay',
            fields=[
                ('maKeHoachGiangDay', models.AutoField(primary_key=True, serialize=False)),
                ('hocKy', models.IntegerField()),
                ('namHoc', models.IntegerField()),
                ('maGiaoVienDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('maLopHoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lophoc.lophoc')),
                ('maMonHoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monhoc.monhoc')),
            ],
        ),
    ]
