# 6. Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "sif" or "harry" and see the effects.


from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fromm, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fromm} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf, fromm, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fromm} to {to} is {randint(222, 5555)}")

p = Train(234567)
p.book("Materewadi", "Mumbai")
p.getStatus()
p.getFare("Materewadi", "Mumbai")



# there will be no difference in output, if you changed the self to slf