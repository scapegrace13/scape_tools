#/bin/python3
#
#	Author: scape
#	Use: find and count characters and length of entries in wordlists
#	I'm a programming noob, I just build the script that it works somehow
#	Maja <3 :)
#
#	example: 
#	python3 wordlist_counter.py /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-10000.txt 
#
#
import sys

if (len(sys.argv) == 1):
	print("You may want to use the filename as argument")
	filename = "testlist.txt"
elif (len(sys.argv) == 2):
	first_argument = sys.argv[1]
	filename = first_argument

lower_count = 0
upper_count = 0
special_count = 0

len_6 = 0
len_7 = 0
len_8 = 0
len_9 = 0
len_10 = 0
len_11 = 0
len_12 = 0
len_13 = 0
len_14 = 0

len_shorter = 0
len_longer = 0

special_characters = '"!#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ '
special_counter = 0
upper_counter = 0
lower_counter = 0
decimal_counter = 0
wordlist_counter = 0


with open(filename,encoding='ISO-8859-1') as file:
	while line := file.readline():
		wordlist_counter += 1
		#print(line.rstrip())
		if (len(line)<6): len_shorter +=1
		elif (len(line)==6): len_6 += 1
		elif (len(line)==7): len_7 += 1
		elif (len(line)==8): len_8 += 1
		elif (len(line)==9): len_9 += 1
		elif (len(line)==10): len_10 += 1
		elif (len(line)==11): len_11 += 1
		elif (len(line)==12): len_12 += 1
		elif (len(line)==13): len_13 += 1
		elif (len(line)==14): len_14 += 1
		elif (len(line)>14): len_longer += 1

#		if any(not c.isalnum() for c in line):
		if any(c in special_characters for c in line):
			special_counter += 1
		else:
			None	
		if any(c.isdecimal() for c in line):
			decimal_counter += 1
		else:
			None
		if any(c.isupper() for c in line):
			upper_counter += 1
		else:
			None
		if any(c.islower() for c in line):
			lower_counter += 1
		else:
			None


# DEBUG print line len OR print lien text
#		print(len(line))
#		print("Length <6: " + str(len_6))

print("")
print("Check the length of entries in the file - " + filename)
print("")
print("Length <6: " + str(len_shorter) + "\t" + str(round(len_shorter/wordlist_counter*100)) + "%" )
print("Length  6: " + str(len_6) + "\t" + str(round(len_6/wordlist_counter*100)) + "%" )
print("Length  7: " + str(len_7) + "\t" + str(round(len_7/wordlist_counter*100)) + "%" )
print("Length  8: " + str(len_8) + "\t" + str(round(len_8/wordlist_counter*100)) + "%" )
print("Length  9: " + str(len_9) + "\t" + str(round(len_9/wordlist_counter*100)) + "%" )
print("Length 10: " + str(len_10) + "\t" + str(round(len_10/wordlist_counter*100)) + "%" )
print("Length 11: " + str(len_11) + "\t" + str(round(len_11/wordlist_counter*100)) + "%" )
print("Length 12: " + str(len_12) + "\t" + str(round(len_12/wordlist_counter*100)) + "%" )
print("Length 13: " + str(len_13) + "\t" + str(round(len_13/wordlist_counter*100)) + "%" )
print("Length 14: " + str(len_14) + "\t" + str(round(len_14/wordlist_counter*100)) + "%" )
print("Length>14: " + str(len_longer) + "\t" + str(round(len_longer/wordlist_counter*100)) + "%" )
print("")
print("_____ _____ _____ _____ _____ _____ _____ _____ _____ _____")
print("")
print("Check for charset in each entry")
print("")
print("wordlist counter: " + str(wordlist_counter) )
print("")
print("special  counter: " + str(special_counter) + "\t" + str(round(special_counter/wordlist_counter*100)) + "%" )
print("upper \t counter: " + str(upper_counter) + "\t" + str(round(upper_counter/wordlist_counter*100)) + "%" )
print("lower \t counter: " + str(lower_counter) + "\t" + str(round(lower_counter/wordlist_counter*100)) + "%" )
print("decimal  counter: " + str(decimal_counter) + "\t" + str(round(decimal_counter/wordlist_counter*100)) + "%" )
print("")
print("")

