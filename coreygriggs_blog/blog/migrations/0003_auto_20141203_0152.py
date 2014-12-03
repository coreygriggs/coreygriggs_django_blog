# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_headline_navmenuoptions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NavMenuOptions',
            new_name='NavMenuOption',
        ),
        migrations.AlterModelOptions(
            name='navmenuoption',
            options={'ordering': ['-created']},
        ),
    ]
