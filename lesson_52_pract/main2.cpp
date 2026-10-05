#include <iostream>

using namespace std;

struct Elem {
    int data;
    Elem *next;
    Elem *prev;
};

int main() {
    srand(time(0));

    Elem *head = nullptr;
    Elem *tail = nullptr;

    Elem *new_elem = new Elem;
    new_elem->data = rand()%100;
    new_elem->next = nullptr;
    new_elem->prev = nullptr;

    head = new_elem;
    tail = new_elem;

    Elem *new_elem2 = new Elem;
    new_elem2->data = rand()%100;
    new_elem2->next = nullptr;
    new_elem2->prev = tail;
    new_elem2->prev->next = new_elem2;

    tail = new_elem2;

    Elem *new_elem3 = new Elem;
    new_elem3->data = rand()%100;
    new_elem3->next = nullptr;
    new_elem3->prev = tail;
    new_elem3->prev->next = new_elem3;

    tail = new_elem3;

    Elem* cur_elem = head;
    do {
        printf("%d\n", cur_elem->data);
        cur_elem = cur_elem->next;
    }while (cur_elem != nullptr);

    printf("\n------------\n");

    Elem *new_elem4 = new Elem;
    new_elem4->data = 999;
    new_elem4->next = head->next;
    new_elem4->prev = head;

    head->next->prev = new_elem4;
    head->next = new_elem4;

    Elem* cur_elem2 = head;
    do {
        printf("%d\n", cur_elem2->data);
        cur_elem2 = cur_elem2->next;
    }while (cur_elem2 != nullptr);


    return 0;
}