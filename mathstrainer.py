import random
import argparse
from timeit import default_timer as timer


class MathsTrainer(object):

    def __init__(self, multiplication=100, addition=10000, loss=2, gain=1, time=60):
        """
        :param multiplication: largest multiplication question
        :param addition: largest addition question
        :param loss: points lost for each wrong answer
        :param gain: points gained for each correct answer
        :param time: time taken
        """

        self.score = 0
        self.multiplication = multiplication
        self.addition = addition
        self.gain = gain
        self.loss = loss
        self.time = time
        self.score_history=[0]

    def wrong(self):
        """
        Reduces score for incorrect answer
        :return:
        """
        self.score -= self.loss
        self.score_history.append(self.score)

    def correct(self):
        """
        Increments score for correct answer
        :return:
        """
        self.score += self.gain
        self.score_history.append(self.score)

    def multiply_q(self):
        """
        Asks a multiplication question to the user
        :return:
        """
        x = random.randint(0, self.multiplication)
        y = random.randint(0, self.multiplication)
        while True:
            a = input('{} * {} = ? \n'.format(x, y))
            if int(a) == x * y:
                self.correct()
                return
            self.wrong()

    def addition_q(self):
        """
        Asks an addition question to the user
        :return:
        """
        x = random.randint(0, self.addition)
        y = random.randint(0, self.addition)
        while True:
            a = input('{} + {} = ? \n'.format(x, y))
            if int(a) == x + y:
                self.correct()
                return
            self.wrong()

    def division_q(self):
        """
        Asks a division question to the user
        :return:
        """

        x = random.randint(0, self.multiplication)
        y = random.randint(0, self.multiplication)
        while True:
            a = input('{} / {} = ? \n'.format(x * y, y))
            if int(a) == x:
                self.correct()
                return
            self.wrong()

    def subtraction_q(self):
        x = random.randint(0, self.addition)
        y = random.randint(0, self.addition)
        while True:
            a = input('{} - {} = ? \n'.format(x+y , y))
            if int(a) == x:
                self.correct()
                return
            self.wrong()

    def run_questions(self):
        """
        Asks a series of questions to the user
        :return:
        """

        start = timer()
        time_left = self.time
        while time_left > 0:
            print( '{} Seconds Left'.format(int(time_left)))
            q = random.randint(0, 4)
            if q == 0:
                self.addition_q()
            if q == 1:
                self.multiply_q()
            if q ==2:
                self.division_q()
            if q==3:
                self.subtraction_q()
            end = timer()
            time_left = start + self.time - end
        print('Congratulations')
        print('Score = {}'.format(self.score))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Train Mental Arithmetic')
    parser.add_argument('--mult', metavar='N', type=int,default=100,
                        help='max integer for multiply')
    parser.add_argument('--sum', metavar='N', type=int,default=1000,
                        help='max integer for sum')
    parser.add_argument('--time', metavar='N', type=int,default=60,
                        help='max integer for time')
    args = parser.parse_args()
    m = MathsTrainer(multiplication=args.mult,
                     addition=args.sum,
                     time=args.time)
    m.run_questions()
