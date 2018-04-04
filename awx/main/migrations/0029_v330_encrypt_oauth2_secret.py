# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 20:48
from __future__ import unicode_literals

import awx.main.fields
from django.db import migrations
import oauth2_provider.generators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_v330_modify_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth2application',
            name='client_secret',
            field=awx.main.fields.OAuth2ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=1024),
        ),
    ]
