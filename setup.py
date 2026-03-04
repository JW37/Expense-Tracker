#!/usr/bin/env python3
"""
FaithLedger Quick Setup Script
Run this once after installing requirements.
"""
import os
import sys
import subprocess

def run(cmd):
    print(f"\n▶  {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(1)

print("=" * 60)
print("  FaithLedger – Church Account Management System Setup")
print("=" * 60)

# Run migrations
run("python manage.py migrate")

# Seed default categories
run("python manage.py seed_data")

# Create superuser
print("\n" + "=" * 60)
print("  Create Admin User")
print("=" * 60)
print("\nYou'll now create your admin/login account.")
print("Use your Gmail address as the username.\n")
run("python manage.py createsuperuser")

print("\n" + "=" * 60)
print("  ✅ Setup Complete!")
print("=" * 60)
print("\nRun the server with:")
print("  python manage.py runserver")
print("\nThen open: http://127.0.0.1:8000/")
print("\nAdmin panel: http://127.0.0.1:8000/admin/")
print("=" * 60)
