- Used for matching patterns in a file

# Description
- grep [OPTIONS] "PATTERN" [FILE]
- grep matches the PATTERN in the FILES
	- If no file specified, just searches the files in the directory
- Displays all lines with a match

# Options
- -r 
	- Searches recursively (subdirectories)
- -E
	- Extended regex expressions
- -l
	- Displays the filenames only
- -o
	- Print only the matched pattern of the lines (doesn't print whole line)