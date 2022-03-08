class Game(object):
    """
        bowling class implemented

    """
    STRIKE = 'X'
    SPARE = '/'
    # to not score extra moves available at the end in case of strike or spare
    EXTRA_STRIKE_MOVES = 2
    EXTRA_SPARE_MOVES = 1
    MINIMUM_CHANCE = 12
    MAXIMUM_CHANCE = 21

    def __init__(self, throw_string=None):
        """
        :throw_string: string where each character
        represents a throw
        :counter integer to make sure that the throw is between 12 to 21
        character
        """
        self.number_of_chances = 0
        self.throw = throw_string
        self.counter = 20

    @property
    def throw(self):
        return self._throw

    @throw.setter
    def throw(self, value):
        self._throw = []
        if value:
            if len(value) < self.MINIMUM_CHANCE or len(value) > self.MAXIMUM_CHANCE:
                raise Exception("Invalid input throw string entered")
            self._throw = list(value)
        self.number_of_chances = len(self._throw)

    def is_valid_input(self, value):
        is_valid = False
        if value.isdigit():
            is_valid = True
        elif value == self.STRIKE or value == self.SPARE:
            is_valid = True
        return is_valid

    def is_valid_throw(self, value):
        """
         TODO: implementation
        """
        pass


    @property
    def score(self):
        total_score = 0
        for index, move in enumerate(self.throw):
            if self.is_valid_input(move):
                if move == self.STRIKE:
                    total_score += self.get_move_value('X') + self.get_strike_bonus(
                        index)
                elif move == self.SPARE:
                    total_score += (
                        self.get_move_value('/') + self.get_spare_bonus(index) -
                        self.get_prev_roll(index)
                    )
                else:
                    total_score += int(move)
        return total_score

    def get_spare_bonus(self, index):
        """
        :return: spare bonus
        """
        return (
            self.get_move_value(self.throw[index+1]) if
            self.number_of_chances > index+self.EXTRA_SPARE_MOVES+1 else 0
        )

    def get_strike_bonus(self, index):
        """
            calculation of strike bonus
        """
        if self.number_of_chances > index+self.EXTRA_STRIKE_MOVES+1:
            next_roll = self.throw[index+1]
            next_next_roll = self.throw[index+2]
            if next_next_roll == '/':
                return self.get_move_value('/')
            else:
                return self.get_move_value(next_roll) + self.get_move_value(
                    next_next_roll)
        else:
            return 0

    def get_move_value(self, move):
        """
        :return: score of a particular move
        """
        return 10 if move == self.STRIKE or move == self.SPARE else int(move)


    def get_prev_roll(self, index):
        """
        :param index: current index
        :return: previous roll score
        """
        if index > -1:
            return self.get_move_value(self.throw[index-1])
        else:
            return 0

    def play_real(self, move):
        """
         This function takes an move as argument and display the score of the game
        :param move: knock down value
        :return: current game score
        """
        if self.counter > 0:
            if len(move) > 1 or not self.is_valid_input(move):
                print 'Bad Input!!  Enter again'
            else:
                self.throw.append(move)
                self.number_of_chances = len(self.throw)
                self.counter -= 1
                if move == self.STRIKE:
                    if self.counter > 3:
                        self.counter -= 1
            print 'Score is {} '.format(self.score)
        else:
            print 'Play Again!!Previous Game Score {}'.format(self.score)


if __name__ == '__main__':
    print '{} score is {}'.format('XXXXXXXXXXXX', Game('XXXXXXXXXXXX').score)
    print '{} score is {}'.format('90909090909090909090', Game('90909090909090909090').score)
    print '{} score is {}'.format('5/5/5/5/5/5/5/5/5/5/5', Game('5/5/5/5/5/5/5/5/5/5/5').score)
    print '{} score is {}'.format('X7/729/XXX236/7/3', Game('X7/729/XXX236/7/3').score)
    print '{} score is {}'.format('00000000000000000000', Game('00000000000000000000').score)
    print '{} score is {}'.format('01273/X5/7/345400X70', Game('01273/X5/7/345400X70').score)
    print '{} score is {}'.format('X7/90X088/06XXX81', Game('X7/90X088/06XXX81').score)
    print '{} score is {}'.format('X7/729/XXX236/7/3', Game('X7/729/XXX236/7/3').score)



