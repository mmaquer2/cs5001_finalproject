'''
Michael Maquera
CS50001 Fall 2020
Final Project
test.py

'''
import unittest
import turtle
from game_logic import Game
from game_logic import PlayingCard
class GameTest (unittest.TestCase):
    '''
    class to test calculation methods of the Game and PlayingCard class:
        methods: game_compare_test
        game_compare_test, simulates comparing two different playing cards
        test_guess_points, ensures guess_points function works correctly
        test_correct_points,ensures the add correct function works correctly  
    '''
    def setUp(self):
        '''
        function -- setUp
        params -- self
        returns none
        '''
        self.current_game=Game('Bob',8)
        self.card1 = PlayingCard('3H','3_of_hearts.gif')
        self.card2 = PlayingCard('JS','jack_of_spades.gif')        
    
    def game_compare_test(self):
        '''
        funciton -- game-compare-test
        param-- self
        returns-- true or false/pass or fail  
        '''
        self.assertEqual(self.card1.compare(self.card1), True,
                         'Test: failed returned false')
        self.assertEqual(self.card1.compare(self.card2), False,
                         'Test: failed reutrned false')
        
    def test_guess_points(self):
        '''
        function --test guess_points
        params -- self
        returns -- true or false/pass or fail
        '''
        self.assertEqual(self.current_game.add_guess(), 1)
    
    def test_correct_points(self):
        '''
        function -- test_correct_points
        params -- self
        returns -- true or false/pass or fail
        '''
        self.assertEqual(self.current_game.add_correct(), 1)      
        

    
if __name__ == '__main__':
   unittest.main(verbosity = 3)
    
    