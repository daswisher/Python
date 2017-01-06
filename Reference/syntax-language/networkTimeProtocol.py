import ntplib
import time

NIST = 'nist1-macon.macon.ga.us'
ntp = ntplib.NTPClient()

ntpResponse = ntp.request(NIST)

if ntpResponse:
	nistUTC = ntpResponse.tx_time
	print "NIST reported seconds since the Epoch : ", nistUTC

	now = time.time()
	diff = now -ntpResponse.tx_time
	print "Difference:", diff, "seconds"
	print "Network Delay:",ntpResponse.delay

	print "UTC: NIST :",time.strftime("%a, %d %b %Y %H:%M:%S + 0000", time.gmtime(int(ntpResponse.tx_time)))
else:
	print "NTP Request Failed"
