class Layer:
     def __init__(self, name):
        self.name = name
 
     def __call__(self):
        print("layer "+self.name+" is called")
        pass

layer = Layer("custom layer")
print(layer())
#y = layer(image)