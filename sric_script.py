import subprocess
from ftplib import FTP  # I'd rather use ftputil, since it's a nice wrapper for ftplib, but it might make things slower?
from Modules.file_parse.__file_parse__ import obt_login
from Modules.file_parse.__file_parse__ import obt_pass
from Modules.file_parse.__file_parse__ import obt_message 
# Could we replace this with:
# import Modules.file_parse
# ?

# The IP of the server we're downloading/uploading things to/from
server = 192.168.1.1
ftp_addr = server
# ftp_addr = 'ftp://' + server

# The names of the files were dealing with
creds_file = open('credentials.txt', 'wb')
upload = open('upload_package.txt', 'r')

# Where we want to put the file
upload_name = 'tmp-dicks'

# Download creds
down_user = 'tmp'
down_pass = 'tmp'

# Upload Creds
up_user = 'tmp'
up_pass = 'tmp'
up_mess = 'tmp'

# Set up the FTP object
FTP.set_debuglevel(2)

# Can we use this to remove the network connection test?
#ftp = FTP()
#ftp.connect(ftp_addr, timeout=1)

# Loop forever!
while True:

	# Verify connection
	# Does ftplib automatically check connections?  If so we should remove this whole block and set ftplib's timeout to like, 1s
	output = subprocess.check_output(['ping', '-n', '1', server]) # Need to fix this command to work on linux....
	if output = 'tmp string for network down':
		continue
	
	# connect to the FTP object and Login anonymously
	ftp = FTP(ftp_addr)
	ftp.login()
	
	# Change directory if needed
	#ftp.cwd()
	
	# Need to do more testing with this line, we might be able to just use storelines or retrlines...
	ftp.retrbinart('RETR ', creds_file.write)
	
	# Parse it mytext reads all lines of the file contents
	# up_usr and up_pass defined in file contents
	text = creds_file.readlines()
		
	up_user = obt_login(text)
	up_pass = obt_pass(text)
	up_mess = obt_message(text)
	
	# Login with the new creds and put the file
	ftp.login(up_user, up_pass)
	ftp.storelines('STOR', upload_name, upload)
	
	
	# Close files (After the put since we need to get that done as fast as possible)
	cred_file.close()
	uplaod.close()
	# End this script to save resources for other things
	break
	
# Not currently connected... Time to try again
