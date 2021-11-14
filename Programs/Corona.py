def test():
    TestResult="Positive"
    virus="coronavirus"
    bloodsample="irv"
    for alpha in bloodsample:
        if alpha in virus:
            virus1=virus.index(alpha)
            virus=virus[virus1+1:]
        else:
            TestResult="Negative"
            break
    return TestResult   

Result=test()
print(Result)