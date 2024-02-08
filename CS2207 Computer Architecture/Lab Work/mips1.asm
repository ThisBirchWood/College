.data
	lol:	.asciiz "LOL"
	
.text
	li $v0, 4
	la $a0, lol
	syscall
	
	li $v0, 4
	la $a0, lol
	syscall
