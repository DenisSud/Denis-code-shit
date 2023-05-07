#input
#parse input
n = int(input())
eng_lat = {}
for i in range(n):
    s = input().split(" - ")
    eng_lat[s[0]] = s[1].split(", ")

lat_eng = {}
for eng, lats in eng_lat.items():
    for lat in lats:
        if lat in lat_eng:
            lat_eng[lat].append(eng)
        else:
            lat_eng[lat] = [eng]

#sort the dictionary
lat_eng = {k: sorted(v) for k, v in lat_eng.items()}
lat_eng = dict(sorted(lat_eng.items()))
print(len(lat_eng))
for lat, engs in lat_eng.items():
    eng_str = ', '.join(engs)
    print(lat + " - " + eng_str)
