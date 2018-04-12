S_ALONE = 0
S_TALKING = 1

#==============================================================================
# Group class:
# member fields: 
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
#==============================================================================

""" CHANGE CHATTING MODE """

class Group:
    
    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0
        
    def join(self, name):
        # add member key to member dictionary
        self.members[name] = S_ALONE
        return
        
        
    #implement   (COMPLETE)     
    def is_member(self, name):
        # return boolean whether name in member dictionary
        return name in self.members.keys()
            
    #implement (COMPLETE)
    def leave(self, name):
        # disconnect name from group
        self.disconnect(name)
        # delete name key from members dictionary
        del self.members[name]
        
    #implement       (complete)      
    def find_group(self, name):
        # set initial state
        found = False
        group_key = 0
        # Check if name is in members
        for k,v in self.chat_grps.items():
            # if name found, update variables and break
            if name in v:
                found = True
                group_key = k
                break
        return found, group_key
        
    #implement  (connect)           
    def connect(self, me, peer):
        #if peer is in a group, join it
        peer_in_group, group_key = self.find_group(peer)
        if peer_in_group == False:
            # update group count for new group
            self.grp_ever += 1
            # create new group key with updated value
            self.chat_grps[self.grp_ever] = [me, peer]
            # update member states
            self.members[me] = S_TALKING
            self.members[peer] = S_TALKING
        else:
            # if already exists, append and update state
            self.chat_grps[group_key].append(me)
            self.members[me] = S_TALKING

    #implement (check this one)         
    def disconnect(self, me):
        # find myself in the group, quit
        group_bool, group_key = self.find_group(me)
        # remove from chat
        self.chat_grps[group_key].remove(me)
        for k, v in self.chat_grps.items():
            if len(v) == 1:
                # if the length of group is 1, delete group and change member state
                self.members[v[0]] = S_ALONE
                del self.chat_grps[k]
                break
        self.members[me] = S_ALONE
        return
        
    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    #implement
    def list_me(self, me):
        # return a list, "me" followed by other peers in my group
        my_list = []
        found, key = self.find_group(me)
        if found:
            # add 'me' first
            my_list.append(me)
            # create temp list and remove 'me'
            temp = self.chat_grps[key] * 1
            temp.remove(me)
            # append temp list to 'me'
            my_list += temp
            return my_list

if __name__ == "__main__":
	g = Group()
	g.join('a')
	g.join('b')
	print(g.list_all())

	g.connect('a', 'b')
	print(g.list_all())