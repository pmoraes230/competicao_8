from django.db import models


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'client'
        
    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    event_name = models.CharField(max_length=45)
    limit_peaple = models.BigIntegerField()
    date_event = models.DateField(unique=True)
    hour_event = models.TimeField(unique=True)
    description = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    image_event = models.ImageField(upload_to="event")

    class Meta:
        managed = False
        db_table = 'event'
        
    def __str__(self):
        return self.event_name

class Profile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'profile'
        
    def __str__(self):
        return self.name

class Sector(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    limit_ticket = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sector'
        
    def __str__(self):
        return self.name

class Ticket(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    event = models.ForeignKey(Event, models.DO_NOTHING, db_column='event')
    sector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sector_ID')  # Field name made lowercase.
    id_ticket = models.CharField(primary_key=True, max_length=50)
    date_issue = models.DateTimeField()
    status = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'ticket'
        
    def __str__(self):
        return f"Ingresso no evento {self.event.event_name} - para o cliente {self.client.name}"

class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=50)
    cpf = models.CharField(unique=True, max_length=11)
    password = models.CharField(max_length=130)
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_ID')  # Field name made lowercase.
    name_completed = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.name