import urllib2
import pysftp

# The IP of the server we're downloading/uploading things to/from
server = 192.168.1.1
server = 'http://' + server

# The name of the file we're downloading
file = 'credentials.txt'


# Loop forever!
while True:

  # Verify connection
  try:
    connection = urllib2.urlopen(server, timeout = 1)
    
    # Get the file (using SFTP until I'm sure we can use SCP)
    with pysftp.Connection(server) as sftp:
      sftp.get(file, '/creds.txt')
      
      
  except urlib2.URLError as err: pass
  # Not currently connected... Time to try again
