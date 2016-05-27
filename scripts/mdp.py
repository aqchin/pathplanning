# mdp implementation needs to go here
def mdp ():
    
    config = read_config()
    move_list = self.config["move_list"]
    map_size = self.config["map_size"]
    start =
    goal =
    walls =
    pits = 
    end_states = pits
    end_states.append(goal)
    current_pos = start
    cur_val = defaultdict(lambda: 0)
    cur_val[goal] = reward_for_reaching_goal
    for i in pits:
        cur_val[i] = reward_for_falling_in_pit
    tmp_val = defaultdict(lambda: 0)
    for i in range(max_iterations):
        

        for r in range(map_size[0]):
            for c in range(map_size[1]):
                hululu(r,c):   
         
        for i in cur_val.keys():
            cur_val(i) = tmp_val(i)
def hululu(r, c):
    cur_pos = [r,c]
    cur_best = 0
    for i in move_list:
        move_sum = 0
        for pr in move_list: 

            tmp_pos = cur_pos + pr
            pr_s = set(pr)
            prob = 0.0
            if eql(pr, i):
                prob = prob_move_forward
            elif eql(([-x for x in i]), pr):
                prob = prob_move_backward
            else:
                if i[1] == 0:
                    tmp = [i[1], i[0]]
                    if eql(tmp, pr):
                        prob = prob_move_left
                    else:
                        prob = prob_move_right
                else:
                    tmp = [-i[1]. i[0]]
                    if eql(tmp, pr):
                        prob = prob_move_left
                    else:
                        prob = prob_move_right
            if tmp_pos[0] < 0 or tmp_pos[1] < 0 or tmp_pos in walls:
                new_val = prob*(reward_for_hitting_wall + discount * cur_val[cr_pos]
            elif tmp_pos[0] > map_size[0] or tmp_pos[1] > map_size[1]:
                new_val = prob*(reward_for_hitting_wall + discount * cur_val[cr_pos]
            elif tmp_pos in pits:
                new_val = prob * (reward_for_falling_in_pit + reward_for_each_step + discount * cur_val[tmp_pos])
            elif eql(tmp_pos, goal):
                new_val = prob * (reward_for_falling_in_pit + reward_for_each_step + discount * cur_val[tmp_pos])
            else:
                new_val = prob * (reward_for_each_step + discount * cur_val[tmp_pos])
            move_sum += new_val
        
        if move_sum > cur_best:
            cur_best = move_sum
    temp_val(cur_pos) = cur_best

            
                                    

def eql(a, b):
    if sum(i != j for i, j in zip(a, b)) > 0:
        return False
    else:
        return True
