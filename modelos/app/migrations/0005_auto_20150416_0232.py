# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pato_bd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pato',
            name='bd',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
