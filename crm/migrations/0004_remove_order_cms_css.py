# Generated by Django 4.0.6 on 2022-10-02 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_order_cms_css'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cms_css',
        ),
    ]