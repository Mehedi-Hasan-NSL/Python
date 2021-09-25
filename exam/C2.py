class LaptopBrand:
    def __init__(self):
         self.name = {}

    # populating the dictionary
    def __setitem__(self, index, value):
        self.name[index] = value

    # getting the value from our custom_list
    def __getitem__(self, index):
        return "{} : {}".format(index, self.name[index])


laptopBrand = LaptopBrand()

laptopBrand[0] = 'DELL'
laptopBrand[1] = 'HP'

print(laptopBrand[0])
print(laptopBrand[1])


