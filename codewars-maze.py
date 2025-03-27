

'''
Task description
https://www.codewars.com/kata/58663693b359c4a6560001d6

Testing data
direction = ["N","N","N","W","W","E","E","E","N","N"]  - out of maze
direction = ["N","N","N","N","N","E","E","E","N","N"] -  hit into wall
direction = ["N","N","N","N","N","E","E","E","E","S"] -  lost
'''


# Initial data
direction = ["N","N","N","N","N","E","E","E","E","E"] 

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

size = len(maze[0]) # borders
	
# Finding start and end points	

positions_s = {"x": None, "y": None}  # start
positions_e = {"x": None, "y": None}  # end
	
def pos(a, positions):
	for row_idx, row in enumerate(maze):
		for col_idx, value in enumerate(row):
			if value == a:
				positions["x"] = row_idx
				positions["y"] = col_idx
				break  # Exit loop once found
	return positions
    
start_point = pos(2,positions_s)  # Find index of number 2
end_point = pos(3,positions_e)
print(start_point) 			# {'x': 6, 'y': 1}
print(end_point)   			# {'x': 1, 'y': 6}


# Position calculation
def moving(start_point, direction):

	if direction == "N":
		start_point["x"] -= 1
	elif direction == "E":
		start_point["y"] += 1
	elif direction == "W":
		start_point["y"] -= 1 
	else:                           # direction == "S":
		start_point["x"] += 1
        
	return start_point

# Main logic
steps = 0
result = ''
for i in direction:
	new_start_point = moving(start_point, i)
	print(new_start_point) 
	if (maze[new_start_point["x"]][new_start_point["y"]] == 1) or (new_start_point["x"] not in range(0, size+1)) or (new_start_point["y"] not in range(0, size+1)):
		result += "Dead"
		break
	elif new_start_point["x"] == end_point["x"] and new_start_point["y"] == end_point["y"]:
		result += "Finish"
		break
	else:
		steps += 1

# Printing result
if steps == len(direction) and result == '':
	print('Lost')
else:	
	print(result)	
