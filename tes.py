from clips import Environment

env = Environment()

env.load('rule.txt')
listFact = [
    '(angles 60 40 80)'
]

for fact in listFact:
    env.assert_string(fact)

env.run()