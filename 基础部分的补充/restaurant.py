class Restaurant():

    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("reataurant's name is "+self.restaurant_name.title())
        print("餐厅主要烹饪类型是%s"%self.cuisine_type)

    def open_restaurant(self):
        print("%s正在营业..."%self.restaurant_name)


    def set_number_served(self):
        print("This restaurant has " + str(self.number_served) + "客人")

    def increment_number_served(self,number):
        self.number_served+=number

restaurant=Restaurant('he颜悦色','西餐',0)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served=23
restaurant.set_number_served()

restaurant.increment_number_served(12)
restaurant.set_number_served()