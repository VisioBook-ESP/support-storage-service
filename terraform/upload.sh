# Get the SAS token directly from Terraform output
TOKEN="$(terraform output -raw curl_sas_command | sed -E 's/.*\?\??(.*)"/\1/')"

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

curl -X PUT \
     -T example.txt \
     -H "x-ms-blob-type: BlockBlob" \
     "$URL/example.txt?$TOKEN"