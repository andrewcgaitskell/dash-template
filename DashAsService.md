
nano /etc/nginx/sites-enabled/yourdomain.com

paste the following content:

    server {
        listen 80;
        server_name yourdomain.com;  ####### change this
        proxy_buffering off;
        location / {
                proxy_pass http://localhost:8050;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_read_timeout 86400;
        }

        client_max_body_size 100M;
        error_log /var/log/nginx/error.log;
    }

## Enable and start the nginx service:

    systemctl enable nginx.service
    systemctl start nginx.service

## Install pip:

    apt update
    apt upgrade

    apt install python3-pip

## Create a new systemd service for running notebook



## Enable and start the service:

    sudo systemctl enable .service
    sudo systemctl start .service


Note

## To check the logs for voila:

    journalctl -u .service

## Go to Domain

Now go to yourdomain.com:8866 to access the voila application.

    http://yourdomain.com:8866
    
    http://andrewcgaitskell.com:8866
# voila_current
