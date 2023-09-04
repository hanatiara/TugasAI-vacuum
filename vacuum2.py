import random
class Environment(object):
    def __init__(self):
        self.locationCondition={'A':'0','B':''}
        self.locationCondition['A']=random.randint(0,1)
        self.locationCondition['B']=random.randint(0,1)

class VacuumAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        vacuumspace=random.randint(0,1)
        shape_of_dirt=random.randint(1,2)
        size_of_brush=random.randint(10,40)
        score=0
        if(vacuumspace==0):
            print("VacuumCleaner is randomly start from A")
            if(Environment.locationCondition['A']==1):
                print("Location A is dirty")
                Environment.locationCondition['A']=0;
                if(shape_of_dirt==1):
                    if(size_of_brush<=20):
                        score+=1
                    else:
                        score+=2;
                else:
                    if(size_of_brush<=20):
                        score-=1
                    else:
                        score+=1
            print("Suck the dirt from A..")
            print("Location A has been cleaned..")
            score+=5
            if(Environment.locationCondition['B']==1):
                print("Location B is dirty")
                print("Move Right to reach location B")
                score-=5
                Environment.locationCondition['B']=0;
                if(shape_of_dirt==1):
                    if(size_of_brush==20):
                        score+=1
                    else:
                        score+=2;
                else:
                    if(size_of_brush==20):
                        score-=1
                    else:
                        score+=1
                print("Suck the dirt from B..")
                print("Location B has been cleaned..")
                score+=5
            else:
                if(Environment.locationCondition['B']==1):
                    print("Location B is dirty")
                    print("Move Right to reach location B")
                    score-=5
                    Environment.locationCondition['B']=0;
                    if(shape_of_dirt==1):
                        if(size_of_brush==20):
                            score+=1
                        else:
                            score+=2;
                    else:
                        if(size_of_brush==20):
                            score-=1
                        else:
                            score+=1
                        print("Suck the dirt from B..")
                        print("Location B has been cleaned..")
                        score+=5
                    
        elif(vacuumspace==1):
            print("VacuumCleaner is randomly start from B")
            if(Environment.locationCondition['B']==1):
                print("Location B is dirty")
                Environment.locationCondition['B']=0;
                if(shape_of_dirt==1):
                    if(size_of_brush==20):
                        score+=1
                    else:
                        score+=2;
                else:
                    if(size_of_brush==20):
                        score-=1
                    else:
                        score+=1
                print("Suck the dirt from B..")
                print("Location B has been cleaned..")
                score+=5
                if(Environment.locationCondition['A']==1):
                    print("Location A is dirty")
                    print("Move left to reach location A")
                    score-=5
                    Environment.locationCondition['A']=0;
                    if(shape_of_dirt==1):
                        if(size_of_brush==20):
                            score+=1
                        else:
                            score+=2;
                    else:
                        if(size_of_brush==20):
                            score-=1
                        else:
                            score+=1
                    print("Suck the dirt from A..")
                    print("Location A has been cleaned..")
                    score+=5
        else:
            if(Environment.locationCondition['A']==1):
                print("Location A is dirty")
                print("Move left to reach location A")
                score-=5
                Environment.locationCondition['A']=0;
                if(shape_of_dirt==1):
                    if(size_of_brush==20):
                        score+=1
                    else:
                        score+=2;
                else:
                    if(size_of_brush==20):
                        score-=1
                    else:
                        score+=1
                print("Suck the dirt from A..")
                print("Location A has been cleaned..")
                score+=5
        print(Environment.locationCondition)
        print("Shape of dirt :",shape_of_dirt)
        print("Size of brush :",size_of_brush)
        print("performance measured in environment :" ,score)

theEnvironment = Environment()
theVacuum = VacuumAgent(theEnvironment)
