class Email:

  def __init__(self, sender, receiver, date, subject):
      self.sender = sender
      self.receiver = receiver
      self.date = date
      self.subject = subject

  def __str__(self) -> str:
      return f"{self.sender}, {self.receiver}, {self.date}, {self.subject}"
