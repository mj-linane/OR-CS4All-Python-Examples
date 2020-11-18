import math

current_speed = 0
acceleration_steps = 0


def exponential_acceleration_to(max_speed):
    global acceleration_steps
    global current_speed
    growth_rate = .02  # Growth Rate
    exponent = 1
    if current_speed < 1:
        current_speed = 1
    while current_speed < max_speed:
        # Calculation of acceleration using doubling time
        current_speed = math.ceil(current_speed * ((1 + growth_rate) ** exponent))
        exponent += 1
        if current_speed > max_speed:
            current_speed = max_speed
        acceleration_steps += 1
        print("Speed: ", current_speed)
        print("Test Counter:", acceleration_steps)
