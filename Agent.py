class Agent(object):
    def __init__(self, id):
        self.id = id

    def wanna_build_house(self, game_state):
        print("Player ", self.id, " wanna build house? Press Y to yes and N to no")
        return True if str(raw_input()).lower()=="y" else False

    def wanna_build_hotel(self, game_state):
        print("Player ", self.id, " wanna build hotel? Press Y to yes and N to no")
        return True if str(raw_input()).lower()=="y" else False

    def wanna_trade(self, game_state):
        print("Player ", self.id, " wanna trade? Press Y to yes and N to no")
        return True if str(raw_input()).lower()=="y" else False

    def wanna_mortgage(self, game_state):
        print("Player ", self.id, " wanna mortgage? Press Y to yes and N to no")
        return True if str(raw_input()).lower() == "y" else False

    def build_house(self, game_state):
        """
        return the box number where you wanna build house
        :param game_state:
        :return:
        """
        print("Player %s give the position of the box where you wanna build house "%(self.id, ))
        return int(raw_input())

    def wanna_sell_house(self, game_state):
        print("Player ", self.id, " wanna sell house? Press Y to yes and N to no")
        return True if str(raw_input()).lower()=="y" else False

    def sell_house(self, game_state):
        """
        return the box number where you wanna SELL house
        :param game_state:
        :return:
        """
        print("Player %s give the position of the box where you wanna SELL house "%(self.id, ))
        return int(raw_input())

    def mortgage(self, game_state):
        """
        return the box number which you wanna mortgage
        :param game_state:
        :return: box_number
        """
        print("Player %s give the position of the box which you wanna mortgage " % (self.id,))
        return int(raw_input())


    def wanna_buy(self, game_state, current_box):
        print("Player %s , do u wanna buy your current box %s. Press Y to confirm" % (self.id, current_box.display_name))
        return True if str(raw_input()).lower() == "y" else False