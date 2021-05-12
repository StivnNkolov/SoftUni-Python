results = {}
submissions = {}

command = input()

while not command == "exam finished":
    if "banned" not in command:
        username, language, points = command.split("-")
        points = int(points)
        if username not in results:
            results[username] = points
        else:
            if results[username] < points:
                results[username] = points
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        username = command.split("-")[0]
        results.pop(username)
    command = input()

sorted_results = sorted(results.items(), key=lambda kvs: (-kvs[1], kvs[0]))

print("Results:")
for key, value in sorted_results:
    print(f"{key} | {value}")

sorted_submissions = sorted(submissions.items(), key=lambda kvs: (-kvs[1], kvs[0]))

print("Submissions:")
for key, value in sorted_submissions:
    print(f"{key} - {value}")