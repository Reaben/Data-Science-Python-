import pandas as pd
import matplotlib.pyplot as plt
class Overall_report:
    def __init__(self,df,Spacing=80):
        self.df=df
        self.Spacing=Spacing
        self.df['Position'] = pd.to_numeric(self.df['Position'])
        self.n=len(self.df)
        self.Means=self.df[['PTS', 'W', 'L', 'D', 'GF', 'GA', 'GD']].mean()
    
    def ValtoMean(self,Val,Average,Subject):
        outcome="incomparible to"
        if Val>Average:
            outcome=f"{Val-Average:.0f} {Subject} more than average ({Average:.0f})"
        elif Val==Average:
            outcome=f"same {Subject} as average"
        else:
            outcome=f"{Average-Val:.0f} {Subject} less than average ({Average:.0f})"
        return outcome
    
    def Display_table(self):
        df=self.df
        print("="*self.Spacing)
        print(df)
        
    def Top(self):
        df=self.df
        Top_number=int(input("Enter number: "))
        for i in range(1,4):
            print("="*self.Spacing)
            print("\n")
        print(f"\t\t\t\t\t\t\tTop {Top_number}.")
        print("="*self.Spacing)
        print(df[df["Position"]<=Top_number])
        
    def Bottom(self):
        df=self.df
        Bottom_number=int(input("Enter number: "))
        print("="*self.Spacing)
        print(df[df["Position"]>Bottom_number])
        
    def Team_statistics(self):
        ValtoMean=Overall_report(self.df).ValtoMean
        df=self.df
        Means=self.Means
        Name_of_team=str(input("Enter name of Team: "))
        #TeamStats=DF[DF["Teams"]==Name_of_team]
        team_data = df[df['Teams'] == Name_of_team].iloc[0]
        print("="*self.Spacing)
        print(f'Points.\n{Name_of_team} obtained {team_data["PTS"]} points, which is {ValtoMean(team_data["PTS"],Means["PTS"],"points")} and dropped {6*(self.n-1)-team_data["PTS"]} points')
        
        # Assuming team_data and Name_of_team are already defined
        # Assume team_data and Name_of_team are defined
        labels = ['Wins', 'Losses', 'Draws']
        colors = ['#2ecc71', '#e74c3c', '#f1c40f']
        sizes = [team_data['W'], team_data['L'], team_data['D']]

        # Create subplots: 1 row, 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # ----- Main heading (centered at top of figure) -----
        fig.suptitle(f'{Name_of_team} – Wins, Draws, and Losses', fontsize=16, fontweight='bold')

        # ----- Left subplot: Doughnut chart -----
        wedges, texts, autotexts = ax1.pie(sizes, labels=labels, colors=colors,
                                           autopct='%1.1f%%', startangle=90,
                                           wedgeprops=dict(width=0.4))
        centre_circle = plt.Circle((0, 0), 0.6, fc='white', linewidth=0)
        ax1.add_artist(centre_circle)
        ax1.text(0, 0, f'{Name_of_team}', ha='center', va='center', fontsize=12, fontweight='bold')
        ax1.set_title('Distribution (Doughnut)')           # subplot title
        ax1.axis('equal')

        # ----- Right subplot: Bar chart -----
        categories = ['Wins', 'Draws', 'Losses']
        values = sizes.copy()   # [wins, draws, losses]
        bar_colors = ['#2ecc71', '#f1c40f', '#e74c3c']
        bars = ax2.bar(categories, values, color=bar_colors, edgecolor='black', linewidth=1.2)

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                     f'{int(height)}', ha='center', va='bottom', fontsize=12)

        ax2.set_title('Counts (Bar Chart)')                # subplot title
        ax2.set_ylabel('Count')
        ax2.set_ylim(0, max(values) + 3)
        ax2.grid(axis='y', linestyle='--', alpha=0.7)

        # Adjust layout so suptitle doesn't overlap
        plt.tight_layout()
        plt.subplots_adjust(top=0.88)   # leave room for the main title
        plt.show() 
       
    def Recommendation(self):
        df=self.df
        
    def Team_status(self):
        n=self.n
        df=self.df
        Name_of_team=str(input("Enter name of Team: "))
        #Team data
        td = df[df['Teams'] == Name_of_team].iloc[0]
        if n<=16:
            if n==15:
                if td["MP"]<2*(n-1):
                    if td["Position"]==1:
                        print(f"Current leader  and qualifies for CAF Champions league and top 8 tournament")
                    elif td["Position"]>1 and td["Position"]<3:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for CAF Champions league and top 8 tournament")
                    elif td["Position"]>2 and td["Position"]<4:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for CAF Confederations and top 8 tournament")
                    elif td["Position"]>4 and td["Position"]<9:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for top 8 tournament and does not qualify for continental football")
                    elif td["Position"]>9 and td["Position"]<15:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football.")
                    else:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football and facing play offs")
                else:
                    if td["Position"]==1:
                        print(f"Champion and qualified for CAF Champions league and top 8 tournament")
                    elif td["Position"]>1 and td["Position"]<3:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for CAF Champions league and top 8 tournament")
                    elif td["Position"]>2 and td["Position"]<4:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for CAF Confederations and top 8 tournament")
                    elif td["Position"]>4 and td["Position"]<9:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for top 8 tournament and does not qualify for continental football")
                    elif td["Position"]>9 and td["Position"]<15:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football.")
                    else:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football and facing play offs")
            else:
                if td["MP"]<2*(n-1):
                    if td["Position"]==1:
                        print(f"Current leader  and qualifies for CAF Champions league and top 8 tournament")
                    elif td["Position"]>1 and td["Position"]<3:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for CAF Champions league and top 8 tournament")
                    elif td["Position"]>2 and td["Position"]<4:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for CAF Confederations and top 8 tournament")
                    elif td["Position"]>4 and td["Position"]<9:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for top 8 tournament and does not qualify for continental football")
                    elif td["Position"]>9 and td["Position"]<15:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football.")
                    else:
                        print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football and facing play offs")
                else:
                    if td["Position"]==1:
                        print(f"Champion and qualified for CAF Champions league and top 8 tournament")
                    elif td["Position"]>1 and td["Position"]<3:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for CAF Champions league and top 8 tournament")
                    elif td["Position"]>2 and td["Position"]<4:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for CAF Confederations and top 8 tournament")
                    elif td["Position"]>4 and td["Position"]<9:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for top 8 tournament and does not qualify for continental football")
                    elif td["Position"]>9 and td["Position"]<15:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football.")
                    elif td["Position"]==15:
                        print(f"Number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for top 8 tournament and or continental football and facing play offs")
                    else:
                        print(f"Religated at number {td['Position']} on the log table, with {td['PTS']} points.")
                        
        else:
            if td["MP"]<2*(n-1):
                if td["Position"]==1:
                    print(f"Current leader  and qualifies for UEFA Champions league and Shield.")
                elif td["Position"]>1 and td["Position"]<5:
                    print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for UEFA Champions league.")
                elif td["Position"]==5:
                    print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for UEFA Europa League.")
                elif td["Position"]==6:
                    print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and qualifies for UEFA Europa Conference League.")
                elif td["Position"]>6 and td["Position"]<18:
                    print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for continental football.")
                else:
                    print(f"Current number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for continental football and facing relegation.")
            else:
                if td["Position"]==1:
                    print(f"Champion and qualified for UEFA Champions league and Shield.")
                elif td["Position"]>1 and td["Position"]<5:
                    print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for UEFA Champions league and top 8 tournament.")
                elif td["Position"]==5:
                    print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for UEFA Europa League and top 8 tournament.")
                elif td["Position"]==6:
                    print(f"Number {td['Position']} on the log table, with {td['PTS']} points and qualified for UEFA Europa Conference League.")
                elif td["Position"]>6 and td["Position"]<18:
                    print(f"Number {td['Position']} on the log table, with {td['PTS']} points and does not qualify for continental football.")
                else:
                    print(f"Religated at number {td['Position']} on the log table, with {td['PTS']} points.")
