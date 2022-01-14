
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

mkdir -p ~/my-mysql/sql-scripts

cd ~/my-mysql/sql-scripts

Now that the scripts are ready, we can write a Dockerfile to create our own Docker image (based on the official image of MySQL).

$ cd ~/my-mysql/
$ vi Dockerfile

Content of Dockerfile:

# Derived from official mysql image (our base image)
FROM mysql

# Add a database
ENV MYSQL_DATABASE company

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

Create your Docker image:

$ cd ~/my-mysql/
$ docker build -t my-mysql .


Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM mysql
latest: Pulling from library/mysql
Digest: sha256:691c55aabb3c4e3b89b953dd2f022f7ea845e5443954767d321d5f5fa394e28c
Status: Downloaded newer image for mysql:latest
 ---> 5195076672a7
Step 2/2 : ADD sql-scripts/ /docker-entrypoint-initdb.d/
 ---> 25065c3d93c0
Successfully built 25065c3d93c0
Successfully tagged my-mysql:latest

And start your MySQL container from the image:

$ docker run -d -p 3306:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=pythonuser my-mysql

Now we can verify. We will exec inside the container:

$ docker exec -it my-mysql bash
root@c86ff80d7524:/# mysql -uroot -p
Enter password: (supersecret)
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| company            |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)mysql> use company;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -ADatabase changed
mysql> show tables;
+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.00 sec)mysql> show columns from employees;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| first_name | varchar(25) | YES  |     | NULL    |       |
| last_name  | varchar(25) | YES  |     | NULL    |       |
| department | varchar(15) | YES  |     | NULL    |       |
| email      | varchar(50) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)mysql> select * from employees;
+------------+-----------+------------+-------------------+
| first_name | last_name | department | email             |
+------------+-----------+------------+-------------------+
| Lorenz     | Vanthillo | IT         | lvthillo@mail.com |
+------------+-----------+------------+-------------------+
1 row in set (0.01 sec)

It works! We have our customized MySQL database Docker image! This is a great solution for local development between multiple developers. By sharing the Docker image, every developer can use the database by just starting a container from the image.

It’s important to note, however, that this is not always the best solution:

    If you insert a lot of data your image size will grow significantly
    Need to build a new image when you want to update the data

That’s why there is another way to customize your Docker MySQL.
