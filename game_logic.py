'''
Michael Maquera
Final Project Cs 5001
Fall 2020
game_logic.py
'''
import turtle


screen = turtle.Screen()
class PlayingCard:
    """ 
    class PlayingCard -- stores the card values used into the game
    methods --  init, turtle, card_key, turtle_shape, and box_number
    compare, compares the values of two cards to deteremine if they are equal
    place_card, places cards onto the game canvas
    store_box_number, stores the box number of the cards location on the canvas
    """
    def __init__(self,card_key,shape):
        self.turtle = turtle.Turtle()
        self.turtle.shape = shape
        self.card_key = card_key
        self.box_number = 0
           
    def compare(self,other):
        '''
        function -- compare
        params -- self, other: instance of the PlayingCard class
        returns: boolean
        '''
        if self.card_key == other.card_key:
            print('match found')
            return True
        else:
            print("these cards arent a match")
            return False
    def place_card(self,x,y):
        '''
        function -- place_card, places an image of the playing card object based on x,y coordinates
        params -- self, x,y:int
        returns -- an image of the card selected 
        '''
        turtle.shape(self.turtle.shape)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.stamp()
    
    def store_box_number(self,box_number):
        '''
        function -- store_box_number
        params -- self, box_number
        returns -- self.box_number: int
    
        '''
        self.box_number = box_number
        return self.box_number
            
