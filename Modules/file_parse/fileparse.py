
import sys

#methods for obtaining credentials from a sample file.
#The paramemter passed is the file itself once opened.
#these methods are based on the sample of how the credentials will be sent remotely.

def obt_login(text):
	first_line = text[0]
	line_list = first_line.split(',')
#indentation can cause an error
	return line_list[0].replace(" ", "")

def obt_pass(text):
        first_line = text[0]
        line_list = first_line.split(',')
        return line_list[1].replace(" ", "")
	
def obt_message(text):
        mess_line = text[1]
	return mess_line




