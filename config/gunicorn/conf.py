name = 'docker_django'
loglevel = 'debug'
errorlog = '-'
acceslog = '-'


bind = "0.0.0.0:8000"
module = "myproject.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

# certfile = "/etc/letsencrypt/live/your_domain.com/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/your_domain.com/privkey.pem"