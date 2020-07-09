# 9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the 
# dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
    # Checks if the line starts with 'From' or not
    if line.startswith("From "):
        # Removing enter from the end of the line
        line = line.rstrip()
        
        # Spliting the line and creating a list with the words of the line
        sp = line.split()
        
        # Counting the maximum times and creating a dictionary
        for word in sp:
            if word == sp[1]:
                dic[word] = dic.get(word, 0) + 1



# Finding which word is maximum and print the word with count

bigcount = None
bigword = None


for word,count in dic.items():
    # Checks, if each word is empty OR count is greater 
    if bigword is None or count>bigcount:
        bigword = word
        bigcount= count

        
print(bigword, bigcount)
    
    