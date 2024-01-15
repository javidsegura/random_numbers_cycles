import numpy as np

def random(n,seed,a,c,m): #Note this parameters fall under specfic conditions for the values they can take.
      global output
      random_numbers = []
      random_numbers.append(seed)
      for i in range(1,n+1):
            random_numbers.append(round((a*random_numbers[-1]+c) % m,3))
      global length  # To be used for the range in the second function
      length = len(random_numbers)
      output = [i / m for i in random_numbers] # Division by m for all i's in the sequence
      return output


def cycle_detect(x):
      results = list()  #Aggrupation of results
      for i in range(length): # i takes all possible indexed of the random numbers list
            for j in range(1,length): # starts 1 so that it does not count itself
                  if output[i] == output[j]:
                        results.append(f"Cycle ends at value '{output[j]}' in position '{j}', the original cyle is composed of {output[:j]} \n")
                        return results

      
            
if __name__ == "__main__":
      first_list = random(n = 10,seed = 4,a = 13, c = 0, m = 64)
      print("-"*10,"1st list of random numbers:", "-"*10,"\n",first_list) # Parameters for the random number generation 
      print(cycle_detect(first_list))
      second_list = random(10,2024,1103515245,12345,2**32)
      print("\n","-"*10,"Second list of r.nº:", "-"*10, "\n", second_list) # Error on this printig          
      print(cycle_detect(second_list))
