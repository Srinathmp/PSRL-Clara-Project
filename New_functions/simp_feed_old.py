import re
import sys

def cleaning_feedback3(text,wrong_comma_list):
	print(text)
	ops=[]
	comma_pos=[]
	two_char_op=0
	initial_op_pos=[]

	bt_match = [m.start()+len('FuncCall') for m in re.finditer('FuncCall', text)]
	# print(bt_match)
	for i in range(len(bt_match)):
		j=bt_match[i]
		opb_count=0
		while(j<len(text)):
			if text[j]=='(':
				# print(j)
				opb_count+=1
			if text[j]==")":
				opb_count-=1
			if opb_count == 0 and text[j]==')':
				new = list(text)
				new[j] = "#"
				text="".join(new)
				break
			j+=1

	for i in range(len(text)-6):
		if text[i] in "<*+-/%^>&" and text[i+1]=="(":
			ops.append(text[i])
			new = list(text)
			new[i] = " "
			text="".join(new)
		elif ((text[i] in "<>=!") and text[i+1]=="=" and text[i+2]=="("):
			ops.append(text[i]+text[i+1])
			initial_op_pos.append(i+1)
			two_char_op+=1
			new = list(text)
			new[i]= " "
			new[i+1]=" "
			text="".join(new)
		if text[i] =="," and i not in wrong_comma_list:
			comma_pos.append(i)

		if text[i]==")" and len(ops)!=0 and len(comma_pos)!=0:
			new = list(text)
			new[comma_pos[len(comma_pos)-1]] = ops[len(ops)-1]
			text="".join(new)
			char_length=len(ops[len(ops)-1])
			comma_pos.pop()
			ops.pop()
			if(two_char_op>0) and char_length>1:
				new = list(text)
				new[initial_op_pos[0]] = ""
				text="".join(new)
				initial_op_pos=[]
				two_char_op-=1

	bt_rep =[m.start() for m in re.finditer('#', text)] #reverting hashes to )
	for i in bt_rep:
		new = list(text)
		new[i] = ")"
		text="".join(new)
	# print(text)
	# print()
	return text

def feed_ini(file):  # !! ======== change path based on where ur repo of progs is stored =============== !! 
	f=open('/home/abhay/Summer_of_System_2020/clara/TestSuite1/'+file, 'r')
	strtxt = f.read()
	# print(strtxt)
	func_names_list=list(set(re.findall(r"(?![a-z])[^\:,>,\.]([a-z,A-Z]+[_]*[a-z,A-Z]*)+[(]", strtxt)))
	#can add other irrelevant tokens here to the list
	irr_token_list=['float','int','double','long','$ret','$in','$out']
	func_names_list= func_names_list+irr_token_list
	return func_names_list


def wrong_comma_func(uncleaned_feedback,func_names_list):
	wrong_comma_list=[]
	# print(func_names_list)
	for i in func_names_list:
		try:
			# a = re.search(i, uncleaned_feedback)
			# index=a.start()+len(i)
			str_matches = [m.start()+len(i) for m in re.finditer(i, uncleaned_feedback)]
			if len(str_matches)!=0:
				for i in str_matches:
					if(uncleaned_feedback[i]==","):
						wrong_comma_list.append(i)
		except:
			pass
	return wrong_comma_list


def legend_key_extract(text):
	legend_words=list(set(re.findall(r'[a-zA-Z]+[(]',text)))
	legend_words=[i.strip('(') for i in legend_words]
	# print(legend_words)

def findall_occurence(string,sub):
    test_str = string
    test_sub = sub
    res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]
    return res

# def func_call_clean(text):
# 	# func_call_text = list(set(re.findall(r'[FuncCall]+[(]+[^)]*[)]',text)))
# 	func_call_text = re.findall(r'[FuncCall]+[(]+[^)]*[)]',text)
# 	func_call_text = [i.strip('FuncCall(').split(',') for i in func_call_text]

# 	for i in func_call_text:
# 		if '(' in i[1]:
# 			i[1]=i[1]+')'

# 	replace_txt_list=['FuncCall('+i[0]+','+i[1] for i in func_call_text]


# 	for i in func_call_text:
# 		if '(' not in i[1]:
# 			i[1]=i[1].strip(')')
# 		i[1]=i[1].strip()

# 	new_funcall_text=['FuncCall('+i[0]+'('+i[1].strip('(').strip(')')+')' for i in func_call_text]
# 	temp_text=text
# 	j=0

# 	# print(replace_txt_list)

