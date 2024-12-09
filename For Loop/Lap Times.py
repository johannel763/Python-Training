## User enters the number of times they've run around a racetrack.
## Program returns fastest, slowest and average lap times.

total_time = float(0)
laps = int(input('How many laps did you comlete? '))
lap_list = []


for x in range(laps):
    time = float(input('Enter lap time: '))
    lap_list.append(time)
    total_time += time
    avg_laptime = total_time / laps
    lap_list.sort()
    fastest_lap = lap_list[0]
    slowest_lap = lap_list[-1]

print('Fastest lap: ', fastest_lap)
print('Slowest lap: ', slowest_lap)
print('Average lap time', avg_laptime)