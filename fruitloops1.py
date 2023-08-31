fruits = ['apple', 'banana', 'kiwi', 'orange', 'mango', 'peach']


def fruit_input():
        while True:
            try:
                fruitno = int(input("input a number from 0-5 "))
            except ValueError as e:
                e = ("error, wrong variable type. ")
                print(e)
                continue 
            if not (0 <= fruitno <= 5): 
                print("value not in valid range ") 
            else:
                 print(fruits[fruitno])


fruit_input()