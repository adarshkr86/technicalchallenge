# Technical Challenge #2
This folder contains Solution to Query the Metadata of an instance for AWS and Azure.

**Azure**
1. For Azure, we will use Azure Instance Metadata Service.
2. Azure IMDS is a REST API that's available at a well-known, non-routable IP address (169.254.169.254)
3. IMDS Response is in JSON Format.
4. Application is assumed to be hosted in Liux machine.
5. Following Additional Parameters are queried through IMDS Service: Networking Information, Running VM.

**AWS**
