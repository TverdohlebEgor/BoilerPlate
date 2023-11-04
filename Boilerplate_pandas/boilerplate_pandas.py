from pandas import DataFrame,read_csv

class boilerplate_pandas(object):
    def __init__(self,columns : list = [], csv_path : str = None) -> None:
        if(not csv_path):
            self.columns = columns
            self.df = DataFrame(columns=columns)
            self.height = 0
        else:
            try:
                self.df = read_csv(csv_path,skipinitialspace=True,sep=None,engine="python")
            except Exception as e:
                print("Error catched while reading csv")
                print(e)
                exit(1)
            self.columns = list(self.df.columns)
            self.height = len(self.df.iloc[:,0])


    def append_row(self,row_dict : dict = {}):
        if(row_dict is None): row_dict = {}
        new_row = []
        for col in self.columns:
            if(col in row_dict.keys()):
                new_row.append(row_dict[col])
            else:
                new_row.append(None)
        self.df.loc[-1] = new_row
        self.df.index += 1 
        self.height += 1
        self.df = self.df.reset_index(drop=True)

    def delete_row(self,row_number : int):
        self.df = self.df.drop(row_number)
        self.df = self.df.reset_index(drop=True)

    def set_row(self,row_number : int, new_row : list):
        if(len(self.columns) != len(new_row)):raise Exception("La lista non è della lunghezza giusta")
        self.df.loc[row_number,:] = new_row

    def get_row(self,row_number : int):
        return list(self.df.loc[row_number,:])

    def append_column(self,column_name : str , column_content):
        if(self.height != len(column_content)):raise Exception("La nuova colonna non è della lunghezza giusta")
        self.df[column_name] = column_content

    def delete_column(self,column : str | int):
        if(type(column) is str):
            self.df.drop(column, axis=1, inplace=True)
        elif(type(column) is int):
            self.df.drop(self.df.columns[column], axis=1, inplace=True)

    def set_column(self,column : str | int , new_array : list):
        if(self.height != len(new_array)):raise Exception("La lista non è della lunghezza giusta")
        if(type(column) is str):
            self.df.loc[:,column] = new_array
        elif(type(column) is int):
            self.df.iloc[:,column] = new_array 
        else:
            raise TypeError("column must be sellected by a str or int")

    def get_column(self,column : str | int):
        if(type(column) is str):
            return list(self.df[column])
        elif(type(column) is int):
            return list(self.df.iloc[:,column]) 
        else:
            raise TypeError("column must be sellected by a str or int")
    
    def delete_cell(self,y : str | int,x : int,new_value):
        set_cell(y,x,None)

    def set_cell(self,y : str | int,x : int,new_value):
        if(type(y) is str):
            self.df.at[y,x] = new_value
        elif(type(y) is int):
            self.df.iat[y,x] = new_value
        else:
            raise TypeError("column must be a str or int")

    def get_cell(self,y : str | int,x : int):
        if(type(y) is str):
            return self.df.at[y,x]
        elif(type(y) is int):
            return self.df.iat[y,x] 
        else:
            raise TypeError("column must be a str or int")

    def set_matrix(self,
                  y_start : int,
                  y_end   : int,
                  x_start : int,
                  x_end   : int,
                  matrix_new_values :list):

        if(type(y_start) is not int or type(x_start) is not int or 
           type(y_end)   is not int or type(x_end)   is not int):raise TypeError("le cordinate devono essere interi")
        if(y_end <= y_start or x_end <= x_start):raise Exception("cordinate matrice non valide")
        if(y_end - y_start +1 != len(matrix_new_values)): raise Exception("La matrice da inserire e le cordinate devono essere della stessa dimensione")
        for l in matrix_new_values: 
            if(x_end - x_start +1 != len(l)): raise Exception("La matrice da inserire e le cordinate devono essere della stessa dimensione")

        self.df.iloc[y_start:y_end+1,x_start:x_end+1] = matrix_new_values

    def get_matrix(self,
                  y_start : int,
                  y_end   : int,
                  x_start : int,
                  x_end   : int,):
        if(type(y_start) is not int or type(x_start) is not int or 
           type(y_end)   is not int or type(x_end)   is not int):raise TypeError("le cordinate devono essere interi")
        if(y_end <= y_start or x_end <= x_start):raise Exception("cordinate matrice non valide")

        return self.df.iloc[y_start:y_end+1,x_start:x_end+1]

    def to_csv(self,csv_path : str = ""):
        self.df.to_csv(csv_path)

if __name__ == "__main__":
    test = boilerplate_pandas(["Prova","B"])
    test.append_row({"Prova" : 1})
    test.append_row({"Prova" : 2,"B" : "YEAHS"})
    test.append_row({"Prova" : 3,"B" : "YEAHS"})
    test.append_row({"Prova" : 4,"B" : "YEAHS"})
    test.append_row({"Prova" : 5,"B" : "YEAHS"})
    test.append_column("Test", [-1,-1,-1,-1,-1])
    test.to_csv("test.csv")