# 	for i in range(len(replace_txt_list)):
# 		occ_list = findall_occurence(temp_text,replace_txt_list[i])
# 		# print(occ_list)
# 		index=occ_list[0]
# 		j=index+len(replace_txt_list[i])
# 		temp_text = temp_text[:index]+new_funcall_text[i]+temp_text[j:]
		
# 	text=temp_text
# 	print(text)
# 	print()

def replace_substr(temp_text,substr,repltxt):
	sub_ret = findall_occurence(temp_text,substr)      #for replacing all '$ret' to 'return'
	# print(sub_ret)
	val=sub_ret[0]
	while val < len(temp_text):
		# print(val)
		j=val+len(substr)
		temp_text = temp_text[:val]+repltxt+temp_text[j:]
		# print(temp_text)
		sub_ret = findall_occurence(temp_text,substr)
		# print(sub_ret)
		if len(sub_ret)==0:
			break
		else:
			val=sub_ret[0]

	return temp_text

# def return_clean(temp_text):
# 	sub_ret = findall_occurence(temp_text,'$ret :=')      #for replacing all '$ret' to 'return'
# 	# print(sub_ret)
# 	val=sub_ret[0]
# 	while val < len(temp_text):
# 		# print(val)
# 		j=val+len('$ret :=')
# 		temp_text = temp_text[:val]+'return'+temp_text[j:]
# 		# print(temp_text)
# 		sub_ret = findall_occurence(temp_text,'$ret :=')
# 		# print(sub_ret)
# 		if len(sub_ret)==0:
# 			break
# 		else:
# 			val=sub_ret[0]

# 	return temp_text

def func_call_clean2(text):
	func_call_text = re.findall(r'[FuncCall]+[(]+[^)]*[)]',text)
	new_call_text = [i.strip('FuncCall').strip('()') for i in func_call_text if 'FuncCall' in i]
	
	for i in range(len(new_call_text)):
		temp=new_call_text[i].split(",")
		temp[1:]=[i.strip().strip('()') for i in temp[1:]]
		# print(temp)
		new_call_text[i]='FuncCall('+temp[0]+'('+','.join(temp[1:])+'))'
	
	temp_text=text
	j=0
	# print(func_call_text)
	for i in range(len(func_call_text)):
		occ_list = findall_occurence(temp_text,func_call_text[i])
		# print(occ_list)
		index=occ_list[0]
		j=index+len(func_call_text[i])
		if temp_text[j]==')' and temp_text[j+1]==')' and temp_text[index-1]=='(':
			temp_text = temp_text[:index]+new_call_text[i]+temp_text[j+2:]
		elif temp_text[j]==')' and temp_text[j+1]==')' and temp_text[index-1]!='(':
			# print(temp_text[index-1])
			temp_text = temp_text[:index]+new_call_text[i]+temp_text[j+1:]
		else:
			temp_text = temp_text[:index]+new_call_text[i]+temp_text[j:]
		# temp_text = temp_text[:index]+new_call_text[i]+temp_text[j+1:]
	
	text=temp_text
	# print(text)
	# print()
	return text

def remove_substr(temp_text,substr):
	sub_ret = findall_occurence(temp_text,substr)      #for removing parts like StrAppend and StrFormat 
	# print(sub_ret)
	val=sub_ret[0]
	while val < len(temp_text):
		# print(val)
		j=val+len(substr)
		temp_text = temp_text[:val]+''+temp_text[j:]
		# print(temp_text)
		sub_ret = findall_occurence(temp_text,substr)
		# print(sub_ret)
		if len(sub_ret)==0:
			break
		else:
			val=sub_ret[0]
	
	return temp_text

# def strappend_strformat_clean(text):
	# temp_text=text
	# sub_ret = findall_occurence(temp_text,'StrAppend')      #for removing all StrAppend and StrFormat
	# # print(sub_ret)
	# val=sub_ret[0]
	# while val < len(temp_text):
	# 	# print(val)
	# 	j=val+len('StrAppend')
	# 	temp_text = temp_text[:val]+''+temp_text[j:]
	# 	# print(temp_text)
	# 	sub_ret = findall_occurence(temp_text,'StrAppend')
	# 	# print(sub_ret)
	# 	if len(sub_ret)==0:
	# 		break
	# 	else:
	# 		val=sub_ret[0]

	# sub_ret = findall_occurence(temp_text,'StrFormat')      #for removing all StrAppend and StrFormat
	# # print(sub_ret)
	# val=sub_ret[0]
	# while val < len(temp_text):
	# 	# print(val)
	# 	j=val+len('StrFormat')
	# 	temp_text = temp_text[:val]+''+temp_text[j:]
	# 	# print(temp_text)
	# 	sub_ret = findall_occurence(temp_text,'StrFormat')
	# 	# print(sub_ret)
	# 	if len(sub_ret)==0:
	# 		break
	# 	else:
	# 		val=sub_ret[0]
	# text=temp_text
	# # print(text)
	# return text
	
