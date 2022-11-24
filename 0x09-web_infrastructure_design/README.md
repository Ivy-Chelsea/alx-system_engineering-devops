## WEB INFRASTRUCTURE DESIGN

# 0-simple_web_stack
* A one server web infrastructure design that hosts the website reachable via ww.foobar.com with the following requirements:
* A server
* A web server(Nginx)
* An application server
* A pplication files,
* A database(SQL)
* A domain name foobar.com configured with www record that points to 8.8.8.8 IP server

# 1-distributed_web_infrastructure
* A three server web infrastructure design that hosts the website ww.foobar.com with the foolowing requirements:
* 2 servers
* A web server (Nginx)
* An applcation server
* A load-balancer(HAproxy)
* A set of application files
* A database(MySQL)

# 2-secured_and_monitored_web_infrastructure
* A three server web infrastructure design that hosts website ww.foobar.com with the following requirements:
* 3 firewalls
* 1 SSL certificate to serve ww.foobar.com over HTTPS
* 3 monitoring clients(data collector for Sumlogic or any other monitoring services)

# 3-scale_up
* A web infrastructure with the following requirements:
* A server
* A load-balancer(HAproxy) configured as clustr with the one
* Split components(web server, application server, database) with their ow server
