# Импортируем библиотеку datetime
from datetime import datetime
#import datetime

current_date_time = datetime.now()
print(current_date_time)

date_format_date = datetime.strptime("2022.12.31", "%Y.%m.%d")

print(date_format_date)


