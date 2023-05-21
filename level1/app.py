import random
key = random.randint(1, 100) * (random.randint(1, 100) / random.randint(1, 100))
secret = "❸➄➄➀➃❊✿✿➃❵➀➄✽➃➀➂❹❾❷✾❳❿❴❹❾❷✾❾❵➄✿➀✿❼❹➅➉❹➉➅➂❵✿❴✿❽❹❴❴❼❵❃✿❷❹➄"
a = 5 + random.randint(random.randint(5, 10), random.randint(20, 30))
b = (a + random.randint(random.randint(5, 10), random.randint(20, 30))) * random.randint(random.randint(5, 10), random.randint(20, 30))
if 50 <= b + a <= 60:
    result = ""
    for c in secret:
        result += chr(ord(c) - int(key))
    print(result)