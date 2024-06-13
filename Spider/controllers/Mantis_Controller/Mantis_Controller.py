from controller import Robot

robot = Robot()

timestep = 320

leftleg1 = robot.getDevice("LAC")
leftleg2 = robot.getDevice("LMC")
leftleg3 = robot.getDevice("LPC")

rightleg1 = robot.getDevice("RAC")
rightleg2 = robot.getDevice("RMC")
rightleg3 = robot.getDevice("RPC")

flag=0

while robot.step(timestep) != -1:
    if flag%10==0:
        leftleg1.setPosition(-0.3)
    elif flag%10==1:
        rightleg1.setPosition(0.3)
    elif flag%10==2:
        leftleg2.setPosition(-0.3)
    elif flag%10==3:
        rightleg2.setPosition(0.3)
    elif flag%10==4:
        leftleg3.setPosition(-0.3)
    elif flag%10==5:
        rightleg3.setPosition(0.3)
    elif flag%10==6:
        leftleg1.setPosition(0.2)
        leftleg2.setPosition(0.2)
        leftleg3.setPosition(0.2)
        rightleg1.setPosition(0.2)
        rightleg2.setPosition(0.2)
        rightleg3.setPosition(0.2)
    flag+=1