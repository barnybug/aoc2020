
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    int data[] = {2, 5, 3, 1, 4, 9, 8, 6, 7};
    const int datalen = sizeof(data)/sizeof(int);
    const int n = 1000000;
    const int times = 10000000;
    int *nodes = (int *)malloc((n+1) * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int a = i < datalen ? data[i] : i + 1;
        int b = (i + 1) % n < datalen ? data[(i+1) % n] : i + 2;
        nodes[a] = b;
    }

    int current = data[0];

    for (int i = 0; i < times; ++i) {
        int a = nodes[current];
        int b = nodes[a];
        int c = nodes[b];
        nodes[current] = nodes[c];
        int destination = current;
        while (1) {
            destination -= 1;
            if (destination < 1)
                destination = n;
            if (destination != a && destination != b && destination != c)
                break;
        }
        
        nodes[c] = nodes[destination];
        nodes[destination] = a;
        current = nodes[current];
    }

    long answer = (long)nodes[1] * (long)nodes[nodes[1]];
    printf("%lu\n", answer);

    free(nodes);
    return 0;
}
