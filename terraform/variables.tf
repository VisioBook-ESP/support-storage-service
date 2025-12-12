variable "resource_group_name" {
  type    = string
  default = "rg-terraform-demo"
}

variable "location" {
  type    = string
  default = "East US"
}

variable "storage_account_name" {
  type    = string
  default = "tfdemostorage1234"
}

variable "container_name" {
  type    = string
  default = "tf-container"
}
