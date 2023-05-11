from datetime import datetime
print("welcome sir,")
while True:
    print(datetime.now().strftime("%H:%M:%S"), ">>>")
    inp = input()
    if inp == "exit":
        break
    else:
        continue
