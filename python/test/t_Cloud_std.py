#! /usr/bin/env python

from openturns import *

TESTPREAMBLE()
RandomGenerator.SetSeed(0)

try:
    # Instantiate one distribution object
    dim = 2
    meanPoint = Point(dim, 1.0)
    meanPoint[0] = 0.5
    meanPoint[1] = -0.5
    sigma = Point(dim, 1.0)
    sigma[0] = 2.0
    sigma[1] = 3.0
    R = CorrelationMatrix(dim)
    for i in range(1, dim):
        R[i, i - 1] = 0.5

    distribution1 = Normal(meanPoint, sigma, R)

    # Instantiate another distribution object
    meanPoint[0] = -1.5
    meanPoint[1] = 0.5
    sigma[0] = 4.0
    sigma[1] = 1.0
    for i in range(1, dim):
        R[i, i - 1] = -0.25

    distribution2 = Normal(meanPoint, sigma, R)

    # Test for sampling
    size = 200
    sample1 = distribution1.getSample(size)
    sample2 = distribution2.getSample(size)

    # Create an empty graph
    myGraph = Graph("Normal sample", "x1", "x2", True, "topright")

    # Create the first cloud
    myCloud1 = Cloud(sample1, "blue", "fsquare", "First Cloud")

    # Then, draw it
    myGraph.add(myCloud1)
    myGraph.draw("Graph_Cloud_a_OT.png")

    # Check that the correct files have been generated by computing their
    # checksum

    # Create the second cloud
    myCloud2 = Cloud(sample2, "red", "circle", "Second Cloud")

    # Add it to the graph and draw everything
    myGraph.add(myCloud2)
    myGraph.draw("Graph_Cloud_b_OT.png")

except:
    import sys
    print("t_Cloud_std.py", sys.exc_info()[0], sys.exc_info()[1])
