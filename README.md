## README
dbCombiner only used when incorporating more databases. All files are databases channeled into combineDBs.pkl.

Searches the nodes table for the query name anywhere (hence str.contains)
Does not handle when a user tries to query with an ID because that is already handled.

CanDo:
Could cut down on space by curling the tsv files and pickling the full df locally via dockerfile entrypoint.
Current method saves time but not space. (With provided combinedDBs.pkl)