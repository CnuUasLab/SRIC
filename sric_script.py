import sys
import subprocess
import ftplib

# The IP of the server we're downloading/uploading things to/from
ftp_addr = '192.168.2.2'

# The names of the files were dealing with
download = 'auth.txt'
upload = open('upload_package.jpg', 'rb')
creds_file = open('credentials', 'wb')

# Where we want to put the file
upload_name = 'CNU-IMPRINT_upload_package.jpg'
#team_dir = 'auvsi/team1/'

# Look for mavproxy packet saying we're at the SRIC, identified via msg command

# Loop forever!
while True:

    # Attempt to connect
    try:
	    ftp = ftplib.FTP(ftp_addr, timeout = 30)
    except ftplib.all_errors, e:
	    print "FTP ERROR:", e
	    continue
	
	# Login anonymously
    ftp.login()
	
	# Change directory if needed
    if 'team_dir' in locals():
		ftp.cwd(team_dir)
	
    # Download the credentials file
    ftp.retrbinary('RETR ' + download, creds_file.write)
    
    # If read failed, attempt to read again X number of times

    creds_file.close()
    creds_file = open('credentials', 'rb')
	
    # Parse it mytext reads all lines of the file contents
    text = creds_file.readlines()
	
    # Login with the new creds and put the file
    ftp.quit()
    
    break

    uname = '' + str(obt_login(text)).replace('\n', '')
    pword = '' + str(obt_pass(text)).replace('\n', '')
    print 'Connecting with %r %r' % (uname, pword)

while true:
    try:
        ftp2 = ftplib.FTP(ftp_addr, uname, pword)
   except ftplib.all_errors, e:
	    print "FTP ERROR:", e
	    continue

    print 'Login successful!'

    ftp2.storlines('STOR ' + upload_name, upload)
#    ftp.storlines('STOR', upload_name, upload.write)
#    ftp.storbinary('RETR %s' % 'upload_package', upload.write) 
#    ftp2.storlines('STOR ' + 'CNU-IMPRINT_upload_package.jpg', upload)

    # If write failed, attempt to write again X number of times

    # Tell mavproxy to finish loiter unlimited

    ftp2.quit()
    break
	
# End this script to save resources for other things
creds_file.close()
upload.close()


# Define functions...  Should be moved to within the script..

def obt_login(text):
    first_line = text[0]
    line_list = first_line.split(',')
    # Indentation can cause an error
    return line_list[0].replace(" ", "")

def obt_pass(text):
        first_line = text[0]
        line_list = first_line.split(',')
        return line_list[1].replace(" ", "")
    
def obt_message(text):
        return text[1]


