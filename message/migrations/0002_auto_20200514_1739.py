# Generated by Django 2.2.10 on 2020-05-14 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagestatus',
            name='configuration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Configuration'),
        ),
        migrations.AddField(
            model_name='messagestatus',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_messagestatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagestatus',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.Message'),
        ),
        migrations.AddField(
            model_name='messagestatus',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_messagestatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_message', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='status_detail',
            field=models.ManyToManyField(blank=True, through='message.MessageStatus', to='settings.Configuration'),
        ),
        migrations.AddField(
            model_name='message',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_message', to=settings.AUTH_USER_MODEL),
        ),
    ]
