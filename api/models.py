from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50 , null=True)

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    place = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'



class Message(models.Model):
    reciever_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever')
    sender_user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='sender')
    date = models.DateField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=50)
    content=models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.sender_user} {self.type} {self.reciever_user}'


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class FollowUp(models.Model):
    followUp_id = models.IntegerField()
    record_date = models.DateField(auto_now=False, auto_now_add=False)
    followUp_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.followUp_id} {self.owner}'



class Meal(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Rest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    meal=models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user} {self.meal} {self.group} {self.date}'
