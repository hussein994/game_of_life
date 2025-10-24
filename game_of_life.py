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

	paded_frame = numpy.pad(frame, 1, mode="constant")

	return frame


while True :
	print(frame)
	time.sleep(1)
	os.system("cls")
	compute_next_frame(frame)