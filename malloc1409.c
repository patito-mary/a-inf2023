#include <stdio.h>
#include <stdlib.h>

int main() {
    int *counter;
    int Nele = 5; // Nele es Numero de elementos hahsfjk
    // malloc reserva la memoria
    counter = malloc(Nele*sizeof(int));
    // Ahora counter[*] se puede usar igual a un array estatico:
    for (int i=0; i<Nele; i++)
        counter[i] = i;
    // Imprime los valores asignados
    for (int i = 0; i < Nele; i++)
        printf("counter[%d] = %d\n", i, counter[i]);
    // Luego de usar la memoria dinamica se debe liberar:
    free(counter);
}   