#!/bin/bash

# Loop through all files with the pattern 'YY-MM-DD - [STRING PLACEHOLDER]'
for file in [0-9][0-9]-[0-1][0-9]-[0-3][0-9]*; do
    if [[ -f "$file" ]]; then  # Check if it's a file
        # Extract year, month, and day from the filename
        year="20$(echo $file | cut -d '-' -f 1)"
        month=$(echo $file | cut -d '-' -f 2)
        day=$(echo $file | cut -d '-' -f 3 | awk '{print substr($1, 1, 2)}')  # Extract day and handle additional content

        # Convert month number to month name using macOS compatible date command
        month_name=$(date -j -f "%Y-%m-%d" "$year-$month-$day" "+%B")

        # Check if the month directory exists, if not create it
        if [ ! -d "$month_name" ]; then
            mkdir "$month_name"
        fi

        # Move the file into the respective month directory
        mv "$file" "$month_name/"
    fi
done
