#--------- Flask settings
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants
API_URL = "https://developerproject2function.azurewebsites.net/api"
