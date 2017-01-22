
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True
    def __init__(self, more_words):
        print "I am a Chicken Class derived from Bird !", more_words

if __name__ == "__main__":
    spring = Bird()
    summer = Chicken("hahahaha")

    print spring.way_of_reproduction
    print summer.way_of_reproduction

    print summer.move(3,5)
    print summer.move(4,6)
    print summer.move(1,2)
