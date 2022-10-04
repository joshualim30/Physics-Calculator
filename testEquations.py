# physics equation to find the final velocity of an object
# given the initial velocity, acceleration, and time
def finalVelocity(initialVelocity, acceleration, time):
  return initialVelocity + acceleration * time

# physics equation to find maximum height of an object
# given the initial velocity and acceleration
def maxHeight(initialVelocity, acceleration):
    return (initialVelocity * initialVelocity) / (2 * acceleration)

# physics equation to find the time it takes for an object to reach maximum height
# given the initial velocity and acceleration
def timeToMaxHeight(initialVelocity, acceleration):
    return -initialVelocity / acceleration