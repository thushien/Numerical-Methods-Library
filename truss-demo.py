from numerics.fea import TrussAnalysis
import numpy as np

# Example: Analyze a single member at 45 degrees
member = TrussAnalysis(E=210e9, A=0.005, L=2.0, theta=45)
print("Stiffness Matrix for Member:")
print(member.local_stiffness())
