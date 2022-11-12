#include <stdio.h>

#include <string.h>

int main(void) {
  char str[80];
  int check[] = {
    1269, 1286, 1272, 1325, 1253, 1299, 1317, 1323, 1297, 1320, 1303, 1316, 1323, 1297, 1253, 1299, 1317, 1323, 1327
  };
 int i;

  printf("Enter flag: ");
  fgets(str, 20, stdin);

  /* remove newline, if present */
  i = strlen(str) - 1;
  if (str[i] == '\n')
    str[i] = '\0';

  for (int i = 0; i < 19; i++) {
//printf("%d ", (int)(str[i]) + 1202);
//printf("%d\n", (int)(check[i]));
    if ((int)(str[i]) + 1202 != (int)(check[i])) {
      printf("Bad flag\n");
      exit(1);
    }
  }
  printf("good flag\n");
  return 0;
}
