hour = 0
mins = 1
dura = 2939

# Write your code here.
if 0 <= hour <= 23 and 0 <= mins <= 59:
    if hour < 10 and mins < 10:
        print(f"0{hour}:0{mins}")

    mins1 = mins + dura

    hours1 = mins1 // 60

    finalhours = ((hours1 + hour) % 24)

    finalminutes = (mins1 % 60)

    if finalhours and finalminutes < 10:
        print(f"0{finalhours}:0{finalminutes}")
    else:
        print(f"{finalhours}:{finalminutes}")