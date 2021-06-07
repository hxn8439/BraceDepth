# Hamilton Nguyen
# 1000538439
# 04/23/2021
# Python 3.9.1 --OS: Microsoft Windows

#open input file
file = open("input.txt","r")

#variables used for error checking, ignore braces in comments and brace counters.
counter = 0
ignore_char = False
error_trip1 = 0
error_trip2 = 0

#for loop when reading line in file
for line in file.readlines():

	#tokens for variable "hit" and "spaceinput"
	hit = line.strip()
	space_input = ""

	#for loop for handling token "hit"
	for char in hit:

		# if, elseif, else statements for detecting characters and handling them accordingly.
		if char == "\"" or char == "\'" or char == "/" :
			ignore_char = True

		elif  ignore_char == False and char == "{" :
			counter += 1
			space_input = str(counter)+' ' +line
			error_trip1 += 1
		
		elif ignore_char == False and char == "}" :
			space_input = str(counter)+' ' +line
			counter -= 1
			error_trip2 += 1

		else:
			space_input = str(counter)+' ' +line

	#reset boolean to false for boolean variable.
	ignore_char = False

	#print statement to output the whole data.
	print(space_input,end='')	

#Error handling when unbalanced braces found.
if error_trip1 != error_trip2 and counter !=0:
	print("\n ERROR FOUND IN CODE: expected ‘}’ but found EOF. Unbalance Braces Found. \n")
	
