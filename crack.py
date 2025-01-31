import hashlib   #list of hashes of words to probable passwords

flag = 0  #Use flag to keep track of how many passwords that were found
counter = 0   #Keep track of how many passwords we are going through

#Take in the md5 hash
pass_hash = input("Enter md5 hash: ")

#Input filename with probable passwords
wordlist = input("File name: ")

try:
	pass_file = open(wordlist, "r")  #Give the file read permission

except:
	#If file not found
	print("No file found")
	quit()

for word in pass_file:
	
	#Compare the hashes. Convert a word to an encoded format. Create a hash digest
	enc_wrd = word.encode('utf-8') 
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	print(word)
	print(digest)
	print(pass_hash)
	counter += 1

	#Compare the hash digest to the hashes in the file
	if digest == pass_hash:   
		print("Password found")
		print("password is " + word)
		flag = 1
		break  #Break the loop once the password if found

#If the password is not in the file
if flag == 0:
	print("password/passphrase is not in the list")