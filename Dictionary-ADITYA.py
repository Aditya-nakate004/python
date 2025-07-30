#crestin dict
phone={"aditya":57688,
        "JOY":8768346,
        "RAM":93836376}

print(phone)

print(type(phone))

print(len(phone))

#how to acces items of dictionary
print(phone["JOY"])
print(phone.get("JOY"))

print(phone.keys())

phone["JOY"]=87979
print(phone)


#adding items in dictionary
phone["riya"]=768577
print(phone)

more_phons={
    "kia":89498
}
phone.update(more_phons)
print(phone)

#to remove items
phone.pop("kia")
print(phone)

# to remove last item addes ti dict
phone.popitem()
print(phone)


#for clear to dictionary
phone.clear()
print(phone)

#how can i print values of a dict

for x in phone:  
    print(x)         #...this will print only keys
    print(phone[x])     #....this will print oly values of key

for x in phone.items():
    print(x)  

# printing elements of dict
for x,y in phone.items():
    print(x,y)  

 #nasted dic
phons={
  "area1":{
   "x":3,
   "y":8,
   "z":3
  },
  "area2":{
      "a":4,
      "b":5,
      "c":6
  }
 }

#access the nasted dic
print(phons["area1"]["x"])
print(phons["area2"]["b"])



#example
#find the sum of the valuse of dict
dic={"x":2,"y":55,"z":34}
print(dic.values())
print("The sum of dic values:",(sum(dic.values())))