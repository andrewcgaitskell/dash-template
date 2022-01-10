thank you to:
https://thucnc.medium.com/how-to-create-a-sudo-user-on-ubuntu-and-allow-ssh-login-20e28065d9ff

The sudo command is used to allow a permitted user to execute a command as the superuser or another user, as specified by the security policy.

In this guide, I will show you how to create a new user on an Ubuntu server and give it sudo access and allow SSH login to that user.

# Create a sudo user
1. Log in to your server as the user with superuser privilege

$ ssh root@server_address

# Create a new user account

For this, we use adduser command. Don’t be confused with the useradd command here. useradd is a low level binary command compiled with the system, whereas adduser is a high level Perl script built on top of useradd.

You should always use adduser to create new user as it provides more user friendly and interactive procedure.

$ sudo adduser newuser

Then follow the instruction to finish the procedure

   Adding user `newuser' ...
   Adding new group `newuser' (1005) ...
   Adding new user `newuser' (1004) with group `newuser' ...
   Creating home directory `/home/newuser' ...
   Copying files from `/etc/skel' ...
   Enter new UNIX password: 
   Retype new UNIX password: 
   passwd: password updated successfully
   Changing the user information for newuser
   Enter the new value, or press ENTER for the default
    Full Name []: Thuc Nguyen                
    Room Number []: 1234
    Work Phone []: 0123456789
    Home Phone []: 0987654321
    Other []: 
   Is the information correct? [Y/n] Ysudo

# Add the user to the sudo group

$ usermod -aG sudo newuser

On Ubuntu, members of the sudo group have sudo privileges by default.

# Test

    Switch to the new user account

$ su - newuser

    Verify the superuser privileges by the sudo command

$ sudo ls -la /root

# Add public key to allow remote SSH login for the new user
1. Switch to the new user account

$ su - newuser

# Create .ssh folder in home directory

$ mkdir ~/.ssh

# Create authorized_keys file in side the .ssh folder and add the public key

Use your favorite text editor for this. I use vim here, for example:

$ vim ~/.ssh/authorized_keys

And paste your SSH public key here, save and close file

# Verify SSH remote login

Open another terminal on your machine and try to remote SSH login using new user.

$ ssh newuser@server_address

This should work if you have your SSH private key in ~/.ssh/id_rsa file, otherwise you must specify the path to your private key with -i option:

$ ssh -i path_to_your_ssh_private_key newuser@server_address

# If you can login successfully, congratulations!
