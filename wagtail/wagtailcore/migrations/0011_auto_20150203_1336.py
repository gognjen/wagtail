# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/'),
            preserve_default=True,
        ),
    ]
