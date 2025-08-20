# Name: John Castillo
# Course Number: CIS261
# Lab Title: Movie Guide Part 2

import os

FILE_NAME = "movies.txt"

def display_menu():
    """Displays the command menu for the user."""
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def read_movies():
    """
    Reads movie titles from the movies.txt file and returns them as a list.
    Handles file not found errors by creating a new file with initial movies.
    """
    try:
        with open(FILE_NAME, "r") as file:
            movies_list = [line.strip() for line in file.readlines()]
            return movies_list
    except FileNotFoundError:
        # Create the file with initial movies if it doesn't exist
        print("Creating movies.txt with initial data...")
        initial_movies = ["Cat on a Hot Tin Roof", "On the Waterfront", "Monty Python and the Holy Grail"]
        with open(FILE_NAME, "w") as file:
            for movie in initial_movies:
                file.write(movie + "\n")
        return initial_movies

def write_movies(movies_list):
    """Writes the movies list back to the movies.txt file."""
    with open(FILE_NAME, "w") as file:
        for movie in movies_list:
            file.write(movie + "\n")

def display_movies(movies_list):
    """Displays the numbered list of movies."""
    print()
    if not movies_list:
        print("There are no movies in the list.\n")
    else:
        for i, movie in enumerate(movies_list, start=1):
            print(f"{i}. {movie}")
        print()

def add_movie(movies_list):
    """Prompts the user to add a movie, adds it to the list, and saves it to the file."""
    movie_title = input("Movie: ").strip()
    if movie_title:
        movies_list.append(movie_title)
        write_movies(movies_list)
        print(f"{movie_title} was added.")
    else:
        print("Movie title cannot be empty.")

def delete_movie(movies_list):
    """Prompts the user to delete a movie, validates the input, and saves the updated list."""
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies_list):
            deleted_movie = movies_list.pop(number - 1)
            write_movies(movies_list)
            print(f"{deleted_movie} was deleted.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid movie number. Please enter an integer.")

def main():
    """Main function to run the Movie Guide program."""
    print("The Movie List program\n")
    
    # Check if the file exists and create it with initial movies if not
    movies_list = read_movies()
    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            display_movies(movies_list)
        elif command == "add":
            add_movie(movies_list)
            display_movies(movies_list)
        elif command == "del":
            delete_movie(movies_list)
            display_movies(movies_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            
if __name__ == "__main__":
    main()
