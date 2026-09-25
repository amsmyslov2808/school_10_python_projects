#include <iostream>

using namespace std;

int main() {
    // Запускаем генератор случайных чисел с новым значением при каждом старте программы.
    srand(time(0));

    int number1, number2;
    int right_answer, user_answer;

    // Цикл создаёт новые примеры, пока программа не будет остановлена.
    while (true) {
        // Остаток от деления на 10 даёт случайное число от 0 до 9.
        number1 = rand() % 10;
        number2 = rand() % 10;

        right_answer = number1 + number2;

        printf("%d + %d = ?\n", number1, number2);

        printf("введите свой ответ: ");
        // Символ & передаёт scanf адрес переменной, в которую нужно записать ответ.
        scanf("%d", &user_answer);

        // Сравниваем ответ ученика с заранее вычисленной суммой.
        if (user_answer == right_answer) {
            printf("отлично правильный ответ!");
        }else {
            printf("ответ %d неверный! правильный ответ = %d",user_answer,right_answer);
        }

        printf("\n\n");

    }

    return 0;
}
