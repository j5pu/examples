FROM python
MAINTAINER Jack Sullivan

# Install nginx
RUN apt-get update -y && apt-get install -y nginx sudo
RUN rm -rf /etc/nginx/sites-enabled
RUN ln -s /data/nginx/sites-enabled /etc/nginx/sites-enabled

# Install devpi packages
RUN pip install --upgrade pip
RUN pip install devpi-server devpi-web devpi-client

# Copy init script
COPY entrypoint.sh /data/entrypoint.sh
RUN chmod +x /data/entrypoint.sh

# Create devpi user and directory
RUN mkdir -p /data/devpi/server
RUN useradd -s /bin/bash -G daemon -m -d /data/devpi devpi
RUN chown devpi:devpi /data/devpi/server
ENV DEVPI_SERVERDIR=/data/devpi/server
WORKDIR /data/devpi

# Expose proxy port
EXPOSE 80

# Run devpi-server
ENTRYPOINT ["/data/entrypoint.sh"]
