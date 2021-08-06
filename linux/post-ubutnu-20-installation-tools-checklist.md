### Ubtunu 20 Post Installation Checklist

- Run an update first
      
```
apt-get update
```

- Install necessary dev tools
      
```
apt-get install zip unzip wget curl youtube-dl git subversion
```

- Install Sublime Text

```
apt-get update
sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common
curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt install sublime-text
```

- Install Google chrome

```
apt-get update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

- Install Apache, MySQL, PHP, PHPMyAdmin

Apache and MySQL
```
apt-get update
sudo apt install apache2
sudo apt install mysql-server
sudo mysql_secure_installation
```

PHP and some extensions

```
sudo apt install php libapache2-mod-php php-mysql
```

- Install nvm, npm (7.7.6), node (15.14.0)

NVM
```
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
source ~/.profile   
```

Node using NVM  
`nvm install 15.14.0`


- Install docker

```
apt-get update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install docker-ce
sudo systemctl status docker
```

- Install docker-compose

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
