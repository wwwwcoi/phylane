from PIL import Image

def image_to_bits(image_path):
    """Converts an image to a string of bits representing its raw pixel data."""
 
    try:
        
        img = Image.open(image_path)
        img = img.convert("RGB")  # Convert to RGB for simplicity
        width, height = img.size
        bits = ""
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                bits += format(r, '08b')  # 8 bits for Red
                bits += format(g, '08b')  # 8 bits for Green
                bits += format(b, '08b')  # 8 bits for Blue
        return bits
    except FileNotFoundError:
        return f"Error: File not found at {image_path}"
    except Exception as e:
        return f"Error processing image: {e}"

if __name__ == "__main__":
    image_file = "red.png"  # Replace with the path to your image
    bit_representation = image_to_bits(image_file)
    flag=[]
    if isinstance(bit_representation, str) and bit_representation.startswith("Error"):
        print(bit_representation)
    else:
        print(f"Bit representation of {image_file} (first 100 bits):")
        with open("bin.txt", "a") as f:
            for i in range (0,393216,8)  :  
                print(bit_representation[i:i+8]) # Print only the first 100 bits for brevity
                a= bit_representation[i:i+8]
                if a != "00000000" or a != "11111111":
                    flag.append(a[-1])
                    f.write(a[-1])
        #for i in flag[::8]:
            

        print("Flag: ",flag)
        print(f"Total number of bits: {len(bit_representation)}")

# To get the encoded binary data of the entire file:
def image_to_raw_binary(image_path):
    """Reads the entire image file as raw binary data."""
    try:
        with open(image_path, 'rb') as f:
            binary_data = f.read()
        return binary_data
    except FileNotFoundError:
        return f"Error: File not found at {image_path}"
    except Exception as e:
        return f"Error reading image: {e}"

if __name__ == "__main__":
    image_file_raw = "red.png" # Replace with the path to your image
    raw_binary = image_to_raw_binary(image_file_raw)
    if isinstance(raw_binary, str) and raw_binary.startswith("Error"):
        print(raw_binary)
    else:
        print(f"\nRaw binary data of {image_file_raw} (first 20 bytes):")
        print(raw_binary[:20])
        print(f"Total number of bytes: {len(raw_binary)}")