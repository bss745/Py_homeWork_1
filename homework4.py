#1

string = input('Enter a string: ')

letter_count = 0

digit_count = 0

for i in string:
   if i.isalpha():
       letter_count += 1

   elif i.isdigit():
       digit_count += 1

print('Number of letters:', letter_count)
print('Number of digits:', digit_count)

#2
text2 = input("Enter some text: ")
some_found_index = 0
print(text2.find("m", some_found_index + 1)) 

#3
text3 = "hello, world!"
result = text3.replace("hello", "goodbye", 1)
print(result)

#4
sentence = "hello, world!"
print(sentence[2])
print(sentence[-2])
print(sentence[0:5])
print(sentence[:-2])
print(sentence[::2])
print(sentence[1::2])
print(sentence[::-1])
print(sentence[::-2])
print(len(sentence))

# add
print(sentence.capitalize())

digit_count2 = 0

for i in sentence:
	if i.isdigit():
		digit_count2 += 1

print('Number of digits:', digit_count)

first_found_index = sentence.find(",")
print(sentence.find(",", first_found_index + 1)) 
    

second_found_index = sentence.find("!")
print(sentence.find("!", second_found_index + 1)) 