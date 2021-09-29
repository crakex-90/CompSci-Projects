import math

people_attending = int(input("Enter the number of people attending: "))
hotdogs_each = int(input("Enter the number of hot dogs each person will receive: "))

number_of_hotdogs_per_package = 10
number_of_buns_per_package = 8

total_number_of_hotdogs = people_attending * hotdogs_each
total_number_of_hotdog_buns = people_attending * hotdogs_each

number_of_hotdog_packages_needed = math.ceil(total_number_of_hotdogs / 10)
number_of_bun_packages_needed = math.ceil(total_number_of_hotdog_buns / 8)

hot_dogs_in_packages = number_of_hotdog_packages_needed * 10
buns_in_packages = number_of_bun_packages_needed * 8

number_of_hotdogs_leftover = hot_dogs_in_packages - total_number_of_hotdogs
number_of_buns_leftover = buns_in_packages - total_number_of_hotdog_buns

print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_bun_packages_needed)
print("Number of hot dogs left over =", number_of_hotdogs_leftover)
print("Number of buns leftover =", number_of_buns_leftover)