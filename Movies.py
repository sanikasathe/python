#Q10
# Initialize an empty dictionary to store the movie collection
movie_collection = {}

while True:
    print("\nMovie Collection Menu:")
    print("1. Add Movie")
    print("2. Update Rating")
    print("3. Display Movies")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the movie title: ")
        rating = float(input("Enter the movie rating (out of 10): "))
        movie_collection[title] = rating
        print(f"Movie '{title}' added successfully!")

    elif choice == "2":
        title = input("Enter the movie title: ")
        if title in movie_collection:
            new_rating = float(input("Enter the new movie rating (out of 10): "))
            movie_collection[title] = new_rating
            print(f"Rating for '{title}' updated successfully!")
        else:
            print(f"Movie '{title}' not found in the collection.")

    elif choice == "3":
        if movie_collection:
            print("Movie Collection:")
            for title, rating in movie_collection.items():
                print(f"{title}: {rating}/10")
        else:
            print("Movie collection is empty.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")
