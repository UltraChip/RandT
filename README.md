# Random Triops (RandT)

Random Triops (RandT) is a dirt-simple pseudo-random number generator which is seeded from on-demand webcam images. In the original implementation the webcam was situated in front of an inhabited triops aquarium, thus ensuring no two images (and therefore no two seeds) are the same. This should have the effect of producing truly random numbers. 

The fswebcam package is a required dependency in order to interface with the webcam. This package should be available in most major Linux distributions. 

randt-cgi.py is nearly identical to the main script, but includes a #!/usr/bin/python header to aid in making the script available over web servers.

By default, the script will return a single random integer in the range 0-1,000


RandT supports the following command line arguments:

-v    : Verbose Mode - In addition to your random number, the script will also provide the seed value that was used to generate it as well as the range the number was selected from.

-m    : Max Number - Allows you to modify the default range by specifying its upper bounds. For example, randt.py -m 500 will result in a range of 0-500.

-c    : Count - Allows you to request the number of random numbers returned (default is 1). For example, randt.py -c 5 will return 5 random numbers.