def ite_check(text):
	sub_ite = findall_occurence(text,'ite')
	sub_ite = [i+3 for i in sub_ite]
	# print(sub_ite)
	temp=""
	templist=[]
	p_match=0
	for i in sub_ite:
		while i<len(text):
			temp+=text[i]
			if text[i]=='(':
				p_match+=1
			elif text[i]==')':
				p_match-=1
			if p_match==0:
				# print(temp)
				templist.append(temp)
				temp=""
				break
			i+=1
	
	
	for i in range(len(templist)):  # for removing ite() outer brackets
		templist[i]=templist[i][1:]
		templist[i]=templist[i][:len(templist[i])-1]
		templist[i]=templist[i].strip()

	# print(templist)

	itelist=[]
	for i in range(len(templist)):
		p_match=0
		temp=""
		itelist.append([])
		for j in range(len(templist[i])):
			if templist[i][j]=='(':
				p_match+=1
			elif templist[i][j]==')':
				p_match-=1
			if templist[i][j]!=' ':
				temp+=templist[i][j]
			if p_match==0 and templist[i][j]==')':
				itelist[i].append(temp)
				temp=""
	# print(itelist)
	if itelist[0][0] != itelist[1][0]:
		print('Problem in condition of if-then-else statement')
		print('Change',itelist[0][0],'to',itelist[1][0])
		print()
	if itelist[0][1] != itelist[1][1]:
		# print('Problem in body of if-then-else statement')
		pcount=0
		temp=""
		bodylist=[[],[]]
		j=0
		for i in range(len(templist[0])): #incorrect part
			if templist[0][i]=='(':
				pcount+=1
			elif templist[0][i]==')':
				pcount-=1
			if pcount == 0 and templist[0][i]==',':
				bodylist[0].append(temp)
				temp=""
				j=i
			else:
				temp+=templist[0][i]
		bodylist[0].append(templist[0][j+1:])
		j=0
		temp=""
		for i in range(len(templist[1])): #correct part
			if templist[1][i]=='(':
				pcount+=1
			elif templist[1][i]==')':
				pcount-=1
			if pcount == 0 and templist[1][i]==',':
				bodylist[1].append(temp)
				temp=""
				j=i
			else:
				temp+=templist[1][i]
		bodylist[1].append(templist[1][j+1:])
		# print(bodylist)
		if bodylist[0][1]!=bodylist[1][1]:
			print('Problem in true block of ite')
			print('Change',bodylist[0][1],'to',bodylist[1][1])
			print()
		if bodylist[0][2]!=bodylist[1][2]:
			print('Problem in false block of ite')
			print('Change',bodylist[0][2],'to',bodylist[1][2])
			print()

	if itelist[0][0] == itelist[1][0] and itelist[0][1] == itelist[1][1]:
		print('unnecessary feedback')
	
	# print(itelist)


