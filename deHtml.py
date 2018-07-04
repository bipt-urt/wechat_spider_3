import re
import io
import sys
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
	return res
def main():
	with open("target.txt", "r", encoding="gb2312") as f:
		content = f.read()
	co = re.compile(u'[\u2100-\u214F][\u0E01-\u0E5B][\u20A0-\u20CF][\u3300-\u33FF]')#[\uD800-\uDBFF][\uDC00-\uDFFF]
	co2 = re.compile(u'[\U00010000-\U0010ffff]')
	co3 = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF][\uFE70-\uFEFF]')
	res = co.sub(restr, res)
	res = co2.sub(restr, res)
	res = co3.sub(restr, res)
if __name__ == "__main__":
	main()