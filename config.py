from dotenv import load_dotenv
load_dotenv()


import os


# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY")

# MySQL Database
# MySQL Database
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# Email Settings
MAIL_SERVER = "smtp-relay.brevo.com"
MAIL_PORT = 587
MAIL_USE_TLS = True

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")


# Razorpay
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")


RESEND_API_KEY = os.getenv("RESEND_API_KEY")




#This file stores database settings & secret key.
# config.py
# ------------------------------------
# This file holds all configurations
# like Secret Key, Database connection
# details, Email settings, Razorpay keys etc.
# ------------------------------------

