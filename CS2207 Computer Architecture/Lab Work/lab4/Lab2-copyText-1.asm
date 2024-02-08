	.text
	.globl	main
main:
	la	$a0, prntTxt1
	jal printText
	la	$a0, text1
	jal printText
	la	$a0, lf
	jal printText
	la	$a0, prntTxt2
	jal printText	
	la	$a0, text2
	jal printText
	la	$a0, lf
	jal printText
	la	$a0, prntSep
	jal printText 	
	la	$a0, text1
	la	$a1, text2
	
	#breakpoint
	li $v0, 5
	syscall
	jal 	strcpy
	la	$a0, prntTxt1
	jal printText
	la	$a0, text1
	jal printText
	la	$a0, lf
	jal printText
	la	$a0, prntTxt2
	jal printText	
	la	$a0, text2
	jal printText
	la	$a0, lf
	jal printText
	li	$v0,10
	syscall
strcpy:
    	add  	$t0, $zero, $zero #initialize the loop index 
L1: 	add  	$t1, $t0, $a1      # calculate the address of the byte to be processed from the second string
    	lbu  	$t2, 0($t1)         # load the string character from the memory using lb
    	add  	$t3, $t0, $a0     # calculate the address of the byte to be processed from the first string
    	sb   	$t2, 0($t3)         # copy the string character to the first string using sb
    	beq  	$t2, $zero, L2   # check if the read byte is zero (string termination) to exit in L2
    	addi 	$t0, $t0, 1         # if string is not terminated,increment the index
    	j    	L1                     # loop to copy the following character
L2: 	jr   	$ra                 #  return 

printText:     
	li	$v0, 4
	syscall
	jr $ra
    # ------------------------------------------------------------------
	# Start .data segment (data!)
	.data
	text1:	.space	40
	text2:	.asciiz	"text 2"
	prntTxt1:  .asciiz	"Text 1 is: "
	prntTxt2:  .asciiz	"Text 2 is: "
	prntSep: 	.asciiz	"======================== \n"
	lf:     		.asciiz	"\n"
