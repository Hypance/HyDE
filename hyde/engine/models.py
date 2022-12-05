# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Backtests(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    market = models.IntegerField(db_column='Market')  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='OrderType')  # Field name made lowercase.
    positiontype = models.IntegerField(db_column='PositionType')  # Field name made lowercase.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Backtests'


class Bots(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    market = models.IntegerField(db_column='Market')  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='OrderType')  # Field name made lowercase.
    positiontype = models.IntegerField(db_column='PositionType')  # Field name made lowercase.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.
    pricevolume = models.DecimalField(db_column='PriceVolume', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetids = models.TextField(db_column='AssetIds')  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    formationids = models.TextField(db_column='FormationIds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    strategyids = models.TextField(db_column='StrategyIds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Bots'


class Candlesticks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    opentime = models.DateTimeField(db_column='OpenTime')  # Field name made lowercase.
    openprice = models.DecimalField(db_column='OpenPrice', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    highprice = models.DecimalField(db_column='HighPrice', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    lowprice = models.DecimalField(db_column='LowPrice', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    closeprice = models.DecimalField(db_column='ClosePrice', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    closetime = models.DateTimeField(db_column='CloseTime')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candlesticks'


class Formations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    backtestid = models.ForeignKey(Backtests, models.DO_NOTHING, db_column='BacktestId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.ForeignKey('Notifications', models.DO_NOTHING, db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Formations'


class Indicatorsignals(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    indicatorname = models.TextField(db_column='IndicatorName')  # Field name made lowercase.
    symbolname = models.TextField(db_column='SymbolName')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    signals = models.TextField(db_column='Signals')  # Field name made lowercase. This field type is a guess.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicatorSignals'


class Indicators(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    defaultperiod = models.IntegerField(db_column='DefaultPeriod')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicators'


class Notifications(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    market = models.IntegerField(db_column='Market')  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='OrderType')  # Field name made lowercase.
    positiontype = models.IntegerField(db_column='PositionType')  # Field name made lowercase.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.
    messagechannel = models.IntegerField(db_column='MessageChannel')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Signals(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    indicatorid = models.IntegerField(db_column='IndicatorId')  # Field name made lowercase.
    signalresult = models.IntegerField(db_column='SignalResult')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.
    strategyid = models.ForeignKey('Strategies', models.DO_NOTHING, db_column='StrategyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Signals'


class Strategies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    backtestid = models.ForeignKey(Backtests, models.DO_NOTHING, db_column='BacktestId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.ForeignKey(Notifications, models.DO_NOTHING, db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Strategies'


class Symbols(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    minquantity = models.DecimalField(db_column='MinQuantity', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    maxquantity = models.DecimalField(db_column='MaxQuantity', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    backtestid = models.ForeignKey(Backtests, models.DO_NOTHING, db_column='BacktestId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.ForeignKey(Notifications, models.DO_NOTHING, db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Symbols'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'
