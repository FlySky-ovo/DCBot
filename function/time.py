from datetime import datetime, timedelta
from pytz import timezone

def now_time():
	tz = timezone('Asia/Taipei')
	now = datetime.now().replace(tzinfo=tz)
	print(f'［Debug　//　{now}］')