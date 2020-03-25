"""Huffman Coding
CPE202

Author:
    Parth Ray
"""
from huffman import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters in file
    Args:
        filename (file): text file
    Returns:
        list: list of size 256 integers with the frequencies of characters in file
    """
    list_of_freqs = [0] * 256
    text_file = open(filename, "r")
    text = text_file.readline()
    text_file.close()
    for i in text:
        list_of_freqs[ord(i)] += 1
    return list_of_freqs


def create_huff_tree(list_of_freqs):
    """creates the root node of a Huffman Tree using a list of freqencies
    Args:
        list_of_freqs (list): list of size 256 integers with the frequencies of characters in file
    Returns:
        HuffmanNode: the root of Huffman Tree
    """
    heap_arr = []
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            heap_arr.append(HuffmanNode(list_of_freqs[i], chr(i)))
    min_heap = MinPQ(heap_arr)
    while min_heap.num_items > 1:
        huff_node1 = min_heap.del_min()
        huff_node2 = min_heap.del_min()
        new_huff_node = HuffmanNode(huff_node1.freq + huff_node2.freq,
                                    min(huff_node1.char, huff_node2.char))
        new_huff_node.left, new_huff_node.right = huff_node1, huff_node2
        min_heap.insert(new_huff_node)
    return min_heap.arr[0]

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    Args:
        root_node (HuffmanNode): root of HuffmanTree
    Returns:
        list: an array of size 256 whose index corresponds to ascii code of a letter
    """
    code_list = [None] * 256
    return create_code_helper(root_node, code_list, "")

def create_code_helper(root_node, code_list, code):
    """helper function to traverse the Huffman Tree and assign code
    Args:
        root_node (HuffmanNode): root of HuffmanTree
        code_list (list): an array of size 256 whose index corresponds to ascii code of a letter
        code (str): Huffman code for a specific letter
    Returns:
        list: an array of size 256 whose index corresponds to ascii code of a letter
    """
    if root_node is None:
        return None
    if root_node.left is None and root_node.right is None:
        code_list[ord(root_node.char)] = code
    create_code_helper(root_node.left, code_list, code + "0")
    create_code_helper(root_node.right, code_list, code + "1")
    return code_list


def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    Args:
        in_file (file): file with text
        out_file (file): file to write encoded text
    """
    code_list = create_code(create_huff_tree(cnt_freq(in_file)))
    in_text_file = open(in_file, "r")
    in_text = in_text_file.readline()
    in_text_file.close()
    out_text_file = open(out_file, "w")
    encode = ""
    for i in in_text:
        encode += code_list[ord(i)]
    out_text_file.write(encode)
    out_text_file.close()

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    Args:
        list_of_freqs (list): list of size 256 integers with the frequencies of characters in file
        encoded_file (file): file with encoded text
        decode_file (file): file to write decoded text in
    """
    root_node = create_huff_tree(list_of_freqs)
    encoded_file = open(encoded_file, "r")
    decode_file = open(decode_file, "w")
    encoded_code = encoded_file.readline()
    pointer = 0
    while pointer < len(encoded_code):
        char, pointer = find_char(root_node, encoded_code, pointer)
        decode_file.write(char)
    encoded_file.close()
    decode_file.close()

def find_char(root_node, encoded_code, pointer):
    """finds character associated with huffman code
    Args:
        root_node (HuffmanNode): the root of HuffmanTree
        encoded_code (str): encoded string
        pointer (int): pointer to where to start reading code
    Returns:
        str : character associated with the code
        int : where the last character was found in the code 
    """
    if root_node.left is None and root_node.right is None:
        return root_node.char, pointer
    if encoded_code[pointer] == "0":
        return find_char(root_node.left, encoded_code, pointer + 1)
    if encoded_code[pointer] == "1":
        return find_char(root_node.right, encoded_code, pointer + 1)
