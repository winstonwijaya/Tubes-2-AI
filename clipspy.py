from clips import Environment

def findFact(ListFact):
    env = Environment()
    env.load('rule.txt')
    for fact in listFact:
        env.assert_string(fact)
    res = []
    env.run()
    for fact in env.facts():
        res.append(fact)
