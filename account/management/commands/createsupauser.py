from django.core.management.base import BaseCommand
from account.models import UserAccount

from account.models import UserAccount

class Command(BaseCommand):
    help = 'Create super user (nhien/1234) to edit in admin site'
    
    # Create new usersuper (nhien/1234)
    def handle(self, *args, **options):
        user = UserAccount.objects.create_user(name='nhien',email='nhien')
        user.set_password("1234")
        
        # Set super user tags
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        
        # Save new superuser and notify
        user.save()
        print("Created supa user")
        
        return