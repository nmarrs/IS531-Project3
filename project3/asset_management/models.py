from django.db import models


class Location(models.Model):
    ''' A model that represents a location object '''
    LOCATIONS = (
        ('SJ', 'San Jose, CA, USA'),
        ('LA', 'Los Angeles, CA, USA'),
        ('D', 'Denver, CO, USA'),
        ('M', 'Madrid, Spain'),
        ('P', 'Paris, FrancLe'),
        ('B', 'Beijing, China'),
    )
    location = models.TextField(blank=True, null=True, choices=LOCATIONS)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.location)


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
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}, {}'.format(self.pk, self.name, self.description)


class Employee(models.Model):
    ''' A model that represents a location object '''
    ROLE_TYPES = (
        ('A', 'Admin'),
        ('M', 'Manager'),
        ('E', 'Employee'),
    )
    name = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True, choices=ROLE_TYPES)

    def __str__(self):
        return '{}: {}, {}'.format(self.pk, self.name, self.role)

class Asset(models.Model):
    ''' A model that represents an asset object '''
    ASSET_NAMES = (
        ('computer', 'Computer'),
        ('phone', 'Phone'),
        ('software', 'Software'),
        ('car', 'Car'),
        ('rocket', 'Rocket'),
    )
    location = models.ForeignKey(Location, blank=True)
    organization = models.ForeignKey(Organization, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True)
    employee = models.ForeignKey(Employee, blank=True)
    tag = models.CharField(blank=True, null=True, max_length=10, unique=True)
    name = models.TextField(blank=True, null=True, choices=ASSET_NAMES)
    description = models.TextField(blank=True, null=True)
    maintenance_notes = models.TextField(blank=True, null=True)
    date_acquired = models.TextField(blank=True, null=True, default='July, 2000')
    date_implemented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}, {}, {}, {}, {}'.format(self.pk, self.tag, self.name, self.description, self.maintenance_notes, self.date_implemented)
