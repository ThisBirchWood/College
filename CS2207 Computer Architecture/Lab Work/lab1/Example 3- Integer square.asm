.globl    main
#  Data Section: variable declarations [reserve memory space and possible initialize]
.data
		integerX:         .word 0  # input number taken from the memory
		integerY:         .word 0  # memory space to store the result
		myString1:  	.asciiz   "The square of " #the output message 
		myString2:	.asciiz " is "
		caption: 	.asciiz "Enter a number between 1 and 99: "
# Text/code Section [where instructions reside]
.text  					
main:
	li $v0, 4		#get system ready for printing string
	la $a0, caption		#add string to register
	syscall			#call system
	
	li $v0, 5		#get system ready for reading int
	syscall			#call system
	sw $v0, integerX	#store result in integerX
	
	mul $t0, $v0, $v0	#multiply the output against itself and store the value in $t0
	sw $t0, integerY	#store the value of the register within integerY
	
	li $v0, 4		#get system ready for printing string
	la $a0, myString1	#store the address of the string in $a0
	syscall			#call system
	
	li $v0, 1
	lw $a0, integerX
	syscall
	
	li $v0, 4
	la $a0, myString2
	syscall
	
	li $v0, 1		#get system ready for printing int
	lw $a0, integerY	#store value of int in $a0
	syscall			#call sys
	
	li $v0, 10		#end program
	syscall
	
	
	
	
