# Current Laptop

Intel® Core™ i5-1035G1 Processor

CPU Specifications

    Total Cores 4
    Total Threads 8
    Max Turbo Frequency 3.60 GHz
    Processor Base Frequency 1.00 GHz
    
Memory

  8 Gb
  
# Created VM

# VM Setup

    sudo apt update
    sudo apt upgrade
    sudo apt install nodejs
    sudo apt install npm
    sudo apt install python3-pip
    git clone https://github.com/andrewcgaitskell/dash-template.git
    cd dash-template
    pip install --user pipenv
    export PATH=$PATH:/home/andrew_gaitskell/.local/bin
    echo $PATH
    sudo apt install software-properties-common
    
## installed python version

    python --version
    
    ### edit pipfile and add python version
    nano Pipfile
    
## install python packages

    pipenv --python 3.9.5 install pandas
    
## Jupyterlab Setting Up

    sudo npm install -g npm@8.3.0 to update
    ?? sudo npm install -g configurable-http-proxy
    sudo npm init
  
    npm install configurable-http-proxy

  
    pipenv install -r my_requirements_jupyterlab.txt
  
  
# install mysql

    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation utility
    
    ## root/pythonuser
    
    sudo /usr/bin/mysql -u root -p

# nginx

    sudo apt update
    sudo apt install nginx
    
# add sub domain

    https://uk.godaddy.com/help/add-a-subdomain-4080
    

# add https support

## certbot

    sudo apt install certbot python3-certbot-nginx

    sudo certbot --nginx -d andrewcgaitskell.com -d www.andrewcgaitskell.com - -d data.andrewcgaitskell.com

    Requesting a certificate for andrewcgaitskell.com and 2 more domains
    Performing the following challenges:
    http-01 challenge for andrewcgaitskell.com
    http-01 challenge for data.andrewcgaitskell.com
    http-01 challenge for www.andrewcgaitskell.com
    Waiting for verification...
    Cleaning up challenges
    Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/default
    Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/default
    Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/default
    Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/default
    Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/default
    Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/default
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Congratulations! You have successfully enabled https://andrewcgaitskell.com,
    https://www.andrewcgaitskell.com, and https://data.andrewcgaitskell.com
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Subscribe to the EFF mailing list (email: andrew@gaitskell.com).
    IMPORTANT NOTES:                                                                                                   
     - Congratulations! Your certificate and chain have been saved at:                                                 
       /etc/letsencrypt/live/andrewcgaitskell.com/fullchain.pem
       Your key file has been saved at:
       /etc/letsencrypt/live/andrewcgaitskell.com/privkey.pem
       Your certificate will expire on 2022-04-08. To obtain a new or
       tweaked version of this certificate in the future, simply run
       certbot again with the "certonly" option. To non-interactively
       renew *all* of your certificates, run "certbot renew"
     - If you like Certbot, please consider supporting our work by:
       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le

# check sites enabled file

    sudo nano /etc/nginx/sites-enabled/default



