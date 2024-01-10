import json

students_data = []

def insert_data():
    name = input("Enter name: ")
    # Checking if name is unique
    for student in students_data:
        if student.get('Name') == name:
            print("Value already exists with this name")
            return
    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter pincode: ")
    sat_score = int(input("Enter SAT score: "))

    # Calculate Passed status
    passed = "Pass" if sat_score > 30 else "Fail"

    # Insert data into the memory
    students_data.append({
        "Name": name,
        "Address": address,
        "City": city,
        "Country": country,
        "Pincode": pincode,
        "SAT Score": sat_score,
        "Passed": passed
    })
    print("Data inserted successfully!")

def view_data():
    print("All data in JSON format:")
    print(json.dumps(students_data, indent=2))

def get_rank():
    students_data.sort(key=lambda x: x['SAT Score'], reverse=True)
    print("Ranking:")
    for i, student in enumerate(students_data, start=1):
        print(f"Rank {i}: {student['Name']} - {student['SAT Score']} points")

def update_score():
    name = input("Enter name to update SAT score: ")
    for entry in students_data:
        if entry['Name'] == name:
            new_score = int(input("Enter new SAT score: "))
            entry['SAT Score'] = new_score

            # Recalculate Passed status
            entry['Passed'] = "Pass" if new_score > 30 else "Fail"

            print("SAT score updated successfully!")
            return

    print(f"No record found for {name}")

def delete_record():
    name = input("Enter name to delete record: ")
    for entry in students_data:
        if entry['Name'] == name:
            students_data.remove(entry)
            print("Record deleted successfully!")
            return

    print(f"No record found for {name}")

def save_to_json():
    with open('sat_results.json', 'w') as json_file:
        json.dump(students_data, json_file, indent=2)
    print("Data saved to 'sat_results.json'")

while True:
    print("\nMenu:")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update SAT score")
    print("5. Delete one record")
    print("6. Save data to JSON")
    print("7. Exit")

    choice = input("Enter your choice from 1 to 7 : ")

    if choice == '7':
        break
    elif choice == '1':
        insert_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        get_rank()
    elif choice == '4':
        update_score()
    elif choice == '5':
        delete_record()
    elif choice == '6':
        save_to_json()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
