
# O(n) time | O(n) space

def isPalindrome(string, i = 0):
	j = len(string) - 1 - i
	return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)



#tail Recursive


def isPalindrome(string, i = 0):
	j = len(string) - 1 - i
	if i >= j:
		return True
	if string[i] != string[j]:
		return False
		return isPalindrome(string, i + 1)