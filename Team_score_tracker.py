scores = [0, 0, 0]

while True:
    x = input("Which team scored: ")
    if x.lower() == 'done':
        break

    team_number = int(x)

    points = input("how many points did the team score ")
    points = int(points)

    scores[team_number-1] += points

    print(f"Scores: {scores}\n")

print(f"Final scores: Team1: {scores[0]} || Team2: {scores[1]} || Team3: {scores[2]}")
print(max(scores))
winner = scores.index(max(scores)) + 1
print(f"Winner is team {winner}")
print(max(scores))