.data
	userInput:	.word 24
	caption1:	.asciiz "Enter a integer: "
	caption2:	.asciiz "You entered: "

.text

	addi $v0, $zero, 4 	#load syscall for printing
	la  $a0, caption1	#add the address of caption1 to memory
	syscall			#call system
	
	li $v0, 5		#load syscall for reading integer
	syscall			#call system to read the input
	sw $v0, userInput	#store that input in the label userInput
	
	li $v0, 4		#add 4 to v0, which sets the system to print string
	la $a0, caption2	#add the string address of caption2 to the register a0
	syscall			#call system to print string
	
	li $v0, 1		#set system to print integer
	lw $a0, userInput	#load the integer into the register a0
	syscall			#call system to print the int
	
	li $v0, 10
	syscall			#end the program
	
	
