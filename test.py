from datetime import datetime,date,timedelta  
now = datetime.now();  
nextDay = now + timedelta(days = 1);#增加一天后的时间  
nextSecond = now + timedelta(seconds = 1);#增加一秒后的时间  
span  = now - nextDay;#获取时间差对象  
print(now);  
print(nextDay);  
print(nextSecond);  
print(span.total_seconds());#获取时间差 以秒为单位  
