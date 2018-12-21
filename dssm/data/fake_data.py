import numpy as np
import pickle
from scipy.sparse import coo_matrix

query_test_data = coo_matrix((10240, 49284), dtype=np.int64)
doc_test_data = coo_matrix((10240, 49284), dtype=np.int64)

doc_train_data = coo_matrix((2048000, 49284), dtype=np.int64)
query_train_data = coo_matrix((2048000, 49284), dtype=np.int64)

qtd = open('query.test.pickle', 'wb+')
dtd = open('doc.test.pickle', 'wb+')
qtr = open('query.train.pickle', 'wb+')
dtr = open('doc.train.pickle', 'wb+')

pickle.dump(query_test_data, qtd)
pickle.dump(doc_test_data, dtd)
pickle.dump(query_train_data, qtr)
pickle.dump(doc_train_data, dtr)