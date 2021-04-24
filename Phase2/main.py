from state_class import CPU, State,BTB
from hdu_class import HDU
states=[None for i in range(5)] # don't change it
predictionEnabled=1
hduob = HDU()
knob2_stallingEnabled= False # don't change it
controlChange = False
cntBranchHazards = 0
cntBranchHazardStalls = 0
controlChange_pc = 0
controlHazard = False
controlHazard_pc = 0
btb = BTB()
ProcessingUnit = CPU(predictionEnabled)
ProcessingUnit.readFile()
master_PC=0
master_cycle=0
# states[0] - fetch
# states[1] - Decode
# states[2] - execute
# states[3] - MemoryAccess
# states[4] - writeback
while True:

    if knob2_stallingEnabled:
        checkDataHazard = hduob.checkDataHazardStalling(states)
        copyOfStates = states[:] 

        for i in reversed(range(5)):
            if(i==0):
                states[i+1] = ProcessingUnit.Fetch(states[i],btb)
                controlChange = states[i+1].predictionOutcome
                controlChange_pc= states[i+1].predictionPC
                # states[i]=None  
            if(i==1):
                if(states[i]==None):
                    continue
                controlHazard,control_hazard_pc,states[i+1] = ProcessingUnit.Decode(states[i],btb)
                states[i]=None         
            if(i==2):
                if(states[i]==None):
                    continue
                ProcessingUnit.Execute(states[i])
                states[i+1]=states[i]
                states[i]=None                
            if(i==3):
                if(states[i]==None):
                    continue
                ProcessingUnit.MemoryAccess(states[i])
                states[i+1]=states[i]
                states[i]=None
            if(i==4):
                if(states[i]==None):
                    continue
                ProcessingUnit.RegisterUpdate(states[i])
                states[i]=None
        
        if states[1].IR != 0 and (not checkDataHazard):
            master_PC+=4

        if(controlChange == True and checkDataHazard == False):
            master_PC = controlChange_pc
        
        vis = False
        if(controlHazard == True and checkDataHazard == False):
            cntBranchHazards+=1
            cntBranchHazardStalls+=1
            master_PC = controlHazard_pc
            # out_states[0] = State(0)
            states[0]=None
            vis = True
        
        if (not vis) and controlHazard and checkDataHazard and predictionEnabled:
            btb.updateState(master_PC)


    else:
        pass
    # master_cycle+=1
    # for i in reversed(range(5)):
    #     if(i==0):
    #         states[i]=State(master_PC)
    #         states[i]=ProcessingUnit.Fetch(states[i])
    #         if(states[i]==None):
    #             continue
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==1):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.Decode(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==2):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.Execute(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==3):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.MemoryAccess(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==4):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.RegisterUpdate(states[i])
    #         states[i]=None
    # if(states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None):
    #     break
    # master_PC += 4
print("Program Executed!!!")