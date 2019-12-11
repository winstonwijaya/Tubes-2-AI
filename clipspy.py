from clips import Environment

def findFact(ListFact):
    env = Environment()
    env.load('rule.txt')
    for fact in ListFact:
        env.assert_string(fact)
    res = []
    env.run()
    for fact in env.facts():
        res.append(str(fact))

    return res
