# {
# 	"t_price" : t_price,
# 	"t_time" : t_time,
# 	"call_or_put" : c_p,
# 	"pos" : pos,
# 	"time" : time,
# 	"quantity" : quant,
# 	"price" : price,
# 	"stock_price" : value,
# 	"transaction_price" : price * quant
# }

def get_index_from_daily_transactions(trans):
	call_c = 0
	put_c = 0

	for t in trans:
		if t['call_or_put'] == 'P':
			put_c += 1

		if t['call_or_put'] == 'C':
			call_c += 1

		mt = t['price'] * t['quantity']


	tt = len(trans)
	date = datetime.now().strftime("%Y/%m/%d")

	cc = round(float(call_c)/tt, 2)
	pc = round(float(put_c)/tt, 2)

	return {
		'date' : date,
		'total' : tt,
		'call' : call_c,
		'put' : put_c,
		'call_ratio' : cc,
		'put_ratio' : pc,
		'call_ratio_skip_same_day_close' : call_ratio_skip,
		'put_ratio_skip_same_day_close' : put_ratio_skip
	}
