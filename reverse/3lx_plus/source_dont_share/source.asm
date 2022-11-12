lea r0 #19
trap putsp

lea r1 #3
ld r6 #1
jmp r1
addr 0x5000

xor r1 r1 r1
xor r2 r2 r2
add r2 r2 #15
add r2 r2 r2
add r2 r2 #6

label inp_loop
trap getc
trap out
add r3 r6 r1
str r0 r3 #0
add r1 r1 #1
sub r4 r1 r2
brn inp_loop

lea r7 #90
com check this
jmp r7

addr 0x6e45
addr 0x6574
addr 0x2072
addr 0x6c66
addr 0x6761
addr 0x003a
addr 0x0000


com check_vertical

add r0 r0 r6
ldr r4 r0 #0
add r1 r1 r4

add r0 r0 #3
ldr r4 r0 #0
add r1 r1 r4

add r0 r0 #3
ldr r4 r0 #0
mult r1 r1 r4

xor r3 r3 r5
sub r1 r1 r3

brpn #1
jmp r7
com check this
brpn #62



com check first diag


add r0 r0 r6
ldr r4 r0 #0
add r1 r1 r4

add r0 r0 #4
ldr r4 r0 #0
add r1 r1 r4

add r0 r0 #4
ldr r4 r0 #0
sub r1 r1 r4

xor r3 r3 r5
sub r1 r1 r3

brpn #1
jmp r7
com check this
brpn #48


com check second diag

add r0 r0 r6
ldr r4 r0 #0
mult r1 r1 r4

add r0 r0 #2
ldr r4 r0 #0
mult r1 r1 r4

add r0 r0 #2
ldr r4 r0 #0
sub r1 r1 r4

xor r3 r3 r5
sub r1 r1 r3

brpn #1
jmp r7
com check this
brpn #34

com xor all sym in block

add r0 r0 r6
ldr r4 r0 #0
add r5 r5 r4
xor r1 r1 r1
xor r2 r2 r2
add r2 r2 #8

add r0 r0 #1
ldr r4 r0 #0
xor r5 r5 r4

add r1 r1 #1
sub r4 r1 r2
brn #-6

jmp r7

com check_horisontal

add r0 r0 r6
ldr r4 r0 #0
mult r1 r1 r4

add r0 r0 #1
ldr r4 r0 #0
mult r2 r2 r4

add r1 r1 r2

add r0 r0 #1
ldr r4 r0 #0

sub r1 r1 r4
xor r3 r3 r5
sub r1 r1 r3
brpn #1
jmp r7
com check this
brpn #6


com correct
com check this
lea r0 #2
trap putsp
trap halt
addr 0x4559
addr 0x0a53
addr 0x0000


com not_correct
com check this
lea r0 #2
trap putsp
trap halt
addr 0x4e0a
addr 0x004f
addr 0x0000

com main

com #######################FIRST BLOCK
xor r0 r0 r0
xor r5 r5 r5
xor r4 r4 r4
lea r1 #3
ld r3 #1
jmp r1
addr 0x274d
xor r1 r1 r1
add r1 r1 #9
mult r1 r1 r1
xor r2 r2 r2
add r2 r2 #14
add r2 r2 r2
add r2 r2 r2
jsr #-42

xor r0 r0 r0
add r0 r0 #3
xor r5 r5 r5
xor r4 r4 r4
lea r1 #3
ld r3 #1
jmp r1
addr 0x10ff
xor r1 r1 r1
add r1 r1 #12
xor r2 r2 r2
add r2 r2 #15
add r2 r2 r2
add r2 r2 #4
jsr #-57

xor r0 r0 r0
add r0 r0 #6
xor r5 r5 r5
xor r4 r4 r4
lea r1 #3
ld r3 #1
jmp r1
addr 0x12cb
xor r1 r1 r1
add r1 r1 #15
add r1 r1 r1
xor r2 r2 r2
add r2 r2 #13
jsr #-71

xor r0 r0 r0
xor r5 r5 r5
xor r4 r4 r4
lea r1 #3
ld r3 #1
jmp r1
addr 0x549c
xor r1 r1 r1
xor r2 r2 r2
jsr #-136

xor r0 r0 r0
add r0 r0 #1
xor r5 r5 r5
xor r4 r4 r4
lea r1 #3
ld r3 #1
jmp r1
addr 0x4d08
xor r1 r1 r1
xor r2 r2 r2
jsr #-147

xor r0 r0 r0
add r0 r0 #2
lea r1 #3
ld r3 #1
jmp r1
addr 0x3663
xor r1 r1 r1
xor r2 r2 r2
jsr #-156

xor r0 r0 r0
lea r1 #3
ld r3 #1
jmp r1
addr 0x0024
xor r1 r1 r1
xor r2 r2 r2
jsr #-150

xor r0 r0 r0
add r0 r0 #2
lea r1 #3
ld r3 #1
jmp r1
addr 0xeab6
xor r1 r1 r1
add r1 r1 #10
xor r2 r2 r2
jsr #-147

xor r0 r0 r0
jsr #-134
com #######################FIRST BLOCK END

com #######################SECOND BLOCK

xor r0 r0 r0
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x461a
xor r1 r1 r1
add r1 r1 #9
mult r1 r1 r1
add r1 r1 #10
xor r2 r2 r2
add r2 r2 #9
mult r2 r2 r2
add r2 r2 #4
jsr #-136

xor r0 r0 r0
add r0 r0 #12
lea r1 #3
ld r3 #1
jmp r1
addr 0x2abd
xor r1 r1 r1
add r1 r1 #9
mult r1 r1 r1
sub r1 r1 #10
xor r2 r2 r2
add r2 r2 #7
mult r2 r2 r2
add r2 r2 #6
jsr #-151

