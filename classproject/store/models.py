from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.




class Product_table(models.Model):
    product_id = models.AutoField(primary_key=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    product_name = models.CharField(unique=False, max_length=50)
    date_upload = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(unique=False)
    price = models.CharField(unique=False, max_length=11)
    description = models.CharField(unique=False, max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='productImage/', unique=False)
    status = models.CharField(unique=False, max_length=20, null=True)


class staff_table(models.Model):

    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("United StatesOf America", "USA")
    ]

    states = [
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Ogun", "Ogun"),
        ("Lagos", "Lagos"),
        ("Kano","kano"),
        ("Abuja", "Abuja"),
    ]

    

    staff_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    profile_picture = models.ImageField(upload_to='staffImage/', unique=False)
    status = models.CharField(unique=False, max_length=100, null=True)
    position = models.CharField(unique=False, max_length=100, null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    nationality = models.CharField(choices=countries, unique=False, max_length=100, null=True)
    state = models.CharField(choices=states, unique=False, max_length=100, null=True)
    identification = models.ImageField(upload_to='staffid/', unique=False, null=True)
    particulars = models.FileField(upload_to='staffid/', unique=False, null=True)
    staff_passport = models.FileField(upload_to='staffid/', unique=False, null=True)
    


class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("United StatesOf America", "USA"),

    ]

    states = [
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Ogun", "Ogun"),
        ("Lagos", "Lagos"),
        ("Kano","kano"),
        ("Abuja", "Abuja"),
    ]

    job_status = [
        ("Active", "Active"),
        ("Suspended", "Suspended"),
        ("Resigned", "Resigned"),
        ("Fired", "Fired"),
    ]

    position = [
        ("CEO" , "CEO"),
        ("GMD" , "GMD"),
        ("CTO" , "CTO"),
        ("Supervisor" , "Supervisor"),
        ("Accountant" , "Accountant"),
        ("Staff" , "Staff"),
        ("HR" , "HR"),
    ]

    
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    status = models.CharField( unique=False, max_length=100, null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    nationality = models.CharField( unique=False, max_length=100, null=True)
    state = models.CharField( unique=False, max_length=100, null=True)
    identification = models.ImageField(upload_to='staffid/', unique=False, null=True)
    particulars = models.FileField(upload_to='staffid/', unique=False, null=True)
    profile_picture = models.ImageField(upload_to='staffImage/', unique=False)
    profile_passport = models.FileField(upload_to='staffid/', unique=False, null=True)
    position = models.CharField(unique=False, max_length=100, null=True)

# Now this is where th magic happens , we will now define signals 
# automatically created/updated when we create / update user instace
    @receiver(post_save, sender= User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        

    @receiver(post_save, sender= User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()




# class Invoice_table(models.Model):
#     invoice_id = models.AutoField(primary_key=True)
#     date_cashout = models.DateTimeField(default=timezone.now)
#     order_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_price = models.CharField(unique=False, max_length=11)
#     cashout = models.BooleanField(unique=False)


# class Order_table(models.Model):
    # order_id = models.AutoField(primary_key=True)
    # date_purchased = models.DateTimeField(default=timezone.now)
    # product = models.ForeignKey(Product_table, on_delete=models.CASCADE)
    # order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # quantity = models.IntegerField(unique=False)
    # price = models.CharField(unique=False, max_length=11)
    # purchaged = models.BooleanField(default=False, unique=False)
