from parentDD import ParentDD, ChildTL

homer = ParentDD("Homer", "donuts", "watching TV", "D'oh!", 39)
marge = ParentDD("Marge", "pasta", "gardening", "hmm... I don't know, Homie", 36)
bart = ChildTL("Bart", "pizza", "skateboarding", "eat my shorts!", 10)
lisa = ChildTL("Lisa", "salad", "playing the saxophone", "If anyone wants me, I'll be in my room", 8)
maggie = ChildTL("Maggie", "baby food", "playing with her toys", "*suck* *suck*", 1)

homer.speak()
marge.speak()
bart.speak()
lisa.speak()
maggie.speak()