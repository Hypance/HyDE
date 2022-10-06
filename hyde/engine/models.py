# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Backtests(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    market = models.TextField(db_column='Market')  # Field name made lowercase. This field type is a guess.
    ordertypes = models.TextField(db_column='OrderTypes')  # Field name made lowercase. This field type is a guess.
    positiontypes = models.TextField(db_column='Positiontypes')  # Field name made lowercase. This field type is a guess.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Backtests'


class Bots(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    markets = models.TextField(db_column='Markets')  # Field name made lowercase. This field type is a guess.
    ordertypes = models.TextField(db_column='OrderTypes')  # Field name made lowercase. This field type is a guess.
    positiontypes = models.TextField(db_column='PositionTypes')  # Field name made lowercase. This field type is a guess.
    trendstrategies = models.IntegerField(db_column='TrendStrategies')  # Field name made lowercase.
    pricevolume = models.DecimalField(db_column='PriceVolume', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bots'


class Formations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    signalresults = models.TextField(db_column='SignalResults')  # Field name made lowercase. This field type is a guess.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    backtestid = models.ForeignKey(Backtests, models.DO_NOTHING, db_column='BacktestId', blank=True, null=True)  # Field name made lowercase.
    botid = models.ForeignKey(Bots, models.DO_NOTHING, db_column='BotId', blank=True, null=True)  # Field name made lowercase.
    notificationid = models.ForeignKey('Notifications', models.DO_NOTHING, db_column='NotificationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Formations'


class Indicators(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    defaultperiod = models.IntegerField(db_column='DefaultPeriod')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    formationid = models.ForeignKey(Formations, models.DO_NOTHING, db_column='FormationId', blank=True, null=True)  # Field name made lowercase.
    signalid = models.ForeignKey('Signals', models.DO_NOTHING, db_column='SignalId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicators'


class Notifications(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    markets = models.TextField(db_column='Markets')  # Field name made lowercase. This field type is a guess.
    ordertypes = models.TextField(db_column='OrderTypes')  # Field name made lowercase. This field type is a guess.
    positiontypes = models.TextField(db_column='PositionTypes')  # Field name made lowercase. This field type is a guess.
    trendstrategy = models.IntegerField(db_column='TrendStrategy')  # Field name made lowercase.
    messagechannels = models.TextField(db_column='MessageChannels')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Signals(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    signalresults = models.TextField(db_column='SignalResults')  # Field name made lowercase. This field type is a guess.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    strategyid = models.ForeignKey('Strategies', models.DO_NOTHING, db_column='StrategyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Signals'


class Strategies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    backtestid = models.ForeignKey(Backtests, models.DO_NOTHING, db_column='BacktestId', blank=True, null=True)  # Field name made lowercase.
    botid = models.ForeignKey(Bots, models.DO_NOTHING, db_column='BotId', blank=True, null=True)  # Field name made lowercase.
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
    botid = models.ForeignKey(Bots, models.DO_NOTHING, db_column='BotId', blank=True, null=True)  # Field name made lowercase.
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
