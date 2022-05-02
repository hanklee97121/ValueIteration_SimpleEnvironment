import numpy as np

#use linked list to initialize environment
class LinkedNode():
  def __init__(self, val = 0, up = None, down = None, vs = 0):
    '''
    Arg:
      val: value of current node
      up: upper node to the current node (take action 'U' to move from current node)
      down: lower node to the current node (take action 'D' to move from current node)
      vs: estimate value of current node
    '''
    self.val = val
    self.up = up
    self.down = down
    self.vs = vs

#initialize environment
#fake terminal
terminal = LinkedNode()

#last layer (5)
l_0 = LinkedNode(val = 30, up = terminal, down = terminal)
l_1 = LinkedNode(val = -4, up = terminal, down = terminal)
l_2 = LinkedNode(val = 59, up = terminal, down = terminal)
l_3 = LinkedNode(val = 30, up = terminal, down = terminal)
l_4 = LinkedNode(val = 59, up = terminal, down = terminal)
l_5 = LinkedNode(val = 29, up = terminal, down = terminal)

#second last layer (4)
sl_0 = LinkedNode(val = 59, up = l_0, down = l_1)
sl_1 = LinkedNode(val = 36, up = l_1, down = l_2)
sl_2 = LinkedNode(val = 30, up = l_2, down = l_3)
sl_3 = LinkedNode(val = 40, up = l_3, down = l_4)
sl_4 = LinkedNode(val = 60, up = l_4, down = l_5)

#third layer 
t_0 = LinkedNode(val = 0, up = sl_0, down = sl_1)
t_1 = LinkedNode(val = 3, up = sl_1, down = sl_2)
t_2 = LinkedNode(val = 2, up = sl_2, down = sl_3)
t_3 = LinkedNode(val = -1, up = sl_3, down = sl_4)

#second layer
s_0 = LinkedNode(val = 1, up = t_0, down = t_1)
s_1 = LinkedNode(val = 0, up = t_2, down = t_3)

#start node
head = LinkedNode(val = 0, up = s_0, down = s_1)

state_space = [l_0, l_1, l_2, l_3, l_4, l_5, sl_0, sl_1, sl_2, sl_3, sl_4, t_0, t_1, t_2, t_3, s_0, s_1, head]
action_space = ['U', 'D']

#hyperparameter initialization
theta = 0.1
gamma = 1
delta = 100
iteration = 0

#value iteration loop
while delta > theta and iteration <= 10:
  delta = 0
  for s in state_space:
    old_vs = s.vs
    down_value = s.down.val + gamma*s.down.vs
    up_value = s.up.val + gamma*s.up.vs
    s.vs = max(down_value, up_value)
    delta = max(delta, abs(old_vs - s.vs))
  iteration += 1

#output the best policy
policy = []
current = head
while current.up.up:
  down_value = current.down.val + gamma*current.down.vs
  up_value = current.up.val + gamma*current.up.vs
  if up_value > down_value:
    current = current.up
    policy.append('U')
  else:
    current = current.down
    policy.append('D')
print(f'iteration is {iteration:.0f}')
print(f'Delta value is {delta:.1f}.')
print(f'The best policy after value iteration is:{policy}')
