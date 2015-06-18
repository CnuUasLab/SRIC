import sys
import subprocess
import ftplib  # I'd rather use ftputil, since it's a nice wrapper for ftplib, but it might make things slower?
#from ftplib import FTP

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

# The IP of the server we're downloading/uploading things to/from
ftp_addr = '192.168.2.2'

# The names of the files were dealing with
download = 'auth.txt'
#upload = open('upload_package.txt', 'r')
filer= open('/usr/bin/upload_package.jpg', 'rb')
creds_file = open('credentials', 'wb')

# Where we want to put the file
upload_name = 'CNU-IMPRINT_upload_package.txt'
#team_dir = 'auvsi/team1/'

# Loop forever!
while True:

	# Verify connection before attempting to create FTP instance so we don't have to wait for 30 second timeout
	
    try:
        print "submodule"
        # output = subprocess.check_output(['ping', '-w2', ftp_addr])
    except subprocess.CalledProcessError as e:
        print "host not found"
        continue


    
    try:
	    ftp = ftplib.FTP(ftp_addr, timeout = 30)
	    # Set up the FTP object
	    ftp.set_debuglevel(2)

    except ftplib.all_errors, e:
	    print "FTP ERROR:", e
	    continue
	
	# Connect to the FTP object and Login anonymously
	# ftp = FTP(ftp_addr)
    ftp.login()
	
	# Change directory if needed
    if 'team_dir' in locals():
		ftp.cwd(team_dir)
	
	# Need to do more testing with this line, we might be able to just use storelines or retrlines...
    ftp.retrbinary('RETR ' + download, creds_file.write)
#	ftp.retrlines('RETR ' + download, lambda s, w = creds_file.write: w(s + '\n'))
    
    creds_file.close()
    creds_file = open('credentials', 'rb')
	
    # Parse it mytext reads all lines of the file contents
    text = creds_file.readlines()
	
    # Login with the new creds and put the file
    ftp.quit()

    uname = '' + str(obt_login(text)).replace('\n', '')
    pword = '' + str(obt_pass(text)).replace('\n', '')

    ftp2 = ftplib.FTP(ftp_addr, uname, pword)
    # ftp2 = ftplib.FTP(ftp_addr, fp.obt_login(text), fp.obt_pass(text))
#   ftp.storlines('STOR', upload_name, upload.write)
#   ftp.storbinary('RETR %s' % 'upload_package', upload.write)

    print 'Login successful!'

    ftp2.storlines('STOR ' + 'CNU-IMPRINT_upload_package.jpg', filer)

    # End this script to save resources for other things
    ftp2.quit()
    creds_file.close()
    # upload.close()
    break
	
# Not currently connected... Time to try again
