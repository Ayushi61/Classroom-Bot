# Generated by Django 3.1 on 2020-09-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_service', '0003_slackcred_bot_communication_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotServerEndpoint',
            fields=[
                ('log_bot_server_endpoint_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_name', models.CharField(max_length=1000)),
                ('endpoint_url', models.CharField(max_length=1000)),
                ('endpoint_name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'log_bot_server_endpoint',
            },
        ),
    ]
