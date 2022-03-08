import datetime
import pytz

# ====================Ways of creating date=====================

# d=datetime.date(2022,3,3)
# print(d)


# tday=datetime.date.today()
# print(tday.weekday())
# print(tday.isoweekday())

# tday=datetime.date.today()
# tdelta=datetime.timedelta(days=7)
# print(tday+tdelta) or print(tday-tdelta)

# tday=datetime.date.today()
# bday=datetime.date(2022, 9, 1)
# till_day=bday-tday
# print(till_day)
# print(till_day.total_seconds())

# t=datetime.time(9, 30, 45, 100000)
# print(t.hour)

# dt=datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)
# tdelta=datetime.timedelta(hours=12)
# print(dt+tdelta)

# dt_today=datetime.datetime.today()
# dt_now=datetime.datetime.now()
# dt_utcnow=datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt=datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.utc)
# print(dt)
# dt_now=datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)
# dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
# dt_mtn=dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# for tz in pytz.all_timezones:
#     print(tz)


# dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
# ###### print(dt_utcnow)
# dt_mtn=datetime.datetime.now()
# mtn_tz=pytz.timezone('US/Mountain')
# dt_mtn=mtn_tz.localize(dt_mtn)
# dt_east=dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)
# ###### print(dt_mtn)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'March 3, 2022'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
