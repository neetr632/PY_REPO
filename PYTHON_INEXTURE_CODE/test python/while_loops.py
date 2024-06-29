count = 0
while True:
    for i in range(100):
        count += 1
        if i == 10:
            print("index is at greater than 10")
        elif i == 50:
            print("index is greater than 50")
        elif i == 60:
            print("index is greater than 60")
        elif i == 70:
            print("index is greater than 70")
        elif i == 80:
            print("index is greater than 80")
        elif i == 90:
            print("index is greater than 90")
        else:
            print(i)
    if count >= 100:
            break  
print(f"the while has run for {count} times")
