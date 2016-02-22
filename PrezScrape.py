import datetime
import json
import re
import string
import nltk
from collections import Counter

stopwords = set(nltk.corpus.stopwords.words('english'))
regex = re.compile('[%s]' % re.escape(string.punctuation))


def getDate(dateString):
	return datetime.datetime.strptime(dateString, "%B %d, %Y").date()

def makeSpeakerDic(unfilt):
	res = re.search("[A-Z]+: ", unfilt, re.DOTALL)
	dic = {}
	text = unfilt[res.end():]
	name = unfilt[res.start():res.end()-2].lower()
	nextRes = re.search("[A-Z]+: ", text, re.DOTALL)
	while nextRes:
		if name not in dic:
			dic[name] = []
		dic[name].append(text[:nextRes.start()])
		name = text[nextRes.start():nextRes.end()-2].lower()
		text = text[nextRes.end():]
		res = nextRes
		nextRes = re.search("[A-Z]+: ", text, re.DOTALL)

	return dic

debateDict = {}
with open('debates.json', 'r') as infile:
	debateDict = json.load(infile)
	debateDict = {tuple(key.split("|")): value
				for key, value in debateDict.items()}


sortedKeys = sorted(debateDict.keys(), key=lambda x: getDate(x[1]), reverse=True)
lastDemDebate = debateDict[sortedKeys[1]]
debateDic = makeSpeakerDic(lastDemDebate)

def tokenize(resp):
	cleaned = string.replace(resp, "[applause]", "")
	tokens = [token for token in nltk.word_tokenize(cleaned)
				if token.lower() not in stopwords and
					token.lower() != "applause"]
	return tokens


def candidateString(name, dict_):
	return regex.sub(''," ".join(dict_[name]))

def tokenizeCandidate(name, dict_):
	return tokenize(candidateString(name, dict_))

def getCounts(tokens):
	counts = Counter(tokens)
	return sorted(counts.items(), key=lambda (k,v): v, reverse=True)

BernieTokens = tokenizeCandidate('sanders', debateDic)
HilaryTokens = tokenizeCandidate('clinton', debateDic)

BernieCounts = getCounts(BernieTokens)
hilaryCounts = getCounts(HilaryTokens)
