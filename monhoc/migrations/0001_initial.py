# Generated by Django 4.0.4 on 2022-05-25 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lophoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonHoc',
            fields=[
                ('maMonHoc', models.AutoField(primary_key=True, serialize=False)),
                ('tenMonHoc', models.CharField(default='', max_length=50)),
                ('moTa', models.CharField(default='', max_length=100)),
                ('lopHoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lophoc.lophoc')),
                ('maGiaoVienDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
