# first of all import the socket library
# !/usr/bin sage -python
from scipy.stats import chi2_contingency
from Compression import count_letters, compression, shannon_fano
from socketConnection import send_data_to_client, receive_data_from_client
from Codification import circular_code, word_to_coded


# the number N from the user
n = receive_data_from_client()
print("n is : ", n)
G, H = circular_code(n[0], n[1])

file = open('input_message', 'r')
input = file.readline()
print(input)

# Count the letters for word 'a'
letters = count_letters(input)

# sorted with the possibility
letters.sort(key=lambda x: x[1], reverse=True)

# i find the possibility and make the dictionary
for i in letters:
    i[1] = i[1] / len(input)

dictionary = []
for i in range(0, len(letters)):
    dictionary.append("5")

dictionary = shannon_fano(letters, 0, 0, len(letters), dictionary)
for i in range(0, len(letters)):
    dictionary[i] = dictionary[i][1:]


# the letter list has the letter and the encryption
# ['a',011]
for i in range(len(letters)):
    letters[i][1] = dictionary[i]
compressed_word = compression(letters, input)

# make the word coded
codded_word = word_to_coded(G, compressed_word)

# save to the list a the data
a = [codded_word, letters]
length_message = len(input) * 8
length_codded_message = len(codded_word)
print("----------------------------------------------------------------------------------")
print("~Statistics~")
print("1. Length Message:                        ", length_message)
print("2. Length Codded message:                 ", length_codded_message)
print("3. Entropy Message:                       ", "Δεν θυμαμαι τον τυπο")
print("3. Entropy Codded Message:                ", "Δεν θυμαμαι τον τυπο")
print("4. chi square test for message:           ", 'chi2_contingency(input) παταει error δεν ξερω γιατι')
print("5. chi square test for the coded message: ", 'chi2_contingency(input) παταει error δεν ξερω γιατι')
print("6. Errors that there added to the message:", "Εδω εμφανιζει ποσο θορυβο μπηκε")

send_data_to_client(a)
