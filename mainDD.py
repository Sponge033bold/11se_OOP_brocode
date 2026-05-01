from parentDD import ParentDD, ChildTL

homer = ParentDD("Homer", "Donuts", "Watching TV", "D'oh!", 39)
marge = ParentDD("Marge", "Pasta", "Gardening", "Hmm… I don't know, Homie.", 36)
bart = ChildTL("Bart", "Pizza", "Skateboarding", "Eat my shorts!", 10)
lisa = ChildTL("Lisa", "Salad", "Playing the saxophone", "If anyone wants me, I'll be in my room.", 8)
maggie = ChildTL("Maggie", "Baby food", "Playing with her toys", "Goo goo ga ga!", 1)

homer.speak()
marge.speak()
bart.speak()
lisa.speak()
maggie.speak()




