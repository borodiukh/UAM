def encodeLZ78(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE, 'r') as input_file, open(OUTPUT_FILE, 'w') as encoded_file:
        text_from_input_file = input_file.read()
        # print(text_from_input_file)
        dictionary_of_codes = dict()

        entry = ''
        index = 1

        # start algorithm
        for char in text_from_input_file:
            entry += char

            if entry not in dictionary_of_codes:
                dictionary_of_codes[entry] = str(index)
                print(f'add {entry} to the dictionary with index {index}')

                if len(entry) == 1:
                    encoded_file.write('0' + entry)
                    print(f'write into output file 0(zero) and entry {entry}')
                    print()
                else:
                    # write index of entry without last character from dictionary
                    index_of_entry_from_dictionary = dictionary_of_codes[entry[:-1]]
                    encoded_file.write(str(index_of_entry_from_dictionary) + entry[-1])
                    print(f'write into output file {index_of_entry_from_dictionary}(index of entry {entry[:-1]}) and entry {entry[-1]}')
                    print()

                index += 1
                entry = ''

    # print(dictionary_of_codes)
    return True


def decodeLZ78(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE, 'r') as input_file, open(OUTPUT_FILE, 'w') as output_file:
        text_from_input_file = input_file.read()
        dictionary_of_codes = dict()
        dictionary_of_codes['0'] = ''
        # print(text_from_input_file)

        entry = ''
        index = 1

        print(f'at the beginning dictionary have only one element entry ""(nothing) with index 0(zero)')
        print()

        for char in text_from_input_file:
            if char in '1234567890':
                entry += char
            else:
                # entry here is a number, char is letter
                print(f'entry before decoding {entry + char}')

                dictionary_of_codes[str(index)] = dictionary_of_codes[entry] + char
                print(f'add to the dictionary entry {dictionary_of_codes[entry] + char}(because {entry} is a index of entry {dictionary_of_codes[entry]}) with index {index}')
                #print(dictionary_of_codes)
                output_file.write(dictionary_of_codes[entry] + char)
                print(f'write into output file entry {dictionary_of_codes[entry] + char}')
                print()
                entry = ''
                index += 1
    return True



encodeLZ78('input_file', 'encoded_file.txt')
decodeLZ78('encoded_file.txt', 'decoded_file.txt')