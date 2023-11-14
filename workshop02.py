import random

def randomNumber():
    Number = random.randint(1, 100)
    
    while True:
        try:
            userInput = int(input("ทายตัวเลขที่มีค่าอยูที่ 1-100: "))
            if userInput == Number:
                print("ยินดีด้วยคุณทายถูก!")
                break
            elif userInput < Number:
                print("ตัวเลขน้อยไป ทายใหม่นะ !")
            else:
                print("ตัวเลขมากไป ทายใหม่นะ!")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

randomNumber()