# Numbers Sets (Lesson 7: Exercise 3)
odd_set = set()
for i in range(101):
    if i % 2 == 0:
        odd_set.add(i)
    else:
        continue
    
print(odd_set)

even_set = set()
for j in range(100):
    if j % 2 == 1:
        even_set.add(j)
    else:
        continue
    
print(even_set)
