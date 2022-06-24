import csv
import numpy as np

# import matplotlib
# matplotlib.use("TKagg")


intial_state = [[], [], []]
parity_game_states = [[], [], []]
bisim_blocks = [[], [], []]
block_division = [[], [], []]
block_percentage = [[], [], []]

file = open('bisim_min_data.csv')
reader = csv.reader(file)
for row in reader:
    num_states = int(row[1])
    if num_states < 11:
        intial_state[0].append(int(row[0]))
        parity_game_states[0].append(num_states)
        bisim_blocks[0].append(int(row[2]))
        block_division[0].append(list(map(int, row[3:])))
    elif num_states < 101:
        intial_state[1].append(int(row[0]))
        parity_game_states[1].append(num_states)
        bisim_blocks[1].append(int(row[2]))
        block_division[1].append(list(map(int, row[3:])))
    else:
        intial_state[2].append(int(row[0]))
        parity_game_states[2].append(num_states)
        bisim_blocks[2].append(int(row[2]))
        block_division[2].append(list(map(int, row[3:])))

file.close()

highest_percent = 1
highest_reduction = (0, 0)
max_block = (0, 0)
percent_sum = 0
percent_sum_no_zero = 0
no_zero_counter = 0
avg_block_size_total = 0
total_reduction = 0
total_reduction_no_zero = 0
reduction_counter = 0

for j in range(3):
    cur_range_hp = 1
    cur_range_hr = (0, 0)
    cur_range_mb = (0, 0)
    cur_range_ps = 0
    cur_range_psno = 0
    cur_range_nzc = 0
    cur_range_abst = 0
    cur_range_tr = 0
    cur_range_trnz = 0
    cur_range_rc = 0
    for i in range(len(intial_state[j])):
        cur_old = parity_game_states[j][i]
        cur_new = bisim_blocks[j][i]
        cur_percent = cur_new / cur_old
        percent_sum += cur_percent
        cur_range_ps += cur_percent
        cur_red = cur_old - cur_new
        total_reduction += cur_red
        cur_range_tr += cur_red
        if cur_percent != 1:
            percent_sum_no_zero += cur_percent
            cur_range_psno += cur_percent
            no_zero_counter += 1
            cur_range_nzc += 1
            total_reduction_no_zero += cur_red
            cur_range_trnz += cur_red
            reduction_counter += 1
            cur_range_rc += 1
        if cur_range_hp > cur_percent:
            cur_range_hp = cur_percent
            if highest_percent > cur_percent:
                highest_percent = cur_percent
        if cur_red > cur_range_hr[0]:
            cur_range_hr = (cur_red, cur_old)
            if cur_red > highest_reduction[0]:
                highest_reduction = (cur_red, cur_old)
        cur_max_block = max(block_division[j][i])
        if cur_range_mb[0] < cur_max_block:
            cur_range_mb = (cur_max_block, cur_old)
            if max_block[0] < cur_max_block:
                max_block = (cur_max_block, cur_old)
        cur_avg_block_size = np.mean(block_division[j][i])
        cur_range_abst += cur_avg_block_size
        avg_block_size_total += cur_avg_block_size

    print("Block " + str(j))
    print("The highest percentage that has been reducted was " + str(cur_range_hp))
    print("The highest reduction of states was " + str(cur_range_hr[0]) + " with originaly " + str(cur_range_hr[1]) + " states")
    print("The largest block was " + str(cur_range_mb[0]) + " in a game with originaly " + str(cur_range_mb[1]))
    print("The average reduction percentage is " + str(
        cur_range_ps / len(intial_state[j])))
    print("The average reduction when at least something was reduced is " + str(cur_range_psno / cur_range_nzc))
    print("The average reduction of states is " + str(cur_range_tr / len(intial_state[j])))
    print("The average reduction of states when at least something was reduced is " + str(cur_range_trnz / cur_range_nzc))
    print("The average block size is " + str(cur_range_abst / len(intial_state[j])))
    print("The number of reduced games is " + str(cur_range_rc) + " which was " + str(100 * cur_range_rc/len(intial_state[j])) + "%")
    print("The total number of games is " + str(len(intial_state[j])))
    print("")

#         cur_percentage_list = []
#         for cur_block in block_division[j][i]:
#             # if cur_block != 1:
#             cur_percentage_list.append(cur_block / cur_old)
#         block_percentage.append(cur_percentage_list)
#
#
# y_axis = np.zeros(101)
#
# for percents in block_percentage:
#     for percent in percents:
#         index = int(round(percent * 100))
#         y_axis[index] = y_axis[index] + 1
total_games = len(intial_state[0]) + len(intial_state[1]) + len(intial_state[2])

print("Block 3")
print("The highest percentage that has been reducted was " + str(highest_percent))
print("The highest reduction of states was " + str(highest_reduction[0])  + " with originaly " + str(highest_reduction[1]) + " states")
print("The largest block was " + str(max_block[0]) + " in a game with originaly " + str(max_block[1]))
print("The average reduction percentage is " + str(percent_sum / total_games))
print("The average reduction when at least something was reduced is " + str(percent_sum_no_zero / no_zero_counter))
print("The average reduction of states is " + str(total_reduction / total_games))
print("The average reduction of states when at least something was reduced is " + str(total_reduction_no_zero / no_zero_counter))
print("The average block size is " + str(avg_block_size_total / total_games))
print("The number of reduced games is " + str(reduction_counter) + " which was " + str(100 * reduction_counter/total_games) + "%")
print("The total amount of games are " + str(total_games))

# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# ax.bar(np.arange(101), y_axis)
# plt.xticks(np.arange(101))
# # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

# plt.show()


print("done")
