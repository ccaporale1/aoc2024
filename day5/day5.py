
rules = []
pages = []
with open('day5/input.txt', 'r') as file:
    for line in file:
        if "|" in line:
            rules.append(line.strip().split("|"))
        if "," in line:
            pages.append(line.strip().split(","))

rule_fail = True
sum = 0
#while rule_fail:#
for page in pages:
    rule_fail = False
    for rule in rules:
        if rule[0] in page and rule[1] in page:
            if page.index(rule[0]) > page.index(rule[1]):
                rule_fail = True
                continue
                
                #temp = page.remove(rule[0])
                #page.insert(page.index(rule[1]),temp)
                #rule_fail = True
    if not rule_fail:
        middle_index = int((len(page) - 1)/2)
        sum += int(page[middle_index])

print(f'Day 5 Part 1: {sum}')

sum = 0
for page in pages:
    page_incorrect = False
    rule_fail = True
    while rule_fail:
        rule_fail = False
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    page_incorrect = True
                    page.remove(rule[0])
                    page.insert(page.index(rule[1]),rule[0])
                    rule_fail = True
    if page_incorrect:
        middle_index = int((len(page) - 1)/2)
        sum += int(page[middle_index])

print(f'Day 5 Part 2: {sum}')