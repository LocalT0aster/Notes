#!/bin/bash

# Directory where the markdown files are located
SOURCE_DIR="./"
# Output directory
OUTPUT_DIR="./output"

# Function to convert Markdown to HTML with Pandoc
convert_md_to_html() {
    local input=$1
    local output=$2
    pandoc "$input" -o "$output" --mathjax --standalone
}

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Find all markdown files in the source directory and its subdirectories
find "$SOURCE_DIR" -name '*.md' -not -path "$OUTPUT_DIR/*" | while read -r mdfile; do
    # Get the relative path from SOURCE_DIR
    relative_path="${mdfile#$SOURCE_DIR}"
    # Construct the new output path by changing the extension to .html
    new_html_path="${relative_path%.md}.html"
    # Replace 'FolderName/FolderName.html' with 'FolderName/index.html' for subdirectories
    new_html_path=$(echo "$new_html_path" | sed -E 's@/(.+)/\1\.html@/\1/index.html@')
    # Create full output path
    full_output_path="$OUTPUT_DIR$new_html_path"

    # Create output subdirectory if it doesn't exist
    mkdir -p "$(dirname "$full_output_path")"

    # Convert Markdown to HTML
    convert_md_to_html "$mdfile" "$full_output_path"
done

# Special case for README.md
if [ -f "$SOURCE_DIR/README.md" ]; then
    convert_md_to_html "$SOURCE_DIR/README.md" "$OUTPUT_DIR/index.html"
fi

echo "Conversion completed."
