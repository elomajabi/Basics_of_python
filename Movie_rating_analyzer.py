ratings = []

while True:
    x = input("input your rating: ")

    if x.lower() == "done":
        break

    x = float(x)
    ratings.append(x)

print(ratings)
print(sum(ratings)/len(ratings))
print(max(ratings))
print(min(ratings))

count1 = 0
count2 = 0
for rating in ratings:
    if rating > sum(ratings)/len(ratings):
        count1+=1
    elif rating < sum(ratings)/len(ratings):
        count2+=1

print(count1)
print(count2)