def feed_main(file,uncleaned_feedback):
	# feedInput = sys.stdin.readlines()
	func_names_list=feed_ini(file)
	# for i in feedInput:
	# uncleaned_feedback="Change '$out := ite(==(%(num', 2), 1), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' to '$out := ite(==(%(num', 2), 0), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' at the beginning of the function 'main' (cost=1.0)"
	# uncleaned_feedback=uncleaned_feedback[2:]
	# uncleaned_feedback="Change '$ret := /(FuncCall(fact, n), FuncCall(fact, +(n, r)))' to '$ret := /(FuncCall(fact, n), FuncCall(fact, -(n, r)))' at line 19 (cost=3.0)"
	# uncleaned_feedback="Change '$ret := /(FuncCall(fact, n), *(FuncCall(fact, r), FuncCall(fact, -(n, r))))' to '$ret := /(FuncCall(fact, n), *(FuncCall(fact, r), FuncCall(fact, -(n, r))))' at line 24 (cost=3.0)"
	# uncleaned_feedback="Change 'ncr_var := *(FuncCall(fact, n'), /(FuncCall(fact, r'), FuncCall(fact, -(n', r'))))' to 'ncr_var := /(FuncCall(fact, n'), *(FuncCall(fact, r'), FuncCall(fact, -(n', r'))))' at line 16 (cost=5.0)"
	# uncleaned_feedback="Change '$ret := /(FuncCall(fact, n), FuncCall(fact, +(n, r)))' to '$ret := /(FuncCall(fact, n), FuncCall(fact, -(n, r)))' at line 19 (cost=3.0)"
	# uncleaned_feedback="Change 'npr_var := /(FuncCall(fact, n'), FuncCall(fact, -(n', r')))' to 'npr_var := /(FuncCall(fact, n'), FuncCall(fact, -(n', r')))' at line 15 (cost=2.0)"
	# uncleaned_feedback="Change '$ret := ite(>(n, 0), 1, *(n, FuncCall(find_factorial, -(n, 1))))' to '$ret := ite(==(n, 0), 1, *(n, FuncCall(find_factorial, -(n, 1))))' at the beginning of the function 'find_factorial' (cost=2.0)"
	# uncleaned_feedback="Change 'avg := FuncCall(average, num1', num2')' to 'avg := FuncCall(average, num1', num2')' at line 15 (cost=1.0)"
	# uncleaned_feedback="Change 'ncr_var := *(FuncCall(fact, n'), /(FuncCall(fact, r'), FuncCall(fact, -(n', r'))))' to 'ncr_var := /(FuncCall(fact, n'), *(FuncCall(fact, r'), FuncCall(fact, -(n', r'))))' at line 16 (cost=5.0)"
	# uncleaned_feedback="Change 'next_term := ite(<=(i, 1), i, +(first_term, second_term))' to 'next_term := ite(<=(i, 1), i, +(first_term, count))' inside the body of the 'for' loop beginning at line 12 (cost=1.0)"
	# uncleaned_feedback="Change '$out := ite(==(%(num', 2), 1), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' to '$out := ite(==(%(num', 2), 0), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' at the beginning of the function 'main' (cost=1.0)"
	# uncleaned_feedback="Change '$ret := ite(>(n, 0), 1, *(n, FuncCall(find_factorial, -(n, 1))))' to '$ret := ite(==(n, 0), 1, *(n, FuncCall(find_factorial, -(n, 1))))' at the beginning of the function 'find_factorial' (cost=2.0)"
	# uncleaned_feedback = "Change '$out := ite(==(%(num', 2), 1), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' to '$out := ite(==(%(num', 2), 0), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' at the beginning of the function 'main' (cost=1.0)"
	# uncleaned_feedback = "Change '$out := ite(==(%(num', 2), 0), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')))' to '$out := ite(==(%(num', 2), 0), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an even number, num')), StrAppend(StrAppend($out, StrFormat(Enter an integer: )), StrFormat(%d is an odd number, num')))' at the beginning of the function 'main' (cost=1.0)"
	# uncleaned_feedback = "Change 'number := ite(>([](number, j), [](number, k)), ArrayAssign(number, j, [](number, j)), number)' to 'number := ite(>([](number, j), [](number, k)), ArrayAssign(ArrayAssign(number, j, [](number, k)), k, [](number, j)), number)' inside the body of the 'for' loop beginning at line 12 (cost=5.0)"
	# uncleaned_feedback = "Change '$cond := !=(%(i, j), 0)' to '$cond := ==(%(i, j), 0)' at line 20 (cost=1.0)"


	wrong_comma_list=wrong_comma_func(uncleaned_feedback,func_names_list)
	op_cleaned_feedback = cleaning_feedback3(uncleaned_feedback,wrong_comma_list)
	#legend_key_extract(uncleaned_feedback)     # may require later for complex feedback
	
	if 'FuncCall' in op_cleaned_feedback:
		op_cleaned_feedback = func_call_clean2(op_cleaned_feedback)
	
	if '$ret' in op_cleaned_feedback:
		# op_cleaned_feedback = return_clean(op_cleaned_feedback)
		op_cleaned_feedback = replace_substr(op_cleaned_feedback,'$ret :=','return')

	if 'StrAppend' in op_cleaned_feedback:
		# op_cleaned_feedback = strappend_strformat_clean(op_cleaned_feedback)
		op_cleaned_feedback = remove_substr(op_cleaned_feedback,'StrAppend')
		
	if 'StrFormat' in op_cleaned_feedback:
		op_cleaned_feedback = remove_substr(op_cleaned_feedback,'StrFormat')

	print(op_cleaned_feedback)

	if 'ite' in op_cleaned_feedback:
		ite_check(op_cleaned_feedback)
	else:
		# print(op_cleaned_feedback)
		# print()
		pass


# feed_main('p28_1_i.c',uncleaned_feedback) #calling the main feedback function