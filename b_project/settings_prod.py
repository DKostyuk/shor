DEBUG = False			# there will no message for ERRORS
ALLOWED_HOSTS = ['*']	# we can input IP address of the server where we can run our project

#settings for db on server - standard construction
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',	#psycopg2 - connector Django & Postgres, have to be installed on the server
        'NAME': 'h49085c_db_shor',
        'USER': 'h49085c_dk',
        'PASSWORD': 'Tropinka123!',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}