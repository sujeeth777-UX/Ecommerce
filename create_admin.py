import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth.models import User

# Check if a superuser already exists
if not User.objects.filter(is_superuser=True).exists():
    print("Creating admin superuser...")
    # Change the username and password below if you want something different
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created successfully!")
else:
    print("Superuser already exists. Skipping creation.")
