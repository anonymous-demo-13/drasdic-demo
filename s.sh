#!/bin/bash

# Navigate to the directory containing your audio files
cd /Users/davidrobinson/Code/esp/drasdic-demo/audio/ || exit

# Find all files with %20 in their name and rename them by replacing %20 with an underscore
find . -type f -name "*%20*" | while IFS= read -r file; do
    newfile=$(echo "$file" | sed 's/%20/_/g')
    echo "Renaming: $file -> $newfile"
    mv "$file" "$newfile"
done
