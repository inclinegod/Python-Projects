#mortgage calculator

def borrowing():
    while True:
        try:
            salary = int(input("input your salary "))
        except ValueError as e:
            e = print("wrong data type inputted ")
            continue

max_allowed = borrowing()*4

print("the most you can borrow is,", max_allowed , "GBP")

def timetopay():
    while True:
        try:
            ttp = int(input("input years you would like to take a mortgage out for "))
        except ValueError as e:
            e = print("wrong data type inputted ")
            continue
        

################################### currently in progress #######################

