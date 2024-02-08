- Files are owned by both a user and a group
- Each file has 3 sets of group permission
	- Permissions for the user who owns it
	- Permissions for the group that owns it
	- Permissions for everyone else

# Types of permissions
- **r**ead - controls ability to read file
- **w**rite - controls ability to change/write to a file
- e**x**ecutable - can a file be executed

# Commands for Permissions
## [[ls]] (View Permissions)
- To see the permissions on files, you can use `ls -l`
![[Pasted image 20231126183110.png]]
- The first character determines whether or not the file is a directory or not ('d' means directory, '-' means not)
- The rest is split up into three files (each of 3 characters)
	- 'r' means read permission
	- 'w' means write permission
	- 'x' means execute permission
- An empty character ('-') means no permission for that operation
## chmod (Change Permissions)
- `chmod (ugoa)(+-=)(rwx) <filename>`
- *UGOA meaning*:
	- U - User
	- G - Group
	- O - Others
	- A - All (Everyone)
- +-=
	- + add the permission
	- - remove the permission
	- = set permission to 

Examples:
- `chmod u+w rgb.txt` - Give **u**ser permission to **w**rite to rgb.txt
- `chmod go-w rgb.txt`- Remove **g**roup and **o**thers permission to write
- `chmod a-x rgb.txt` - Block **a**ll from executing

### Octal Mode
- You can also use numbers in chmod to change permissions
- The digits are calculated by adding the values of the individual digits:
	- 4 - Read Permission
	- 2 - Write Permission
	- 1 - Execute Permission
- Example: `chmod 674 [filename]`
	- 6 represents the owner (2+4, write and read)
	- 7 represents the group (1+2+4, execute, write and read)
	- 4 represents the others (4, read)