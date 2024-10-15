import json
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser

USERTYPE_CHOICES={
    ("Councellor","councellor"),
    ("ADMIN", "admin"),
    ("PENDING","pending"),
    ("Rejected","rejected"),
    ("User","user")


}
STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Deactive"),
}
# Create your models here.
class Logintable(AbstractUser):
    otp=models.CharField(max_length=25,null=True,blank=True)
    user_type=models.CharField(max_length=30,null=True,choices=USERTYPE_CHOICES,default="pending")
    is_active = models.BooleanField(null=True,blank=True,default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions', )
    def __str__(self):    #  for displaying foreign key loginid in usertable default foreignkey username ayirikum
        return str(self.id)

class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        Logintable,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        unique=True,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    def generate_key(self):
        """Generate a random key for the token."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    def read_session(self):
        """Read session data from the session_dict attribute."""
        try:
            self.data_dict = json.loads(self.session_dict)
        except json.JSONDecodeError:
            self.data_dict = {}

    def write_back(self):
        """Write session data back to the session_dict attribute."""
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        """Get a value from the session data."""
        self.read_session()
        return self.data_dict.get(key, default)

    def set(self, key, value, save=True):
        """Set a value in the session data."""
        self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def update_session(self, tdict, save=True, clear=False):
        """Update session data with the provided dictionary."""
        self.read_session()
        if clear:
            self.data_dict = tdict
        else:
            self.data_dict.update(tdict)
        if save:
            self.write_back()

    def save(self, *args, **kwargs):
        """Override the save method to generate a key if not provided."""
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def str(self):
        """Return a string representation of the token."""
        return str(self.user) if self.user else str(self.id)


class Usertable(models.Model):
    login_id=models.OneToOneField(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=35,null=True,blank=True)
    age=models.CharField(max_length=35,null=True,blank=True)
    gender=models.CharField(max_length=35,null=True,blank=True)
    email=models.CharField(max_length=40,null=True,blank=True)
    place=models.CharField(max_length=40,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)

class Councellortable(models.Model):
    login_id=models.OneToOneField(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    fname=models.CharField(max_length=35,null=True,blank=True)
    lname=models.CharField(max_length=35,null=True,blank=True)
    age=models.CharField(max_length=35,null=True,blank=True)
    gender=models.CharField(max_length=35,null=True,blank=True)
    email=models.CharField(max_length=40,null=True,blank=True)
    place=models.CharField(max_length=40,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    pincode= models.CharField(max_length=40,null=True,blank=True)
    district=models.CharField(max_length=40,null=True,blank=True)
    state=models.CharField(max_length=40,null=True,blank=True)
    qualification=models.CharField(max_length=40,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)