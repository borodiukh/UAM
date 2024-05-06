from collections import Counter


def encodeLZW(data):
    dictionary = {}
    # 128 because ASCII last symbol has index 127
    index = 128

    # add all different entry into dictionary using ASCIiI
    tmp = Counter(data)
    for key in tmp.keys():
        # entry : number
        dictionary[key] = ord(key)

    result = []
    sequence = ''

    print(f'Dictionary at the beginning: {dictionary}')
    print()

    for char in data:
        sequence += char
        if sequence not in dictionary:
            dictionary[sequence] = index
            print(f'add entry {sequence} to dictionary with index {index}')
            index += 1
            result.append(dictionary[sequence[:-1]])
            print(f'add number {dictionary[sequence[:-1]]} to result because entry {sequence[:-1]} have this index')
            sequence = char
            print()

    # add last symbol
    # he is definitely in dictionary
    result.append(dictionary[sequence])
    print(f'add number {dictionary[sequence]} to result because entry {sequence} have this index')
    print()

    return result


def decodeLZW(data):
    dictionary = {}
    index = 128
    result = []
    sequence = ''

    # for number in array
    for code in data:
        # if code in ascii table(entry has lenght == 1)
        if code < 128:
            result.append(chr(code))
            print(f'add entry {chr(code)} to result because it has index {code} ')
            if sequence:
                dictionary[index] = sequence + chr(code)
                print(f'add entry {sequence + chr(code)} to dictionary with index {index}')
                index += 1
            sequence = chr(code)
            print()
        # if code > 128
        else:
            if code in dictionary:
                entry = dictionary[code]
            # special case
            elif code == index:
                entry = sequence + sequence[0]
            else:
                raise ValueError("Invalid LZW code")

            result.append(entry)
            print(f'add entry {entry} to result because it has index {code} ')

            dictionary[index] = sequence + entry[0]
            print(f'add entry {sequence + entry[0]} to dictionary with index {index}')
            print()
            index += 1
            sequence = entry

    return ''.join(result)


# data = "TOBEORNOTTOBEORTOBEORNOT"
data = "The United States of America, commonly known as the USA, is a diverse and vast country located in North America. It is renowned for its cultural, economic, and technological influence on a global scale."

compressed_data = encodeLZW(data)
print("Compressed data:".upper(), compressed_data)

print()
print()
print()

# compressed_data = [67, 108, 111, 115, 101, 32, 116, 104, 132, 71, 105, 116, 32, 66, 97, 115, 104, 32, 119, 105, 110, 100, 111, 119, 32, 97, 148, 32, 114, 101, 108, 97, 117, 110, 99, 144, 138, 133, 111, 152, 112, 112, 108, 121, 133, 135, 32, 162, 153, 103, 101, 115, 46]

decompressed_data = decodeLZW(compressed_data)
print("Decompressed data:".upper(), decompressed_data)
