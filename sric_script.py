import subprocess

# The IP of the server we're downloading/uploading things to/from
server = 192.168.1.1

# The names of the files were dealing with
creds = 'credentials.txt'
upload = 'upload-package.txt'

# Download creds
down_user = 'tmp'
down_pass = 'tmp'

# Loop forever!
while True:

	# Verify connection
	output = subprocess.check_output(['ping', '-n', '1', server])
	if output = 'tmp string for network down':
		continue
	
	# Using SFPT because I'm not sure if we can use SCP
	with pysftp.Connection('http://' + server, username = down_user, password = down_pass) as sftp:
		# Get the download payload
		sftp.get(creds, '/creds.txt')
		
	# Open download file
	cred_file = open(creds)
	
	# Parse it
	
	
	with pysftp.Connection(server, username = up_user, password = up_pass) as sftp:
		# Put the upload payload
		sftp.put(uplpad)
	
	# Close cred_file (After the put since we need to get that done as fast as possible)
	cred_file.close()
	# End this script to save resources for other things
	break
	
  # Not currently connected... Time to try again
