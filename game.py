import turtle

def Error(text: str):
    print(text)
    input("Click any button to exit...")
    exit()

players:list = []
colors:list = [
    'red', 'orange', 'yellow', 'green', 'blue', 'silver', 'gray',
    'black', 'purple', 'pink', 'gold'
]
nowPlayer = 1
playersCount = None
speed = 10

try:
    playersCount = int(input("Select how many players will be - "))
    if playersCount > 11:
        Error("Oops.. Too many players!")
    elif playersCount < 1:
        Error("Oops.. Too few players!")
except: Error("Oops.. Writed players count is not a number!")

try:
    speed = int(input("Select arrows speed - "))
    if speed > 70:
        Error("Oops.. Too big speed!")
    if speed < 3:
        Error("Oops.. Too small speed!")
except: Error("Oops.. Writed arrow's speed is uncorrect!!")

for iter in range(1, playersCount+1):
    player = turtle.Turtle()
    player.speed(15)
    player.color(colors.pop(0))
    players.append(player)

while True:
    def turning():
        global nowPlayer, playersCount, players

        turn = input(f"Player {nowPlayer}'s turns (w, a, s, d): ")
        if turn == "":
            print("Oops.. You must write W, A, S or D!")
            turning()

        match turn.lower():
            case "w":
                players[nowPlayer-1].forward(speed)
            case "a":
                players[nowPlayer-1].left(45)
            case "d":
                players[nowPlayer-1].right(45)
            case "s":
                players[nowPlayer-1].backward(speed)
                players[nowPlayer-1].left(180)
            case "quit" | "exit" | "выйти" | "выход":
                print("Exit...")
                exit()
            case _:
                print("Oops.. You must write W, A, S или D!")
                turning()

        if nowPlayer > playersCount-1:
            nowPlayer = 1
        else:
            nowPlayer += 1

    turning()
