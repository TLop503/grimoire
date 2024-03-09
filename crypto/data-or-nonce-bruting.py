"""Given a known data or nonce brute force sha256 combinations until output with desired condition is met.
For this example the goal is `000000` at the start of the hash

this is used for psuedo-proof of work type challenges
"""


from decimal import Rounded
from os import popen
import hashlib, datetime, time, math, subprocess, json
import string
from itertools import chain, product

def hardcode_nonce():
	# Unix timestamp
	timestamp = 1705783380
	return hashlib.sha256(str(int(timestamp)).encode()).hexdigest()

def time_generate_nonce():
	current_time = time.time()
	rounded_time = round(current_time / 60) * 60  # Round to the nearest 1 minutes (60 seconds)
	return hashlib.sha256(str(int(rounded_time)).encode()).hexdigest()

def is_valid_proof(data, nonce):
	"""Verify if proof meets condition"""
	DIFFICULTY_LEVEL = 6
	guess_hash = hashlib.sha256(f'{data}{nonce}'.encode()).hexdigest()
	return guess_hash[:DIFFICULTY_LEVEL] == '0' * DIFFICULTY_LEVEL

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


if __name__ == '__main__':
	
	# if you want to time-seed nonces for whatever reason
	# server_nonce = generate_nonce()
	
	nonce = hardcode_nonce()

	for attempt in bruteforce(string.ascii_lowercase, 10):
    # match it against your password, or whatever
		if is_valid_proof(attempt, nonce):
			print(attempt)
			data = attempt
			
			server_hash = hashlib.sha256(f'{data}{nonce}'.encode()).hexdigest()

			print("configured:\n\n\n{\"data\":\"" + data + "\",\"nonce\":\"" + 
		    	nonce + "\",\"hash\":\"" + server_hash  +
	    		"\"}")
			break
			


	
		
