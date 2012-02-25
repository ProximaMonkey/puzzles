import math
import sys

class Prediction():
    """
    An interval with a start, end, and a score.
    """
    def __init__(self, l):
        self.start = int(l[0])
        self.end = int(l[1])
        self.score = int(l[2])

class PredictionSet():
    """
    A node that contains the best score sum up to a given index. Also contains all predictions that make up that best score. 
    """
    def __init__(self, max_index, best_score, predictions):        
        self.max_index = max_index #predictions must end before or on this index.
        self.best_score = best_score #sum of scores in each prediction
        self.predictions = list(predictions) #list of predictions

class PredictionSets():
    """
    Contains a list of PredictionSets
    Calculates the optimal score in O(nlogn) time using dynamic programming, memoization
    
    Basic Algorithm:
    - Get a list of predictions, and sort by 'end'
    - For each 'end' index value, create an entry into prediction_sets
    -- This entry will store the best possible score up to the index 'end'
    -- Look at the largest element in prediction_sets such that there is no overlap between that element and the PredictionSet we are inserting
    -- Insert the PredictionSet
    - After all insertions have been made, print the total score of the optimal solution 
    """
    def __init__(self, predictions):
        self.predictions_end_order = sorted(predictions, key=lambda p: p.end, reverse=True) 
        self.prediction_sets = []
    
    def print_predictions_end_order(self):
        print 'st end score'
        for p in self.predictions_end_order:
            print p.start, p.end, p.score
            
    def next_largest_prediction_set(self, p):
        if not self.prediction_sets:
            return None
        for ps in reversed(self.prediction_sets):
            if ps.max_index < p.start:
                return ps
            
    def get_optimal_score(self, PRINT_MEMOIZED_DATA=False):
        if not self.predictions_end_order:
            return None
        
        p = self.predictions_end_order.pop()
        self.prediction_sets.append(PredictionSet(p.end, p.score, [p]))        
        
        while self.predictions_end_order:
            p = self.predictions_end_order.pop()
            nlps = self.next_largest_prediction_set(p)
            if not nlps:
                self.prediction_sets.append(PredictionSet(p.end, p.score, [p]))
            else:
                best_score = nlps.best_score + p.score
                previous_best = self.prediction_sets[-1].best_score
                if best_score > previous_best:
                    predictions = nlps.predictions + [p]
                    self.prediction_sets.append(PredictionSet(p.end, best_score,predictions))
        
        if PRINT_MEMOIZED_DATA:
            print "\n---- prediction sets -----"
            print "end score list of predictions"
            for ps in self.prediction_sets:
                sys.stdout.write(str(ps.max_index) + " " + str(ps.best_score))
                for p in ps.predictions:
                    sys.stdout.write(" | " + str(p.start) +","+ str(p.end) +","+ str(p.score))
                sys.stdout.write('\n')
             
        return self.prediction_sets[-1].best_score    
    
def gattaca():
    f = open('input', 'r')
    dna_sequence_length = float(f.readline())
    dna_sequence_lines = int(math.ceil(dna_sequence_length/80))
    dna_sequence = ''
    for i in range(0,dna_sequence_lines):
        dna_sequence += f.readline().strip()
    num_predictions = int(f.readline())    

    predictions = []
    for i in range(0, num_predictions):
        predictions.append(Prediction(f.readline().split()))        
        
    prediction_sets = PredictionSets(predictions)
    
    #prediction_sets.print_predictions_end_order()
    
    print prediction_sets.get_optimal_score()            

if __name__ == '__main__':
    gattaca()
    #unittest.main()
    
    
    
    
