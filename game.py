import arcade
import arcade.key
from models import World, Ship

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color((55,71,79))
        self.world = World(width,height)
        self.ship_sprite = ModelSprite('assets/images/rocket.png',model=self.world.ship)
    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()
    def update(self, delta):
        self.world.update(delta)

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
