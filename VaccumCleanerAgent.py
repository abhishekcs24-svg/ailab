
import random


class Environment:
    def __init__(self):
        
        self.locationCondition = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}


class SimpleReflexVacuumAgent:
    def __init__(self, environment):
        
        print(environment.locationCondition)

        
        score = 0

       
        vacuumLocation = random.randint(0, 1)

        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A.")
           
            if environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
                
                environment.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned.")
            else:
                print("Location A is Clean.")

            print("Moving to Location B...")
           
            if environment.locationCondition['B'] == 1:
                print("Location B is Dirty.")
               
                environment.locationCondition['B'] = 0
                score += 1
                print("Location B has been Cleaned.")
            else:
                print("Location B is Clean.")

        else:
            print("Vacuum is randomly placed at Location B.")
           
            if environment.locationCondition['B'] == 1:
                print("Location B is Dirty.")
              
                environment.locationCondition['B'] = 0
                score += 1
                print("Location B has been Cleaned.")
            else:
                print("Location B is Clean.")

            print("Moving to Location A...")
            
            if environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
               
                environment.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned.")
            else:
                print("Location A is Clean.")

      
        print(environment.locationCondition)
       
        print("Performance Measurement: " + str(score))

theEnvironment = Environment()

theVacuum = SimpleReflexVacuumAgent(theEnvironment)
        
    
