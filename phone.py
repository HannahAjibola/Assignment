def main():
    print("Phone book")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("5. Tone")
    print("6. Setting")
    print("7. Call divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")

    home = int(input("\nSelect an option: "))

    if home == 1:
        print("1. Search")
        print("2. Servic Nos")
        print("3. Add Name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign Tone")
        print("7. Send b card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice Tags")

        phone_book_option = int(input("Enter choice: "))

        if phone_book_option == 1:
            print("Search")
        elif phone_book_option == 2:
            print("Service Nos")
        elif phone_book_option == 3:
            print("Add Name")
        elif phone_book_option == 4:
            print("Erase")
        elif phone_book_option == 5:
            print("Edit")
        elif phone_book_option == 6:
            print("Assign Tone")
        elif phone_book_option == 7:
            print("Send b card")
        elif phone_book_option == 8:
            print("Options")
            print("1. Type of view")
            print("2. Memory status")
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
