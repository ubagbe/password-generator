class Application:
    def __init__(self):
        pass

    def show_menu(self):
        print("-------------------------")
        print("PASSWORD GENERATOR SYSTEM")
        print("-------------------------")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("please Enter You Choice : ")
            if choice == "1":
                print("Generate Password")
            elif choice == "2":
                print("Check Password Strength")    
            elif choice == "3":
                print("Exit")
                break
            else:
                print("Invalid menu choice")    


if __name__ == "__main__":
    app = Application()
    app.run()
