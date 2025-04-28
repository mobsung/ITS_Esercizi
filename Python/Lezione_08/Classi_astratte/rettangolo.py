from forma_generica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")


    def draw(self):
        print(f'\n{self.getShape()}\n')
        
        # rettangolo = [["*" for i in range(10)] for j in range (5)]

        # for row in rettangolo:
        #     print(f"{''.join(row)}")

        for i in range(5):
            for j in range(10):
                if i == 0 or i == 5 - 1:
                    print("*", end=" ")
                elif j == 0 or j == 9:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("\n", end="")



r = Rettangolo()

r.draw()
