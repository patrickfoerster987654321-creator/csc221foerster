import string

song = "The rain in Spain..."

s = "The rain in Spain..."

new_s = s.join(s.split(song))

print(s)
print(new_s)

"""
The main difference is there are no spaces left after join and split.
"""
