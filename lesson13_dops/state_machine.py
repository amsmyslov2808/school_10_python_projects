import state_machine_func

STAGE_LOBBY = 1
STAGE_ROOM1 = 2
STAGE_ROOM2 = 3
STAGE_ROOM3 = 4

global_current_stage = STAGE_LOBBY


def proccess_stage_lobby():
    global global_current_stage

    print("добро пожаловать в лобби")
    answer = state_machine_func.input_int("выбери комнату куда пойдёшь 1 2 3: ")
    if answer == 1:
        global_current_stage = STAGE_ROOM1
    if answer == 2:
        global_current_stage = STAGE_ROOM2
    if answer == 3:
        global_current_stage = STAGE_ROOM3


def proccess_stage_room1():
    global global_current_stage
    print("ты пришёл в комнату 1")
    print("сейчас тебя перекинет назад в лобби")
    global_current_stage = STAGE_LOBBY


def proccess_stage_room2():
    global global_current_stage
    print("ты пришёл в комнату 2")
    print("сейчас тебя перекинет назад в лобби")
    global_current_stage = STAGE_LOBBY


def proccess_stage_room3():
    global global_current_stage
    print("ты пришёл в комнату 3")
    print("сейчас тебя перекинет назад в лобби")
    global_current_stage = STAGE_LOBBY


while True:
    if global_current_stage == STAGE_LOBBY:
        proccess_stage_lobby()
    elif global_current_stage == STAGE_ROOM1:
        proccess_stage_room1()
    elif global_current_stage == STAGE_ROOM2:
        proccess_stage_room2()
    elif global_current_stage == STAGE_ROOM3:
        proccess_stage_room3()

    print("Нажмите enter")
    input()
