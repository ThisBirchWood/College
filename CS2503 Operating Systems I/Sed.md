- Sed - **s**tream **ed**itor
- sed writes to standard output, makes no changes to original file (unless -i is used)
- very similar to [[awk]]
- sed is suitable for modifying or processing large files or streams of text, due to the fact it doesn't use RAM, instead it uses buffers.

# sed vs [[awk]]
- sed applies all edits to each line one at a time
- awk applies each edit to all data lines one at a time

# Four Basic Script Types
- Multiple edits to the same file
- Making changes across a bunch of files
- Extracting contents of a file
- Making edits in a pipeline

# Three Basic Principles
- All editing lines of a script apply to all lines of the file being edited
- The original file is unchanged unless redirected
- All editing commands in a script are applied in order to each line of the input file

#

![[Pasted image 20231106143134.png]]
