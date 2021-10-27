import threading

class worker(threading.Thread):

    def __init__(self,widget):
        threading.Thread.__init__(self)

        widget.show()

    def abc(self):
        pass
