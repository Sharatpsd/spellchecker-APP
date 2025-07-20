import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name '{filename}': created successfully!")
    except FileExistsError:
        print(f"File name '{filename}' already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print('No files found.')
    else:
        print('Files in directory:')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exist!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n=== File Management App ===")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter file name to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter file name to read: ")
            read_file(filename)
        elif choice == '5':
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
