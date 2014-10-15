def maxProduct(A):
	result = [];
	tempArr = [];
	if 0 in A:
		result.append(0);
		temp = []
		for num in A:
			if num != 0:
				temp.append(num);
			else:
				if len(temp) == 0:
					temp.append(0);
				tempArr.append(temp);
				temp = [];
		if len(temp) == 0:
			temp.append(0);
		tempArr.append(temp);
	else:
		tempArr.append(A);

	for l in tempArr:
		if len(l) == 1:
			result.append(l[0]);
		else:
			nflag = False;
			calflag = False;
			a = 1;
			b = 1;
			for num in l:
				a = a * num;
				if nflag:
					b = b * num;
					calflag = True;
					if num < 0:
						result.append(a/num);
				else:
					if num < 0:
						nflag = True;
						result.append(a/num);
			result.append(a);
			if calflag:
				result.append(b);

	print tempArr,result
	return max(result);
	#print tempArr,result;


arr = [12, 15, 1, -5, 5, 5, -1, -5, 2, 0, 1, 2, 4, -4, 0, 12, 12, 15, 1000, 2, 0, 3];
arr2 = [-1]
arr3 = [-1,0,-1,0,0,5,0,-1,5]
arr4 = [0]
print maxProduct(arr4)