xor r0 r0 r0
add r0 r0 #15
lea r1 #3
ld r3 #1
jmp r1
addr 0x2924
xor r1 r1 r1
add r1 r1 #5
mult r1 r1 r1
xor r2 r2 r2
add r2 r2 #8
mult r2 r2 r2
add r2 r2 #10
jsr #-165

xor r0 r0 r0
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x567e
xor r1 r1 r1
xor r2 r2 r2
jsr #-229

xor r0 r0 r0
add r0 r0 #10
lea r1 #3
ld r3 #1
jmp r1
addr 0x4b16
xor r1 r1 r1
xor r2 r2 r2
jsr #-238

xor r0 r0 r0
add r0 r0 #11
lea r1 #3
ld r3 #1
jmp r1
addr 0x1c6a
xor r1 r1 r1
xor r2 r2 r2
jsr #-247

xor r0 r0 r0
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x0043
xor r1 r1 r1
xor r2 r2 r2
jsr #-242

xor r0 r0 r0
add r0 r0 #11
lea r1 #3
ld r3 #1
jmp r1
addr 0x3cd7
xor r1 r1 r1
add r1 r1 #4
xor r2 r2 r2
jsr #-238

xor r0 r0 r0
xor r5 r5 r5
add r0 r0 #9
jsr #-228

com #######################SECOND BLOCK END


com #######################THIRD BLOCK 

xor r0 r0 r0
add r0 r0 #9
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x2e8a
xor r1 r1 r1
add r1 r1 #9
mult r1 r1 r1
add r1 r1 #7
xor r2 r2 r2
add r2 r2 #7
mult r2 r2 r2
sub r2 r2 #1
jsr #-231

xor r0 r0 r0
add r0 r0 #11
add r0 r0 #10
lea r1 #3
ld r3 #1
jmp r1
addr 0x07bf
xor r1 r1 r1
add r1 r1 #6
xor r2 r2 r2
add r2 r2 #15
add r2 r2 #1
jsr #-244


xor r0 r0 r0
add r0 r0 #14
add r0 r0 #10
lea r1 #3
ld r3 #1
jmp r1
addr 0x1e33
xor r1 r1 r1
add r1 r1 #5
mult r1 r1 r1
xor r2 r2 r2
add r2 r2 #8
mult r2 r2 r2
add r2 r2 #5
jsr #-259


xor r0 r0 r0
add r0 r0 #9
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x28b0
xor r1 r1 r1
xor r2 r2 r2
jsr #-324

xor r0 r0 r0
add r0 r0 #10
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x368b
xor r1 r1 r1
xor r2 r2 r2
jsr #-334

xor r0 r0 r0
add r0 r0 #11
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x3b6d
xor r1 r1 r1
xor r2 r2 r2
jsr #-344

xor r0 r0 r0
add r0 r0 #9
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x00ea
xor r1 r1 r1
xor r2 r2 r2
jsr #-340

xor r0 r0 r0
add r0 r0 #11
add r0 r0 #9
lea r1 #3
ld r3 #1
jmp r1
addr 0x82e1
xor r1 r1 r1
add r1 r1 #3
xor r2 r2 r2
jsr #-337

xor r0 r0 r0
xor r5 r5 r5
add r0 r0 #9
add r0 r0 #9
jsr #-328

com #######################THIRD BLOCK END

com #######################FOURTH BLOCK 

xor r0 r0 r0
add r0 r0 #9
mult r0 r0 #3
lea r1 #3
ld r3 #1
jmp r1
addr 0x1b1f
xor r1 r1 r1
add r1 r1 #9
mult r1 r1 #10
xor r2 r2 r2
add r2 r2 #13
mult r2 r2 #2
jsr #-329

xor r0 r0 r0
add r0 r0 #15
mult r0 r0 #2
lea r1 #3
ld r3 #1
jmp r1
addr 0x2c3e
xor r1 r1 r1
add r1 r1 #7
mult r1 r1 #10
xor r2 r2 r2
add r2 r2 #15
add r2 r2 r2
add r2 r2 #2
jsr #-344

xor r0 r0 r0
add r0 r0 #15
mult r0 r0 #2
add r0 r0 #3
lea r1 #3
ld r3 #1
jmp r1
addr 0x3494
xor r1 r1 r1
add r1 r1 #7
mult r1 r1 #11
xor r2 r2 r2
add r2 r2 #4
mult r2 r2 #10
add r2 r2 #3
jsr #-360


xor r0 r0 r0
add r0 r0 #9
mult r0 r0 #3
lea r1 #3
ld r3 #1
jmp r1
addr 0x4c1f
xor r1 r1 r1
xor r2 r2 r2
jsr #-425

xor r0 r0 r0
add r0 r0 #4
mult r0 r0 #7
lea r1 #3
ld r3 #1
jmp r1
addr 0x5574
xor r1 r1 r1
xor r2 r2 r2
jsr #-435

xor r0 r0 r0
add r0 r0 #15
add r0 r0 #14
lea r1 #3
ld r3 #1
jmp r1
addr 0x6aa3
xor r1 r1 r1
xor r2 r2 r2
jsr #-445

xor r0 r0 r0
add r0 r0 #9
mult r0 r0 #3
lea r1 #3
ld r3 #1
jmp r1
addr 0x0053
xor r1 r1 r1
xor r2 r2 r2
jsr #-441


xor r0 r0 r0
add r0 r0 #15
add r0 r0 #14
lea r1 #3
ld r3 #1
jmp r1
addr 0xbf33
xor r1 r1 r1
add r1 r1 #4
xor r2 r2 r2
jsr #-438


lea r0 #2
trap putsp
trap halt
addr 0x590a
addr 0x5345
addr 0x0000

com #######################FOURTH BLOCK END

com end main