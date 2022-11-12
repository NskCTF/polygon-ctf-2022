#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
}


struct laptop_rent {
	int is_admin;
  char tenant[16];
  char password[16];
  char laptop_name[64];
};

int print_flag(){
	char flag[32];
	FILE *fp;

	if (access("/home/easyheap/flag.txt", F_OK) != 0) {
    perror("No flag. Contact with admins.");
    return 1;
	}
	fp = fopen("/home/easyheap/flag.txt", "r");
	fgets(flag, 32, (FILE*)fp);
	printf("%s", flag);
	printf("\n");
	fclose(fp);
	return 0;
}

int main(){
	size_t buffsize = 16;
	char pass[16];
	struct laptop_rent *storage[50];
	int cur_cnt = -1;
	char choice;
	int is_logged_in = 0;
	int uid;
	

	init();
	puts("WELCOME TO JOHN LAPTOP RENTAL!!!\n");
	while (1){
		printf("What do u want to do?\n1)[r]->rent laptop\n2)[c]->change rent information(login required)\n3)[i]->log in\n5)[o]->log out(login required)\n6)[s]->show secret(login required)\n7)[e]->exit\n> ");
		scanf("%c", &choice );
		while( choice != '\n' && getchar() != '\n' );
		switch(choice){
			case 'r':
				if (cur_cnt < 50){
					cur_cnt += 1;
					storage[cur_cnt]=malloc(sizeof(struct laptop_rent));
					storage[cur_cnt]->is_admin = 0;
					printf("Enter your name: ");
					fgets(storage[cur_cnt]->tenant, buffsize, stdin);
					printf("Enter password: ");
					fgets(storage[cur_cnt]->password, buffsize, stdin);
					printf("Enter model for rent: ");
					gets(storage[cur_cnt]->laptop_name);
					printf("Successfully rent. Your id is %d.\n", cur_cnt);
				}
				else{
					printf("We ran out of laptop. Bye bye.\n");
					exit(0);
				}
				break;
			case 'c':
				if (is_logged_in){
					printf("Enter your name: ");
					fgets(storage[uid]->tenant, buffsize, stdin);
					printf("Enter password: ");
					fgets(storage[uid]->password, buffsize, stdin);
					printf("Enter model for rent: ");
					gets(storage[uid]->laptop_name);
					printf("Successfully change data.\n");
				}
				else{
					printf("Log in first.\n");
				}
				break;
			case 'e':
				exit(0);
			case 'i':
				if (is_logged_in){
					printf("Log out first.\n");
				}
				else{
					printf("Enter your id: ");
					scanf("%d%*c", &uid);
					if (uid <= cur_cnt){
						if (uid >= 0 && uid < 50){
							printf("Enter password: ");
							fgets(pass, buffsize, stdin);
							if (!strcmp(pass, storage[uid]->password)){
								printf("Successfully log in.\n");
								is_logged_in = 1;
							}
							else{
								printf("Invalid password.\n");
							}
						}
						else{
							printf("Id out of range.\n");
						}
					}
					else{
						printf("No such records.\n");
					}
				}
				break;
			case 'o':
				if (is_logged_in){
					is_logged_in = 0;
					printf("Successfully log out.\n");
				}
				else{
					printf("Log in first.\n");
				}
				break;
			case 's':
				if (is_logged_in){
					if (storage[uid]->is_admin == 0xCAFE){
						print_flag();
					}
					else{
						printf("You are not admin.\n");
					}
				}
				else{
					printf("Log in first.\n");
				}
				break;
			default:
				puts("Invalid input.\n");
		}
	}
	for (int i = 0; i <= cur_cnt; i++){
		free(storage[i]);
	}
	return 0;
}