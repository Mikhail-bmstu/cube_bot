class WordList:
    def __init__(self, win_path="texts/win.txt", lose_path="texts/lose.txt"):
        with open(win_path, mode='r', encoding="utf-8") as win_f:
            self._win_lst = [line.rstrip('\n') for line in win_f.readlines()]
        with open(lose_path, mode='r', encoding="utf-8") as lose_f:
            self._lose_lst = [line.rstrip('\n') for line in lose_f.readlines()]

    @property
    def win_lst(self):
        return self._win_lst

    @property
    def lose_lst(self):
        return self._lose_lst
