import pandas as pd
def table_cleaner(File_path,NumberOfTeams):
    T,P,S=7, 8, 6
	#Raw data
    text=pd.read_csv(File_path)
	
	#extracting team names and storing them in a list
    Teams = text.iloc[[8*x - T for x in range(1, NumberOfTeams+1)]] 
    
	#Extracting team position numbers and storing them in a list
    Position = text.iloc[[8*x - P for x in range(1, NumberOfTeams+1)]] 

	#Extracting PTS, MP, W, L, D, GF, GA and GD which is in a format PTS\tMP\tW\tL\tD\tGF\tGA\tGD\t
    Stats=text.iloc[[8*x - S for x in range(1, NumberOfTeams+1)]] 

	#Extracting values from Stats and saving them into a readable data frame
    df = pd.DataFrame([[int(x) for x in s.split('\t') if x.strip()] for s in Stats['Team\tPTS\tMP\tW\tL\tD\tGF\tGA\tGD\tLast 5'] if s.strip() and s.split('\t')[0].lstrip('-').isdigit()], columns=['PTS', 'MP', 'W', 'L', 'D', 'GF', 'GA', 'GD'])
        
	#Copying df and pasting it in df1
    df1=df.copy()
 
	#Adding Position number column and placing it on column 1
    df1.insert(0, 'Position', Position.sort_index()['Team\tPTS\tMP\tW\tL\tD\tGF\tGA\tGD\tLast 5'].tolist())

	#Adding team name column and placing it on column 2
    df1.insert(1, 'Teams', Teams.sort_index()['Team\tPTS\tMP\tW\tL\tD\tGF\tGA\tGD\tLast 5'].tolist())
    
    return df1
