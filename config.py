"""
Save Restricted Content Bot Configuration


Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "28578880"))
API_HASH = os.environ.get("API_HASH", "5f8c87efde57e01d12c0ce98ffdf5928")


# ==============================
# Admin Configuration
# ==============================

# Add admin user IDs separated by commas in environment variables
ADMINS = [int(admin) for admin in os.environ.get("ADMIN", "6814614245").split("6814614245,") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "mongodb+srv://suman93:Ss3vpEjyecxM7kPY@cluster0.oq2n3ij.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "saverestricted02")


# ==============================
# Logging Configuration
# ==============================

# Replace with your Telegram log channel ID (example: -1001234567890)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003759762110"))


# ==============================
# Error Handling
# ==============================

# Set to True to send error messages to users
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
