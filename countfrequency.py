def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print(key, value)

    # Driver function


if __name__ == "__main__":
    mylist = ["one", "two", "eleven", "one", "three", "two", "eleven", "three", "seven", "eleven"]

    print(CountFrequency(mylist))


