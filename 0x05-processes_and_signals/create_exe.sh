#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

# Check if the file already exists
if [ -e "$filename" ]; then
  echo "Error: File '$filename' already exists."
  exit 1
fi

filename=$1
touch "$filename"
echo "#!/usr/bin/env bash" > "$filename"

chmod +x "$filename"

echo "'$filename' created and made executable."


