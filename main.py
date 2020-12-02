from puzzle import Puzzle
from solver import Solver
import random
import matplotlib.pyplot as plt 
if __name__ == "__main__":
    #goal board
    board = [[0,1,2],[3,4,5],[6,7,8]]

    ################# Heuristic 1 ###########################
    print("running a* using heuristic 1 : sum of distance of pieces")
    puzzle = Puzzle(board,'sum_distance')
    puzzle = puzzle.shuffle(60)
    #save board to use it later
    board = puzzle.board
    s = Solver(puzzle)
    p = s.solve()

    #save plot of number nodes as function of depth 
    plt.plot(s.num_seen,s.depth)
    plt.xlabel('nodes visited');plt.ylabel('depth')  
    plt.savefig('graph_heuristic_manhattan')


    steps = 0
    f = open("log_heuristic_distance.txt", "w")

    for node in p:
        f.write(f"Step: {steps+1}"+'\n')
        f.write("      action: " + str(node.action)+'\n')
        f.write("      current_state: "+str(node.puzzle.board[0])+'\n')
        f.write("                   : "+str(node.puzzle.board[1])+'\n')
        f.write("                   : "+str(node.puzzle.board[2])+'\n')
        steps += 1
    f.close()
    print("Total number of steps: " + str(steps))


    ####################### Heuristic 2 ###############################
    print("running a* using heuristic 2 : sum of misplaced pieces")
    puzzle = Puzzle(board,'sum_not_placed')
    s = Solver(puzzle)
    p = s.solve()
    steps = 0

    #save plot of number nodes as function of depth 
    plt.plot(s.num_seen,s.depth)
    plt.xlabel('nodes visited');plt.ylabel('depth') 
    plt.savefig('graph_heuristic_sum_misplaced')

    f = open("log_heuristic_sum_not_placed.txt", "w")
    for node in p:
        f.write(f"Step: {steps+1}"+'\n')
        f.write("      action: " + str(node.action)+'\n')
        f.write("      current_state: "+str(node.puzzle.board[0])+'\n')
        f.write("                   : "+str(node.puzzle.board[1])+'\n')
        f.write("                   : "+str(node.puzzle.board[2])+'\n')
        steps += 1
    f.close()
    print("Total number of steps: " + str(steps))