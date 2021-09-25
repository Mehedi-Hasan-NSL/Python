# super class
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("w ",width)
        print("h ",height)
# child class
class FlowerImage(Image):
    def __init__(self, width, height, flower_name):
        # super class can its inhereited parent
        self.flower_name = flower_name 
        super().__init__(width, height)         
        pass

flower = FlowerImage(256, 256, "rose")