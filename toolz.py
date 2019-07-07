

# Repeat a print statement
class pTools(object):
    def __init__(self):
        pass

    def rePrint(self, num, text):
        for n in range(num):
            print(text)

    def betTup(self, num, tup):
        """Evaluates if a number is between a tuples two values."""
        return tup[0] <= num <= tup[1]

    def mulT(self, num, mult):
        return num * mult


n = pTools()
n.betTup(100, (33, 999))

print(n.betTup(100, (33, 999)))
