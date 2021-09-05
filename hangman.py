
def hangman(word):
    wrong = 0
    stages=["",
            "________       ",
            "|       |      ",
            "|       |      ",
            "|       O      ",
            "|      /|\     ",
            "|       |      ",
            "|      / \     ",
            "|              ",
            ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字を予想してね(英小文字):"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print("正解は"+" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

def answer():
    with open("st.txt","r") as f:
        num = f.read().split(", ")
        import random
        return num[random.randint(0,len(num)-1)]
        


hangman(answer())
    


