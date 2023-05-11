# Generated by Django 4.1.7 on 2023-05-02 11:03

from decimal import Decimal

import apps.base.fields
import django.core.validators
import django.db.models.deletion
import djmoney.models.fields
from django.core.management import call_command
from django.db import migrations, models


def load_fixtures(apps, schema_editor):
    call_command(
        'loaddata',
        'apps/payment_accounts/fixtures/owner.json',
        verbosity=0,
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('user_uuid', models.UUIDField(db_index=True, editable=False, unique=True)),
                (
                    'balance_currency',
                    djmoney.models.fields.CurrencyField(
                        choices=[('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')],
                        default='RUB',
                        editable=False,
                        max_length=3,
                    ),
                ),
                (
                    'balance',
                    apps.base.fields.MoneyField(
                        decimal_places=2,
                        default=Decimal('0.00'),
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Insufficient Funds',
                            ),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'revenue_currency',
                    djmoney.models.fields.CurrencyField(
                        choices=[('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')],
                        default='RUB',
                        editable=False,
                        max_length=3,
                    ),
                ),
                (
                    'revenue',
                    apps.base.fields.MoneyField(
                        decimal_places=2,
                        default=Decimal('0.00'),
                        editable=False,
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Insufficient Funds',
                            ),
                        ],
                    ),
                ),
                (
                    'income_currency',
                    djmoney.models.fields.CurrencyField(
                        choices=[('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')],
                        default='RUB',
                        editable=False,
                        max_length=3,
                    ),
                ),
                (
                    'income',
                    apps.base.fields.MoneyField(
                        decimal_places=2,
                        default=Decimal('0.00'),
                        editable=False,
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Insufficient Funds',
                            ),
                        ],
                    ),
                ),
                (
                    'commission',
                    apps.base.fields.CommissionField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Should be positive value',
                            ),
                            django.core.validators.MaxValueValidator(
                                100,
                                message='Should be not greater than 100',
                            ),
                        ],
                    ),
                ),
                ('frozen_time', models.DurationField()),
                ('gift_time', models.DurationField()),
                ('payout_day_of_month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BalanceChange',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'amount_currency',
                    djmoney.models.fields.CurrencyField(
                        choices=[('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')],
                        default='RUB',
                        editable=False,
                        max_length=3,
                    ),
                ),
                (
                    'amount',
                    apps.base.fields.MoneyField(
                        decimal_places=2,
                        default=Decimal('0.00'),
                        editable=False,
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Should be positive value',
                            ),
                        ],
                    ),
                ),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_accepted', models.BooleanField(default=False)),
                (
                    'operation_type',
                    models.CharField(
                        choices=[('WD', 'WITHDRAW'), ('DT', 'DEPOSIT')],
                        max_length=20,
                    ),
                ),
                (
                    'account_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='balance_changes',
                        to='payment_accounts.account',
                    ),
                ),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.RunPython(load_fixtures),
    ]
