string = 'X-DSPAM-Confidence: 0.8475'
start = string.find(':') + 2
end = len(string)
print(float(string[start:end]))