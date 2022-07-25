**Azure**
1. Azire IMDS is a REST API that's available at a well-known, non-routable IP address (169.254.169.254).
2. IMDS is not a channel for sensitive data.
3. The Instance Metadata Service is only accessible from within a running virtual machine instance on a non-routable IP address.
4. Proxies should be bypassed when querying IMDS

**Additional Azure IMDS Parameters Queries**
1. Network Info
2. Azure VM Running Info 

