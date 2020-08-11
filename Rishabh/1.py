""" 
  Input(str) : "this is the random string of python code"
  OutPut(str : "this is   the
`               random string 
                of python code"
"""

def transform_string(x, max_width):
    start = 0
    result = ""
    count = 0
    for word in x:
        count = count + 1
        current_index = start + len(word)
        start = start + len(word) + 1
        if current_index <= max_width:
            result = result + word + " "
        if current_index > max_width:
            if current_index > max_width + 1:
                diff = max_width - ((current_index) - (len(word) + 1))        
                pad_word = x[count-2]
                pad = (" " * diff) + pad_word
                result = result[:(len(result) - (len(pad_word) + 2) )] + pad
            result = result + '\n'
            start = len(word)
            result = result + word + " "
    print (result)

sentence = "this is the random string of python code" ##input("Enter string to convert")
x = sentence.split()
max_width = 14
transform_string(x, max_width)
