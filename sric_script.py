import subprocess
import ftplib  # I'd rather use ftputil, since it's a nice wrapper for ftplib, but it might make things slower?
from ftplib import FTP
import Modules.file_parse.fileparse


# The IP of the server we're downloading/uploading things to/from
ftp_adr = '10.48.22.113'

# The names of the files were dealing with
download = 'cnu.txt'
upload = open('upload_package.txt', 'r')
creds_file = open('credentials.txt', 'wb')

# Where we want to put the file
upload_name = 'CNU-IMPRINT_upload_package.txt'
#team_dir = 'auvsi/team1/'

# Loop forever!
while True:

	# Verify connection before attempting to create FTP instance so we don't have to wait for 30 second timeout
	# Does ftplib automatically check connections?  If so we should remove this whole block and set ftplib's timeout to like, 1s
	output = subprocess.check_output(['ping', '-w2', ftp_addr])
	if output == 'tmp string for network down':
		continue

	try:
		ftp = ftplib.FTP(ftp_addr, timeout = 30)
		# Set up the FTP object
		ftp.set_debuglevel(2)

	except ftplib.all_errors, e:
		print "FTP ERROR:", e
		continue
	
	# Connect to the FTP object and Login anonymously
	ftp = FTP(ftp_addr)
	ftp.login()
	
	# Change directory if needed
	if 'team_dir' in locals():
		ftp.cwd(team_dir)
	
	# Need to do more testing with this line, we might be able to just use storelines or retrlines...
	ftp.retrlines('RETR ' + download, creds_file.write)
#	ftp.retrlines('RETR ' + download, lambda s, w = creds_file.write: w(s + '\n'))
	
	# Parse it mytext reads all lines of the file contents
	text = creds_file.readlines()
	
	# Login with the new creds and put the file
	ftp.quit()
	ftp = FTP(ftp_addr, obt_login(text), obt_pass(text), timeout = 30)
	ftp.storlines('STOR ', upload_name, upload)
	
	# End this script to save resources for other things
	ftp.quit()
	cred_file.close()
	upload.close()
	break
	
# Not currently connected... Time to try again
