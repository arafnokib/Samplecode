import pandas as pd


#Function to convert data files into csvs


class csv_converter():
    def anime_convertcsv(self,list1, list2, list3):
        d1 = pd.DataFrame({
            'name': list1,
            'episode_num': list2,
            'time_posted': list3,
        })
        d1.to_csv('animedata.csv')