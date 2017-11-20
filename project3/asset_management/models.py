from django.core.validators import RegexValidator
from django.db import models


class Location(models.Model):
    ''' A model that represents a location object '''
    LOCATIONS = (
        ('San Jose', 'San Jose, CA, USA'),
        ('Los Angeles', 'Los Angeles, CA, USA'),
        ('Denver', 'Denver, CO, USA'),
        ('Madrid', 'Madrid, Spain'),
        ('Paris', 'Paris, FrancLe'),
        ('Beijing', 'Beijing, China'),
    )
    office_location = models.TextField(blank=True, null=True, choices=LOCATIONS)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.office_location)


class Organization(models.Model):
    ''' A model that represents a organization object '''
    ORGANIZATION_NAMES = (
        ('MO', 'MyOrg'),
        ('EO', 'ExampleOrg'),
    )
    name = models.TextField(blank=True, null=True, choices=ORGANIZATION_NAMES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}, {}'.format(self.pk, self.name, self.description)


class Manufacturer(models.Model):
    ''' A model that represents a manufacturer object '''
    MANUFACTURER_NAMES = (
        ('Dell', 'Dell'),
        ('Apple', 'Apple'),
        ('Tesla', 'Tesla'),
        ('SpaceX', 'SpaceX'),
        ('Microsoft', 'Microsoft'),
    )
    name = models.TextField(blank=True, null=True, choices=MANUFACTURER_NAMES)
    part_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}, {}'.format(self.pk, self.name, self.description)


class Employee(models.Model):
    ''' A model that represents a location object '''
    ROLE_TYPES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    name = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True, choices=ROLE_TYPES)

    def __str__(self):
        return '{}: {}, {}'.format(self.pk, self.name, self.role)

class AssetName(models.Model):
    ''' A model that represents an asset name object.
    We added this in order to get a nice dropdown in the admin site,
    as well as to be able to manage the type of
    assets employees are able to input to reduce
    variability.
    '''
    ASSET_NAMES = (
        ('computer', 'Computer'),
        ('phone', 'Phone'),
        ('software', 'Software'),
        ('car', 'Car'),
        ('rocket', 'Rocket'),
    )
    name = models.TextField(blank=True, null=True, choices=ASSET_NAMES)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.name)

class Asset(models.Model):
    ''' A model that represents an asset object '''
    location = models.ForeignKey(Location, blank=True)
    organization = models.ForeignKey(Organization, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True)
    employee = models.ForeignKey(Employee, blank=True)
    name = models.ForeignKey(AssetName, blank=True, null=True)
    tag = models.CharField(blank=True, null=True, max_length=10, unique=True, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10 characters', code='nomatch')])
    description = models.TextField(blank=True, null=True)
    maintenance_notes = models.TextField(blank=True, null=True)
    date_acquired = models.DateField('date acquired', blank=True, null=True, default='2017-11-19')
    date_implemented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}, {}, {}, {}, {}'.format(self.pk, self.tag, self.name, self.description, self.maintenance_notes, self.date_implemented)
