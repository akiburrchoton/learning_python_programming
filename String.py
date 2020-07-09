text = "X-DSPAM-Confidence:    0.8475";
pos = text.find("0")
r = text[pos:]
number = float(r)
print(number)