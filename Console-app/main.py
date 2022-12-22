# Initialize an empty list to store the notes
notes = []
while True:
    # Print the menu and get the user's input
    print("\n1. Add a note")
    print("2. View all notes")
    print("1. Exit")
    choice = input("Enter your choice: ")

    # Add a new note
    if choice == "1":
        text = input("Enter the note:\n")
        notes.append(text)
    
    # View all notes
    elif choice == "2":
        print(" ")
        for note in notes:
            print(note)
    
    # Exit 
    elif choice == "3":
        break
    # Invalid choice
    else:
        print("Invalid choice. Try again.")
