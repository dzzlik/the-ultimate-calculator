import math

def herons_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

def calculator():
    problem = input("Choose a problem (Basic maths, Algebra, Geometry, Converting): ").lower()

    if problem == "basic maths":
        equation = input("Enter your equation: ")
        answer = eval(equation)
        print(answer)

    elif problem == "algebra":
        equation = input("This can only solve quadratic equations.")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = b ** 2 - 4 * a * c
        print(f"D = {d}")
        if d < 0:
            print("No solutions, D is negative!")
        elif d == 0:
            x = -b / (2 * a)
            x = round(x, 2)
            print(f"x = {x}")
            print("One solution")
        else:
            d = d ** 0.5
            x1 = (-b + d) / (2 * a)
            x2 = (-b - d) / (2 * a)
            x1 = round(x1, 2)
            x2 = round(x2, 2)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print("Two solutions")

    elif problem == "geometry":
        shape = input("Choose a shape (Triangle, Rectangle, Square): ").lower()
        if shape == "triangle":
            first_side = float(input("Enter the first side of the triangle: "))
            second_side = float(input("Enter the second side of the triangle: "))
            third_side = float(input("Enter the third side of the triangle: "))

            issue = input("What do you wish to find? (Perimeter, Area, Height): ").lower()

            if issue == "area":
                area = herons_area(first_side, second_side, third_side)
                print(f"The area of the triangle is: {round(area, 2)}")
            elif issue == "perimeter":
                perimeter = first_side + second_side + third_side
                print(f"The perimeter of the triangle is: {round(perimeter, 2)}")
            elif issue == "height":
                area = herons_area(first_side, second_side, third_side)
                base = first_side  # first side as base
                height = (2 * area) / base
                print(f"The height of the triangle is: {round(height, 2)}")

        elif shape == "rectangle" or shape == "square":
            if shape == "rectangle":
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                perimeter = 2 * (length + width)
                area = length * width
                print(f"The perimeter of the rectangle is: {round(perimeter, 2)}")
                print(f"The area of the rectangle is: {round(area, 2)}")

            elif shape == "square":
                side = float(input("Enter the side length of the square: "))
                perimeter = 4 * side
                area = side * side
                print(f"The perimeter of the square is: {round(perimeter, 2)}")
                print(f"The area of the square is: {round(area, 2)}")
    elif problem == "converting":
        unit = input("What type of measurement unit? (Time, Weight, Length, Temperature): ").lower()
        if unit == "time":
            time = input("Enter the time (Second, Minute, Hour, Day, Week, Month, Year): ").lower()

            if time == "second":
                second = float(input("Enter the number of seconds: "))
                minute = second // 60
                hour = second / 3600
                day = second / 86400
                week = second / 604800
                month = second / 2592000
                year = second / 31536000
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "minute":
                    print(f"The number of {time}s in a(n) {second_unit} is: {round(minute, 2)}")
                elif second_unit == "hour":
                    print(f"The number of {time}s in an {second_unit} is: {round(hour, 2)}")
                elif second_unit == "day":
                    print(f"The number of {time}s in a {second_unit} is: {round(day, 2)}")
                elif second_unit == "week":
                    print(f"The number of {time}s in a {second_unit} is: {round(week, 2)}")
                elif second_unit == "month":
                    print(f"The number of {time}s in a {second_unit} is: {round(month, 2)}")
                elif second_unit == "year":
                    print(f"The number of {time}s in a {second_unit} is: {round(year, 2)}")

            elif time == "minute":
                minute = float(input("Enter the number of minutes: "))
                second = minute * 60
                hour = minute / 60
                day = minute / 1440
                week = minute / 10080
                month = minute / 43800
                year = minute / 525600
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "second":
                    print(f"This many {time}s is {round(second, 2)} {second_unit}s")
                elif second_unit == "hour":
                    print(f"This many {time}s is {round(hour, 2)} {second_unit}s")
                elif second_unit == "day":
                    print(f"This many {time}s is {round(day, 2)} {second_unit}s")
                elif second_unit == "week":
                    print(f"This many {time}s is {round(week, 2)} {second_unit}s")
                elif second_unit == "month":
                    print(f"This many {time}s is {round(month, 2)} {second_unit}s")
                elif second_unit == "year":
                    print(f"This many {time}s is {round(year, 2)} {second_unit}s")

            elif time == "hour":
                hour = float(input("Enter the number of hours: "))
                second = hour * 3600
                minute = hour * 60
                day = hour / 24
                week = hour / 168
                month = hour / 730
                year = hour / 8760
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "second":
                    print(f"This many {time}s is {round(second, 2)} {second_unit}s")
                elif second_unit == "minute":
                    print(f"This many {time}s is {round(minute, 2)} {second_unit}s")
                elif second_unit == "day":
                    print(f"This many {time}s is {round(day, 2)} {second_unit}s")
                elif second_unit == "week":
                    print(f"This many {time}s is {round(week, 2)} {second_unit}s")
                elif second_unit == "month":
                    print(f"This many {time}s is {round(month, 2)} {second_unit}s")
                elif second_unit == "year":
                    print(f"This many {time}s is {round(year, 2)} {second_unit}s")

            elif time == "day":
                day = float(input("Enter the number of days: "))
                second = day * 86400
                minute = day * 1440
                hour = day * 24
                week = day / 7
                month = day / 30.4375
                year = day / 365.25
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "second":
                    print(f"This many {time}s is {round(second, 2)} {second_unit}s")
                elif second_unit == "minute":
                    print(f"This many {time}s is {round(minute, 2)} {second_unit}s")
                elif second_unit == "hour":
                    print(f"This many {time}s is {round(hour, 2)} {second_unit}s")
                elif second_unit == "week":
                    print(f"This many {time}s is {round(week, 2)} {second_unit}s")
                elif second_unit == "month":
                    print(f"This many {time}s is {round(month, 2)} {second_unit}s")
                elif second_unit == "year":
                    print(f"This many {time}s is {round(year, 2)} {second_unit}s")

            elif time == "week":
                week = float(input("Enter the number of weeks: "))
                second = week * 604800
                minute = week * 10080
                hour = week * 168
                day = week * 7
                month = week / 4.34524
                year = week / 52.1429
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "second":
                    print(f"This many {time}s is {round(second, 2)} {second_unit}s")
                elif second_unit == "minute":
                    print(f"This many {time}s is {round(minute, 2)} {second_unit}s")
                elif second_unit == "hour":
                    print(f"This many {time}s is {round(hour, 2)} {second_unit}s")
                elif second_unit == "day":
                    print(f"This many {time}s is {round(day, 2)} {second_unit}s")
                elif second_unit == "month":
                    print(f"This many {time}s is {round(month, 2)} {second_unit}s")
                elif second_unit == "year":
                    print(f"This many {time}s is {round(year, 2)} {second_unit}s")

            elif time == "month":
                month = float(input("Enter the number of months: "))
                second = month * 2592000
                minute = month * 43800
                hour = month * 730
                day = month * 30.4375
                week = month / 4.34524
                year = month / 12
                second_unit = input("What unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "second":
                    print(f"This many {time}s is {round(second, 2)} {second_unit}s")
                elif second_unit == "minute":
                    print(f"This many {time}s is {round(minute, 2)} {second_unit}s")
                elif second_unit == "hour":
                    print(f"This many {time}s is {round(hour, 2)} {second_unit}s")
                elif second_unit == "day":
                    print(f"This many {time}s is {round(day, 2)} {second_unit}s")
                elif second_unit == "week":
                    print(f"This many {time}s is {round(week, 2)} {second_unit}s")
                elif second_unit == "year":
                    print(f"This many {time}s is {round(year, 2)} {second_unit}s")
            elif time == "year":
                year = float(input("Enter the number of years: "))
                second = year * 31536000
                minute = year * 525600
                hour = year * 8760
                day = year * 365.25
                week = year * 52.1429
                month = year / 12
                second_unit = input("Which unit do you want to convert it to?: (Second, Minute, Hour, Day, Week, Month, Year): ").lower()
                if second_unit == "minute":
                    print(f"This many {time}s is {round(minute, 2)} {second_unit}s")
                elif second_unit == "hour":
                    print(f"This many {time}s is {round(hour, 2)} {second_unit}s")
                elif second_unit == "day":
                    print(f"This many {time}s is {round(day, 2)} {second_unit}s")
                elif second_unit == "week":
                    print(f"This many {time}s is {round(week, 2)} {second_unit}s")
                elif second_unit == "month":
                    print(f"This many {time}s is {round(month, 2)} {second_unit}s")

        elif unit == "weight":
            weight = input("Enter the weight (Kilogram, Pound): ").lower()
            if weight == "kilogram":
                kilogram = float(input("Enter the weight in kilograms: "))
                pound = kilogram * 2.20462
                print(f"The weight in pounds is: {round(pound, 2)}")
            elif weight == "pound":
                pound = float(input("Enter the weight in pounds: "))
                kilogram = pound / 2.20462
                print(f"The weight in kilograms is: {round(kilogram, 2)}")

        elif unit == "length":
            length = input("Enter the length unit (Meter, Kilometer, Mile, Foot, Yard): ").lower()
            if length == "centimeter":
                centimeter = float(input("Enter the length in centimeters: "))
                meter = centimeter / 100
                kilometer = centimeter / 100000
                mile = centimeter / 160934
                foot = centimeter / 3280.84
                second_unit = input("Which unit do you want to convert it to?: (Centimeter, Meter, Kilometer, Mile, Foot): ").lower()
                if second_unit == "meter":
                    print(f"This many {length}s is {round(meter, 2)} {second_unit}s")
                elif second_unit == "kilometer":
                    print(f"This many {length}s is {round(kilometer, 2)} {second_unit}s")
                elif second_unit == "mile":
                    print(f"This many {length}s is {round(mile, 2)} {second_unit}s")
                elif second_unit == "foot":
                    print(f"This many {length}s is {round(foot, 2)} {second_unit}s")
            elif length == "meter":
                meter = float(input("Enter the length in meters: "))
                centimeter = meter * 100
                kilometer = meter / 1000
                mile = meter / 1609.34
                foot = meter / 3.28084
                second_unit = input("What unit do you want it convert to?: (Centimeter, Meter, Kilometer, Mile, Foot): ").lower()
                if second_unit == "centimeter":
                    print(f"This many {length}s is {round(centimeter, 2)} {second_unit}s")
                elif second_unit == "kilometer":
                    print(f"This many {length}s is {round(kilometer, 2)} {second_unit}s")
                elif second_unit == "mile":
                    print(f"This many {length}s is {round(mile, 2)} {second_unit}s")
                elif second_unit == "foot":
                    print(f"This many {length}s is {round(foot, 2)} {second_unit}s")
            elif length == "kilometer":
                kilometer = float(input("Enter the length in kilometers: "))
                centimeter = kilometer * 100000
                meter = kilometer * 1000
                mile = kilometer * 0.621371
                foot = kilometer * 3280.84
                second_unit = input("Which unit do you want to convert it to?: (Centimeter, Meter, Kilometer, Mile, Foot): ").lower()
                if second_unit == "centimeter":
                    print(f"This many {length}s is {round(centimeter, 2)} {second_unit}s")
                elif second_unit == "meter":
                    print(f"This many {length}s is {round(meter, 2)} {second_unit}s")
                elif second_unit == "foot":
                    print(f"This many {length}s is {round(foot, 2)} {second_unit}s")
                elif second_unit == "mile":
                    print(f"This many {length}s is {round(mile, 2)} {second_unit}s")
            elif length == "mile":
                mile = float(input("Enter the length in miles: "))
                centimeter = mile * 160934
                meter = mile * 1609.34
                kilometer = mile * 1.60934
                foot = mile * 5280
                second_unit = input("Which unit do you want to convert it to?: (Centimeter, Meter, Kilometer, Mile, Foot): ").lower()
                if second_unit == "centimeter":
                    print(f"This many {length}s is {round(centimeter, 2)} {second_unit}s")
                elif second_unit == "meter":
                    print(f"This many {length}s is {round(meter, 2)} {second_unit}s")
                elif second_unit == "kilometer":
                    print(f"This many {length}s is {round(kilometer, 2)} {second_unit}s")
                elif second_unit == "foot":
                    print(f"This many {length}s is {round(foot, 2)} {second_unit}s")
            elif length == "foot":
                foot = float(input("Enter the length in feet: "))
                centimeter = foot * 3280.84
                meter = foot * 3.28084
                kilometer = foot / 0.3048
                mile = foot / 5280
                second_unit = input("Which unit do you want to convert it to?: (Centimeter, Meter, Kilometer, Mile, Foot): ").lower()
                if second_unit == "centimeter":
                    print(f"This many {length}s is {round(centimeter, 2)} {second_unit}s")
                elif second_unit == "meter":
                    print(f"This many {length}s is {round(meter, 2)} {second_unit}s")
                elif second_unit == "kilometer":
                    print(f"This many {length}s is {round(kilometer, 2)} {second_unit}s")
                elif second_unit == "mile":
                    print(f"This many {length}s is {round(mile, 2)} {second_unit}s")
        elif unit == "temperature":
            temperature = input("Enter the temperature unit (Celsius, Fahrenheit): ").lower()
            if temperature == "celsius":
                celsius = float(input("Enter the temperature in Celsius: "))
                fahrenheit = celsius * 1.8 + 32
                print(f"This many {temperature} is {round(fahrenheit, 2)} Fahrnheits")
            elif temperature == "fahrenheit":
                fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) / 1.8
                print(f"This many {temperature}s is {round(celsius, 2)} Celsius")

calculator()
input()
