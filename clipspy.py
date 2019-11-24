from clips import Environment

env = Environment()

env.load('rule.txt')
listFact = [
    '(angles 90 45 45)',
    '(sides 6 5 5)'
]

for fact in listFact:
    env.assert_string(fact)

env.run()