class Game():
    """ 
    Class-- game is used to manage the gamne logic between the UI in turtle and the score
    Methods --
    layout, stores the seperate 8,10, 12 card layouts a player can choose
    draw_correctpts -- writes the current number of correct gueses on the turtle canvas
    add_correct, simulates drawing a pair of cards during a game session
    add_guess, add a guess point to the object instance every time there is a click on the canvas
    draw_guesspts,  writes the current number of guesses onto the game canvas
    store_coors, stores the x,y coordintes of the player clicks on the canvas board
    remove_coors, removes the x,y coodriantes of the player if a turn is not a match
    hide_cards, places a white square over matching cards so they are no longer in play
    remove_matchng_pair, removes cards from the card layout list that have been found by the player
    compare_cards,compare two cards that comprises of a "turn" in the game
    player_turn, checks to see if two clicks of the player have been made on two seperate cards
    update_leader_board, adds the recent players score onto the scores.txt file
    sort_leader_scores, sorts the players and their scores from highest to lowest
    game_won, display the winning player's game score once all matches have been found
    display_game_progress, displays all of the current values of the game object
    """
    def __init__(self,player_name,card_number):
        self.player_name = player_name
        self.card_number = card_number
        self.guess_pts = turtle.Turtle()
        self.correct_pts = turtle.Turtle()
        self.card_layout = []
        self.layout()
        self.coor_list = []
        self.guess_points = 0
        self.correct_points = 0
        self.stack_list = []
        self.style = ('Courier', 12)
        
    
    def layout(self):
        '''
        function -- layout, providse the various card layouts based on the card selection 8, 10, or 12
        params -- self
        returns -- a list of cards based on the user's selection during the game_setup()
        
        '''
        layout8 = [[0,'2C','2_of_clubs.gif'],[1,'3H','3_of_hearts.gif'],[2,'AD','ace_of_diamonds.gif'] 
                        ,[3,'JS','jack_of_spades.gif'],[4,'3H','3_of_hearts.gif'],[5,'AD','ace_of_diamonds.gif']
                        ,[6,'2C','2_of_clubs.gif'],[7,'JS','jack_of_spades.gif']]
    
        layout10 = [[0,'QH','queen_of_hearts.gif'],[1,'3H','3_of_hearts.gif'],[2,'AD','ace_of_diamonds.gif'] 
                        ,[3,'JS','jack_of_spades.gif'],[4,'3H','3_of_hearts.gif'],[5,'AD','ace_of_diamonds.gif']
                        ,[6,'2D','2_of_diamonds.gif'],[7,'JS','jack_of_spades.gif'],[8,'2D','2_of_diamonds.gif'],[9,'QH','queen_of_hearts.gif']]
    
        layout12 = [[0,'2C','2_of_clubs.gif'],[1,'3H','3_of_hearts.gif'],[2,'AD','ace_of_diamonds.gif'] 
                        ,[3,'JS','jack_of_spades.gif'],[4,'3H','3_of_hearts.gif'],[5,'AD','ace_of_diamonds.gif']
                        ,[6,'JS','jack_of_spades.gif'],[7,'2D','2_of_diamonds.gif'],[8,'QH','queen_of_hearts.gif'],[9,'QH','queen_of_hearts.gif']
                        ,[10,'2D','2_of_diamonds.gif'],[11,'2C','2_of_clubs.gif']]    

        if self.card_number == 8:
            self.card_layout = layout8
            return self.card_layout
        elif self.card_number == 10:
            self.card_layout = layout10
            return self.card_layout
        elif self.card_number == 12:
            self.card_layout = layout12
            return self.card_layout
       
        
    def add_correct(self):
        '''
        function -- add correct, adds a correct point to the game instance when a match is found
        params -- self
        returns -- an updated version of the self. correct_points : int
        '''
        self.correct_points+=1
        winning_number = int(self.card_number) / 2
        self.draw_correctpts(self.correct_points)
        if self.correct_points == winning_number:
            self.game_won()
        else:
            return self.correct_points
           
    def draw_correctpts(self,correct_points):
        '''
        function -- draw _correctpts, writes the current number of correct gueses on the turtle canvas 
        params -- self, correct_points: int
        returns -- a drawing of the number of correct points on the turtle canvas screen
        
        '''
        self.correct_pts.undo()
        self.correct_pts.ht()
        self.correct_pts.up()
        self.correct_pts.goto(110,450)
        self.correct_pts.write(self.correct_points,font = self.style)
        
    def add_guess(self):
       '''
       function -- add_guess -- add a guess point to the object instance every time there is a click on the canvas
       params -- self
       returns -- self.guess_points +1 : int
       '''
       self.guess_points+=1
       self.draw_guesspts(self.guess_points)
       return self.guess_points
          
    def draw_guesspts(self,guess_points):
        '''
        function -- draw_guesspts, writes the current number of guesses onto the game canvas
        params -- self, guess-points:int
        returns -- turtle instance of guess_points
        '''
        self.guess_pts.undo()
        self.guess_pts.ht()
        self.guess_pts.up()
        self.guess_pts.goto(95,400)
        self.guess_pts.down()
        self.guess_pts.write(self.guess_points, font = self.style)
        
    
    def store_coors(self,x,y):
        '''
        function -- store_coors: stores the x,y coordiantes when the cards are clicked
        params -- self, x,y: where the players clicked on the canvas board
        returns -- self.coor_list: list
        '''
        self.coor_list.append([x,y])
        return self.coor_list
    
    def remove_coors(self):
        '''
        function -- remove_coors
        params -- self
        returns self.coor_list
        '''
        self.coor_list.pop()
        self.coor_list.pop()
        return self.coor_list        
    
    
    def hide_cards(self):
        '''
        function -- hide_cards, places a white square over matching cards so they are no longer in play
        params -- self
        returns -- a white square turtle object
        
        '''
        for i in self.coor_list:
            x = i[0]
            y = i[1]
            turtle.ht()
            turtle.up()
        #go to the coordinates saved on the coor_list and place the blankwhite square
            turtle.goto(x,y)
            turtle.down()
            turtle.shape('square')
            turtle.shapesize(10,10)
            turtle.fillcolor('white')
            turtle.pencolor('white')
            turtle.stamp()
        self.coor_list.pop()
        self.coor_list.pop()    
    
    def remove_matching_pair(self,card_one,card_two):
        '''
        function -- remove matching pairs, removes cards from the card layout list that have been found by the player
        params -- self, card_one, card_two : both are objects of the Playingcard class
        returns --self.card_layout:list
        
        '''
        print(self.card_layout)
        print(card_one)
        print(card_two)
        
        card_one_num = card_one.box_number
        card_two_num = card_two.box_number
        
        for i in self.card_layout:
            if i[0] == card_one_num:
                self.card_layout.remove(i)
        for j in self.card_layout:
            if j[0] == card_two_num:
                self.card_layout.remove(j)
        return self.card_layout
    
    
    def compare_cards(self):
        '''
        function -- compare_cards -- compare two cards that comprises of a "turn" in the game
        params -- self
        returns -- a boolean, calls the add_correct method if there is a match
        '''
        #remove both cards being compared from the stack_list
        card_one = self.stack_list.pop()
        card_two = self.stack_list.pop()
        #use the compare method in the PlayingCard class to determine matching pairs
        result = card_one.compare(card_two)
        if result == True:
            print('these are a match')
        #if the cards are matching pair, add a correct point to the scoreboard
            self.add_correct()
            self.add_guess() 
            self.remove_matching_pair(card_one,card_two)
            self.hide_cards()
            return True
            #do somethign to remove these cards     
        else:
            self.add_guess() 
            print('these are not a match')
            #remove the two saved coordinates in order to start a new turn
            self.remove_coors()
            return False 
                     
    def player_turn(self,turn):
        '''
        function -- player_turn
        params -- self, turn:
        returns -- if stack_list length is 2, calls compare cards function
        '''
        self.stack_list.append(turn)
        if len(self.stack_list) == 2:
            self.compare_cards()
    
    def update_leader_board(self):
        '''
        function -- update leader board, adds the recent players score onto the scores.txt file
        params -- self
        returns -- calls the sort leader scores function, 
        '''
        leaders = open('scores.txt','a')
        player_score = str(self.guess_points)
        leaders.writelines([player_score,' ',self.player_name,'\n']) 
        #sort leader list from to lowest to highest afer a new score is added
        self.sort_leader_scores()           
    
    def sort_leader_scores(self):
        '''
        function -- sort_leader_scores, sorts the players and their scores from highest to lowest
            inside of the scores.txt file
        params -- self
        returns -- none
        '''
        #reads the curent entries of the scores.txt file and sorts them numerically
        with open('scores.txt') as f:
            lines= f.readlines()
            lines.sort()
        f = open('scores.txt','r+')
        #deletes the old entries of the file and rewrites them in the new order
        f.truncate(0)
        for i in lines:
            f.write(i)
    
    def game_won(self):
        '''
        function -- game_won, display the winning player's game score once all matches have been found
        params -- self
        returns -- writes the winning game notice and the players final score to the game canvas
        
        '''
        #write the player's winning score onto the scores.txt file
        self.update_leader_board()
        #display the player's name and score
        winning_page = turtle.Turtle()
        winning_page.speed(0)
        winning_page.ht()
        screen.clear()
        winning_page.penup()
        winning_page.goto(0,350)
        winning_page.pendown()
        winning_page.write( self.player_name+' Congrats you won!', font= self.style)
        winning_page.up()
        winning_page.goto(0,300)
        player_score = str(self.guess_points)
        winning_page.write('Your Score was: ' +player_score,font= self.style)
               
    def display_game_progress(self):
        '''
        display_game_progress -- displays all of the current values of the game object
        params -- self
        returns -- prints(player_name,card_number,guess_points,stack_list)
        '''
        print(self.player_name)
        print(self.card_number)
        print(self.guess_points)
        print(self.correct_points)
        print(self.stack_list)
        
           






