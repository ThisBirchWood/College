.data
	hex_value: 	.asciiz  "0"
	hex_prefix:	.asciiz "0x"

.text
	
	li $v0, 5	#load read int value
	syscall 
	add $t0, $v0, $zero	#move value to $t0
	
	#print hex_prefix
	la $a0, hex_prefix
	li $v0, 4
	syscall
	
	#load values that are needed
	li $t1, 4026531840	#mask value = 0xf0000000
	li $t4, 28		#sbift value (amount of bits to shift it down)
	
	loop:
		and $t3, $t0, $t1	#compare value with mask value
		
		add $a1, $t3, $zero	#move value to $a1, to prepare for the procedure call
		srlv $a1, $a1, $t4	#shift the value down by the shift amount, so that it's like 0000 0010, instead of 0000 0010 0000 0000
		add $t4, $t4, -4	#shift the shift value down by 4 bits
		jal print_hex		#print hex
	
		srl $t1, $t1, 4		#shift the mask value right by 4 bits
	
		
		bgtz $t1, loop		#if the mask is bigger than zero, loop again
		
	li $v0, 10
	syscall
	
	
print_hex:
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
		
		jr $ra			#jump back
		
