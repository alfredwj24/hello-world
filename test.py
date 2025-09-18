def main():
    name = input("What is your name? ")
    
    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a valid number for your age.")
    
    current_year = 2023  # You can replace this with a dynamic year if needed
    birth_year = current_year - age

    print(f"Hello, {name}! You are {age} years old.")
    print(f"You were born in the year {birth_year}.")

if __name__ == "__main__":
    main()

