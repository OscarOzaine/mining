import requests
import json
import time
import psutil
import subprocess

algorithms = {
	0: ['Scrypt', 'stratum+tcp://scrypt.usa.nicehash.com:3333'],
	1: ['SHA256', 'stratum+tcp://sha256.usa.nicehash.com:3334'],
	2: ['ScryptNf', 'stratum+tcp://scryptnf.usa.nicehash.com:3335'],
	3: ['X11', 'stratum+tcp://x11.usa.nicehash.com:3336'],
	4: ['X13', 'stratum+tcp://x13.usa.nicehash.com:3337'],
	5: ['Keccak', 'stratum+tcp://keccak.usa.nicehash.com:3338'],
	6: ['X15', 'stratum+tcp://x15.usa.nicehash.com:3339'],
	7: ['Nist5', 'stratum+tcp://nist5.usa.nicehash.com:3340'],
	8: ['NeoScrypt', 'stratum+tcp://neoscrypt.usa.nicehash.com:3341'],
	9: ['Lyra2RE', 'stratum+tcp://lyra2re.usa.nicehash.com:3342'],
	10: ['WhirlpoolX', 'stratum+tcp://whirlpoolx.usa.nicehash.com:3343'],
	11: ['Qubit', 'stratum+tcp://qubit.usa.nicehash.com:3344'],
	12: ['Quark', 'stratum+tcp://quark.usa.nicehash.com:3345'],
	13: ['Axiom', 'stratum+tcp://axiom.usa.nicehash.com:3346'],
	14: ['Lyra2REv2', 'stratum+tcp://lyra2rev2.usa.nicehash.com:3347'],
	15: ['ScryptJaneNf16', 'stratum+tcp://scryptjanenf16.usa.nicehash.com:3348'],
	16: ['Blake256r8', 'stratum+tcp://blake256r8.usa.nicehash.com:3349'],
	17: ['Blake256r14', 'stratum+tcp://blake256r14.usa.nicehash.com:3350'],
	18: ['Blake256r8vnl', 'stratum+tcp://blake256r8vnl.usa.nicehash.com:3351'],
	19: ['Hodl', 'stratum+tcp://hodl.usa.nicehash.com:3352'],
	20: ['DaggerHashimoto', 'stratum+tcp://daggerhashimoto.usa.nicehash.com:3353'],
	21: ['Decred', 'stratum+tcp://decred.usa.nicehash.com:3354'],
	22: ['CryptoNight', 'stratum+tcp://cryptonight.usa.nicehash.com:3355'],
	23: ['Lbry', 'stratum+tcp://lbry.usa.nicehash.com:3356'],
	24: ['Equihash', 'stratum+tcp://equihash.usa.nicehash.com:3357'],
	25: ['Pascal', 'stratum+tcp://pascal.usa.nicehash.com:3358'],
	26: ['X11Gost', 'stratum+tcp://x11gost.usa.nicehash.com:3359'],
	27: ['Sia', 'stratum+tcp://sia.usa.nicehash.com:3360'],
	28: ['Blake2s', ''],
	29: ['Skunk', '']
};

def getMostPaid(json):
	json = sorted(json, key=lambda k: k.get('paying', 0), reverse=True)
	return algorithms[json[0]['algo']]

url = 'https://api.nicehash.com/api?method=simplemultialgo.info'
command = 'gedit'
TIMEOUT = 30#60 * 60  # 1 hour

response = requests.get(url)
response = response.json()

if 'simplemultialgo' in response['result']:
	mostpaid = getMostPaid(response['result']['simplemultialgo'])
	#print(mostpaid[0].lower() + ' ' + mostpaid[1])
	subp = subprocess.Popen([command, str(mostpaid[0].lower()) + '.txt'])
	p = psutil.Process(subp.pid)

while True:

	if (time.time() - p.create_time()) > TIMEOUT:
		p.kill()
		#print(time.time())
		#print(p.create_time())
		#print(time.time() - p.create_time())
		
		response = requests.get(url)
		response = response.json()

		if 'simplemultialgo' in response['result']:
			mostpaid = getMostPaid(response['result']['simplemultialgo'])
			#print(mostpaid[0].lower() + ' ' + mostpaid[1])
			subp = subprocess.Popen([command, str(mostpaid[0].lower()) + '.txt'])
			p = psutil.Process(subp.pid)
		#raise RuntimeError('timeout')

	#time.sleep(1)
