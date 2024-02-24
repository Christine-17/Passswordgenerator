class Authenticate:
    
    def __init__(self):
        self.passwords = {}

    def create_password(self, name, admno):
        name = name.lower()
        if name[0] not in self.passwords:
            self.passwords[name[0]] = []
            print("Password added successfully!")

    # You can add a search_password method here if needed
            
def main():
    authenticator = Authenticate()

    while True:
        print("\n1. create new password")
        print("2. edit password")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter name: ")
            admno = input("Enter admno: ")
            authenticator.create_password(name, admno)
       
elif choice == '2':
            letter = input("Enter the first letter to search password: ")
            # You need to implement the search_password method
            result = authenticator.search_password(letter)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
