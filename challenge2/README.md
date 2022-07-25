# Technical Challenge #2
This folder contains Solution to Query the Metadata of an instance for AWS and Azure.

**Azure**
1. For Azure, we will use Azure Instance Metadata Service.
2. Azure IMDS is a REST API that's available at a well-known, non-routable IP address (169.254.169.254)
3. To retrieve all the metadata information of a Azure Instance: Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -NoProxy -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64. The response is a JSON string.


**AWS**
