from game_classes.figure_output import Output
from game_classes.user_input import Input
from game_classes.word import Word
from game_classes.jumper import Jumper

class Game_loop:
    """The main game play loop.
    
        responsibility: to control the sequence of game play.

        attributes:
            -output: an instance of the the output class
            -input: an instance of the input class
            -word: an instance of the word class
            -jumper: an instance of the jumper class
        
    """
    def __init__(self):
        """
        constructs new game loop

        args: self (Game_loop): an instance of Game_loop.
        """
        self.word = Word()
        self.jumper = Jumper()
        self.input = Input()
        self.output = Output()
        self.letters = []

    def list_compare(self,l1,l2):
        return l1 == l2

    def start_game(self):
        iterator = int(0)

        the_wordArray = self.word.get_letters()

        blanks = []
        for i in the_wordArray:
            blanks.append("_")
        
        win_check = []
        for i in the_wordArray:
            win_check.append(0)

        while (iterator < 4):
            self.output.getLetters(blanks)
            self.output.getSteve(self.jumper.parachute, iterator)
            self.output.getLetters(self.letters)
            self.input.set_input()
            self.letters.append(self.input.get_input())
            
            if self.input.get_input() in the_wordArray:
                #I discovered that using self.word.get_letters() directly will
                #result in an infinite while loop since it will reset the array of letters
                #in self.word.get_letters() instead of turning every instance of the letter to zero
                #so I created a variable the_wordArray that we could use.
                while self.input.get_input() in the_wordArray:
                    x = the_wordArray.index(self.input.get_input())
                    blanks[x] = self.input.get_input()
                    the_wordArray[x] = 0
                
                if self.list_compare(the_wordArray, win_check) == True:
                    print("You Saved Steve!")
                    break
            else:
                iterator += 1

        print("Thanks for playing")