import re
from datetime import datetime

def get_transaction_data(path):
	f = open(path,"r")
	trans = []

	for l in f.readlines():
		if "N/A" in l:
			continue

		ts = l.split("\t")

		time = ts[0]
		quant = int(ts[2].replace(',',''))
		price = float(ts[3])
		value = float(ts[8])

		pos = ts[1]
		pos_regex = r'(\d+ [A-Z]+ \d+) (\d+) ([P|C])'

		match = re.match(pos_regex, pos)
	
		t_time = match.group(1)
		t_price = match.group(2)
		c_p = match.group(3)

		tr = {
			"t_price" : t_price,
			"t_time" : t_time,
			"call_or_put" : c_p,
			"pos" : pos,
			"time" : time,
			"quantity" : quant,
			"price" : price,
			"stock_price" : value,
			"transaction_price" : price * quant
		}
		trans.append(tr)
	f.close()
	return trans

def sort(t): 
    return t['transaction_price']

def get_summary_from_trans(trans):
	call_c = 0
	put_c = 0

	m = 0
	mh = None

	for t in trans:
		if t['call_or_put'] == 'P':
			put_c += 1

		if t['call_or_put'] == 'C':
			call_c += 1

		mt = t['price'] * t['quantity']
		if mt > m:
			m = mt
			mh = t

	tt = len(trans)
	date = datetime.now().strftime("%Y/%m/%d")

	print "*" * 20
	print "%s" % date
	print "Total: %d " % tt
	print "Call: %d (%.2f)" % (call_c, float(call_c)/tt)
	print "Put: %d (%.2f)" % (put_c, float(put_c)/tt)
	print "*" * 20

	cc = round(float(call_c)/tt, 2)
	pc = round(float(put_c)/tt, 2)

	# trans.sort(key=helper.sort, reverse = True)
	# i = 0
	# for t in trans:
	# 	print t
	# 	i += 1
	# 	if i == 10:
	# 		break

	return {
		'date' : date,
		'total' : tt,
		'call' : call_c,
		'put' : put_c,
		'call_ratio' : cc,
		'put_ratio' : pc
	}
