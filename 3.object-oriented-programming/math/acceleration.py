import math

CurrentSpeed = 0
AccelerationSteps = 0


def ExponentialAccelerationTo(MaxSpeed):
    global AccelerationSteps
    global CurrentSpeed
    GrowthRate = .02  # Growth Rate
    Exponent = 1
    if CurrentSpeed < 1:
        CurrentSpeed = 1
    while CurrentSpeed < MaxSpeed:
        # Calculation of acceleration using doubling time
        CurrentSpeed = math.ceil(CurrentSpeed*((1 + GrowthRate) ** Exponent))
        Exponent += 1
        if CurrentSpeed > MaxSpeed:
            CurrentSpeed = MaxSpeed
        AccelerationSteps += 1
        print("Speed: ", CurrentSpeed)
        print("Test Counter:", AccelerationSteps)


ExponentialAccelerationTo(50)
