from clips import Environment

env = Environment()

env.load('rule.txt')
listFact = []

for fact in listFact:
    env.assert_string(fact)

env.rule()