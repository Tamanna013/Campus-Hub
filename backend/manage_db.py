#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from mongoengine import connect, get_db
from decouple import config

# In manage_db.py, try changing these to empty strings temporarily:
db = connect(
    db=config('MONGO_DB_NAME', default='campus_management'),
    host=config('MONGO_HOST', default='localhost'),
    port=config('MONGO_PORT', default=27017, cast=int),
    # username='',  # Leave empty if no user is set up
    # password='',  # Leave empty if no user is set up
)

# Create indexes and initial data
from auth_app.models import User

print("✅ Database connected successfully!")
print(f"Database: {db.name}")

# Create collections
User.ensure_indexes()
print("✅ Indexes synchronized!")
print("✅ Indexes created!")


from django.contrib.auth.hashers import make_password

def create_admin():
    email = "admin@example.com"
    # Check if admin already exists
    if not User.objects(email=email).first():
        admin = User(
            email=email,
            first_name="Admin",
            last_name="User",
            role="admin",
            is_active=True,
            is_verified=True
        )
        # Use your model's helper to hash the password
        admin.set_password("admin123") 
        admin.save()
        print(f"👤 Superuser created: {email} (Password: admin123)")
    else:
        print("ℹ️ Superuser already exists.")

# Run the setup
print("✅ Database connected successfully!")
User.ensure_indexes()
create_admin()
print("✅ Setup complete!")