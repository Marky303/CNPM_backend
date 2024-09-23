from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Manager class for user account with customized create user function
class UserAccountManager(BaseUserManager):
    # Function to create new user
    # By default django will not allow no password
    def create_user(self, email, name, password=None):
        # Raise error if there is no email
        if not email:
            raise ValueError('User must have an email address')
        
        # Normalizer normalizing email (lowercasing,...) 
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        # Hashing password for security reasons
        user.set_password(password)
        
        # Finally save the user
        user.save()
        return user

# Custom user model goes here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    # Important user fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Other informative user fields
    currentJob = models.CharField(max_length=50, default="Unemployed")
    currentLocation = models.CharField(max_length=120, default="Nowhere")
    shortDesc = models.CharField(max_length=100, default="Relatively hard-working and normal human being")
    
    # Choosing email as username for login/signup
    USERNAME_FIELD = 'email'
    
    # Required fields, must not be null
    REQUIRED_FIELDS = ['name']
    
    objects = UserAccountManager()
    
    # Functions to get user information
    def get_full_name(self):
        return self.name
    
    # Admin page default function
    def __str__(self):
        return self.name 

# EXAMPLE MODEL FOR TESTING
class Note(models.Model):
    # Foreign key
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    
    # Admin page default function
    def __str__(self):
        return self.body