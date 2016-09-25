import crypt
import sys
def printme(str):
    length = len(str)
    with open(sys.argv[2], "r") as f:
        array = []
        for line in f:
            array.append(line)
            sLine = (line[0:length])
            if(sLine == str):
                print ("User Name found\n")
                return line
        f.close()
def dictAttack(originalPw, hashVal):
    with open("/home/seed/Documents/cosc440/john.txt", "r") as f:
        print("we are looking for a password with a hash value of " + originalPw + "\n")
        for line in f:
	    line = line.strip();	
	    hashedPw = crypt.crypt(line, hashVal)
	    hashedPw = hashedPw.split("$")[3]
            #print(line + " is now " + hashedPw)	
            if(hashedPw == originalPw):
                print ("Password Found \n")
                return line      
        f.close()

def main():
	if (len(sys.argv) < 3):
		print("You have not entered the correct number of arguments \n")
		exit()
	userName = sys.argv[1]
	shadowLine = printme(userName)
	if(shadowLine is None):
		print("User name not found in shadow file \n")
		exit() 
	sep = shadowLine.split("$")
	if(len(sep) == 1):
		print("User name does not have a password")
		exit()	
	hashVal = "$"+sep[1]+ "$" + sep[2]
	hashPw = sep[3]
	hashPw = hashPw.split(":")[0]
	result = dictAttack(hashPw, hashVal)
	if(result is None):
		print("Password not found in dictionary")
		exit()
	print("password is " + result)	

main()

