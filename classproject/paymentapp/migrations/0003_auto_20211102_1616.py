# Generated by Django 3.1.1 on 2021-11-02 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paymentapp', '0002_auto_20210914_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_table',
            name='delivery_agent',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Invoice_table',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_cashout', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_price', models.CharField(max_length=11)),
                ('cashout', models.BooleanField()),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]