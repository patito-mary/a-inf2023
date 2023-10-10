#include <stdio.h>
// #define manguito
/* Si pongo manguito aca, va a correr con el if de gato naranja
pero tambien puedo agregarlo con -D en la terminal */


int main()
{
#ifdef manguito
printf("Mi gato naranja es esquizofrenico \n");
#else
printf("Mi gato es normal \n");
#endif
return 0;
}
