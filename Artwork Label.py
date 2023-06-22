class Artist:  # Artist class

    # Artist class constructor, takes in name, birth year, and death year
    # Default value for name is "unknown", and for birth and death year is -1
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    # print_info function prints out the artist's name, birth year, and death year
    def print_info(self):
        year_info = "" # year info string
        # if birth year is nonnegative and death year is negative
        if self.birth_year >= 0 and self.death_year < 0:
            year_info = str(self.birth_year) + " to present"
        # if birth year is negative
        elif self.birth_year < 0:
            year_info = "unknown"
        else: # birth year is nonnegative and death year is nonnegative
            year_info = str(self.birth_year) + " to " + str(self.death_year)
        print(f"Artist: {self.name} ({year_info})") # print artist info


class Artwork:  # Artwork class

    # Artwork class constructor, takes in title, year of creation, and artist
    # Default value for title is "unknown", for year of creation is -1, and for artist is "Artist"
    def __init__(self, title="unknown", year_created=-1, artist="Artist"):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    # print_info function prints out the artist information, and then the artwork's title and year of creation
    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":  # if this file is run directly
    user_artist_name = input()  # get user input for artist name
    user_birth_year = int(input())  # get user input for birth year
    user_death_year = int(input())  # get user input for death year
    user_title = input()  # get user input for artwork title
    user_year_created = int(input())  # get user input for year of creation

    # create an artist object with the user input
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    # create an artwork object with the user input
    user_artwork = Artwork(user_title, user_year_created, user_artist)

    # print out the artwork information
    user_artwork.print_info()
