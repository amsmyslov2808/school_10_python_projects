#include <iostream>

using namespace std;

int main() {
    int balance_money = 10000;
    bool is_run = true;

    while (is_run) {
        printf("Текущий баланс на счету: %d руб.\n\n", balance_money);

        printf("Меню:\n");
        printf("1. Полнить баланс\n");
        printf("2. Снять деньги\n");
        printf("3. Разменять деньги на определённые купюры\n");
        printf("0. Выйти из программы\n");

        printf("Введите действие: ");
        int choose_action;

        scanf("%d", &choose_action);

        switch (choose_action) {
            case 1: {
                printf("Введие сумму нужную для пополнения: ");
                int income_money;

                scanf("%d", &income_money);

                balance_money += income_money;
                printf("Баланс успешно пополнен");
            }
            break;
            case 2: {
                printf("Введие сумму нужную для снятия: ");
                int outcome_money;

                scanf("%d", &outcome_money);

                if (outcome_money > balance_money) {
                    printf("Ошибка. Невозможно списать денег больше чем у вас есть на балансе.");
                } else {
                    balance_money -= outcome_money;
                    printf("Баланс успешно уменьшен");
                }
            }
            break;
            case 3: {
                printf("Введие сумму нужную для размена: ");
                int change_money;

                scanf("%d", &change_money);

                if (balance_money%change_money!=0) {
                    printf("Ошибка. Невозможно разменять %d по %d руб.", balance_money, change_money);
                }else {
                    printf("Можно разменять я выдам вам %d купюр по %d рублей",balance_money/change_money, change_money);
                }
            }
            break;
            case 0: {
                is_run = false;
                printf("Программа будет закрыта");
            }
            break;
            default: {
                printf("Ошибка. Такого действия нет");
            }
            break;
        }


        printf("\n\n\nНажмите Enter, чтобы продолжить...");
        getchar();     // Ожидаем нажатия клавиши
        getchar();     // Ожидаем нажатия клавиши
        printf("\n-----------------------------------\n\n");
    }
}
