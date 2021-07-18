print("Hello World!")
counties = ["Arapahoe","Denver","Jefferson"]
my_list = [ ]
my_list = list()
counties
print(counties[0])
print(counties[2])
print(counties[-1])
len(counties)
print (counties[0:2])
print(counties[:3])
print(counties[1:])
counties.append("El paso")
counties
print (counties)
counties.insert(2, "El Paso")
print (counties)
counties.remove("El Paso")
print (counties)
counties.pop(3)
print(counties)
counties[2] = ("El Paso")
print(counties)
counties[2]=("Jefferson")
print(counties)
counties[1]=("El Paso")
print(counties)
counties.remove("Arapahoe")
print(counties)
print (counties)
counties_dict = {}
counties_dict["Arapahoe"]=422829
print (counties_dict)
counties_dict["Denver"]=463353
print (counties_dict)
counties_dict["Jefferson"]=432438
print (counties_dict)
print(len(counties_dict))
print((counties_dict.items()))
print((counties_dict.keys()))
print((counties_dict.values()))
print (counties_dict.get("Arapahoe"))
#practicing if
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
#practicing for loops"
for county in counties:
    print(county)
counties = ["Arapahoe","Denver","Jefferson"] 
for county in counties_dict.keys():
    print(county)
    for county in counties_dict:
        print (counties_dict[county])
for voters in counties_dict.values():
    print(voters)
for county in counties_dict.keys():
    print(county)
for county in counties_dict.values():
    print(county)
    voting_data=[{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)    
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}    
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")   
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
message= f"{county} county has{voters:,} registered voters"  

