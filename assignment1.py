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

def load_movies(filename):
    """Load movies from CSV file into list of lists."""
    movies = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            title = parts[0]
            year = int(parts[1])
            category = parts[2]
            status = parts[3]
            movies.append([title, year, category, status])
    return movies

def save_movies(filename, movies):
    with open(filename, 'w') as out_file:
        for movie in movies:
            print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=out_file)

def display_movies(movies):
    """Display all movies sorted by year and title."""
    sorted_movies = sorted(movies, key=lambda m: (m[1], m[0]))
    to_watch = 0
    watched = 0

    for i in range(len(sorted_movies)):
        movie = sorted_movies[i]
        mark = "*" if movie[3] == STATUS_UNWATCHED else " "
        print(f"{i:2}. {mark} {movie[0]:35} - {movie[1]:4} ({movie[2]})")
        if movie[3] == STATUS_UNWATCHED:
            to_watch += 1
        else:
            watched += 1

    print(f"{watched} movies watched. {to_watch} movies still to watch.")



if __name__ == '__main__':
    main()
