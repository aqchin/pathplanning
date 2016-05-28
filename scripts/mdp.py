#!/usr/bin/env python
# mdp implementation needs to go here
from read_config import read_config
from operator import add
from collections import defaultdict

class mdp:


    def __init__(self):

        self.config = read_config()
        self.move_list = self.config["move_list"]
        self.map_size = self.config["map_size"]
        self.start = self.config["start"]
        self.goal = self.config["goal"]
        self.walls = self.config["walls"]
        self.pits = self.config["pits"]
        self.discount = self.config["discount_factor"]
        self.step = self.config["reward_for_each_step"]
        self.hit_wall = self.config["reward_for_hitting_wall"]
        self.reaching_goal = self.config["reward_for_reaching_goal"]
        self.falling_pit = self.config["reward_for_falling_in_pit"]
        self.prob_forward = self.config["prob_move_forward"]
        self.prob_backward = self.config["prob_move_backward"]
        self.prob_left = self.config["prob_move_left"]
        self.prob_right = self.config["prob_move_right"]


        current_pos = self.start
        self.cur_val = defaultdict(lambda: 0)
        self.cur_val[tuple(self.goal)] = self.reaching_goal
        for i in self.pits:
            print "PIT"
            self.cur_val[tuple(i)] = self.falling_pit
        self.tmp_val = defaultdict(lambda: 0)
        for r in range(self.map_size[0]):
            for c in range(self.map_size[1]):
                print self.cur_val[(r,c)]
        print "end initial cur val"
        for i in range(self.config["max_iterations"]):
  #      for i in range(1):
            for r in range(self.map_size[0]):
                for c in range(self.map_size[1]):
                    if (r,c) not in self.pits and (r,c) not in self.walls and (r,c) != tuple(self.goal):
                        self.hululu(r,c)


            for k in self.cur_val.keys():
                if list(k) not in self.pits and list(k) not in self.walls and k != tuple(self.goal):

                    self.cur_val[tuple(k)] = self.tmp_val[tuple(k)]

            for r in range(self.map_size[0]):
                for c in range(self.map_size[1]):
                    if i ==0:
                        print self.cur_val[(r,c)]
        self.policy_list = list()
        self.find_policy()
        print "WHAT THE FUCK?"
        for r in range(self.map_size[0]):

            for c in range(self.map_size[1]):
                print self.cur_val[tuple([r,c])]
            print "\n"

        #self.policy_list = list()
        #self.find_policy()
        print "PRINT POLICY"
        print self.policy_list

    def find_policy(self):

        for r in range(self.map_size[0]):
            for c in range(self.map_size[1]):
                if (r,c) == tuple(self.goal):
                    self.policy_list.append("GOAL")
                elif [r,c] in self.pits:
                    self.policy_list.append("PIT")
                elif [r,c] in self.walls:
                    self.policy_list.append("WALL")
                else:
                    max_prob = -100000
                    direction = 'N'
                    for i in self.move_list:
                        directio = 'N'
                        if tuple(i) == (0,1):
                            directio = 'E'
                        elif tuple(i) == (0,-1):
                            directio = 'W'
                        elif tuple(i) == (-1,0):
                            directio = 'N'
                        else:
                            directio = 'S'
                        pos_f = map(add, [r,c], i)
                        pos_b = map(add, [r,c], [-x for x in i])
                        pos_l = 0.0
                        pos_r = 0.0
                        if i[1] == 0:
                            pos_l = [r, c + i[0]]
                            pos_r = [r, c - i[0]]
                        else:
                            pos_l = [r - i[1], c]
                            pos_r = [r + i[1], c]
                        if r == 1 and c == 2:
                            print i
                            print directio
                            print pos_f, pos_b, pos_l, pos_r
                        tmp_max = self.prob_forward*self.cur_val[tuple(pos_f)]
                        tmp_max += self.prob_backward*self.cur_val[tuple(pos_b)]
                        tmp_max += self.prob_left*self.cur_val[tuple(pos_l)]
                        tmp_max += self.prob_right*self.cur_val[tuple(pos_r)]
                        if r == 1 and c == 2:
                            print tmp_max
                        if tmp_max > max_prob:
                            max_prob = tmp_max
                            direction = directio
                        if tuple(pos_f) == tuple(self.goal):
                            max_prob = 999999
                            direction = directio
                    self.policy_list.append(direction)


    def hululu(self, r, c):

        cur_pos = [r,c]
        cur_best = -10000000
        for i in self.move_list:
            move_sum = 0
            for pr in self.move_list:

                tmp_pos = map(add, cur_pos, pr)
 #               if r == 0 and c == 2:
 #                   print "tmp pos ", tmp_pos
                prob = 0.0
                if self.eql(pr, i):
                    prob = self.prob_forward
                elif self.eql(([-x for x in i]), pr):
                    prob = self.prob_backward
                else:
                    if i[1] == 0:
                        tmp = [i[1], i[0]]
                        if self.eql(tmp, pr):
                            prob = self.prob_left
                        else:
                            prob = self.prob_right
                    else:
                        tmp = [-i[1], i[0]]
                        if self.eql(tmp, pr):
                            prob = self.prob_left
                        else:
                            prob = self.prob_right


                if tmp_pos[0] < 0 or tmp_pos[1] < 0 or tmp_pos in self.walls:
                    new_val = prob*(self.hit_wall + self.discount * self.cur_val[tuple(cur_pos)])
                elif tmp_pos[0] > self.map_size[0] or tmp_pos[1] > self.map_size[1]:
                    new_val = prob*(self.hit_wall + self.discount * self.cur_val[tuple(cur_pos)])
                elif tmp_pos in self.pits:
                    new_val = prob * (self.falling_pit + self.step + self.discount * self.cur_val[tuple(tmp_pos)])
                elif self.eql(tmp_pos, self.goal):
                    new_val = prob * (self.reaching_goal + self.step + self.discount * self.cur_val[tuple(tmp_pos)])
                else:
                    new_val = prob * (self.step + self.discount * self.cur_val[tuple(tmp_pos)])
                move_sum += new_val

            if move_sum > cur_best:
                cur_best = move_sum

        self.tmp_val[tuple(cur_pos)] = cur_best




    def eql(self, a, b):
        if sum(i != j for i, j in zip(a, b)) > 0:
            return False
        else:
            return True
