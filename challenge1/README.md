# Technical Challenge #1
This folder contains solution to 3-Tier Architecture for any environment.

Approach

1. Presentation Tier
    We have deployed web server called web-vm that is running the web site we are accessging. Network interface has public ip address and NSG was used so we can configure inbound rule to aloow tracffic only on port 80.

2. Application Tier
    The application tier has been deployed on a VM called demo-biz-vm that is running the business logic. It also has a network interface, demo-biz-vm-nic, but this network interface only has a private IP address, providing no mechanism for direct inbound connectivity to the server. It also has a network security group, demo-biz-nsg, that only allows access from the subnet of the presentation tier.

3. Data Tier
    Azure SQL Database server, demo-dbserver-abc123 stores the data for the application in a database called demo-sqldb. This tier of the application is solely concerned with the storage of data, and providing a method to access it.



Style
What all outside users will be able to access in architecture.
Presentation and data layers should not be accessible from outside.
Have separate subnets between tiers for security.
We will have two subnets , one for presentation and one for application layer in the virtual network.

Reproducibility
Usage of variables for all resources in three tiers so same code can be deployed in different environments by just updating the variable names.

Assumptions
Data tier is an Azure SQL Database server
Non business critical web application
PaaS services in place
