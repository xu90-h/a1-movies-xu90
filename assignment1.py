"""
Name: Huang Xu
Date started: 06/14/2025
GitHub URL: https://github.com/cp1404-students/a1-movies-xu90-h.git
"""

# Constants for file handling and data
FILENAME = 'movies.csv'
VALID_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
STATUS_UNWATCHED = 'u'
STATUS_WATCHED = 'w'

def main():
    """Main function handling the menu loop."""
    print("Must-See Movies 1.0 - by Huang Xu")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")

    menu_choice = ""
    while menu_choice != "Q":
        print("Menu:")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        menu_choice = input(">>> ").strip().upper()

        # Conduct menu selection
        if menu_choice == "D":
            display_movies(movies)
        elif menu_choice == "A":
            add_movie(movies)
        elif menu_choice == "W":
            watch_movie(movies)
        elif menu_choice == "Q":
            save_movies(FILENAME, movies)
            print(f"{len(movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")



if __name__ == '__main__':
    main()
