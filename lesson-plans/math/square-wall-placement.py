# To be used later to calculate 1/3 placement on wall height
wl = int(input('What is the length of the wall space? (in centimeters) '))
num_objects = int(
    input('How many objects of the same length are being hanged? '))
ol = int(input('What is the length of one of the objects? (in centimeters) '))


def calculate_buffer():
    # finds the total used space for each of the combined objects on a straight path on the wall space
    total_used_length = (num_objects*ol)
    # calculates the remaining space between each object on the wall minus the used space
    remaining_space = wl - total_used_length
    # adds padding space before every object and then once more after the final object
    padding = remaining_space/(num_objects+1)
    return padding


buffer = calculate_buffer()
print('Hang the first object by measuring\n'+str(buffer) +
      'cm \nfrom the edge of the wall to the edge of the object. \nThen, hang each object so that there is\n'+str(buffer)+'cm \nbetween them.')
