import json
import helper
import setting
from datetime import datetime

def add_new_data():
	#data = "data/trans/spx_03_20_2020.txt"
	date = datetime.now().strftime("%m_%d_%Y")
	data = "data/raw/spx_%s.txt" % date

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

	# for t in trans:
	# 	print json.dumps(t, indent=4)
	# 	raise

	# print helper.get_summary_from_trans(trans)

######################################
#add_new_data()
show_all()
#today()


