n = int(input())
countries = {}
for i in range(n):
    country, *cities = input().split()
    countries[country] = set(cities)

m = int(input())

for i in range(m):
    city = input()
    for country, cities in countries.items():
        if city in cities:
            print(country)
            break
