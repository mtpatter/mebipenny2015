import sys
import itertools

## Given a wardrobe, print the unique outfits that can be put together

## Input: Each line of the input will be a space separated list of items for one
## position on the body.

## Output: Each line of output should represent one outfit, combining one item of each
## type (space separated). Outfits and outfit items should preserve the input
## orderings.


def process(line):
  # Process each line of input here
  return line

lines = sys.stdin.readlines()
sections = [ x.strip() for x in lines]
cgroups = []
for section in sections:
    section = section.split()
    cgroups.append(section)
lengroups = [len(x) for x in cgroups]

indices = []
for item in lengroups:
   indices.append(range(item))    
   iters = list(itertools.product(*indices))
for combo in iters:
   numitems = len(combo)
   #for x in range(numitems):
   result = [cgroups[x][combo[x]] for x in range(numitems)] 
   print ' '.join(result)


