from game.action import Action

class DrawActorsAction(Action):
    """This class will handle the displaying of object on the screen.
    """
    def __init__(self, output_service):
        self.output_service = output_service

    def execute(self, cast):
        """Overrides the super class method. Executes the necessary
        code to display the actors to the screen.
        Args:
            Self (Action): An action
        """
        self.output_service.clear_screen()
        if cast["paddle"]:
            self.output_service.draw_actors(cast["paddle"])
        if cast["brick"]:
            self.output_service.draw_actors(cast["brick"])
        if cast["ball"]:
            self.output_service.draw_actors(cast["ball"])
        self.output_service.flush_buffer()