from sys import stdout,platform
from time import sleep
from os import system

class Boilerplate_loading_bar(object):
    def __init__(self,length = 10,suffix="Standard %",update_sleep_time = 0.2) -> None:
        self.current_percentance = 0
        self.length = length
        self.suffix = suffix
        self.update_sleep_time = update_sleep_time

    def error_handler(fn):
        def wrapper(self, *args, **kwargs):
            try:
                return fn(self, *args, **kwargs)
            except Exception as e:
                if(platform.startswith("win")):system("cls")
                else:system("clear")
                raise Exception(e)
        return wrapper

    @error_handler
    def display(self) -> None:
        if(self.current_percentance == 0):print("")
        if(self.current_percentance > 100):
            self.current_percentance = 100
        bar = '=' * round(self.current_percentance*self.length/100) + '-' * (self.length - round(self.current_percentance*self.length/100)) 
        stdout.write('[%s] %s%s %s\r' %(bar, self.current_percentance, '%', self.suffix))
        stdout.flush()

        if(self.current_percentance == 100): print("")
        sleep(self.update_sleep_time)

    @error_handler
    def update_percentage(self,much = 0):
        self.current_percentance+=much
        self.display()
    
    @error_handler
    def set_percentage(self,much = 0):
        self.current_percentance=much
        self.display()

if __name__ == "__main__":
    loading_bar = Boilerplate_loading_bar(length=30,suffix="TEST",update_sleep_time=0.01)
    for _ in range(100):
        loading_bar.update_percentage(1)
