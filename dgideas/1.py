import urllib.request
import http.cookiejar

def main():
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')]
	urllib.request.install_opener(opener)
	# 然后正常使用urllib.urlopen().read()等即可，不需要使用任何特殊方法

if __name__ == "__main__":
	main()