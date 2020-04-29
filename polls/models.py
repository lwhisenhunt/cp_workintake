from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    clarity_project = models.CharField(max_length=25, null=True)
    ace_number = models.CharField(max_length=200, null=True, default='tbd')
    ace_approved = models.BooleanField(default=False)
    project_priority = models.CharField(max_length=200, null=True, default = 'low',choices = (('high','high'),('medium','medium'),('low','low')))
    requested_budget = models.FloatField(max_length=25, null=True, default='0')
    approved_budget = models.FloatField(max_length=25, null=True, default='0')
    status = models.CharField(max_length=200, null=True, default = 'Unknown',choices = (('Not Started','Not Started'),('In Progress','In Progress'),('Complete','Complete')))
    def __str__(self):
        return self.name

class Milestone(models.Model):
    name = models.CharField(max_length=200, null=True)
    project_name = models.CharField(max_length=200, null=True, default='tbd')
    justification = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return self.name

class Capability(models.Model):
    capability = models.CharField(max_length=200, null=True)
    milestone = models.ManyToManyField("Milestone", null=True)
    project_name = models.ForeignKey("Project", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    priority = models.TextField(null=True, default = 'low',choices = (('high','high'),('medium','medium'),('low','low')))
    product_type = models.CharField(max_length=200, null=True, default = 'service',choices = (('Zeus','Zeus'),('Athena','Athena'),('Monitor','Monitor')))
    discovery_complete = models.BooleanField(default=False)
    benefit = models.TextField(max_length=200, null=True)
    requirements_link = models.URLField(max_length=512)
    target_date = models.DateField(null=True)
    def __str__(self):
        return self.capability
    class Meta:
        verbose_name_plural='capabilities'
