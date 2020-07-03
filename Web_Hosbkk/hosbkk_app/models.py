from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project_subgroup(models.Model):
    name = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " : " + str(self.project_id)

class Hospitals(models.Model):
    code = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    h_type = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code + " : " + self.label

class Service(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=255)
    modified_user_id = models.CharField(max_length=255)
    project_subgroup_id = models.ForeignKey(Project_subgroup, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assigned_user_id = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    description = models.TextField()
    resolution = models.TextField()
    service_id = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    hospitals_id = models.ForeignKey(Hospitals, on_delete=models.DO_NOTHING)
    date_entered = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()
