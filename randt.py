##           RANDOM TRIOPS (RANDT)
##        Pseudorandom Number Generator
##
## A simple PRNG seeded by on-demand webcam images
## of an inhabited aquarium, thus ensuring true
## randomness. 

import random
import subprocess
import sys

def makeSeed():
    subprocess.check_output("fswebcam -q /tmp/image.jpg", shell=True)
    hash = subprocess.check_output("md5sum /tmp/image.jpg", shell=True)
    # Clean up captured image for privacy
    subprocess.check_output("rm /tmp/image.jpg", shell=True)
    return hash.split()[0]

# Default Values
verbose = False
max = 1000
count = 1
r = 0

# Parse command line arguments
opts = [opt for opt in sys.argv[1:]]
if "-v" in opts:
    verbose = True
if "-m" in opts:
    max = int((opts[(opts.index("-m")+1)]))
if "-c" in opts:
    count = int((opts[(opts.index("-c")+1)]))

while r < count:
    # Generate Result
    hash = makeSeed()
    random.seed(hash)
    result = random.randint(0,max)

# Output results
    if verbose:
        print "Seed:          ", hash
        print "Selection range 0 -",max
        print ""
        print "Result: ",result
        print ""
    else:
        print result
    r += 1