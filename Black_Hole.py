def Black_Hole_compress(data):
    compressed_data = bytearray()
    count = 1
    current = data[0]

    for byte in data[1:]:
        if byte == current:
            count += 1
        else:
            compressed_data.append(current)
            compressed_data.append(count)
            current = byte
            count = 1

    compressed_data.append(current)
    compressed_data.append(count)
    return bytes(compressed_data)

def Black_Hole_decompress(data):
    decompressed_data = bytearray()

    for i in range(0, len(data), 2):
        byte = data[i]
        count = data[i + 1]

        decompressed_data.extend(byte for _ in range(count))

    return bytes(decompressed_data)

def generate_variations():
    variations = []
    for length in range(1, 33):
        for i in range(2**length):
            variations.append(bin(i)[2:].zfill(length))
    return variations

def Black_Hole_search(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        bits = ''.join(format(byte, '08b') for byte in data)  # Convert bytes to a single bit string
        for k in range(1, 33):  # Predict bit sequences up to length 32
            for i in range(len(bits) - k + 1):
                bit_sequence = bits[i:i+k]
                # Do something with the predicted bit sequence
                print("Predicted bit sequence of length", len(bit_sequence), ":", bit_sequence)
    print("Search complete.")

def compress_and_extract():
    file_name = input("Enter the name of the file: ")
    user_option = input("Do you want to compress or extract the file? (compress/extract): ")

    if user_option == "compress":
        output_file_name = input("Enter the name of the output file for compression: ")
        with open(file_name, 'rb') as file:
            input_data = file.read()
            compressed_data = Black_Hole_compress(input_data)
            with open(output_file_name, 'wb') as compressed_file:
                compressed_file.write(compressed_data)
        print("Compression complete. Compressed file saved as", output_file_name)

    elif user_option == "extract":
        output_extracted_name = input("Enter the name of the output file for extraction: ")
        with open(file_name, 'rb') as compressed_file:
            compressed_data = compressed_file.read()
            extracted_data = Black_Hole_decompress(compressed_data)
            with open(output_extracted_name, 'wb') as extracted_file:
                extracted_file.write(extracted_data)
        print("Extraction complete. Extracted file saved as", output_extracted_name)

    else:
        print("Invalid option. Please choose 'compress' or 'extract'.")

# Example usage:
compress_and_extract()
variations = generate_variations()