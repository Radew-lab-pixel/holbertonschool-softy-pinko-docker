FROM nginx:latest

# Copy front-end files to Nginx's default web root
COPY softy-pinko-front-end  /var/www/html/softy-pinko-front-end 

# Override default Nginx config in docker image
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Expose port 9000 (custom port to avoid conflicts)
EXPOSE 9000