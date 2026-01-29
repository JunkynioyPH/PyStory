# from PyQt6.QtCore import QThread



# # Usage in your Window class:
# self.thread = QThread()
# self.worker = NetworkWorker()
# self.worker.moveToThread(self.thread)

# self.thread.started.connect(self.worker.do_work)
# self.worker.finished.connect(self.thread.quit)
# self.worker.finished.connect(self.worker.deleteLater)
# self.thread.finished.connect(self.thread.deleteLater)

# self.thread.start()