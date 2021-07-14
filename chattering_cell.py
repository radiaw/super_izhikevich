import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.C = 50
        self.k = 1.5
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
     
#%%
if __name__ == "__main__":
    myCell = cCell(4000)
    myCell.simulate()
    izh.plotMyData(myCell)