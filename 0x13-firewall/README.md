0-block_all_incoming_traffic_but
# Firewall Configuration on web-01

In this project, we'll be configuring the UFW (Uncomplicated Firewall) on the web-01 server to block all incoming traffic except for specific TCP ports. Below are the steps and commands used to achieve this configuration:

## Installation of UFW
First, we need to ensure that UFW is installed on the system. We can do this by running the following command:
```
sudo apt-get update
sudo apt-get install ufw
```

## Configure UFW Rules
Once UFW is installed, we'll configure it to block all incoming traffic except for SSH (port 22), HTTPS SSL (port 443), and HTTP (port 80). We can accomplish this with the following commands:
```
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow https
sudo ufw allow http
```

## Enable UFW
After configuring the rules, we need to enable UFW to start applying them. This can be done using the following command:
```
sudo ufw enable
```

## Verify UFW Status
To ensure that UFW is active and the rules are applied correctly, we can check its status with:
```
sudo ufw status
```

## Conclusion
By following the above steps and commands, we have successfully configured the UFW firewall on web-01 to block all incoming traffic except for SSH, HTTPS SSL, and HTTP. This helps enhance the security of the server by restricting access to only essential ports.

For any further configuration or troubleshooting, refer to the [UFW documentation](https://help.ubuntu.com/community/UFW).

---

