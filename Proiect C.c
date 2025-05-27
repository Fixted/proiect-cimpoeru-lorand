#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numar_secret, incercare, numar_incercari = 0;
// Number Guesser 

    srand(time(0));
    numar_secret = rand() % 100 + 1;

    printf("Ghiceste numarul (intre 1 si 100):\n");

    do {
        printf("Introdu o valoare: ");
        scanf("%d", &incercare);
        numar_incercari++;

        if (incercare < numar_secret) {
            printf("Prea mic!\n");
        } else if (incercare > numar_secret) {
            printf("Prea mare!\n");
        } else {
            printf("Felicitari! Ai ghicit numarul in %d incercari!\n", numar_incercari);
        }

    } while (incercare != numar_secret);

    return 0;
}
