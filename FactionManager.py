import json
import os

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = {"factions": {"faction_data": []}, "relations": []}
    return data

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_faction(data):
    new_faction = {}
    new_faction["id"] = int(input("Enter faction ID: "))
    new_faction["portrait"] = input("Enter faction portrait (optional, enter 'None' if not available): ")
    new_faction["name"] = input("Enter faction name: ")
    new_faction["description"] = input("Enter faction description: ")
    default_relation = input("Enter default relation for the faction (optional, press Enter to skip): ")
    if default_relation:
        new_faction["defaultRelation"] = int(default_relation)
    data["factions"]["faction_data"].append(new_faction)

def add_relation(data):
    new_relation = {}
    new_relation["faction1Id"] = int(input("Enter faction1 ID for the relation: "))
    new_relation["faction2Id"] = int(input("Enter faction2 ID for the relation: "))
    new_relation["relation"] = int(input("Enter relation value: "))
    data["relations"].append(new_relation)

def edit_faction(data):
    print("Available factions:")
    for faction in data["factions"]["faction_data"]:
        print(f"Faction ID: {faction['id']}, Name: {faction['name']}")
    faction_id = int(input("Enter the ID of the faction to edit: "))
    for faction in data["factions"]["faction_data"]:
        if faction["id"] == faction_id:
            print("Editing Faction ID:", faction_id)
            faction["portrait"] = input("Enter faction portrait (optional, enter 'None' if not available): ")
            faction["name"] = input("Enter faction name: ")
            faction["description"] = input("Enter faction description: ")
            default_relation = input("Enter default relation for the faction (optional, press Enter to skip): ")
            if default_relation:
                faction["defaultRelation"] = int(default_relation)
            print("Faction edited successfully.")
            return
    print("Faction with ID", faction_id, "not found.")

def delete_faction(data):
    print("Available factions:")
    for faction in data["factions"]["faction_data"]:
        print(f"Faction ID: {faction['id']}, Name: {faction['name']}")
    faction_id = int(input("Enter the ID of the faction to delete: "))
    for faction in data["factions"]["faction_data"]:
        if faction["id"] == faction_id:
            data["factions"]["faction_data"].remove(faction)
            print("Faction with ID", faction_id, "deleted successfully.")
            return
    print("Faction with ID", faction_id, "not found.")

def edit_relation(data):
    print("Available relations:")
    for relation in data["relations"]:
        print(f"Faction1 ID: {relation['faction1Id']}, Faction2 ID: {relation['faction2Id']}, Relation: {relation['relation']}")
    faction1_id = int(input("Enter faction1 ID for the relation to edit: "))
    faction2_id = int(input("Enter faction2 ID for the relation to edit: "))
    for relation in data["relations"]:
        if relation["faction1Id"] == faction1_id and relation["faction2Id"] == faction2_id:
            print("Editing relation between Faction ID:", faction1_id, "and Faction ID:", faction2_id)
            relation["relation"] = int(input("Enter new relation value: "))
            print("Relation edited successfully.")
            return
    print("Relation between Faction ID", faction1_id, "and Faction ID", faction2_id, "not found.")

def delete_relation(data):
    print("Available relations:")
    for relation in data["relations"]:
        print(f"Faction1 ID: {relation['faction1Id']}, Faction2 ID: {relation['faction2Id']}, Relation: {relation['relation']}")
    faction1_id = int(input("Enter faction1 ID for the relation to delete: "))
    faction2_id = int(input("Enter faction2 ID for the relation to delete: "))
    for relation in data["relations"]:
        if relation["faction1Id"] == faction1_id and relation["faction2Id"] == faction2_id:
            data["relations"].remove(relation)
            print("Relation between Faction ID", faction1_id, "and Faction ID", faction2_id, "deleted successfully.")
            return
    print("Relation between Faction ID", faction1_id, "and Faction ID", faction2_id, "not found.")

def show_current_data(data):
    print("Current factions:")
    for faction in data["factions"]["faction_data"]:
        print(f"Faction ID: {faction['id']}, Name: {faction['name']}, Description: {faction['description']}")
    
    print("\nCurrent relations:")
    for relation in data["relations"]:
        print(f"Faction1 ID: {relation['faction1Id']}, Faction2 ID: {relation['faction2Id']}, Relation: {relation['relation']}")

def main():
    filename = "Factions.json"
    data = load_json(filename)

    while True:
        print("\nChoose operation:")
        print("1. Add Faction")
        print("2. Edit Faction")
        print("3. Delete Faction")
        print("4. Add Relation")
        print("5. Edit Relation")
        print("6. Delete Relation")
        print("7. Show Current Data")
        print("8. Save and Exit")
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            add_faction(data)
        elif choice == '2':
            edit_faction(data)
        elif choice == '3':
            delete_faction(data)
        elif choice == '4':
            add_relation(data)
        elif choice == '5':
            edit_relation(data)
        elif choice == '6':
            delete_relation(data)
        elif choice == '7':
            show_current_data(data)
            input("Press Enter to go back to the main menu...")
        elif choice == '8':
            save_json(data, filename)
            print("Data saved successfully.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
