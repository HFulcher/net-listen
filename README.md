# Network Connection Notifier

Simple Python script that checks for a MAC address on the local network specified in a .env file. Little afternoon project to see if this could be used as a way to notify that someone has arrived at home.

Issue currently encountered is that an idle MAC address will be seen intermitently on the arp-scan utility. Don't think there's much way around this unless if a 3-strikes policy is used.