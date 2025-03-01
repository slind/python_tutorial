def create_story(adj, verb, noun):
    return "There once was a {0} {1} {2} called Carl.".format(adj, verb, noun)

def get_adj():
    print("please input an adjective:")
    return input()

def get_verb():
    print("please input a verb:")
    return input()

def get_substantive():
    print("please input a substantive:")
    return input()

print(create_story(get_adj(), get_verb(), get_substantive()))