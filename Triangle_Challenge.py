side_1 = int(input("The length of side a ="))
side_2 = int(input("The length of side b ="))
side_3 = int(input("The length of side c ="))

if side_3 >= side_1 + side_2 or side_2 >= side_1 + side_3 or side_1 >= side_2 + side_3:
    print("Triangle is not valid")
elif side_3 < 0 or side_2 < 0 or side_1 < 0:
    print("Triangle is not valid")
else:
    print("Hooray! Your triangle is valid")