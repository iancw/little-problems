#include <stdio.h>

void reverse(char* str){
  char tmp;
  int len,i;
  for (len=0; str[len] != '\0'; len++);
  for (i=0; i<len/2; i++){
    tmp = str[i];
    str[i] = str[len-1-i];
    str[len-1-i] = tmp;
  }
}

int main(int argc, char** argv){
  printf("Input: %s\n", argv[1]);
  reverse(argv[1]);
  printf("Result: %s\n", argv[1]);
  return 0;
}
