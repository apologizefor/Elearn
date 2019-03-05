# Generated by Django 2.0.6 on 2019-03-05 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courseware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseawre_name', models.CharField(max_length=100, verbose_name='课件名称')),
                ('courseware_upload', models.FileField(max_length=200, upload_to='resources/courseware/%Y%m%d', verbose_name='课件路径')),
                ('courseawre_size', models.CharField(editable=False, max_length=20, verbose_name='课件大小')),
                ('courseware_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('courseware_download_nums', models.CharField(default=0, editable=False, max_length=10, verbose_name='下载量')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.TeacherProfile', verbose_name='老师')),
            ],
            options={
                'verbose_name': '课件',
                'verbose_name_plural': '课件',
                'db_table': 'courseware',
                'ordering': ['courseware_time'],
            },
        ),
    ]
