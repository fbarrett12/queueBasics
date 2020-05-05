class Queue:

  def __init__(self):
    self.queue = list()

  def addToQueue(self, dataval):
    # Insert method to add element
    if dataval not in self.queue:
      self.queue.insert(0, dataval)
      return True
    return False

  # Pop method to remove elements
  def removeFromQueue(self):
    if len(self.queue) > 0:
      return self.queue.pop()
    return ("No elements in Qu")

  def size(self):
    return len(self.queue)

TheQueue = Queue()
TheQueue.addToQueue("Mon")
TheQueue.addToQueue("Tue")
TheQueue.addToQueue("Thu")
# print(TheQueue.size())
print(TheQueue.removeFromQueue())
print(TheQueue.removeFromQueue())