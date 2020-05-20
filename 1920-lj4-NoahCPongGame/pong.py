"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import os
import sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Starting Template"

MOVEMENT_SPEED = 5

class Paddle1():
    def __init__(self, position_x, position_y, delta_x, delta_y, rect_height, rect_width):
        self.position_x = position_x
        self.position_y = position_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.width = rect_width
        self.height = rect_height
        
    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, arcade.color.PINK)

    def update(self):
        self.position_y += self.delta_y
        self.position_x += self.delta_x
    

class Paddle2():
    def __init__(self, position_x, position_y, delta_x, delta_y, rect_height, rect_width):
        self.position_x = position_x
        self.position_y = position_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.width = rect_width
        self.height = rect_height

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, arcade.color(13,21,163))


class Cat():
    def __init__(self, position_x, position_y, delta_x, delta_y, sprite):
        self.position_x = position_x
        self.position_y = position_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.sprite = sprite
        


    def draw(self):
        arcade.draw_texture_rectangle(self.position_x, self.position_y, 150, 150, self.sprite)
    
    def update(self, paddle1, paddle2):
        self.position_x = self.position_x + self.delta_x
        self.position_y = self.position_y + self.delta_y
        # if self.position_x <= 125 or self.position_x >= SCREEN_WIDTH - 125:
        #     self.delta_x*= -1
        if self.position_y <= 125 or self.position_y >= SCREEN_HEIGHT - 125:
            self.delta_y*= -1
        if self.position_x + 75 >= paddle1.position_x - paddle1.width//2 and self.position_x - 75 <= paddle1.position_x + paddle1.width//2 and self.position_y + 75 >= paddle1.position_y - paddle1.height//2 and self.position_y - 75 <= paddle1.position_y + paddle1.height//2:
            self.delta_x *= -1 
        if self.position_x + 75 >= paddle2.position_x - paddle2.width//2 and self.position_x - 75 <= paddle2.position_x + paddle2.width//2 and self.position_y + 75 >= paddle2.position_y - paddle2.height//2 and self.position_y - 75 <= paddle2.position_y + paddle2.height//2:
            self.delta_x *= -1 


 

   
        

    
    
     # ALS rechterkant van bal groter of gelijk aan linkerkant van paddle EN
    # linkerkant van bal kleiner of gelijk aan rechterkant van paddle EN
    # etc

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.PINK)

        self.background = None


        sprite = arcade.load_texture("katx2.png")
        self.my_cat = Cat(300, 400,-7, -7, sprite)

        self.my_paddle2 = Paddle1(50, SCREEN_HEIGHT/2, 0, 0, 250, 25)
        
        self.my_paddle1 = Paddle1(1150, SCREEN_HEIGHT/2, 0, 0, 250, 25)

        self.score1 = 0
        self.score2 = 0
        # If you have sprite lists, you should create them here,
        # and set them to None
 

    
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.my_paddle1.delta_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.my_paddle1.delta_y = -MOVEMENT_SPEED
        if key == arcade.key.W:
            self.my_paddle2.delta_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.my_paddle2.delta_y = -MOVEMENT_SPEED
        if key == arcade.key.SPACE:
             self.my_cat = os.execl(sys.executable, sys.executable, * sys.argv)

            
            
        
        

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.my_paddle1.delta_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.my_paddle1.delta_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.my_paddle2.delta_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.my_paddle2.delta_x = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.my_paddle1.delta_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.my_paddle1.delta_x = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.my_paddle2.delta_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.my_paddle2.delta_x = 0

    
    


    def setup(self):
        # Create your sprites and sprite lists here
        self.background = arcade.load_texture("sterren.jpg")
        

    #font

  

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        # Draw the background texture
        arcade.draw_texture_rectangle(600, 300,
                                1200, 1000, self.background)
        
        self.my_cat.draw()
        self.my_paddle1.draw()
        self.my_paddle2.draw()
        arcade.draw_text(f"Player 1: {self.score1}", 300, 700, arcade.color.ALICE_BLUE, 25, 0, "left", "QuietMeows-48jx.ttf" )
        arcade.draw_text(f"Player 2: {self.score2}", 700, 700, arcade.color.ALICE_BLUE, 25, 0, "right", "QuietMeows-48jx.ttf")
    
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.my_cat.update(self.my_paddle1, self.my_paddle2)
        self.my_paddle1.update()
        self.my_paddle2.update()
        if self.my_cat.position_x - 75 <= 0:
            self.score2 += 1 
            self.my_cat.position_x = SCREEN_WIDTH/2
            self.my_cat.position_y = SCREEN_HEIGHT/2
        if self.my_cat.position_x + 75 >= SCREEN_WIDTH:
            self.score1 += 1 
            self.my_cat.position_x = SCREEN_WIDTH/2
            self.my_cat.position_y = SCREEN_HEIGHT/2
        
        

    

    

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()