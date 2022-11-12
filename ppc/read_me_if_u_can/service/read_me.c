#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <seccomp.h>
#include <unistd.h>
#include <errno.h>


void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
	seccomp_load(ctx);
	seccomp_release(ctx);
}


int main(){
	init();
	printf("Hello, flag is in /home/read_me/flag.txt .\nEnter your shellcode here.\n> ");
	char shellcode[128];
	fgets(shellcode, 128, stdin);
	int (*function)() = (int(*)())shellcode;
	function();
	return 0;
}