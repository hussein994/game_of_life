import numpy
import os
import time

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 1, 1, 1, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0]])

def compute_number_of_neighbors(paded_frame, index_row, index_column):
	def compute_number_of_neighbors(paded_frame, index_row, index_column):

    # Pour calculer le nombre de voisin vivant d’une cellule il suffit de sommer les valeurs de ses 8 cases voisines. 
    # Le résultat de cette somme est égale au nombre de voisins.
    
		number_of_neighbors = 0
		number_of_neighbors += paded_frame[index_row - 1, index_column - 1]
		number_of_neighbors += paded_frame[index_row - 1, index_column]
		number_of_neighbors += paded_frame[index_row - 1, index_column + 1]
		number_of_neighbors += paded_frame[index_row, index_column - 1]
		number_of_neighbors += paded_frame[index_row, index_column + 1]
		number_of_neighbors += paded_frame[index_row + 1, index_column -1]
		number_of_neighbors += paded_frame[index_row + 1, index_column]
		number_of_neighbors += paded_frame[index_row + 1, index_column + 1]

	
		return number_of_neighbors


def compute_next_frame(frame):
	# Step 1: Calculate the padded matrix
    paded_frame = numpy.pad(frame, 1, mode='constant')
    

    # Step 2:

    for index_row in range(1, 8):
        for index_column in range(1, 8):
            # Step 3: 
            neighbors = compute_number_of_neighbors(paded_frame, index_row, index_column)
            # Step 4: 
            current_cell = paded_frame[index_row, index_column]
            if current_cell == 1:  
                if neighbors == 2 or neighbors == 3:
                    frame[index_row-1, index_column-1] = 1  
                else:
                    frame[index_row-1, index_column-1] = 0 
            else: 
                if neighbors == 3:
                    frame[index_row-1, index_column-1] = 1  
                else:
                    frame[index_row-1, index_column-1] = 0
    return frame


while True :
	print(frame)
	time.sleep(1)
	os.system("cls")
	compute_next_frame(frame)