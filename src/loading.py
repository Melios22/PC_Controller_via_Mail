
import multiprocessing 
import time

class CLI_Spinner:
    def __init__(self, messenger = "", speed = 0.2) -> None:
        self.messenger = messenger
        self.speed = speed
        
        self.process = multiprocessing.Process(
            target = self.spin,
            args = (),
            name = "CLI Spinner"
        )
    
    def spin(self):
    #    spinner = ["◴", "◷", "◶", "◵"]
    #    spinner = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    #    spinner = ["◐","◓","◑","◒"]
    #    spinner = ["◜","◝","◞","◟"]
    #    spinner = ['▉','▊','▋','▌','▍','▎','▏','▎','▍','▌','▋','▊','▉']
    #    spinner = ['▌','▀','▐','▄']
    #    spinner = ['▁','▃','▄','▅','▆','▇','█','▇','▆','▅','▄','▃']
    #    spinner = ['▖','▘','▝','▗']
       spinner = ['      ','.     ', '. .   ', '. . . ']
    #    spinner = ['◢','◣','◤','◥']
    #    spinner = ['◰','◳','◲','◱']
    #    spinner = ['⠁','⠂','⠄','⡀','⢀','⠠','⠐','⠈']
       

       
       n = 0
       while True:
            try:
              print(f"\r{self.messenger} {spinner[n]}", end = "")  
              n += 1
              if (n >= len(spinner)):
                     n = 0
              time.sleep(self.speed)
            except KeyboardInterrupt:
                print("\r", end = "")
                break
    

    def start(self):
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            return
        else:
            self.process.terminate()
            print("\r", end = "")
            return

'''

    def loop(self):
        spinner = CLI_Spinner("\rWaiting for new mail ", 0.5)
        spinner.start()
        while True:
            self.fetch_mail()
            if len(self.cmd_list) != 0:
                spinner.stop()
                # print(self.cmd_list)
                self.process_command()
                self.send_mail()
                self.refresh()
                if not spinner.process.is_alive():
                    spinner = CLI_Spinner("\rWaiting for new mail ", 0.5)
                    spinner.start()

            sleep(2)
 
'''