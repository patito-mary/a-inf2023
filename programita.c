#include<stdio.h>
#include<stdlib.h>

int main()
{
    void *p;
    while(1)
        p=malloc(1000*sizeof(char));
    return 0;

}
