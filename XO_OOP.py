def CleanScreen():
    import os
    os.system("cls" if os.name == "nt" else "clear")

class clsPlayer:
    def init(self):
        self.__Name = ""
        self.__Single = ""
    def get_Name(self):
            return self.__Name
    def set_Name(self):
        return self.__Name
    def get_Single(self):
            return self.__Single
    def set_Single(self):
        return self.__Single
    def ChooseName(self, N):
        while True:
            Name = input(f"Enter Name {N}: ")
            if str(Name).isalpha():
                self.__Name = Name
                break
            print("Error Name")
    def ChooseSingle(self):
        while True:
            Single = input(f"{self.__Name}, Enter Single: ")
            if str(Single).isalpha() and len(Single) == 1:
                self.__Single = Single.upper()
                break
            print("Error Single")



    




class clsMenu:
    @staticmethod
    def PrintTitleGame():
        print("Welcome To My X - O Game: ")
    @staticmethod
    def ChooseMenu():
        print("1. Start Game.")
        print("2. Quit Game.")
    @staticmethod
    def ReadNumber(Massage, From, To):
        try:
            Number = int(input(Massage))
        except:
            print("Only Number")
            return clsMenu.ReadNumber(Massage, From, To)
        if Number < From or Number > To:
            print(f"Enter Number From {From} To {To}: ")
            return clsMenu.ReadNumber(Massage, From, To)            
        return Number
    @staticmethod
    def PrintGameOver():
        print("Game Over!")
    @staticmethod
    def ChooseRestartGame():
        print("1. Restart Game")
        print("2. Quit Game")
    @staticmethod
    def StartGame():
        clsMenu.PrintTitleGame()
        clsMenu.ChooseMenu()
        return clsMenu.ReadNumber("Enter Your Choice (1 or 2): ", 1, 2)
    @staticmethod
    def GameOver():
        clsMenu.PrintGameOver()
        clsMenu.ChooseRestartGame()
        return clsMenu.ReadNumber("Enter Your Choice (1 or 2): ", 1, 2)







class clsBoard:
    def __init__(self):
        self.ListBoard = [str(i) for i in range(1, 10)]
    def PrintBoard(self):
        for i in range(0, 9, 3):
            print("  |  ".join(self.ListBoard[i:i+3]))
            if i < 6:
                print("-"*13)

    def UpdateBoard(self, Move, Single):
        if self.IsValidMove(Move):
            self.ListBoard[Move - 1] = Single
            return 1
        return 0
    def IsValidMove(self, Move):
        return str(self.ListBoard[Move - 1]).isdigit()
    def ShowWinBoard(self, ListMoveWin):
        self.ListBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.ListBoard[ListMoveWin[0] - 1] = "*"
        self.ListBoard[ListMoveWin[1] - 1] = "*"
        self.ListBoard[ListMoveWin[2] - 1] = "*"
    def voidBoard(self):
        self.ListBoard = [str(i) for i in range(1, 10)]


class clsGame:
    def __init__(self):
        self.ListPlayer = [clsPlayer(), clsPlayer()]
        self.Menu = clsMenu()
        self.Board = clsBoard()
        self.IndexListPlayer = 0

    def StartGame(self):
        CleanScreen()
        ChooseNumber = self.Menu.StartGame()
        if ChooseNumber == 1:
            self.InfoPlayer()
            self.GamePlay()
        else:
            self.QuitGame()

    def QuitGame(self):
        print("Quit Game, Thank You.")
    def InfoPlayer(self):
        ListNotSingle = []
        for i, List in enumerate(self.ListPlayer, start = 1):
            CleanScreen()
            print(f"Info Player ({i})")
            List.ChooseName(i)
            while True:
                List.ChooseSingle()
                if List.get_Single() not in ListNotSingle:
                    break
            ListNotSingle.append(List.get_Single())
    def GamePlay(self):
        while(True):
            CleanScreen()
            self.Play()
            if self.CheckWin() or self.CheckDrow():
                ChooseNumber = self.Menu.GameOver()
                if ChooseNumber == 1:
                    self.RestartGame()
                else:
                    self.QuitGame()
                    break
    def RestartGame(self):
        self.Board.voidBoard()
        self.IndexListPlayer = 0
        self.GamePlay()

    def Play(self):
        self.Player = self.ListPlayer[self.IndexListPlayer]
        self.Board.PrintBoard()
        print(f"{self.Player.get_Name()} ({self.Player.get_Single()})")
        while True:
            ChooseNumber = clsMenu.ReadNumber("Choose Number (1-9): ", 1, 9)
            if self.Board.IsValidMove(ChooseNumber):
                self.Board.UpdateBoard(ChooseNumber, self.Player.get_Single())
                break
        self.SwapPlayer()
    def SwapPlayer(self):
        self.IndexListPlayer = 1 - self.IndexListPlayer
    def CheckWin(self):
        # 1 2 3
        # 4 5 6
        # 7 8 9
        Board = self.Board.ListBoard
        ListWin = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
        for List in ListWin:
            if Board[List[0] - 1] == Board[List[1] - 1] == Board[List[2] - 1]:
                self.Win(List)
                return 1    
        return 0
    def Win(self, List):
        CleanScreen()
        self.Board.PrintBoard()
        self.Board.ShowWinBoard(List)
        self.Board.PrintBoard()
        print(f"Win Player: {self.ListPlayer[self.IndexListPlayer - 1].get_Name()}")

    def CheckDrow(self):
        for i in self.Board.ListBoard:
            if str(i).isdigit():
                return 0
        self.Drow()
        return 1
        # return all(i.isalpha() for i in self.Board.ListBoard)
        # return all(not i.isdigit() for i in self.Board.ListBoard)                
    def Drow(self):
        CleanScreen()
        self.Board.PrintBoard()
        print("Drow")



clsGame().StartGame()