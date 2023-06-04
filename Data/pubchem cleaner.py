data = []
with gzip.open(curr_dir+'/CID-SMILES.gz', 'r') as f:
  for line in f:
    data.append(line.split()[1])

with open(curr_dir+'/smiles_pubchem112m.txt', 'w')as f:
    for d in data:
        f.write(d+'\n')