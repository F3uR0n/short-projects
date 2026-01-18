import os

if __name__ == '__main__':
    print("Welcome to Robo Voice")

    while True:
        z = input("Enter what you want me to speak: ")
        if z == "end":
            print("Goodbye 👋")
            break

        command = f"say {z}"
        os.system(command)