#!/usr/bin/env python
# mdp implementation needs to go here
from read_config import read_config



class mdp:


    def __init__(self):
        
        self.config = read_config()
        self.move_list = self.config["move_list"]
        self.map_size = self.config["map_size"]
        self.start = self.config["start"]
        self.goal = self.config["end"]
        self.walls = self.config["walls"]
        self.pits = self.config["pits"]
        self.discount = self.config["discount_factor"]
        self.step = self.config["reward_for_each_step"]
        self.hit_wall = self.config["reward_for_hitting_wall"]
        self.reaching_goal = self.config["reward_for_reaching_goal"]
        self.falling_pit = self.config["reward_for_falling_in_pit"]
        end_states = pits
        end_states.append(goal)
        current_pos = start
        self.cur_val = defaultdict(lambda: 0)
        cur_val[goal] = reward_for_reaching_goal
        for i in pits:
            cur_val[i] = reward_for_falling_in_pit
        self.tmp_val = defaultdict(lambda: 0)
        for i in range(self.config["max_iterations"]):
        
            for r in range(self.map_size[0]):
                for c in range(self.map_size[1]):
                    hululu(r,c) 
         
            for i in self.cur_val.keys():
                self.cur_val[i] = self.tmp_val[i]
        print "WHAT THE FUCK?"
        for r in range(self.map_size[0]):
            for c in range(self.map_size[1]):
                print self.cur_val[[r,c]]   

    def hululu(self, r, c):
        print "HUHUHU"
        cur_pos = [r,c]
        cur_best = 0
        for i in self.move_list:
            move_sum = 0
            for pr in self.move_list: 

                tmp_pos = cur_pos + pr

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
                if tmp_pos[0] < 0 or tmp_pos[1] < 0 or tmp_pos in self.walls:
                    new_val = prob*(self.hit_wall + self.discount * self.cur_val[cr_pos])
                elif tmp_pos[0] > self.map_size[0] or tmp_pos[1] > self.map_size[1]:
                    new_val = prob*(self.hit_wall + self.discount * self.cur_val[cr_pos])
                elif tmp_pos in self.pits:
                    new_val = prob * (self.falling_pit + self.step + self.discount * self.cur_val[tmp_pos])
                elif eql(tmp_pos, self.goal):
                    new_val = prob * (self.reaching_pit + self.step + self.discount * self.cur_val[tmp_pos])
                else:
                    new_val = prob * (self.step + self.discount * self.cur_val[tmp_pos])
                move_sum += new_val
        
            if move_sum > cur_best:
                cur_best = move_sum
        self.temp_val[cur_pos] = cur_best

            
                                    

    def eql(self, a, b):
        if sum(i != j for i, j in zip(a, b)) > 0:
            return False
        else:
            return True
