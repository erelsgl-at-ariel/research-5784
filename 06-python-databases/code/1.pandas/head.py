import itertools
source = "c:\\users\\user\\Desktop\\national-budget.csv"
target = "c:\\users\\user\\Desktop\\national-budget-1000.csv"
# with open(target, "w", encoding="utf-8") as w:
#     with open(source, "r", encoding="utf-8") as f: 
#         w.write("\n".join(itertools.islice(f,1000)))


with open(source, "r", encoding="utf-8") as f:
    print(list(itertools.islice(f,1000)))
