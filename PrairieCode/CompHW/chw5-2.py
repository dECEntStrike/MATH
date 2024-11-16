import numpy as np
import numpy.linalg as la


num_friend_groups = 0
nulFriends = nullspace(friends)
for f in nulFriends[0]:
    num_friend_groups = num_friend_groups + 1

#count the number of 1s in that column
num_meme_spread = 0
index = 111 % num_friend_groups
for i in nulFriends[:, index]:
    num_meme_spread = num_meme_spread + i