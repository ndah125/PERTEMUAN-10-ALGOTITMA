print ("perulangan 1")
for i in range (6):
    print (i)

print ("perulangan 2")
for i in range(1,6):
    print (i)

print ("perulangan dengan step")
for i in range (0,20,3):
    print (i)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total nilai:", total)

#pengulangan  for dengan list 
print ("perulangan 1")
for i in[1,2,3,4,5]:
    print (f"ini pengulangan ke- {i}")

           
#pengulangan for isi list dengan isi string 
print ("pengulangan sebanyak 8 kali")
for i in ["Rawon","Nasi Kuning","Soto Madura","Kupat Tahu","Kerak Telor","Rendan Batoko","Pempek Selam","Ayam Betutu"] :
              print (i,"adalah masakan khas Nusantara")

#perulangan for dengan string
print ("pengulangan sebanyak 5 kali for i in abcde")             
for i in ["a","b","c","d","e"]:
    print (i,"adalah alfabet")
