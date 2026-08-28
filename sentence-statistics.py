import math

def calculate_average_word_length(sentence):
    words = sentence.split()
    lengths = []
    for word in words:
        letter_count = 0
        for char in word:
            if char.isalpha():
                letter_count += 1
        if letter_count > 0:
            lengths.append(letter_count)

    average = sum(lengths) / len(lengths)
    average = math.ceil(average)
    return average

def find_most_frequent_letter(sentence): 
    counts = {} 
    for char in sentence:
        if char.isalpha():
            if char not in counts:
                counts[char] = 0
            counts[char] += 1


    most_frequent = None
    highest = -1
    for char, count in counts.items():
        if count > highest:
            highest = count
            most_frequent = char
    return most_frequent



def print_sentence_report(sentence, most_frequent_letter, average_word_length):
    print('-------')
    print("Sentence Report: ", sentence)
    print("Most frequent letter: ", most_frequent_letter)
    print("Average word length: ", average_word_length)

def main():
    sentence = input("Enter your sentence: ")
    most_frequent_letter = find_most_frequent_letter(sentence)
    average_word_length = calculate_average_word_length(sentence)
    print_sentence_report(sentence, most_frequent_letter, average_word_length)
   



if __name__ == '__main__':
    # if you run python sentence-statistics.py, then this is true
    main()