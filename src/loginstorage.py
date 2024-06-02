import keyring
import keyring.util.platform_ as keyring_platform
import bcrypt
import hashlib
import json

FOLDER_FOR_LOGINS = "AutoESignature-logins"  # Like a folder for organizing your secrets
URL_LABEL = "URL_LOGIN"      # A label for the specific url login
PASSWORD_LABEL = "SERVICE_PASSWORD"      # A label for the specific password
SALT_LABEL = "PASSWORD_SALT" # a label for storing the salt of password
