# =====================================
# PROVIDER CONFIGURATION
# =====================================
provider "azurerm" {
  features {}
  subscription_id = "6abb0618-87c3-4fc8-81d7-0b7ea10c511a"
}

# =====================================
# RESOURCE GROUP
# =====================================
resource "azurerm_resource_group" "rg" {
  name     = "rg-terraform-demo"
  location = "francecentral"
}

# =====================================
# STORAGE ACCOUNT (SECURE)
# =====================================
resource "azurerm_storage_account" "storage" {
  name                     = "blobpourcamille"  # globally unique
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"

  min_tls_version = "TLS1_2" # require TLS1.2
}

# =====================================
# PRIVATE BLOB CONTAINER
# =====================================
resource "azurerm_storage_container" "container" {
  name                  = "tf-container"
  storage_account_id  = azurerm_storage_account.storage.id
  container_access_type = "private"
}

# =====================================
# SAS TOKEN FOR CONTAINER (DATA SOURCE)
# =====================================
data "azurerm_storage_account_blob_container_sas" "container_sas" {
  connection_string  = azurerm_storage_account.storage.primary_connection_string
  container_name     = azurerm_storage_container.container.name
  https_only         = true

  start  = formatdate("YYYY-MM-DD'T'HH:mm:ss'Z'", timestamp())
  expiry = formatdate("YYYY-MM-DD'T'HH:mm:ss'Z'", timeadd(timestamp(), "24h"))

  permissions {
    read   = true
    write  = true
    delete = false
    list   = true
    add    = false
    create = false
  }
}


# =====================================
# OUTPUTS
# =====================================
output "storage_account_name" {
  value       = azurerm_storage_account.storage.name
}

output "container_name" {
  value       = azurerm_storage_container.container.id
}

output "curl_sas_command" {
  sensitive = true
  value       = "curl \"https://${azurerm_storage_account.storage.name}.blob.core.windows.net/${azurerm_storage_container.container.name}?${data.azurerm_storage_account_blob_container_sas.container_sas.sas}\""
  description = "Curl command including the SAS token to access the private container"
}
