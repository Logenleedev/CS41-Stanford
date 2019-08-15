a = True
b = False 


# A a and b 
# B not (not (a)) or b
# C  a and not b or not a
# D (b and not(b)) or (a or not(a))

print(a and b )
print(not (not (a)) or b)
print(a and not b or not a)
print((b and not(b)) or (a or not(a)))

'''
A => False
B => True
C => True
D => True
'''

percent = 12.3456789
megabytes = 4100
message = 'Progress: {0}%, {1} MB'.format(percent, megabytes)  # finish this line, so that . . .
print(message)  # . . . the program prints: "Progress: 12.35%, 004100 MB"

