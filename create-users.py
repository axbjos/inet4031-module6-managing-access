#!/usr/bin/python3

# INET4031
# Your Name
# Data Created
# Date Last Modified

#REPLACE THIS COMMENT - identify what each of these imports is for.
import os
import re
import sys

#REMOVE THIS COMMENT WHEN DONE WITH THE ASSIGNMENT
#Make sure you add comments throughout the code
def main():
    for line in sys.stdin:

        #REPLACE THIS COMMENT - this "regular expression" is searching for the presence of a character - what is it and why?
        match = re.match("^#",line)

        #REPLACE THIS COMMENT - what is this field doing?
        fields = line.strip().split(':')

        #REPLACE THESE COMMENTS with a single comment describing the logic of the IF 
        #what would an appropriate comment be for describing what this IF statement is checking for?
        #what happens if the IF statement evaluates to true?
        #how does this IF statement rely on what happened in the prior two lines of code? The match and fields lines.
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        
        #print cmd
        #os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        #os.system(cmd)

        for group in groups:
            #what is this if statement looking for?
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
