# put your code here.
def frequency_of_words(filename):
    """Takes a file and creates a dictionary to count
        frequency of words in file. 
        Prints each word and frequency."""
    file_of_text = open(filename)
    word_count_dict = {}

    # Loops through each line in file and splits for each word
    for line in file_of_text:
        line = line.rstrip("\n")
        line = line.split(" ")

        # Loops through each word in line and adds to dictionary
        # or increases word count
        for word in line:
            if word not in word_count_dict:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    # Prints each word and count
    for word in word_count_dict:
        print word, word_count_dict[word]

    # print "\n \n"


frequency_of_words('test.txt')
# frequency_of_words('twain.txt')