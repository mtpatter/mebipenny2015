import sys

## Convert to roman numerals

def process(line):
  # Process each line of input here
  remainder500 = int(line) % 500
  numD = (int(line) - remainder500)/500
  numM = numD / 2
  if numD == 1:
    result1 = 'M'*numM+'D'
  else:
    result1 = 'M'*numM
 
  remainder50 = remainder500 % 50
  numL = (remainder500 - remainder50) / 50
  numC = numL / 2
  numL2 = numL % 2
  if numC == 4:
      result2 = 'CM' + 'L'*numL2
  else: 
      result2 = 'C'*numC + 'L'*numL2

  remainder5 = remainder50 % 5
  numV = (remainder50 - remainder5) / 5
  numX = numV / 2
  numV2 = numV % 2
  if numX == 4:
      result3 = 'XL' + 'V'*numV2
  else:
      result3 = 'X'*numX + 'V'*numV2

  if remainder5 == 4:
      result4 = 'IV'
  else:
      result4 = 'I'*remainder5

  return str(result1 + result2 + result3 + result4)

lines = sys.stdin.readlines()

processed = map(process, lines)
for line in processed:
    print line.strip()

