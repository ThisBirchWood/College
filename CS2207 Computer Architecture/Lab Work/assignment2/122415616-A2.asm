.data
	input_str:	.space 12
	str1:		.asciiz "Enter a number: "
	str2float:	.float 0
	hex_value:	.word 0
	
	sign_bit:	.asciiz "Sign Bit: "
	exponent_bits:	.asciiz "\nExponent Hex: "
	fraction_bits:	.asciiz "\nFraction Hex: "
	floating_value:	.asciiz "\nFloating Point Hex: "
	hex_prefix:	.asciiz "0x"
	
	#errors
	too_large_message:	.asciiz "Value too large!"
	invalid_char_message:	.asciiz "Invalid Character entered!"
	
.text
	#print str1
	la $a0, str1
	li $v0, 4
	syscall
	
	#ask for input and store in "input_str"
	li $v0, 8
	la $a0, input_str
	li $a1, 20
	syscall
	
	li $s0, 1	#what to divide the fractional part by (will be updated in loop)
	li $s1, 0	#0 = positive number, 1 = negative number, this is the sign bit
	
	#convert string to 2 numbers, the integer part and the fractional part in $s2 and $s3
	li $t0, 0	#loop counter, byte shift amount
	
	lb $t1, input_str($t0)	#load the first digit
	jal invalid_char_checker
	bne $t1, 45, integer_loop	#check if the first char is a minus, if it isn't go straight to loop
	li $s1, 1	#change $s0 to 1
	addi $t0, $t0, 1
	lb $t1, input_str($t0)
	jal invalid_char_checker
	
	#integer loop to loop through the bytes and build the first int
	integer_loop:
		addi $t1, $t1, -48	#remove 48 to get real value, not ascii value
		
		mulu $s2, $s2, 10	#multiply $s2 by 10
		addu $s2, $s2, $t1	#add $t0 number to $s2 register
		
		#read next byte
		addi $t0, $t0, 1	
		lb $t1, input_str($t0)
		
		#doing checks
		jal invalid_char_checker
		beq $t1, 10, skip_loop	#if next char is a new line, skip the fraction loop entirely
		bne, $t1, 46, integer_loop	#check if the next char is a dot, if so move on
		
	addi $t0, $t0, 1
	lb $t1, input_str($t0)
	jal invalid_char_checker
	fraction_loop:
		addi $t1, $t1, -48	#remove 48 to get real value, not ascii value
		
		mul $s3, $s3, 10	#multiply $s2 by 10
		add $s3, $s3, $t1	#add $t0 number to $s2 register
		mul $s0, $s0, 10	#multiply fractional division part by 10 every time
		
		#read next byte
		addi $t0, $t0, 1	
		lb $t1, input_str($t0)
		jal invalid_char_checker
		
		#check if line is over
		bne, $t1, 10, fraction_loop	#if next char is a new line, move on
	
	skip_loop:
	
	#check if value is too large to be represented by a signed integer
	bgtu $s2, 2147483647, too_large
	j after
	
	too_large:
		j too_large_error
	
	after:
		
	#move values to co processor one
	mtc1 $s2, $f0
	mtc1 $s3, $f1
	
	#convert to floating point
	cvt.s.w $f0, $f0
	cvt.s.w $f1, $f1
	
	#move fractional division part into co processor $f2 and convert
	mtc1 $s0, $f2
	cvt.s.w $f2, $f2
	
	#divide fractional component by fractional division part $s0
	div.s $f1, $f1, $f2
	
	#add $f0 and $f1
	add.s $f0, $f0, $f1
	
	#check if number is negative from $s1, if it is, mul by -1
	beq $s1, 1, if_negative
	else:
		j after1
	
	if_negative:
		#move -1 into coprocessor
		li $t0, -1
		mtc1 $t0, $f1
		cvt.s.w $f1, $f1
		#multiply by -1
		mul.s $f0, $f0, $f1
	after1:
	#store word into memory
	swc1 $f0, str2float
	
	#load word into register
	lw $t0, str2float
	
	#printing the sign bit + it's string in .data
	la $a0, sign_bit
	li $v0, 4
	syscall
	
	andi $a2, $t0, 2147483648
	srl $a2, $a2, 31
	jal print_register_hex
	
	#printing the exponent part + it's string in .data
	la $a0, exponent_bits
	li $v0, 4
	syscall
	
	andi $a2, $t0, 2139095040
	srl $a2, $a2, 23
	jal print_register_hex
	
	#printing the fractional parts + it's string in .data
	la $a0, fraction_bits
	li $v0, 4
	syscall
	
	andi $a2, $t0, 8388607	
	jal print_register_hex
	
	#print the full thing
	la $a0, floating_value
	li $v0, 4
	syscall
	
	move $a2, $t0
	jal print_register_hex
	
	li $v0, 10
	syscall
	
	# $a2 = value to print as hex
	print_register_hex:
		#print hex_prefix "0x"
		li $v0, 4
		la $a0, hex_prefix
		syscall
		
		#load values
		li $t2, 0xf0000000	#masking value to check value
		li $t3, 28		#shift amount to move value down (move 0xf0000000 to 0x0000000f) to print it properly
		#looping through each char
		hex_loop:
			and $a1, $a2, $t2	#using masking value to isolate value
			
			srlv $a1, $a1, $t3	#shift down by certain amount
			add $t3, $t3, -4	#move shift value down to prepare for next value
			
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
		
	too_large_error:
		li $v0, 4
		la $a0, too_large_message
		syscall
		
		li $v0, 10
		syscall
		
	#checks if value in $t1 is between 48 and 57
	invalid_char_checker:
		beq $t1, 46, is_valid
		beq $t1, 45, is_valid
		beq $t1, 10, is_valid
		bge $t1, 58, has_error
		ble $t1, 47, has_error
		
		is_valid:
			jr $ra
		
		has_error:
			li $v0, 4
			la $a0, invalid_char_message
			syscall
		
			li $v0, 10
			syscall
		
		
	
	
	
