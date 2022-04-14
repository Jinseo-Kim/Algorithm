N = int(input())

five_kg = N // 5
remaining_sugar = N % 5

while True:
    if remaining_sugar % 3 > 0:
        if five_kg <= 0:
            print(-1)
            break
        remaining_sugar += 5
        five_kg -= 1
    else:
        five_kg += (remaining_sugar // 3)
        print(five_kg)
        break

