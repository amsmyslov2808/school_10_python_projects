#include <iostream>

using namespace std;

int main() {
    srand(time(0));

    int number1, number2;
    int right_answer, user_answer;

    while (true) {
        number1 = rand() % 10;
        number2 = rand() % 10;

        right_answer = number1 + number2;

        printf("%d + %d = ?\n", number1, number2);

        printf("введите свой ответ: ");
        scanf("%d", &user_answer);

        if (user_answer == right_answer) {
            printf("отлично правильный ответ!");
        }else {
            printf("ответ %d неверный! правильный ответ = %d",user_answer,right_answer);
        }

        printf("\n\n");

    }

    return 0;
}
