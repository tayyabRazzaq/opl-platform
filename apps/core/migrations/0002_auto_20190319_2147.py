# Generated by Django 2.1.7 on 2019-03-19 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('skills', models.TextField(default='')),
                ('biography', models.TextField(default='')),
                ('linkedin', models.CharField(default='', max_length=100)),
                ('github', models.CharField(default='', max_length=100)),
                ('slack', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
