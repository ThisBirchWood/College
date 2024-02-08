.data
	input_str:	.word 0, 0, 0, 0
	str1:	.asciiz "Enter a number: "
	str2float:	.float 99999
	hex_value: 	.asciiz  "0"
	
	sign_bit:	.asciiz "Sign Bit: "
	exponent_bits:	.asciiz "\nExponent Hex: "
	fraction_bits:	.asciiz "\nFraction Hex: "
	floating_value:	.asciiz "\nFloating Point Hex: "
	hex_prefix:	.asciiz "0x"

.text
	#print str1
	li $v0, 4
	la $a0, str1
	syscall
	
	#read real number as string
	li $v0, 8
	li $a1, 20
	la $a0, input_str
	li $s3, 1	#division constant for fractional part
	li $t4, 0	#0 = on int part, 1 = on fraction part 
	li $t5, 0	#0 = positive, 1 = negative
	syscall
	
	#convert from string to float
	li $t0, 0	#byte shift amount
	lb $t2, input_str($t0)
	beq $t2, 45, next_char
	j split_loop
	next_char:
		addi $t0, $t0, 1
		lb $t2, input_str($t0)
		li $t5, 1
		
	split_loop:
		add $t2, $t2, -48	#convert from ASCII to integer
		
		mul $t1, $t1, 10	#multiply the register where the integer is stored by 10
		add $t1, $t1, $t2	#add the new integer to the register $t1
		
		#update division constant
		beq $t4, 0, rest_of_function	#check if we are on the integer part
			update:						#if we are on the fraction part, update the division constant
				mul $s3, $s3, 10		#multiply the division constant by 10
		rest_of_function:
		addi $t0, $t0, 1				#move to the next byte
		lb $t2, input_str($t0)			#load the next byte
		beq $t2, 46, move_to_fraction	#check if the next byte is a decimal point
		bne $t2, 10, split_loop			#check if the next byte is a new line, if it isn't jump back to the split loop
		
	j after_split_loop
		
	move_to_fraction:
		add $s0, $zero, $t1	#move the integer part to $s0
		addi $t0, $t0, 1	#move to the next byte
		li $t1, 0 			#reset the counter
		li $t4, 1	 		#set the division constant to the fractional part
		lb $t2, input_str($t0) 	#load the next byte
		j split_loop	#jump back to the split loop
		
	after_split_loop:
	add $s1, $zero, $t1
			
	#move to floating point co-processor	
	mtc1 $s0, $f0
	mtc1 $s1, $f1
	
	#convert them to floating point format
	cvt.s.w $f0, $f0
	cvt.s.w $f1, $f1
		
	#load the division constant into the floating point co-processor
	add $t0, $s3, $zero
	mtc1 $t0, $f2
	cvt.s.w $f2, $f2
	
	#divide the decimal part by 1000
	div.s $f1, $f1, $f2
	
	#add to the integer number
	add.s $f0, $f0, $f1
	
	#change to negative or positive
	bne $t5, 1, next1
	li $t0, -1
	mtc1 $t0, $f3
	cvt.s.w $f3, $f3
	mul.s $f0, $f0, $f3
	next1:
		
	swc1 $f0, str2float
	lw $t0, str2float
	
	#print sign bit string
	li $v0, 4
	la $a0, sign_bit
	syscall
	
	andi $a2, $t0, 2147483648	#mask for sign bit
	srl $a2, $a2, 31		#shift down by 31 bits
	jal print_hex
	
	li $v0, 4
	la $a0, exponent_bits
	syscall
	
	andi $a2, $t0, 2139095040	#mask for exponent bits
	srl $a2, $a2, 23			#shift down by 23 bits
	jal print_hex
	
	#print fraction bits string
	li $v0, 4				
	la $a0, fraction_bits
	syscall
	
	andi $a2, $t0, 8388607	 	#mask for fraction bits
	jal print_hex				
	
	#print floating point string
	li $v0, 4
	la $a0, floating_value
	syscall
	
	move $a2, $t0				#move the value to $a2	
	jal print_hex
	
	#exit
	li $v0, 10
	syscall
	
	print_hex:

		li $v0, 4
		la $a0, hex_prefix
		syscall
		
		li $t2, 0xf0000000
		li $t3, 28
		hex_loop:
			and $a1, $a2, $t2
			
			srlv $a1, $a1, $t3
			add $t3, $t3, -4
			
			bge $a1, 10,  if_above_10	#check if value is bigger than 10, if bigger than zero, it needs to go to a different place on the ascii table
			add $a1, $a1, 48		#if smaller than 10, add 48 to get to ASCII string value
			j rest				#rest of program
	
			if_above_10:
				add $a1, $a1, 87	#if bigger than 10, add 87 to get to the ASCII letter values
		
			rest:
				#print the "string" value
				sw $a1, hex_value	#store value in "hex_value"
				la $a0, hex_value	#load the address into $a0
				li $v0, 4
				syscall	
				
			srl $t2, $t2,4
			
			bgtz $t2, hex_loop
		
		jr $ra			#jump back
	
		
	
