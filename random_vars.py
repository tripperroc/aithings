import pandas as pd
import numpy as np

arrays1 = [np.array(['true', 'true', 'true', 'true', 'false', 'false', 'false', 'false']),
	np.array(['true', 'true', 'false', 'false','true', 'true', 'false', 'false']),
	np.array(['true','false','true','false','true','false','true','false'])]

index1 = pd.MultiIndex.from_arrays(arrays1, names=('A', 'B', 'C'))

arrays2 = [np.array(['true', 'true', 'false', 'false']),
	np.array(['true', 'false', 'true', 'false'])]

index2 = pd.MultiIndex.from_arrays(arrays2, names=('D', 'E'))
vals = np.random.rand(8,4)
vals = vals/vals.sum()
s = pd.DataFrame(vals, index=index1, columns=index2)

s.to_html("random_vars", float_format='%.3f')