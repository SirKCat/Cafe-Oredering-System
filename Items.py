
import DB


class Items:

    # Constructor of Items
    def __init__(self, ID, name, price, category, description):
        self.name = name
        self.ID = ID
        self.price = price
        self.category = category
        self.description = description

    # get a specific item from the DB creats an instance of class Items according to the data retrieved
    @staticmethod
    def retrieve(num):
        output = DB.getItem(num)[0]
        return Items(output[0], output[1], output[2], output[3], output[4])
        # return

    # get all items from the DB creat a list of instances of class Items according to the data retrieved
    @staticmethod
    def retrieveAll():
        output = DB.getItems()
        # x = ([Items(item[0], item[1], item[2], item[3]) for item in output])
        # for i in x:
        #     print(i.name)
        return [Items(item[0], item[1], item[2], item[3], item[4]) for item in output]
