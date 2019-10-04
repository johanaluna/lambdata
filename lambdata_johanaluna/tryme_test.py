import unittest
import pandas as pd
from tryme2 import Check_Data

class Check_Data_test(unittest.TestCase):

    def test_nulls(self):
        listdata = [['tom', 10,0], ['nick', 15,1],
        ['juli', 14,1],['sebastian', 10,0],['dfs', 10,0],
        ['isa', 34,1],['lucy', 15,0]]
        data = pd.DataFrame(listdata, columns = ['Name', 'Age','Sex'])
        target='Sex'
        nulls_out=data.isnull().sum().sort_values(ascending=False)
        tryme2_go= Check_Data(data,target)
        self.assertIsNotNone(nulls_out,tryme2_go.reportnulls())

    # def test_split(self):
    #     listdata = [['tom', 10,0], ['nick', 15,1],
    #     ['juli', 14,1],['sebastian', 10,0],['dfs', 10,0],
    #     ['isa', 34,1],['lucy', 15,0]]
    #     data = pd.DataFrame(listdata, columns = ['Name', 'Age','Sex'])
    #     target='Sex'
    #     nulls_out=data.isnull().sum().sort_values(ascending=False)
    #     tryme2_go= Check_Data(data,target)
    #     self.assertIsNotNone(nulls_out,tryme2_go.reportnulls())

if __name__ == '__main__':
    unittest.main()
