import random
import sys
import statistics

from ElectoralCollege2024 import *

# Could also be a dataclass
class ElectoralCollegeResult():
    def __init__(self, redElectoralPoints, blueElectoralPoints):
        self.redElectoralPoints = redElectoralPoints
        self.blueElectoralPoints = blueElectoralPoints

    def isRedWin(self):
        return self.redElectoralPoints >= 270
    
    def isBlueWin(self):
        return self.blueElectoralPoints >= 270
    
    def isTie(self):
        return (self.blueElectoralPoints < 270) and (self.redElectoralPoints < 270)

class ElectoralCollegeMonteCarloSimulator():
    # PEP8 style says there should be no whitespace around '=' for default parameters
    def __init__(self, electoralCollegeStates, consensusPointsRed = 0, consensusPointsBlue = 0):
        self.electoralCollegeStates = electoralCollegeStates
        self.consensusPointsRed = consensusPointsRed
        self.consensusPointsBlue = consensusPointsBlue
    
    def getExpectedPointsRed(self):
        # Parentheses around s.xxx * s.xxx are redundant
        return self.consensusPointsRed + sum((s.probabilityRed * s.electoralPoints) for s in self.electoralCollegeStates)
    
    def getExpectedPointsBlue(self):
        # Prentheses are redundant
        return self.consensusPointsBlue + sum(((1 - s.probabilityRed) * s.electoralPoints) for s in self.electoralCollegeStates)
    
    def sampleElectoralCollege(self):
        redElectoralPoints = self.consensusPointsRed
        blueElectoralPoints = self.consensusPointsBlue
        for state in self.electoralCollegeStates:
            if random.random() < state.probabilityRed:
                redElectoralPoints += state.electoralPoints
            else:
                blueElectoralPoints += state.electoralPoints
        
        return ElectoralCollegeResult(redElectoralPoints, blueElectoralPoints)
        
    def runMonteCarloSimulations(self, numIterations = 100000):
        # This could be a list comprehension
        monteCarloSimulations = []
        for i in range(numIterations):
            monteCarloSimulations.append(self.sampleElectoralCollege())

        return monteCarloSimulations

def main():
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        print(f"Usage: {sys.argv[0]} <num_iterations> [-a]")
        return -1

    numIterations = int(sys.argv[1])
    # Unnecessary parentheses, '==' has higher precedence than 'and'
    simulateAllStates = (len(sys.argv) == 3) and (sys.argv[2] == "-a")

    if simulateAllStates:
        simulator = ElectoralCollegeMonteCarloSimulator(ALL_ELECTORAL_COLLEGE_STATES)
    else:
        simulator = ElectoralCollegeMonteCarloSimulator(BATTLEGROUND_ELECTORAL_COLLEGE_STATES, CONSENSUS_ELECTORAL_POINTS_RED, CONSENSUS_ELECTORAL_POINTS_BLUE)

    print("<<< Electoral College Monte Carlo Simulations >>>\n")
    simulations = simulator.runMonteCarloSimulations(numIterations)

    # Why use 'filter' here and list comprehensions elsewhere?
    simulationsRedWin = list(filter(lambda s: s.isRedWin(), simulations))
    simulationsBlueWin = list(filter(lambda s: s.isBlueWin(), simulations))
    simulationsTie = list(filter(lambda s: s.isTie(), simulations))

    # Use 'numIterations' instead of recalculating 'len(simulations)'
    probabilityRedWin = len(simulationsRedWin) / len(simulations)
    probabilityBlueWin = len(simulationsBlueWin) / len(simulations)
    probabilityTie = len(simulationsTie) / len(simulations)

    # These could be generator comprehensions instead of list comprehensions
    # Redundant parentheses in if statement
    medianElectoralPointsRedWin = statistics.median([s.redElectoralPoints for s in simulationsRedWin]) if (len(simulationsRedWin) > 0) else 0
    medianElectoralPointsBlueWin = statistics.median([s.blueElectoralPoints for s in simulationsBlueWin]) if (len(simulationsBlueWin) > 0) else 0

    print(f"Probability of red win = {100 * probabilityRedWin:.2f}%")
    print(f"Probability of blue win = {100 * probabilityBlueWin:.2f}%")
    print(f"Probability of tie = {100 * probabilityTie:.2f}%")
    print()

    print(f"Median electoral college vote for red wins = {medianElectoralPointsRedWin}")
    print(f"Median electoral college vote for blue wins = {medianElectoralPointsBlueWin}")

    return 0

# Should be inside an if __name__ == '__main__' guard
main()
# Should have newline at end of file
