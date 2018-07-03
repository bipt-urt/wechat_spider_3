import re
def convert(_content):
	res = ""
	ignore = False
	for letter in _content:
		if ignore:
			if letter == ">":
				ignore = False
		else:
			if letter == "<":
				ignore = True
			else:
				res += letter
	restr =''
	try:
		co = re.compile(u'[\U00010000-\U0010ffff]')
	except re.error:
		co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
	res = co.sub(restr, res)
	return res

def main():
	with open("target.txt", "r", encoding="gb2312") as f:
		content = f.read()
		print(convert(content))

if __name__ == "__main__":
	main()