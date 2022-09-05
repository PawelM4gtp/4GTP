#include <cstdio>
#include<windows.h>
#include <iostream>
int a;
float b;

int main()
{

  printf("podaj nr zad\n1 zaokraglij \n2 system 16 \n3 zera \n4 koniec \n");
  scanf("%d",&a);
  printf("jakiej liczby chcesz uzyc? \n");
  scanf("%f" ,&b);
switch(a)
{
case 1:
  printf("zaokraglenie: %.2f\n",b);
  system("pause");
  	break;
case 2:
  printf("System 16: %x \n",b);
  system("pause");
  	break;
case 3:
  printf("Zera: %04d  \n" ,b);
  system("pause");
  	break;
case 4:
  printf("Koniec   \n");
  system("pause");
  	break;
  
}
return 0;
}
