import heapq
import os
import pickle
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}
    
    def make_frequency_dict(self, text):
        freq = defaultdict(int)
        for char in text:
            freq[char] += 1
        return freq
    
    def build_heap(self, frequency):
        heap = []
        for char, freq in frequency.items():
            heapq.heappush(heap, Node(char, freq))
        return heap
    
    def merge_nodes(self, heap):
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)
        return heap
    
    def make_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")
    
    def make_codes(self, heap):
        root = heapq.heappop(heap)
        self.make_codes_helper(root, "")
    
    def get_encoded_text(self, text):
        return ''.join([self.codes[char] for char in text])
    
    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * extra_padding
        padded_info = "{0:08b}".format(extra_padding)
        return padded_info + encoded_text
    
    def compress(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        frequency = self.make_frequency_dict(text)
        heap = self.build_heap(frequency)
        heap = self.merge_nodes(heap)
        self.make_codes(heap)
        
        encoded_text = self.get_encoded_text(text)
        padded_encoded_text = self.pad_encoded_text(encoded_text)
        
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        
        with open(output_file, 'wb') as out:
            out.write(bytes(b))
        
        with open(output_file + ".meta", 'wb') as meta:
            pickle.dump(self.codes, meta)
        
        print("\n✅ Compression Complete")
        print(f"Original Size: {os.path.getsize(input_file)} bytes")
        print(f"Compressed Size: {os.path.getsize(output_file)} bytes")

if __name__ == "__main__":
    h = HuffmanCoding()
    h.compress("ebook_sample.txt", "ebook_compressed.huff")