# Get the SAS token directly from Terraform output
TOKEN="sv=2018-11-09&sr=c&st=2025-12-12T03:55:07Z&se=2025-12-13T03:55:07Z&sp=rwl&spr=https&sig=AWJOnMovK6nianUAh7XhQV25TKUobvV7svw6uBuW1m4%3D"

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

curl -X PUT \
     -T example.txt \
     -H "x-ms-blob-type: BlockBlob" \
     "$URL/example.txt?$TOKEN"