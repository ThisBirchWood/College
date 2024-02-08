.data
SegBytes: .byte  0x5c, 0x71, 0x54, 0x74, 0x5b, 0x66, 0x6d	#o, f, n, h, 2, 4, z(5)
keycode:  .word 4, 3, 2, 1

.text
main:
	jal display_on
	start:
	jal getPressedKey
	beq $s0, 0, alarm_off
	beq $s0, 1, alarm_on
	beq $s0, 2, alarm_home
	
	alarm_on:
	
	alarm_off:
		beq $v0, 0xa, display_on
		beq $v0, 0xb, display_home
	
	alarm_home:

	j start
	li $v0, 10
	syscall

display_on:
	lui $t0, 0xffff   # load $t0 with base IO address
	li $t1, 0x5c  
	li $t2, 0x54  
	sb $t1, 0x11($t0)  # send 0 to right segment display
	sb $t2, 0x10($t0)  # send 0 to left segment display
	li $s0, 1
	jr $ra
	
display_off:
	lui $t0, 0xffff 
	li $t1, 0x5c  
	li $t2, 0x71  
	sb $t1, 0x11($t0) 
	sb $t2, 0x10($t0) 
	li $s0, 0 
	jr $ra
	
display_home:
	lui $t0, 0xffff  
	li $t1, 0x74  
	li $t2, 0x5c 
	sb $t1, 0x11($t0) 
	sb $t2, 0x10($t0) 
	li $s0, 2
	jr $ra
	
display_z4:
	lui $t0, 0xffff   
	li $t1, 0x66  
	li $t2, 0x6d
	sb $t1, 0x11($t0) 
	sb $t2, 0x10($t0)  
	jr $ra
	
	
display_z2:
	lui $t0, 0xffff   # load $t0 with base IO address
	li $t1, 0x66  
	li $t2, 0x5b
	sb $t1, 0x11($t0)
	sb $t2, 0x10($t0)  
	jr $ra
	
getPressedKey: 
		lui $t0, 0xffff
		li $t4, 1 		# load $t0 with base IO address  
FstRow:	    # set $t4 to 1 to scan the first row
		sb $t4, 0x12($t0)  	# command first row scanning at 0xFFFF0012
		lb  $t2, 0x14($t0)  	# read  0xFFFF0014 for pressed keys
		mul $t4, $t4, 2
		bne $t2, 0, KeyPress # check any pressed keys [zero --> nothing pressed]
		blt $t4, 16, FstRow  		#scan next row
		li $t4, 1
		j FstRow
KeyPress:andi $t3,$t2,0xf0    	# Mask 0xFFFF0014 most significant nibble s
		move $s1, $t4	#store the row in which the key is pressed		
		andi $t2,$t2,0xf      	# Mask 0xFFFF0014 least significant nibble 
		srl   $t3,$t3,4         	# shift $t3 for further processing 
		####  Calculate log $t3   ##########
		add $t5,$zero, $zero		
logt3:	srl   $t3,$t3,1       
		beqz $t3, t5_t3
		addi $t5, $t5, 1
		j  logt3
t5_t3:	move $t3,$t5
	####  Calculate log $t3   ##########
		add $t5,$zero, $zero
logt2:	srl   $t2,$t2,1       
		beqz $t2, t5_t2
		addi $t5, $t5, 1
		j  logt2
t5_t2:	move $t2,$t5
		#addiu $t3,$t3,-1
		## calculate the value of the pressed key ## 
		mul $t2,$t2,4
		add  $v0,$t3,$t2
key_up:		lb $t2, 0x14($t0)
		bnez $t2, key_up
return: 	jr $ra
	
