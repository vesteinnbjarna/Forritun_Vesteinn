# Given seconds (int) calculate hours, minutes, and seconds.
# For example, given 80000 seconds that is
# 22 hours, 13 minutes, and 20 seconds.
# Hint 1: use integer division (//) and remainder (%)
# Hint 2: we require that you create and output variables hours,
#  minutes, and seconds, but you will likely find an additional variable useful.



seconds_int = int(input('Enter seconds: '))

hours = seconds_int // 3600
minutes = (seconds_int % 3600) // 60
seconds = seconds_int - (hours*3600) - (minutes * 60)

print('Hours: ',hours, ' Minutes: ', minutes, 'Seconds: ', seconds)