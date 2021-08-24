class tree:
    def value(self,array, posi_array ):
        
        return(array[posi_array])
    
    def right(self,array,posi_right):
        posi =  posi_right + int(len(posi_right)/2)
        return(array[posi])
    def left(self,array,posi_left):
        posi =  posi_left - int(len(posi_left)/2)
        return(array[posi])
   


array_tree= [2,4,10,8,3]
complete_tree = tree()
posi_tree= int(len(array_tree)/2)
root = complete_tree.value(array_tree,posi_tree)
right=complete_tree.right(array_tree,posi_tree)
left= complete_tree.left(array_tree,posi_tree)
