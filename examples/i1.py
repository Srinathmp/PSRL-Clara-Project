def computeDeriv(poly):
  new = []
  for i in range(1,len(poly)):
    new.append(
        (i*poly[i]))
  if new==[]:
    return 0.0
  return new
