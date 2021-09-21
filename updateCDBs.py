# Use this script after speciesLabelling.py from REACHVisualization

import pandas as pd
import numpy as np
import pickle

nodes_table = pd.read_pickle("databases/nodes_table_all_labelled.pkl")
cdb = pd.read_pickle("databases/combinedDBs.pkl")

nodes_table_d = nodes_table.drop(columns=["Id"])
nodes_table_d = nodes_table_d.rename(columns={"Label": "name", "Only_Id": "id"})
proper = pd.concat([cdb, nodes_table_d]).drop_duplicates().reset_index(drop=True)
proper
pickle.dump(proper, open("databases/combinedDBs.pkl", "wb"))
