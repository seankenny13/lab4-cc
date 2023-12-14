import requests

# Replace the following placeholders with your Azure details
subscription_id = 'd9a879cf-79ca-4f8e-95b7-9f0a5973afe3'
resource_group = 'skvm_group'
location = 'UK South'
subnet = '10.0.0.0/22'
virtual_network = 'lab4-cc'

# Replace <YOUR_ACCESS_TOKEN> with your Azure AD access token
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzY2MzE3Y2ItZTk0OC00ZTVmLThjZWMtZGFiYzhlMmZkNWRhLyIsImlhdCI6MTcwMjUwOTk2MywibmJmIjoxNzAyNTA5OTYzLCJleHAiOjE3MDI1MTUwNDUsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84VkFBQUFyRS9MWWp0VDU4M1FLZkErZGJabDBmZC9uZWhpdlpHNHZUOEdleWtxRVhoaVpmSCtLdHZKamVQS3NsdVRGeDROeElITys1NFJJN3dNSmpnaGNkM2JxYXlFVDB2QWc3M1pURTJpMjcvK2NLOD0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwiYXBwaWRhY3IiOiIwIiwiY2Fwb2xpZHNfbGF0ZWJpbmQiOlsiMGVhOTRiMzUtMzdlYi00Njg5LWFhNGUtYWZmMmQwZWE1YmUwIl0sImZhbWlseV9uYW1lIjoiS2VubnkiLCJnaXZlbl9uYW1lIjoiU2VhbiIsImdyb3VwcyI6WyI4MTA4YzUwMy1kNjU2LTQyY2YtOGVlNC04OTQ0YWVmMGZhZGUiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCI4MzhhMjg5YS04NGE0LTRjYTgtYWVlYy1iMzFlYzFkNzFkNGEiLCI0ZGMwM2I5Zi0xYjZjLTQ0MTUtYWMwNS04MjQyNzEzYzc1MjAiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCJhYmQ0OWRmZC1jZWZiLTRjMzYtYWQ2Ny0yNWZkOWZmZDMzN2YiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiODkuMTAxLjYwLjIwMyIsIm5hbWUiOiJDMjE0NDM0MDQgU2VhbiBLZW5ueSIsIm9pZCI6ImUxM2IyNDUzLWY3MTctNGFjMC05Y2JhLTk5OWQ4NWE1YmQ0NyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQzOTI0IiwicHVpZCI6IjEwMDMyMDAxN0RBNDU0MzMiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUZRLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IlBfVHZ0SVVEVjhOOThQaEpjZDUyV2htOThOdGlSOThndEpDRjBSdVhXVzQiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQ0MzQwNEBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDQzNDA0QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiIya3V0WEczaVRFaVVlMVdZQTF3R0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfY2MiOlsiQ1AxIl0sInhtc19maWx0ZXJfaW5kZXgiOlsiNDkiXSwieG1zX3JkIjoiMC40MkxsWUJSaU5BUUEiLCJ4bXNfc3NtIjoiMSIsInhtc190Y2R0IjoxNTI1MzM4OTQxfQ.sQx_eH7FoF9IbgVfDZKZXUZPzaEh_Rru-KV3YLbcHhTPYFRgR7G19UZgDIP9T_4H1AF3DgKC5tZrwgvIOW5DRseNbqMNVa-SDW2Bo_T1dpGvks2S5BHt9SCz5W532ZgesAIL3jPMV0kdix3V7Ld2zB4_2wch5hq_cp8Vz9J4DokpC1TGhzyxw0kba0GF6QddWDhIEeEsq0JymNzYyvRow8yhBh3p_EFVSEbJUbw6vLVl3Ithlg5o15toq8B8MKvHQQ_h0Ps8YaXOvv6v-TR_81VQtFSkAU4D9rnJb6RD9xvCVoTanhB2FEM_6wMCwMRnJambdZ8Wr5gtsSmlfK6IDg"'



# Define API URLs
ip_address_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/publicIPAddresses/myPublicIP?api-version=2021-08-01'
network_interface_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/networkInterfaces/myNIC?api-version=2021-08-01'
virtual_machine_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/myVM?api-version=2021-08-01'

# Define headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Define the payload for IP address creation
ip_address_payload = {
    "location": location,
    "properties": {
        "publicIPAllocationMethod": "Dynamic"
    }
}

# Define the payload for network interface creation
network_interface_payload = {
    "location": location,
    "properties": {
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "properties": {
                    "privateIPAllocationMethod": "Dynamic",
                    "subnet": {
                        "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/virtualNetworks/{virtual_network}/subnets/{subnet}"
                    }
                }
            }
        ]
    }
}

# Define the payload for virtual machine creation
virtual_machine_payload = {
    "location": location,
    "properties": {
        "hardwareProfile": {
            "vmSize": "Standard_DS1_v2"
        },
        "osProfile": {
            "computerName": "myVM",
            "adminUsername": "azureuser",
            "adminPassword": "ChangePa$$word123"
        },
        "storageProfile": {
            "imageReference": {
                "publisher": "MicrosoftWindowsServer",
                "offer": "WindowsServer",
                "sku": "2012-R2-Datacenter",
                "version": "latest"
            },
            "osDisk": {
                "name": "myVMosdisk",
                "createOption": "FromImage",
                "caching": "ReadWrite"
            }
        },
        "networkProfile": {
            "networkInterfaces": [
                {
                    "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/networkInterfaces/myNIC"
                }
            ]
        }
    }
}

# Create Public IP Address
response_ip = requests.put(ip_address_url, headers=headers, json=ip_address_payload)
print(f'Create IP Address Status Code: {response_ip.status_code}')

# Create Network Interface
response_nic = requests.put(network_interface_url, headers=headers, json=network_interface_payload)
print(f'Create Network Interface Status Code: {response_nic.status_code}')

# Create Virtual Machine
response_vm = requests.put(virtual_machine_url, headers=headers, json=virtual_machine_payload)
print(f'Create Virtual Machine Status Code: {response_vm.status_code}')

