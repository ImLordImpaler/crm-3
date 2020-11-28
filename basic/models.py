from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Customer(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    age = models.IntegerField(default=10)
    phone = models.CharField(max_length=10 , blank=True , null=True)
    root = models.OneToOneField(User , on_delete=models.CASCADE)
    def __str__(self):
        return self.root.username
@receiver(post_save , sender=User)
def update_user_profile(sender , instance , created , **kwargs):
    if created: 
        Customer.objects.create(root=instance)
    instance.customer.save()

# Services LIST OF SERVICES
GENDER_TYPES = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others') 
    ]

class Service(models.Model):
    name = models.CharField(max_length=100 , null=True ,blank=True)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    mprice = models.IntegerField(default=0)
    gender = models.CharField(max_length=10 , choices=GENDER_TYPES , default='others')
    def __str__(self):
        return (self.name + ' (' + self.gender + ' )')


#LIST OF CATEGORIES


class Category(models.Model):
    name = models.CharField(max_length=100 , null=True , blank=True)
    service = models.ForeignKey(Service , on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100 ,null=True , blank=True )
    bprice = models.IntegerField(default=0 , null=True  , blank=True)
    sprice = models.IntegerField(default=0 , null= True , blank=True)
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    quantity = models.IntegerField(default=10)
    img = models.ImageField(null=True , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


#ENQUIRY

ENQUIRY_TYPE = [
        ('warm', 'warm'),
        ('normal', 'normal'),
        ('cold', 'cold') 
    ]
class Enquiry(models.Model):
    name = models.CharField(max_length=100 , null=True  , blank=True)
    phone = models.CharField(max_length=100 , null=True  , blank=True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    responseType = models.CharField(null=True , blank=True , max_length=100)
    response = models.CharField(max_length= 10 , choices=ENQUIRY_TYPE , default='cold')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    age = models.IntegerField(default=18 )
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True, blank=True)
    def __str__(self):
        return self.name 


class Client(models.Model):
    name = models.CharField(max_length= 100 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True , blank=True)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    address = models.CharField(max_length=500 , null=True , blank=True)

    def __str__(self):
        return self.name

class Slip(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    phone = models.CharField(max_length=10 , null=True )
    client = models.ForeignKey(Client , on_delete = models.CASCADE  , null=True , blank=True)
    service = models.ForeignKey(Service , on_delete= models.CASCADE , null=True , blank=True)
    product = models.ForeignKey(Product , on_delete = models.CASCADE , null=True , blank=True)
    emp = models.ForeignKey(Employee , on_delete = models.CASCADE)
    time = models.TimeField(auto_now=True)
    

    def __str__(self):
        return self.emp.name


class Bill(models.Model):
    date = models.DateField(auto_now=True )
    number = models.CharField(max_length=10 , null=True)
    client = models.ForeignKey(Employee , on_delete=models.CASCADE)
    slip = models.ManyToManyField(Slip )
    def __str__(self):
        return (self.client.name )
    
    
    
    






