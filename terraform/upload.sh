# Get the SAS token directly from Terraform output
TOKEN="a trouver dans la ci "

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

curl -X PUT \
     -T example.txt \
     -H "x-ms-blob-type: BlockBlob" \
     "$URL/example.txt?$TOKEN"