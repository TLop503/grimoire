from decimal import Rounded
from os import popen
import hashlib, datetime, time, math, subprocess, json
import string
from itertools import chain, product


def response(res):
	print(res + ' | ' + popen('date').read())
	exit()

def generate_nonce():
	current_time = time.time()
	rounded_time = round(current_time / 60) * 60  # Round to the nearest 1 minutes (60 seconds)
	#rounded time for noon here
	#9pm sweden time
	return hashlib.sha256(str(int(1705783380)).encode()).hexdigest()

def nogenerate_nonce():
	current_time = time.time()
	rounded_time = round(current_time / 60) * 60  # Round to the nearest 1 minutes (60 seconds)
	return hashlib.sha256(str(int(rounded_time)).encode()).hexdigest()


def is_valid_proof(data, nonce):
	DIFFICULTY_LEVEL = 6
	guess_hash = hashlib.sha256(f'{data}{nonce}'.encode()).hexdigest()
	return guess_hash[:DIFFICULTY_LEVEL] == '0' * DIFFICULTY_LEVEL


class Blacklist:

	def __init__(self, data, nonce):
		self.data = data
		self.nonce = nonce

	def get_data(self):
		out = {}
		out['data'] = self.data if 'data' in self.__dict__ else ()
		out['nonce'] = self.nonce if 'nonce' in self.__dict__ else ()
		return out


def add_to_blacklist(src, dst):
	for key, value in src.items():
		if hasattr(dst, '__getitem__'):
			if dst[key] and type(value) == dict:
				add_to_blacklist(value, dst.get(key))
			else:
				dst[key] = value
		elif hasattr(dst, key) and type(value) == dict:
			add_to_blacklist(value, getattr(dst, key))
		else:
			setattr(dst, key, value)

def lists_to_set(data):
	if type(data) == dict:
		res = {}
		for key, value in data.items():
			res[key] = lists_to_set(value)
	elif type(data) == list:
		res = ()
		for value in data:
			res = (*res, lists_to_set(value))
	else:
		res = data
	return res

def is_blacklisted(json_input):

	bl_data = blacklist.get_data()
	if json_input['data'] in bl_data['data']:
		return True
	if json_input['nonce'] in bl_data['nonce']:
		return True

	json_input = lists_to_set(json_input)
	add_to_blacklist(json_input, blacklist)
	return False

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))




if __name__ == '__main__':

	blacklist = Blacklist(['dd9ae2332089200c4d138f3ff5abfaac26b7d3a451edf49dc015b7a0a737c794'], ['2bfd99b0167eb0f400a1c6e54e0b81f374d6162b10148598810d5ff8ef21722d'])
	# data = 'thequickbrownfoxjumpedoverthelazydog'
	# server_nonce = generate_nonce()
	# server_hash = hashlib.sha256(f'{data}{server_nonce}'.encode()).hexdigest()

	# print(f"Data: {data}\n\n")
	# print(f"Nonce: {server_nonce}\n\n")
	# print(f"Hash: {server_hash}\n\n")

	# print("configured:\n\n\n{\"data\":\"thequickbrownfoxjumpedoverthelazydog\",\"nonce\":\"" + 
	#    server_nonce + "\",\"hash\":\"" + server_hash  +
	#    "\"}")

	# print(datetime.datetime.utcnow())
	server_nonce = generate_nonce()
	for attempt in bruteforce(string.ascii_lowercase, 10):
    # match it against your password, or whatever
		if is_valid_proof(attempt, server_nonce):
			print(attempt)
			data = attempt
			
			server_hash = hashlib.sha256(f'{data}{server_nonce}'.encode()).hexdigest()

			print("configured:\n\n\n{\"data\":\"" + data + "\",\"nonce\":\"" + 
		    	server_nonce + "\",\"hash\":\"" + server_hash  +
	    		"\"}")
			break
			


	
		
