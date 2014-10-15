def reverseWords(s):
	a = s.split(' ');
	r = [];
	for ss in a:
		if len(ss) > 0:
			r.append(ss);
	if len(r) > 0:
		r.reverse();
	return ' '.join(r);

s = "   the sky is blue"
s2 = " "
print '"' + reverseWords(s2) + '"';