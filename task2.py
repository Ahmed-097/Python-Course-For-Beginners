# q1 :
Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
Hint: Dictionaries can be created either by using curly brackets or by using the dict  function.

MyDict={"a":1,"b":2}
# --------------------------------------------------------------------------------------------------

# q2 :
Please complete the script so that it prints out the value of key b .
d = {"a": 1, "b": 2}

z=d["b"]
print(z)

Expected output: 2

# ----------------------------------------------------------------------------------------------------

# q3 :
Calculate the sum of the values of keys a  and b .
d = {"a": 1, "b": 2, "c": 3}

d["a"]+d["b"]

Expected output: 3

# --------------------------------------------------------------------------------------------------

# q4 :
Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.
d = {"a": 1, "b": 2}

d["c"]=3

Expected output: {'a': 1, 'c': 3, 'b': 2} 

# --------------------------------------------------------------------------------------------------

# q5:
Complete the script so that it prints out the second item of the list.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

letters[1]

Expected output: b

# --------------------------------------------------------------------------------------------------

# q6 :
Complete the script so that it prints out letter i  using negative indexing.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

letters[-2]

Expected output: i 

# --------------------------------------------------------------------------------------------------

# q7:
Complete the script so that it prints out a list slice containing the last three items of list letters .
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

letters[-3:]

Expected output: ['h', 'i', 'j'] 

# --------------------------------------------------------------------------------------------------

# q8:
Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

x=[]
for index ,i in enumerate (letters):
    if index%2==0:
        x.append(i)
print(x)
        
Expected output: ['a', 'c', 'e', 'g', 'i'] 

# --------------------------------------------------------------------------------------------------
