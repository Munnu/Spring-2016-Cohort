import random

def sort_restaurants(restaurants_and_ratings):
    """Sorts restaurants in dictionary and prints in alphabetical order"""

    # Sorts restaurants(keys) alphabetically
    sorted_restaurant_names = sorted(restaurants_and_ratings)
    return sorted_restaurant_names

def print_restaurants(sorted_restaurants, restaurants_and_ratings):
    # prints restaurants and ratings
    # print sorted_restaurants
    # print restaurants_and_ratings
    for restaurant in sorted_restaurants:
        print restaurant, "is rated at", restaurants_and_ratings[restaurant]



def restaurant_ratings_from_file(filename):
    """Pulls restaurants and ratings from file"""

    restaurant_file = open(filename)
    # Loop through each line in file, strip, split, and put into a dict
    for line in restaurant_file:
        line = line.rstrip("\n")
        line = line.split(":")
        # setting key, value for restaurant dict from line
        restaurants_and_ratings[line[0]] = int(line[1])


# Take user input for new restaurant and rating, adds to dictionary, sorts, prints
def new_restaurant(restaurants_ratings):
    """Takes user input for new restaurant/rating

         Adds to restaurants_and_ratings, calls sorted_restaurants and print_restaurants"""
    new_restaurant_name = ''
    new_restaurant_rating = ''
    while True:
        new_restaurant_name = raw_input("Please enter a restaurant name: ").capitalize()
        new_restaurant_rating = raw_input("Please enter a numerical rating: ")
        if new_restaurant_name == 'q' or new_restaurant_rating == 'q':
            break
        else:
            restaurants_ratings[new_restaurant_name] = int(new_restaurant_rating)

            sorted_restaurants = sort_restaurants(restaurants_and_ratings)
            print_restaurants(sorted_restaurants, restaurants_and_ratings)


def random_restaurant(restaurants_ratings):
    restaurant_name = list(restaurants_ratings)
    random_num = 0

    while True:
        random_num = random.randint(0, len(restaurant_name) - 1)
        random_restaurant = restaurant_name[random_num]

        print "\nRandom restaurant:", random_restaurant, restaurants_ratings[random_restaurant]
        new_rating = raw_input("\nPlease enter a new rating for this restaurant: ")

        print "Type 'q' if you would like to quit"
        
        if new_rating == 'q':
            break
        else:
            new_rating = int(new_rating)
            restaurants_ratings[random_restaurant] = new_rating
            print_restaurants(restaurant_name, restaurants_ratings)



# -------------------------------------------------------------------
# Initialize dictionary and variables
# -------------------------------------------------------------------
restaurants_and_ratings = {}

# Add restaurants from file to dictionary
restaurant_ratings_from_file('scores.txt')
user_name = raw_input("Hi, what is your name? ")

update_or_create_restaurant = int(raw_input("Press 1 to add a new restaurant listing?\n" +
                                        "Press 2 to update a random listing's rating? "))
if update_or_create_restaurant == 1:
  new_restaurant(restaurants_and_ratings)

elif update_or_create_restaurant == 2:
  random_restaurant(restaurants_and_ratings)
