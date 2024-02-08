.data

.text
	li $v0,5 
	syscall
	add $t0, $v0, $zero
	li $t1, 2147483648	#mask value, divide by 2 each time to move the 1 in the binary value down
	
	loop:
		and $t2, $t0, $t1
		divu $t1, $t1, 2
		
		bgtz $t2, if_true
		else:
			li $a0, 0
		j after_loop
		if_true:
			li $a0, 1
			
		
		after_loop:
			li $v0, 1
			syscall
			bltu $t1, 1, end
			j loop
		
	end:
		li $v0, 10
		syscall
		
