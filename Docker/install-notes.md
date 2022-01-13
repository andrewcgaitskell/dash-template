
# Installing Docker on Ubuntu

     sudo apt remove docker docker-engine docker.io containerd runc
     sudo apt update
     sudo apt-get install     ca-certificates     curl     gnupg     lsb-release
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share
    /keyrings/docker-archive-keyring.gpg
    echo   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archiv
    e-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

      sudo apt-get install docker-ce docker-ce-cli containerd.io

      sudo systemctl enable docker.service
       sudo systemctl enable containerd.service

# Create Jupyterhub Docker Image

https://github.com/jupyterhub/jupyterhub


# Create MYSQL Docker Image

https://betterprogramming.pub/customize-your-mysql-database-in-docker-723ffd59d8fb


