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
    
    
