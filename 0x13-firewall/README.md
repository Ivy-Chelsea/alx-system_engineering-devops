# FIREWALL

##  0-block_all_incoming_traffic_but
~ File contaiming installation instruction of ufw firewall and setup rules on web-01 with the following requirements:
- ufw should be configured so that it blocks all incoming traffic, except following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)
 
 ## 100-port_forwarding
 ~ File containing configuration of web-01 so that its firewall redirects port 8080/TCP to por 80/TCP
