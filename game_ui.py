'''
Michael Maquera
CS5001 fall 2020
Final Project
Game_UI.py
'''

import turtle
from game_logic import PlayingCard
from game_logic import Game
import quit

def setup_command():
    """
    function -- setup-commands --gets user input to star the game
    params -- importing the game class and game_ui file
    returns -- launches the card game program
    """  
    card_number = turtle.numinput('card number','how many cards are we playing with? (8,10, or 12?')
    player_name = turtle.textinput(' player name','what is your name')
    if card_number == 8 or 10 or 12:
        card_int = int(card_number)
        #creating an instance of the game class for the player's name and requested cards
        #call the build_game_ui with the current game object
        current_game =Game(player_name,card_number)
        play_game(current_game)
           
    else:
        exit()
        print('that is not a valid entry, try again')
        setup_command()
        
        
def play_game(current_game):
           
        
    def build_game_ui(current_game):
        '''
        function -- builds the interface for the game and the visual assets
        params -- current_game: a object of the Game  class
        returns -- none
        '''
        create_layout()
        quit_button()
        write_leaders()
        score_board() 
        add_cards(current_game.card_number)
        
    
    def create_layout():
        """
        function -- creates the canvas which game cards will be displayed
        params -- none
        returns -- the canvas board on which the game will be played
        """
    #setting starting location of the canvas box
    
        board = turtle.Turtle()
        board.hideturtle()
        board.speed(0)
        board.pencolor('white')
        board.penup()
    #adjust the pen color of the grid so it cannot be seen
    #board.pencolor('white')
        board.setx(0)
        board.sety(500)
        
    #horizontal bars of the board
        board.up()
        board.goto(-300,100)
        board.down()
        board.forward(600)
        board.up()
        board.goto(-300,-100)
        board.down()
        board.forward(600)
        board.up()
        board.goto(-300,-300)
        board.down()
        board.forward(600)
        board.up()
        
    #vertical bars of the board
        board.goto(-100,300)
        board.setheading(-90)
        board.down()
        board.forward(900)
        board.up()
        board.goto(100,300)
        board.down()
        board.forward(900)
        board.up()
    
   
    def add_cards(card_number):
        """
        function -- add_cards: adds back side of cards to game canvas
        params -- card_number:int
        returns -- none
        """
        image = 'card_back.gif'
        screen.register_shape(image)  
        x = -400
        y = 200
    #adding cards onto the canvas based on the game size
        if card_number == 8:
            row1 = 3
            row2 = 3
            row3 = 2
            row4 = 0
    
        elif card_number == 10:
            row1 = 3
            row2 = 3
            row3 = 3
            row4 = 1
    
        elif card_number ==12:
            row1 = 3
            row2 = 3
            row3 = 3
            row4 = 3
    
        else:
            print('sorry, an invalid number was enterted try again')
            setup_command()
    
        for i in range(row1):
            x = x + 200
            turtle.penup()
            turtle.goto(x,200)
            turtle.pendown()
            turtle.shape(image)
            turtle.stamp()
        x = -400
        for i in range(row2):
            x = x + 200
            turtle.penup()
            turtle.goto(x,1)
            turtle.pendown()
            turtle.shape(image)
            turtle.stamp()
    
        x = -400
        for i in range(row3):
            x = x + 200
            turtle.penup()
            turtle.goto(x,-200)
            turtle.pendown()
            turtle.shape(image)
            turtle.stamp()
        
        x = -400
        for i in range(row4):
            x = x + 200
            turtle.penup()
            turtle.goto(x,-400)
            turtle.pendown()
            turtle.shape(image)
            turtle.stamp()

    def write_leaders():
        """
        function -- write_leaders
        params -- high_scores:dictionary 
        returns -- display the top scores on the leaderboard on the game canvas
        """
        style = ('Courier', 12)
        leaders = open('scores.txt','r+')
        results = leaders.readlines()
        x = -750
        y = 450
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.write('High Scores:', font = style)
        for i in results:
            turtle.penup()
            y = y-50
            turtle.goto(x,y)
            turtle.pendown()
            turtle.write(i, font= style)
        
    def score_board():
        """
        function -- score_board - writes the write number of correct matches and gueses of the game
        params -- none
        returns -- guesses and correct match in the present game round
        """
        style = ('Courier', 12)
        turtle.penup()
        turtle.goto(0,400)
        turtle.pendown()
        turtle.write('Guesses: ',font = style)
        turtle.penup()
        turtle.goto(0,440)
        turtle.pendown()
        turtle.write('Correct: ',font = style)
        turtle.penup()
    
    def quit_button():
        """
        function -- quit_button - places the quit button for the game
        params -- none
        returns -- closes the turtle canvas window
        """
    #creates the quit button
        quit_button = turtle.Turtle()
        quit_button.speed(0) 
        quit_button.penup()
        quit_button.goto(670,450)
        quit_button.pendown()
        screen.addshape('quitbutton.gif')
        quit_button.shape('quitbutton.gif')
        quit_button.onclick(quit.quit_game)
    
    def click(x,y):
        '''
        function -- click, uses the grid created 
        params -- x,y;int based on the coordinates clicked on the game canvas
        returns -- a card when clicked onto the game canvas
        '''
        col = (x + 300) // 200
        row = (-y + 300) // 200
        box_number = int(col + row*3)

        screen.addshape('2_of_clubs.gif')
        screen.addshape('ace_of_diamonds.gif')
        screen.addshape('3_of_hearts.gif')
        screen.addshape('jack_of_spades.gif')
        screen.addshape('queen_of_hearts.gif')
        screen.addshape('king_of_diamonds.gif')
        screen.addshape('2_of_diamonds.gif')
        
        for i in current_game.card_layout:
            if i[0] == box_number:
                screen.addshape(i[2])
                card = PlayingCard(i[1],i[2])
                card.store_box_number(i[0])
                card.place_card(x,y)
                current_game.store_coors(x,y)
                current_game.player_turn(card)
    
    screen = turtle.Screen()
    screen.title("CS5001 Memory Game")    
    build_game_ui(current_game)
    turtle.onscreenclick(click)
    
    turtle.listen()
    turtle.mainloop()
    
    



    