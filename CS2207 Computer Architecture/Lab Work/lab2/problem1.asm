.data
	caption1:	.asciiz "Enter a number between 1 and 99: "
	caption2:	.asciiz "\nYour number is  (I've done a lot more work than it seems) : "
	user_input:	.asciiz "0"
	new_line:	.asciiz "\n"

.text
main:
	#print caption1
	la $a0, caption1
	li $v0, 4
	syscall
	
	#get user input
	la $a0, user_input
	li $a1, 3
	la $v0, 8
	syscall
	
	#calculate 
	lb $a0, user_input	#load the first byte
	addi $t0, $a0, -48	#change from ascii value to real int
	mul $t0, $t0, 10	#multiply by 10 to get the 10's
	
	lb $a0, user_input + 1	#load the second byte
	addi $t1, $a0, -48	#convert to real value from ascii
	
	add $t2, $t1, $t0	#add the first digit (mulitpled by 10) to the second digit, giving us the value
		
	#print caption2
	li $v0, 4
	la $a0, caption2
	syscall
	
	#print the int value
	li $v0, 1
	add $a0, $zero, $t2	#moving the value to $a0
	syscall
	
	#exit program
	li $v0, 10
	syscall