'''#PHASE 1
#input from users
name=input("enter the name:")
phone=input("enter the phone number:")
mail=input("enter the email address:")
#saved message
print("contact details saved")
#printing the input info
print("name:",name,"phone number:",phone,"email address:", mail)

#PHASE 2
#printing the options 
contacts = []  # store all contacts
while True:
    # printing the options
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    # adding contacts
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        mail = input("Enter the email address: ")
        contacts.append([name, phone, mail])
        print("Contact added!")
    # viewing contacts
    elif choice == 2:
        if not contacts:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for i in contacts:
                print("Name:", i[0], "Phone:", i[1], "Email:", i[2])
    # exiting program
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Error.. enter a valid choice")'''

#PHASE 3
#printing the options
contacts=[] #storing all contacts 
while True:
    # printing the options
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    # adding contacts 
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        mail = input("Enter the email address: ")
        c={"name": name, "phone number": phone, "email": mail}
        contacts.append(c)
        print("Contact added!")
    # viewing contacts
    elif choice == 2:
        if not contacts:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for i, j in enumerate (contacts,start=1):
                print(f"{i}) Name: {j['name']} \nPhone number: {j['phone number']} \nEmail: {j['email']}")
    # exiting program
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Error.. enter a valid choice")


