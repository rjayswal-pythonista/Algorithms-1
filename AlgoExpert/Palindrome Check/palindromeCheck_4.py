
# O(n) time | O(1) space

def isPalindrome(string):
	leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return false
		leftIdx += 1
		rightIdx -= 1
	return True