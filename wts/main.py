
ctotal = 186
bar = 35
total = ctotal - bar
plates = {}
plates.update({'45':90})
plates.update({'25':50})
plates.update({'15':30})
plates.update({'10':20})
plates.update({'5':10})
plates.update({'2.5':5})
weights = ['45','25','15','10','5', '2.5']

print("For %dlbs, you need:" % ctotal)
print("Number\tPlate\tTotal\tLEFT")
for plate in weights:
	#print(plate)
	#print(plates[plate])
	#print(plates[plate])
	if total >= plates[plate]:
		num,left = divmod(total,plates[plate])
		total = left
		print("%d\t%s\t%d\t%d" %(2*num,plate,num*plates[plate],left))
		
if left > 0:
	print("With %dlbs left over." % left)