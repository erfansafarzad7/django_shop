# Generated by Django 5.0.4 on 2024-04-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')),
                ('username', models.CharField(blank=True, max_length=25, null=True, verbose_name='نام کاربری')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('code', models.PositiveSmallIntegerField(verbose_name='کد یکبار مصرف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')),
            ],
            options={
                'unique_together': {('phone_number', 'code')},
            },
        ),
    ]