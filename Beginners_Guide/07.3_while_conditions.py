z=0
while z<5:
	print( 'z = ' + str(z) )
	z += 1 # z = z+1


print " "


i = 0
while i<20:
	i += 1
	if i % 3 == 0: 
		continue 
	print ( 'i = ' + str(i) )

print " " 
	


j = 0
while True: 
	print ('j squared = ' + str(j**2))
	j += 1
	if j >= 5:
		print ('End loop as j = ' + str(j))
		break
