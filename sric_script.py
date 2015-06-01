import subprocess

# The IP of the server we're downloading/uploading things to/from
server = 192.168.1.1
server = 'http://' + server

# The name of the file we're downloading
file = 'credentials.txt'


# Loop forever!
while True:

  # Verify connection

	subprocess.call(['ping', '-n', '1', server])
	
	# Get the file (using SFTP until I'm sure we can use SCP)
	with pysftp.Connection(server) as sftp:
	  sftp.get(file, '/creds.txt')
	 
  # Not currently connected... Time to try again
