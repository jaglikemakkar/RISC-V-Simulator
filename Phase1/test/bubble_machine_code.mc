0x0	0x10000597	auipc x11 65536	lw x11, len # length of the array # n
0x4	0x00C5A583	lw x11 12(x11)	lw x11, len # length of the array # n
0x8	0x10000517	auipc x10 65536	la x10, arr # base address of array
0xc	0xFF850513	addi x10 x10 -8	la x10, arr # base address of array
0x10	0x00050613	addi x12 x10 0	addi x12, x10, 0 # base address of array
0x14	0x00200993	addi x19 x0 2	li x19, 2 # constant
0x18	0x00200F93	addi x31 x0 2	addi x31, x0, 2
0x1c	0x008000EF	jal x1 8	jal x1, Bubble_sort
0x20	0x04000A63	beq x0 x0 84	beq x0, x0, exit
0x24	0xFFC10113	addi x2 x2 -4	addi sp, sp, -4
0x28	0x00112023	sw x1 0(x2)	sw x1, 0(sp) # storing current return address
0x2c	0x0135D463	bge x11 x19 8	bge x11, x19 else # branch if n>=2 (x11>=x19)
0x30	0x02000C63	beq x0 x0 56	beq x0, x0, end_bubble_sort
0x34	0xFFF58593	addi x11 x11 -1	addi x11, x11, -1 # n = n-1
0x38	0x00000A13	addi x20 x0 0	li x20, 0 # initializing i = 0
0x3c	0x02BA0463	beq x20 x11 40	beq x20, x11 endfor # if i == n-1 break;
0x40	0x01FA1AB3	sll x21 x20 x31	sll x21, x20, x31 # x21 = i*4 (for getting the offset)
0x44	0x00AA8AB3	add x21 x21 x10	add x21, x21, x10 # x21 = &arr[i]
0x48	0x000AAB03	lw x22 0(x21)	lw x22, 0(x21) # x22 = arr[i]
0x4c	0x004AAB83	lw x23 4(x21)	lw x23, 4(x21) # x23 = arr[i+1]
0x50	0x016BD663	bge x23 x22 12	bge x23, x22 donotswap # if arr[i+1] >= arr[i] donotswap
0x54	0x016AA223	sw x22 4(x21)	sw x22, 4(x21) # swaping
0x58	0x017AA023	sw x23 0(x21)	sw x23, 0(x21) # swaping
0x5c	0x001A0A13	addi x20 x20 1	addi x20, x20, 1 # i = i+1
0x60	0xFC000EE3	beq x0 x0 -36	beq x0, x0, for
0x64	0xFC1FF0EF	jal x1 -64	jal x1, Bubble_sort
0x68	0x00012083	lw x1 0(x2)	lw x1, 0(sp) # retrieving current return address
0x6c	0x00410113	addi x2 x2 4	addi sp, sp, 4
0x70	0x00008067	jalr x0 x1 0
