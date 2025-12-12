# Get the SAS token directly from Terraform output
TOKEN="$(terraform output -raw curl_sas_command | sed -E 's/.*\?\??(.*)"/\1/')"

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

# Download blob named "example.txt"
curl -o downloaded_example.txt "$URL/example.txt?$TOKEN"
