# Get the SAS token directly from Terraform output
TOKEN="a trouver dans la ci"

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

# Download blob named "example.txt"
curl -o downloaded_example.txt "$URL/example.txt?$TOKEN"
