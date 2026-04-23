"""
Custom client-specific overrides.
This file is intentionally empty by default and should NOT be tracked by Git.
"""
import os
from .base import *

# # --- 1️⃣ Basic overrides ---
# DEBUG = False
# ALLOWED_HOSTS = ["client.example.com"]
# WHITE_LABELLING = True
# TWO_FACTORS_AUTHENTICATION = True


# # --- 2️⃣ Add extra apps ---
# # Make sure to extend, not replace
# INSTALLED_APPS += [
#     "client_portal",
#     "client_analytics",
# ]


# # --- 3️⃣ Add custom middleware ---
# MIDDLEWARE += [
#     "client_portal.middleware.ClientTrackingMiddleware",
# ]


# # --- 4️⃣ Override any other settings if needed ---
# TIME_ZONE = "Europe/Berlin"
# LANGUAGE_CODE = "de"
# Database connection pooling
DATABASES['default'].update({'CONN_MAX_AGE': 60})

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{env('REDIS_PASSWORD')}@127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 300,
    }
}

APPEND_SLASH = True
