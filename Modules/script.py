import urllib2

#  Method chack for network connectivity.
def check_connectivity(ip_addr):
    try:
        response=urllib2.urlopen(ip_addr,timeout=1)
	outcome = 'right'
        return True
    except urllib2.URLError as err: pass
    outcome = 'wrong'
    return False



