import datetime
import random
import os

start_date = datetime.datetime(2023, 12, 10) # Year, month, day
end_date = datetime.datetime(2024, 10, 10) # Year, month, day

for i in range((end_date - start_date).days):
    random_date = start_date + datetime.timedelta(days=i, hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))

    file_path = "random.txt"

    with open(file_path, "w") as f:
        f.write(str(random.randint(1, 1000)))

    os.system("git add " + file_path)

    commit_message = "Random commit for " + random_date.strftime("%Y-%m-%d %H:%M:%S")
    print(commit_message)

    os.system("git commit --amend --no-edit --date=\"" + random_date.strftime("%Y.%m.%d %H:%M") + "\" -m \"" + commit_message + "\"")
