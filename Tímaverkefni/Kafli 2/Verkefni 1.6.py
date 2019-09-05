secs_str = input("Input seconds: ") # do not change this line
# hours =
hours = int(secs_str) // 3600
# minutes =
minutes = (int(secs_str) % 3600) // 60
# seconds =
seconds =  int(secs_str) - hours* 3600 - minutes * 60
print(hours,":",minutes,":",seconds) # do not change this line
