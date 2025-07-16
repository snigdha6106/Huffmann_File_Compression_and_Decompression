import pickle

class HuffmanDecompressor:
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    
    def decompress(self, input_file, output_file):
        with open(input_file, 'rb') as file:
            bit_string = ""
            byte = file.read(1)
            while byte:
                bits = bin(ord(byte))[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
        
        with open(input_file + ".meta", 'rb') as meta:
            codes = pickle.load(meta)
        
        reverse_mapping = {v: k for k, v in codes.items()}
        actual_text = self.remove_padding(bit_string)
        current_code = ""
        decoded_text = ""
        
        for bit in actual_text:
            current_code += bit
            if current_code in reverse_mapping:
                decoded_text += reverse_mapping[current_code]
                current_code = ""
        
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(decoded_text)
        
        print("\n✅ Decompression Complete")

if __name__ == "__main__":
    d = HuffmanDecompressor()
    d.decompress("ebook_compressed.huff", "ebook_decompressed.txt")