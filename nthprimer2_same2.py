def in_matrix(needle, haystack):
	for substack in haystack:
		if needle in substack:
			return True
	return False

def multiplylist(lst, pr):
    return [i*pr for i in lst]

# /////////////////////////
# /*************************

# nth Pr. -> RANGE
# 1 -> 2^0
# 3 -> 2^1
# 5 -> 2^2
# 7 -> 2^3
# 10 -> 2^4
# 17 -> 2^5
# 29 -> 2^6
# 48 -> 2^7
# 84 -> 2^8
# 151 -> 2^9
# 270 -> 2^10
# 483 -> 2^11
# 	.
# 	.
# 	.
# 	.
# when i = 100, the 100th P will give 540.
# because 540 is not in the matrix



# *************************/
# /////////////////////////



print ('Hello Primes')

no = 1
pr = 1
no_count = 1

no_arr = []
pr_arr = []

# no_arr.append(no)
# no_arr.append(2)
# #  Needs a table containing all the Ns multiplied by PRs (MATRIX?)

# condition =


i = 12 				#how may primes do I want to find?
rnge = 2**4 		#the range in which all the primes are

matrix = [['' for x in range(i)] for y in range(i)]

#create the number array
# replaced : no_arr = list(range(1, i+1))
no_arr = list(range(1, rnge+1))





while no_count <= i:
	
	print ('-')
	print ('while', no_count)
	print ('-')
	
	while not (no**pr)%pr == no: #test the first condition
		pr += 1

	while in_matrix(pr, matrix): #test if pr is already in the matrix (second condition)
		pr += 1

	pr_arr.append(pr) #if the two conditions meet, insert $pr to $pr_arr

	print (pr) #print the Prime

	# for ax in range(len(no_arr)):
	# 	for bx in range(len(pr_arr)):
	# 		matrix[ax][bx] = no_arr[ax] * pr_arr[bx]

	# for ax in range(len(no_arr)):
	# 	# for bx in range(len(no_arr)):
	# 		matrix[ax] = ax * pr

	matrix[no_count-1] = multiplylist(no_arr, pr)



	no += 1
	pr += 1
	


		
	print ('-')
	print (' ')


	




	no_count += 1




