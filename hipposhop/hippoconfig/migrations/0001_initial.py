# Generated by Django 2.0.6 on 2018-06-26 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='应用名称')),
                ('product_code', models.CharField(help_text='全部小写字母，可以使用下划线', max_length=256, verbose_name='应用代码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '产品配置',
                'verbose_name_plural': '产品配置',
            },
        ),
        migrations.CreateModel(
            name='ErrorCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(help_text='前两位标识错误类型，后三位标识具体的错误码，1x:系统错误, 2x:用户账号错误,3x:商品类错误, 4x:淘宝错误，5x:外部系统错误,9x:其它', unique=True, verbose_name='错误代码')),
                ('msg', models.CharField(help_text='错误信息', max_length=512, verbose_name='错误信息')),
                ('type', models.IntegerField(choices=[(10, '10-系统错误'), (20, '20-用户账号类错误'), (30, '30-商品类错误'), (50, '50-外部系统错误'), (90, '90-其它')], help_text='错误代码的前两位和错误类别代码要一致', verbose_name='错误类别')),
                ('level', models.IntegerField(choices=[(10, '调试-DEBUG'), (20, '通知-INFO'), (30, '警告-WARNING'), (40, '错误-ERROR'), (50, '致命错误-CRITICAL')], help_text='错误级别', verbose_name='错误级别')),
                ('memo', models.TextField(default='', max_length=1000, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '错误代码表',
                'verbose_name_plural': '错误代码表(规范)',
            },
        ),
        migrations.CreateModel(
            name='PlatformConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=256, verbose_name='平台名称')),
                ('platform_code', models.CharField(help_text='全部小写字母，可以使用下划线', max_length=256, verbose_name='平台代码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '平台配置',
                'verbose_name_plural': '平台配置',
            },
        ),
        migrations.CreateModel(
            name='ServiceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='配置名称')),
                ('key', models.CharField(db_index=True, max_length=128, verbose_name='Key')),
                ('value', models.TextField(verbose_name='Value')),
                ('status', models.IntegerField(choices=[(0, 'Enabled'), (1, 'Disabled'), (2, 'Discard')], default=0, verbose_name='状态')),
                ('description', models.CharField(max_length=256, verbose_name='备注')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('app_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hippoconfig.ApplicationConfig')),
                ('platform_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hippoconfig.PlatformConfig')),
            ],
            options={
                'verbose_name': '服务配置',
                'verbose_name_plural': '服务配置管理',
            },
        ),
    ]
