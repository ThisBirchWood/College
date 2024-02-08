.data
	caption1:	.asciiz "Enter a number: "
	caption2:	.asciiz "\nYour number is  (I've done a lot more work than it seems) : "
	user_input:	.asciiz "--------"
	number_length:	.word 0
	multiplation_comp: .word 0

.text
main:
	#print caption1
	la $a0, caption1
	li $v0, 4
	syscall
	
	#get user input
	la $a0, user_input
	li $a1, 30
	la $v0, 8
	syscall
	
	#calculate length of number
	li $t0, 0	#initialise sum register
	length_loop:
		lb $t1, user_input($t0)
		addi $t0, $t0, 1		#update sum register
		bgtz $t1, length_loop
		
	addi $t0, $t0, -2	#remove 2 because it's always 2 over the length
	sw $t0, number_length	#store length of number
	
	#calculate power component (how much to multiply the first digit by)
	lw $t0, number_length	#load the length of the number into $t0
	addi $t0, $t0, -1	#reduce by one because this loop is weird
	li $t1, 1	#multiplication component
	power:
		mul $t1, $t1, 10	#raise power by one
		addi $t0, $t0, -1	#reduce counter by one
		
		bgtz $t0, power		#check if loop again
		
	sw $t1, multiplation_comp	#save the 10^(of amount of digits-1)
	
	#calculate number
	lw $t0, number_length	#load number length
	lw $t1, multiplation_comp	#load the amount to multiply first digit by
	li $t2, 0	#sum counter
	li $t4, 0	#the number itself
	
	loop:
		lb $t3, user_input($t2)	#load the first byte of digit + amount in $t2
		addi $t0, $t0, -1	#reduce number length by one
		
		addi $t3, $t3, -48	#move from hex ascii value to it's actual value
		mul $t3, $t3, $t1	#multiply by the power component
		div $t1, $t1, 10	#divide the power component by 10
		
		add $t4, $t4, $t3	#add all to a register
		add $t2, $t2, 1		#increase sum by one
		
		bgtz $t0, loop		#check loop
	
	#print caption2
	li $v0, 4
	la $a0, caption2
	syscall
	
	#print the int value
	li $v0, 1
	add $a0, $zero, $t4	#moving the value to $a0
	syscall
	
	#exit program
	li $v0, 10
	syscall
