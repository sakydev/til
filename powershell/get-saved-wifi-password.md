### How to get saved wifi password

Following method can be used to retrieve password of a connection that you can automatically connect to because Windows remembers the password but you don't. You need to share password with a friend or you'd like to connect from other device. Just open powershell and run following command.

`netsh wlan show profile name=profilename key=clear`