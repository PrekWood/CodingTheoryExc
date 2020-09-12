# Shannon Fano compression and decompression
def decompression(letters, compressed_word):
    # in the loop checks every time the first bits_to_uncode are same with the encryption of a letter
    decompressed = ""
    bits_to_uncode = 1
    # stops when the codded is empty
    while 0 != len(compressed_word):
        for y in range(0, len(letters)):
            if compressed_word[0:bits_to_uncode] == letters[y][1]:
                # appends the letter to the uncodded and deletes from the codded the bits_to_uncode
                decompressed += letters[y][0]
                compressed_word = compressed_word[bits_to_uncode:]
                bits_to_uncode = 0
                break
        bits_to_uncode += 1
    return decompressed


def compression(letters, decompressed_word):
    compressed_word = ""
    # search the precodded leters
    for i in decompressed_word:
        error = True
        # when the char is same with letter[y][0] appends chars encryption to codded_word
        for y in range(0, len(letters)):
            if i == letters[y][0]:
                compressed_word += letters[y][1]
                error = False
                break
        if error:
            return "error"
    return compressed_word


def shannon_fano(letters, index, start, max, dictionary):
    # dictionary is a list with the letter[i]=dictionary[i](codded letter)
    # letters the list with [letter,posibility], index the point,
    # start the spot to begin,the end for the codded

    # if they are only tow elements to be codded
    if start == max - 2:
        dictionary[start + index] = dictionary[start + index] + "0"
        dictionary[start + index + 1] = dictionary[start + index + 1] + "1"
        return

    # count all the elements right from index
    sum_right = 0
    for y in range(max - 1, index + start, -1):
        sum_right += letters[y][1]

    # count all the elements left from index
    sum_left = 0
    for y in range(start, start + index + 1):
        sum_left += letters[y][1]

    encryption = False
    # if the sum_right is bigger than sum_left
    first_different = sum_right - sum_left
    if first_different >= 0:
        # checks if the index was index+1 , will be better the difference?
        # if yes call the faction with index+1
        # if no put the 0 and 1
        sum_right = sum_right - letters[index + start + 1][1]
        sum_left = sum_left + letters[index + start + 1][1]
        better_difference = sum_right - sum_left
        if abs(better_difference) < first_different:
            shannon_fano(letters, index + 1, start, max, dictionary)
        else:
            encryption = True
    else:
        encryption = True
    # When finds the spot that the possibilities are close
    # if you find the spot
    if encryption:
        # add to dictionary '0' until the index
        for y in range(start, index + start + 1):
            dictionary[y] = dictionary[y] + "0"

        # and '1' index to end of list
        for y in range(index + start + 1, max):
            dictionary[y] = dictionary[y] + "1"

        # if the left has above of two elements must codded again
        if index > 0:
            shannon_fano(letters, 0, start, index + start + 1, dictionary)

        # check if the list is codded already
        if index + start + 1 < max - 1:
            shannon_fano(letters, 0, start + index + 1, max, dictionary)

    return dictionary


# I count all the letters from the variable a
def count_letters(a):
    letters = []
    for i in a:
        exist = False
        for y in range(0, len(letters)):
            if i == letters[y][0]:
                letters[y][1] += 1
                exist = True
                break
        if not exist:
            letters.append([i, 1])
    return letters
