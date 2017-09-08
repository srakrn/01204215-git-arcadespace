import arcade
from models impor Ship

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.ship = Ship(100,100)
        self.ship_sprite = arcade.Sprite('assets/images/rocket.png')
    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()
    def update(self, delta):
        ship = self.ship
        ship.update(delta)
        self.ship_sprite.set_position(ship.x, ship.y)

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, delta):
        if self.y > 600:
            self.y = 0
        self.y += 5

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
