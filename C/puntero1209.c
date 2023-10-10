#include <stdio.h>
#include <stdlib.h>

int main(){
    int a;
    a = 506;
    printf("mi variable es = %d \n", a);
    printf("la direccion de mi variable en hexagesimal es = %p \n", (void*)&a);
    // el %p es de puntero jaja lol
    // int *pa;
    // pa = &a;
    // printf('pa = ')
    return 0;
}
