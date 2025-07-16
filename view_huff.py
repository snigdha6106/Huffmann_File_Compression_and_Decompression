import pickle

def view_codes(meta_file):
    with open(meta_file, 'rb') as file:
        codes = pickle.load(file)
    
    print("\n Huffman Codes:")
    for char, code in codes.items():
        printable = repr(char)
        print(f"{printable} : {code}")

if __name__ == "__main__":
    view_codes("ebook_compressed.huff.meta")