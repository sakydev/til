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

- Install Pyenv and Python3
- Install nvm, npm (7.7.6), node (15.14.0)
- Install docker
