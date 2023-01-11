import random


class RandomPassGenerator:
    count = 0
    slash = 1

    def __init__(self, lenght):
        self.lenght = lenght

    def mixed(self):
        """this function return mixed password"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                   ]
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        sym = ['$', '%', '&', '(', ')', '*', '+', '-',
               '.', '/', ':', ';', '<', '=', '>', '?', '@', '\\'
               ]
        a = self.lenght // 3
        b = self.lenght % 3
        a = random.choices(letters, k=a) + random.choices(numbers, k=a) + random.choices(sym, k=a) \
            + random.choices(numbers, k=b)

        c = random.shuffle(a)
        c = "".join(a)
        res = ''.join(str(e) for e in a)
        return res

    def numbers(self):
        """this function return password of number"""
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = random.choices(numbers, k=self.lenght)
        res = ''.join(str(e) for e in num)
        return res

    def letters(self):
        """this function return password of letters"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                   ]
        let = random.choices(letters, k=self.lenght)
        res = ''.join(str(e) for e in let)
        return res
