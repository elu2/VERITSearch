import pandas as pd

# Only line that needs to be changed
query_list = []
# Turns all entries into lower case
case_proof = [x.lower() for x in query_list]

# Load in necessary pd.DataFrames
full_df = pd.read_pickle("./databases/combinedDBs.pkl")
nodes = pd.read_pickle("./databases/nodes_table_all_labelled.pkl")


def name_query(name):
    # Note: this searches the df for the query name anywhere
    name_query = full_df.query('name.str.contains(@name, na=False)', engine='python').reset_index(drop=True)

    # The following nodes are in the network, but REACH likely grounds to more
    in_net = pd.merge(nodes, name_query, left_on="Only_Id", right_on="id", how="inner").iloc[:, 3:5].drop_duplicates().reset_index(drop=True)
    in_net["user_query"] = name
    return in_net


def multi_query(query_list):
    # initialize empty dataframe
    full_query = pd.DataFrame()

    for query in query_list:
        full_query = full_query.append(name_query(query))

    return full_query


if __name__ == "__main__":
    multi_query(case_proof).to_csv("multiSearchOut.csv", index=False)
