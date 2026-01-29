from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, ListField, ReferenceField
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
import uuid

class User(Document):
    """Custom User model for MongoDB"""
    
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('organizer', 'Organizer'),
        ('participant', 'Participant'),
    ]
    
    id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    email = EmailField(unique=True, required=True)
    password_hash = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    department = StringField(null=True)
    year = StringField(null=True)
    role = StringField(choices=ROLE_CHOICES, default='participant')
    profile_picture = StringField(null=True)
    bio = StringField(null=True)
    phone = StringField(null=True)
    
    # Status flags
    is_active = BooleanField(default=True)
    is_verified = BooleanField(default=False)
    
    # OAuth
    oauth_providers = ListField(default=[])
    
    # Timestamps
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'users',
        'indexes': ['email', 'is_active'],
    }
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = make_password(password)
    
    def check_password(self, password):
        """Verify password"""
        return check_password(password, self.password_hash)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
    class Meta:
        app_label = 'auth_app'
