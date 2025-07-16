Here’s a cleaned-up version of your README for the **Huffman File Compression and Decompression** project, with unwanted symbols removed and formatting polished:

---

# Huffman File Compression

A Python implementation of the Huffman coding algorithm for file compression and decompression. This project demonstrates **lossless data compression** using variable-length encoding based on character frequency.

---

## 🎯 Features

* **Lossless Compression**: Perfect reconstruction of original files
* **Variable-Length Encoding**: More frequent characters get shorter codes
* **Efficient Implementation**: Uses binary heaps for optimal performance
* **Cross-Platform**: Works on Windows, macOS, and Linux
* **Easy to Use**: Simple command-line interface

---

## 📊 Compression Results

* **Compression Ratio**: \~44% reduction in file size
* **Example**: 1,765 bytes → 983 bytes (55.7% of original size)
* **Perfect Reconstruction**: No data loss during compression/decompression

---

## 🚀 Quick Start

### Prerequisites

* Python 3.6 or higher
* No external dependencies (uses only the standard library)

### Installation & Usage

1. **Clone the repository**

```bash
git clone https://github.com/snigdha6106/Huffmann_File_Compression_and_Decompression.git
cd Huffmann_File_Compression_and_Decompression
```

2. **Run compression**

```bash
python huffmann.py
```

3. **Run decompression**

```bash
python decompress.py
```

4. **View Huffman codes**

```bash
python view_huff.py
```

---

## 📁 Project Structure

```
Huffmann_File_Compression_and_Decompression/
├── huffmann.py                # Main compression algorithm
├── decompress.py              # Decompression algorithm
├── view_huff.py               # Huffman codes viewer
├── ebook_sample.txt           # Sample text file for testing
├── ebook_compressed.huff      # Compressed output file
├── ebook_compressed.huff.meta # Metadata with codes
├── ebook_decompressed.txt     # Decompressed output
└── README.md                  # This file
```

---

## 🔧 How It Works

### Compression

1. **Frequency Analysis**: Count occurrences of characters
2. **Tree Construction**: Build binary Huffman tree using a min-heap
3. **Code Generation**: Assign binary codes
4. **Encoding**: Convert text to binary
5. **Packing**: Store binary data and metadata

### Decompression

1. **Load Metadata**: Read `.meta` file
2. **Extract Binary**: Convert bytes to binary string
3. **Remove Padding**: Trim extra bits
4. **Decode**: Reconstruct original text

---

## 📝 Usage Examples

### Compress a File

```python
from huffmann import HuffmanCoding

h = HuffmanCoding()
h.compress("input.txt", "output.huff")
```

### Decompress a File

```python
from decompress import HuffmanDecompressor

d = HuffmanDecompressor()
d.decompress("output.huff", "decompressed.txt")
```

### View Huffman Codes

```python
from view_huff import view_codes

view_codes("output.huff.meta")
```

---

## 🧮 Algorithm Details

### Huffman Tree Example

```text
Character Frequency: {'e': 45, 't': 30, 'a': 25, 'o': 20}
Huffman Codes: {'e': '0', 't': '10', 'a': '110', 'o': '111'}
```

* Most frequent characters get shortest codes
* Optimal prefix codes: No code is prefix of another

---

## 📈 Performance Analysis

| File Type                | Original Size | Compressed Size | Compression Ratio |
| ------------------------ | ------------- | --------------- | ----------------- |
| Text (Pride & Prejudice) | 1,765 bytes   | 983 bytes       | 44.3%             |
| Metadata                 | 1,247 bytes   | -               | -                 |

* **Compression**: O(n log n)
* **Decompression**: O(m)

---

## 🔍 File Formats

* **.huff**: Binary-encoded compressed file
* **.meta**: Pickle file mapping characters to Huffman codes

---

## 🛠️ Customization

You can change file names directly in the Python scripts:

```python
# In huffmann.py
h.compress("your_input.txt", "your_output.huff")

# In decompress.py
d.decompress("your_output.huff", "your_decompressed.txt")
```

---

## 🧪 Testing

```bash
# Compress and decompress
python huffmann.py
python decompress.py

# Compare original and decompressed files
diff ebook_sample.txt ebook_decompressed.txt
```

---

## 📚 Technical Background

* **Static Huffman Coding**: Based on pre-known character frequencies
* **Used in**: ZIP, JPEG, PNG, etc.
* **Entropy-based encoding**: Approaches theoretical compression limits

---

## 🤝 Contributing

1. Fork the repo
2. Create your branch: `git checkout -b feature/YourFeature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

---

## 🙏 Acknowledgments

* David Huffman (1952 Algorithm)
* Python Standard Library
* Jane Austen ("Pride and Prejudice" sample text)

---

Let me know if you’d like this saved as a new `README.md` file or zipped along with the code.
