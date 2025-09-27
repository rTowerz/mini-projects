
# Add jason files to save data between sessions

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number.")

    people.pop(number - 1)
    print("Contact deleted.")

def search_contact(people):
    search_name = input("Search for a name: ").lower()
    result = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)

    display_people(result)

print("Hi, welcome to the Contact Management System.")
print()

people = []

while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()
    

    if command == "add":
        person = add_person()
        people.append(person)
        print("Contact added.")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search_contact(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

