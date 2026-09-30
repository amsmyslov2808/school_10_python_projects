//
// Created by Алексей Смыслов on 30.09.2026.
//

#include <iostream>

using namespace std;

void mas_x2(int* mas, int n) {
    for (int i = 0; i < n; i++) {
        mas[i] *= 2;
    }
}

int main() {

    // int val = 30;
    // int* addr = &val;
    //
    // printf("%p\n", addr);
    // printf("%d\n", *addr);
    //
    // *addr = 20;
    //
    // printf("%d\n", val);

    // int *addr = nullptr;
    // printf("%p\n", addr);

    int a;
    scanf("%d", &a);


    // int a = 10;
    // int* b = new int(10);
    //
    // printf("%p\n", b);
    // printf("%d", *b);

    // int mas[3] = {1,2,3};

    // const long n = 3;
    // int* mas = new int[n]{1,2,3};
    //
    // for (int i=0; i<n; i++) {
    //     printf("mas[%d] = %d\n", i, mas[i]);
    // }
    //
    // mas_x2(mas, n);
    //
    // printf("\n\n-------\n\n");
    //
    // for (int i=0; i<n; i++) {
    //     printf("mas[%d] = %d\n", i, mas[i]);
    // }
    //
    // delete[] mas;

    return 0;
}