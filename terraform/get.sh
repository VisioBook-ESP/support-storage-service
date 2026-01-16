# Get the SAS token directly from Terraform output
TOKEN="sv=2018-11-09&sr=c&st=2025-12-12T03:55:07Z&se=2025-12-13T03:55:07Z&sp=rwl&spr=https&sig=AWJOnMovK6nianUAh7XhQV25TKUobvV7svw6uBuW1m4%3D" # exemple : TOKEN="sv=2018-11-09&sr=c&st=2025-12-12T03:14:25Z..."

# Base URL
URL="https://blobpourcamille.blob.core.windows.net/tf-container"

# Download blob named "example.txt"
curl -o downloaded_example.txt "$URL/example.txt?$TOKEN"


# le ficher arrivera sous la forme downloaded_exemple.tkt une fois recupéré