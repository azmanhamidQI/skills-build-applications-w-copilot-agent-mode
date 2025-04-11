from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    created_at = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)