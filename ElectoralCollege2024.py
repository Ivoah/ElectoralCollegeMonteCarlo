# This could be a dataclass: https://docs.python.org/3/library/dataclasses.html
# I would also separate this generic class from the year specific data in this file.
# Maybe put the data in a JSON file.
class ElectoralCollegeState:
    def __init__(self, abbreviation, electoralPoints, probabilityRed):
        self.abbreviation = abbreviation
        self.electoralPoints = electoralPoints
        self.probabilityRed = probabilityRed


# Odds taken from Polymarket - https://polymarket.com/elections

CONSENSUS_ELECTORAL_POINTS_RED = 219
CONSENSUS_ELECTORAL_POINTS_BLUE = 226

BATTLEGROUND_ELECTORAL_COLLEGE_STATES = [
    ElectoralCollegeState("AZ", 11, 0.60),
    ElectoralCollegeState("GA", 16, 0.58),
    ElectoralCollegeState("MI", 15, 0.41),
    ElectoralCollegeState("NC", 16, 0.57),
    ElectoralCollegeState("NV", 6, 0.50),
    ElectoralCollegeState("PA", 19, 0.51),
    ElectoralCollegeState("WI", 10, 0.40),
]

ALL_ELECTORAL_COLLEGE_STATES = [
    ElectoralCollegeState("AL", 9, 0.98),
    ElectoralCollegeState("AK", 3, 0.90),
    ElectoralCollegeState("AZ", 11, 0.60),
    ElectoralCollegeState("AR", 6, 0.98),
    ElectoralCollegeState("CA", 54, 0.02),
    ElectoralCollegeState("CO", 10, 0.03),
    ElectoralCollegeState("CT", 7, 0.02),
    ElectoralCollegeState("DE", 3, 0.03),
    ElectoralCollegeState("FL", 30, 0.84),
    ElectoralCollegeState("GA", 16, 0.58),
    ElectoralCollegeState("HI", 4, 0.02),
    ElectoralCollegeState("ID", 4, 0.99),
    ElectoralCollegeState("IL", 19, 0.02),
    ElectoralCollegeState("IN", 11, 0.98),
    ElectoralCollegeState("IA", 6, 0.90),
    ElectoralCollegeState("KS", 6, 0.97),
    ElectoralCollegeState("KY", 8, 0.98),
    ElectoralCollegeState("LA", 8, 0.98),
    ElectoralCollegeState("ME_1", 3, 0.10),
    ElectoralCollegeState("ME_2", 1, 0.79),
    ElectoralCollegeState("MD", 10, 0.02),
    ElectoralCollegeState("MA", 11, 0.02),
    ElectoralCollegeState("MI", 15, 0.41),
    ElectoralCollegeState("MN", 10, 0.07),
    ElectoralCollegeState("MS", 6, 0.98),
    ElectoralCollegeState("MO", 10, 0.98),
    ElectoralCollegeState("MT", 4, 0.98),
    ElectoralCollegeState("NE_1", 4, 0.97),
    ElectoralCollegeState("NE_2", 1, 0.19),
    ElectoralCollegeState("NV", 6, 0.50),
    ElectoralCollegeState("NH", 4, 0.14),
    ElectoralCollegeState("NJ", 14, 0.04),
    ElectoralCollegeState("NM", 5, 0.09),
    ElectoralCollegeState("NY", 28, 0.02),
    ElectoralCollegeState("NC", 16, 0.57),
    ElectoralCollegeState("ND", 3, 0.98),
    ElectoralCollegeState("OH", 17, 0.93),
    ElectoralCollegeState("OK", 7, 0.99),
    ElectoralCollegeState("OR", 8, 0.03),
    ElectoralCollegeState("PA", 19, 0.51),
    ElectoralCollegeState("RI", 4, 0.02),
    ElectoralCollegeState("SC", 9, 0.98),
    ElectoralCollegeState("SD", 3, 0.99),
    ElectoralCollegeState("TN", 11, 0.97),
    ElectoralCollegeState("TX", 40, 0.88),
    ElectoralCollegeState("UT", 6, 0.98),
    ElectoralCollegeState("VT", 3, 0.02),
    ElectoralCollegeState("VA", 13, 0.10),
    ElectoralCollegeState("WA", 12, 0.02),
    ElectoralCollegeState("WV", 4, 0.99),
    ElectoralCollegeState("WI", 10, 0.40),
    ElectoralCollegeState("WY", 3, 0.99),
    ElectoralCollegeState("DC", 3, 0.01)
]
