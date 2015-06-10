import subprocess
from ftplib import FTP  # I'd rather use ftputil, since it's a nice wrapper for ftplib, but it might make things slower?
from Modules.file_parse.__file_parse__ import obt_login
from Modules.file_parse.__file_parse__ import obt_pass
from Modules.file_parse.__file_parse__ import obt_message 

# The IP of the server we're downloading/uploading things to/from
ftp_addr = 192.168.1.1

# The names of the files were dealing with
creds_file = open('credentials.txt', 'wb')
upload = open('upload_package.txt', 'r')

# Where we want to put the file
upload_name = 'tmp-dicks'

# Set up the FTP object
FTP.set_debuglevel(2)

# Loop forever!
while True:

#	# Verify connection
#	# Does ftplib automatically check connections?  If so we should remove this whole block and set ftplib's timeout to like, 1s
#	output = subprocess.check_output(['ping', '-n', '1', server]) # Need to fix this command to work on linux....
#	if output = 'tmp string for network down':
#		continue

	try:
		ftp = FTP(ftp_addr, timeout = 1)
	except ftplib.all_errors, e:
		print "FTP ERROR:", e
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
	
	# End this script to save resources for other things
	ftp.quit()
	cred_file.close()
	uplaod.close()
	break
	
# Not currently connected... Time to try again
