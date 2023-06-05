from django.db import models
from .models import User

# Create your models here.
class User(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=24)
    Nickname = models.CharField(max_length=30, null=True, blank=True, default='username')
    Email = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.NullBooleanField()
    Age = models.IntegerField(null=True, blank=True)
    Image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)
    

class Pets(models.Model):
    PetID = models.IntegerField(primary_key=True)
    PetName = models.CharField(max_length=24)
    PetType = models.IntegerField()
    Level = models.IntegerField(null=True, blank=True)
    Exp = models.IntegerField(null=True, blank=True)
    OwnerID = models.ForeignKey(User, on_delete=models.CASCADE)
    ModeType = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)
    

class ChatHistory(models.Model):
    RecordID = models.CharField(max_length=30, primary_key=True)
    SenderID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    ReceiverID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    Content = models.CharField(max_length=100)
    SendTime = models.CharField(max_length=24)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)
    
class FriendRelationship(models.Model):
    FriendshipID = models.IntegerField(primary_key=True)
    UserID1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    UserID2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    CreateTime = models.CharField(max_length=24)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)
