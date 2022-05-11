import matplotlib.pyplot as plt
import Data
import os
file_path = os.path.realpath(__file__)
fp = file_path.split("C:")
fp = fp[1].split("\\Ui.py")
print(fp[0])

path = fp[0]    #'/Users/Declan/Desktop/SWENGT'
files = os.listdir(path)
# Check for valid result files
valid = ".json"
validFiles = []
for file in files:
    if(valid in file):
        validFiles.append(file)

data = Data.Data()
for file in validFiles:
    data.add(file)

if(len(validFiles)>0):

    # PLOT AVG RUNTIME
    # x axis values (Filenames)
    x = validFiles

    # corresponding y axis values
    y = data.average_run


    # plotting the points
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='blue', markersize=10)

    # setting x and y axis range
    plt.ylim(0, max(data.average_run) +50)
    plt.xlim(-0.25, len(data.average_run) - 0.75)

    # naming the x axis
    plt.xlabel('Version')
    # naming the y axis
    plt.ylabel('Average Runtime')

    # giving a title to my graph
    plt.title('Average Runtime For Each Version')

    # function to show the plot
    plt.show()

    # PLOT Rest of data
    figure, axis = plt.subplots(2, 2)
    # For First result
    y1 = data.first_result
    axis[0, 0].plot(x, y1)
    axis[0, 0].set_title("First result")
    axis[0, 0].plot(x, y1, color='blue', linestyle='None', linewidth=2, marker='o', markerfacecolor='blue', markersize=10)
    # For Final result
    y2 = data.final_result
    axis[0, 1].plot(x, y2)
    axis[0, 1].set_title("Final result")
    axis[0, 1].plot(x, y2, color='blue', linestyle='None', linewidth=2, marker='o', markerfacecolor='blue', markersize=10)

    # For 99th Percentile
    y3 = data.p99
    axis[1, 0].plot(x, y3)
    axis[1, 0].set_title("99th Percentile")
    axis[1, 0].plot(x, y3, color='blue', linestyle='None', linewidth=2, marker='o', markerfacecolor='blue', markersize=10)

    # For 50th Percntile
    y4 = data.p50
    axis[1, 1].plot(x, y4)
    axis[1, 1].set_title("50th Percentile")
    axis[1, 1].plot(x, y4, color='blue', linestyle='None', linewidth=2, marker='o', markerfacecolor='blue', markersize=10)

    # Combine all the operations and display
    plt.show()
else:
    print("ERROR: NO RESULT FILES DETECTED IN DIRECTORY")
