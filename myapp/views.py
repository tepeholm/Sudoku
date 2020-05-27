from django.shortcuts import render, redirect
from .forms import sudokuForm 
from .sudoku import solve, print_board
from .solver import Solver





def main(request):
    
    if request.GET:
        # Check if the get field is a valid sudoku puzzle
        valid = True
        values = dict()

        for n in "123456789":
            for l in "ABCDEFGHI":
                # Check that all squares are in the request
                if l+n not in request.GET:
                    valid = False
                else:
                    # If the key is in the get, check if the value is valid
                    if len(request.GET[l+n]) > 1:
                        valid = False
                    elif len(request.GET[l+n]) == 1:
                        if request.GET[l+n] not in "123456789":
                            
                            # If there was an invalid character in the input
                            valid = False
                        else:
                            # Add the value to the values dictionary
                            values[l+n] = request.GET[l+n]
        
        board = [[],[],[],[],[],[],[],[],[]]
        i = 0
        for n in "123456789":
            for l in "ABCDEFGHI":
                try:
                    board[i].append(int(values[l+n]))
                except:
                    board[i].append(0)
            i = i + 1

        solve(board) 

        yzat = {}
        
        for n in "123456789":
            i = 0
            for l in "ABCDEFGHI":
                yzat[l+n] = board[int(n)-1][i]
                i = i + 1

        if valid:
            print("Valid input, trying to solve")
            print(board)
            print(values)
        
            if values:
                return render(request, 'main.html', {'values': yzat})
        print("Invalid input, redirecting")
        return redirect('')
    else:
        
        return render(request, 'main.html')


