import subprocess
import ftplib  # I'd rather use ftputil, since it's a nice wrapper for ftplib, but it might make things slower?
import Modules.file_parse.fileparse


# The IP of the server we're downloading/uploading things to/from
ftp_addr = '192.168.1.1'

# The names of the files were dealing with
download = 'team1.txt'
upload = open('upload_package.txt', 'r')
creds_file = open('credentials.txt', 'wb')

# Where we want to put the file
upload_name = 'CNU/IMPRINT_upload_package.txt'
team_dir = 'auvsi/team1/'

# Loop forever!
while True:

#	# Verify connection
#	# Does ftplib automatically check connections?  If so we should remove this whole block and set ftplib's timeout to like, 1s
#	output == subprocess.check_output(['ping', '-n', '1', server]) # Need to fix this command to work on linux....
#	if output = 'tmp string for network down':
#		continue

	# We don't need to verify that we have a valid connection, because ftplib will do that for us.
	try:
		ftp = ftplib.FTP(ftp_addr, timeout = 1)
		# Set up the FTP object
		ftp.set_debuglevel(2)

	except ftplib.all_errors, e:
		print "FTP ERROR:", e
		continue
	
	# Connect to the FTP object and Login anonymously
	ftp = FTP(ftp_addr)
	ftp.login()
	
	# Change directory if needed
	if team_dir:
		ftp.cwd(team_dir)
	
	# Need to do more testing with this line, we might be able to just use storelines or retrlines...
#	ftp.retrbinary('RETR', creds_file.write)
	ftp.retrlines("RETR " + download, lambda s, w = creds_file.write: w(s + "\n"))
	
	# Parse it mytext reads all lines of the file contents
	text = creds_file.readlines()
		
	up_user = fileparse.obt_login(text)
	up_pass = fileparse.obt_pass(text)
	up_mess = fileparse.obt_message(text)
	
	# Login with the new creds and put the file
	ftp.login(up_user, up_pass)
	ftp.storelines('STOR', upload_name, upload)
	
	# End this script to save resources for other things
	ftp.quit()
	cred_file.close()
	upload.close()
	break
	
# Not currently connected... Time to try again
