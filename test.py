s={'Rahul': {'English': 70, 'Maths': 66, 'Science': 80},
 'Virat': {'English': 58, 'Maths': 88, 'Science': 72},
 'Rohit': {'English': 91, 'Maths': 40, 'Science': 65}}


# Rank of Virat is 1
# Rank of Rahul is 2
# Rank of Rohit is 3

result = 0
name = ''

for x in s:
  temp = 0
  for y in s[x]:
    temp += s[x][y]
  if result < temp:
      result = temp
      name = x
print(result,name)
