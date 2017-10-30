
# Create a new model called 'User' with the information above.

Within app -> models.py

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Successfully create and run the migration files

python manage.py makemigrations
python manage.py migrate
python manage.py shell

# Using the shell:

# Dont forget to import:
from apps.APPNAME.models import *
#or 
from apps.APPNAME.models import Users

# Know how to retrieve all users.

Users.objects.all()

# Know how to get the last user.

Users.objects.last()

# Know how to get the first user.

Users.objects.first()

# Create a few records in the users

Users.objects.create(first_name="Brian", last_name="Kang", email_address="brian@me.com", age=21)
# another way
b = Users(first_name="Brian", last_name="Kang", email_address="brian@me.com", age=21)
b.age = "27" # editing a field
b.email = "briankk123@gmail.com" # editing a field
b.save()

# Know how to get the users sorted by their first name (order by first_name DESC)

Users.objects.all().order_by("-first_name")

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. 
#Know how to do this directly in the console using .get and .save.

user3 = Users.objects.get(id=3)
user3.last_name = 'yoo'
user3.save()

# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).

user4 = Users.objects.get(id=4)
user4.delete()
# or
Users.objects.get(id=4).delete()

# (optional) Ninja:
# Find a way to validate the data coming in to the shell.  
# For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.

















