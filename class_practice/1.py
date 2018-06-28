from math import pow
def isInCircle(x, y, circleX, circleY, circleR):
	return (pow(circleX-x, 2)+pow(circleY-y,2)) == pow(circleR, 2)

def main():
	for x in range(30):
		for y in range(30):
			if isInCircle(x, y, 15, 15, 7):
				print("*", end="")
			else:
				print(" ", end="")
		print("\n")

if __name__ == "__main__":
	main()