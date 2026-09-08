#wap to simulate to simulate a digital lock system. thelock should ask the user to engter 4c digit pins.if entered pin doesnt conataon exacatly 4 digotls. the program shpuld display an error msg and ask again .if the pin enterred is correcr, the lock should open. otherwise the proram sgould ask the user to try again . write the program for me easy and explain the logic


correct_pin = "1234"

while True:
    pin = input("Enter your 4-digit PIN: ")

    # Check whether PIN has exactly 4 digits
    if len(pin) != 4 or not pin.isdigit():
        print("Error! PIN must contain exactly 4 digits.")
        continue

    # Check the PIN
    if pin == correct_pin:
        print("Correct PIN! Lock Opened.")
        break
    else:
        print("Incorrect PIN! Try again.")