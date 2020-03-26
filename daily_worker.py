import json
import helper
import index

import setting
from datetime import datetime

def add_new_data():
	date = datetime.now().strftime("%m_%d_%Y")
	data = "data/transcations/raw/spx_%s.txt" % date

	a = {}
	with open(setting.TOTAL_STATS) as f:
		a = json.load(f)

	trans = helper.get_transaction_data(data)
	summary = helper.get_summary_from_trans(trans)

	a[summary['date']] = summary

	with open(setting.TOTAL_STATS, "w") as f:
		json.dump(a, f, indent=4)

def show_all():
	a = {}
	with open(setting.TOTAL_STATS) as f:
		a = json.load(f)

	st = []
	for s in a:
		st.append(s)
	st.sort(reverse=True)

	for ss in st:
		print json.dumps(a[ss], indent=4)

def today():
	date = datetime.now().strftime("%m_%d_%Y")
	data = "data/transcations/raw/spx_%s.txt" % date
	trans = helper.get_transaction_data(data)

	news = []
	for t in trans:
		if "25 MAR" in t['t_time']:
			continue
		news.append(t)

	res = index.get_index_from_daily_transactions(news)
	print json.dumps(res, indent=4)

######################################
#add_new_data()
#show_all()
today()


