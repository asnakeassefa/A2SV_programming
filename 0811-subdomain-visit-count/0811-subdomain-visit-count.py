class Solution:
	def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
		answer = defaultdict(int)
		final = []
		for domains in cpdomains:
			sepDomain = domains.split(' ')
			num = int(sepDomain[0])
			url = sepDomain[1].split('.')
			length = len(url) - 1
			temp = ""
			for i in range(length,-1,-1):
				if temp == "":
					answer[url[i]] += num
					temp = "." + url[i]
				elif i == 0:
					temp = url[i] + temp
					answer[temp] += num
				else:
					temp = url[i]+temp
					answer[temp] += num
					temp = "." + temp
		for key,val in answer.items():
			final.append(str(val) + " " + key)
            
		return final