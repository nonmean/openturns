#! /usr/bin/env python

from openturns import *

TESTPREAMBLE()
RandomGenerator.SetSeed(0)

try:
    # Instantiate one distribution object
    distribution = ZipfMandelbrot(15, 1.2, 2.)
    print("Distribution ", repr(distribution))
    print("Distribution ", distribution)

    # Is this distribution elliptical ?
    print("Elliptical = ", distribution.isElliptical())

    # Is this distribution continuous ?
    print("Continuous = ", distribution.isContinuous())

    # Test for realization of distribution
    oneRealization = distribution.getRealization()
    print("oneRealization=", repr(oneRealization))

    # Test for getRange
    print("getRange=", repr(distribution.getRange()))

    # Test for sampling
    size = 1000
    oneSample = distribution.getSample(size)
    print("oneSample first=", repr(oneSample[0]), " last=", repr(oneSample[1]))
    print("mean=", repr(oneSample.computeMean()))
    print("covariance=", repr(oneSample.computeCovariance()))

    # size = 100;
    # for i in range(2):
    # msg = ''
    # if FittingTest::ChiSquared(distribution.getSample(size), distribution).getBinaryQualityMeasure():
    # msg = "accepted"
    # else:
    # msg = "rejected"
    # print "ChiSquare test for the generator, sample size=", size, " is", msg
    # size *= 10;

    # Define a point
    point = Point(distribution.getDimension(), 5.0)
    print("Point= ", repr(point))

    # Show PDF and CDF of point
    eps = 1e-5
    # PDF value
    PDF = distribution.computePDF(point)
    print("pdf     =%.6f" % PDF)
    # by the finite difference technique from CDF
    print("pdf (FD)=%.6f" % (distribution.computeCDF(
        point + Point(1, 0)) - distribution.computeCDF(point + Point(1, -1))))

    # derivative of the PDF with regards the parameters of the distribution
    CDF = distribution.computeCDF(point)
    print("cdf=%.6f" % CDF)
    # quantile
    quantile = distribution.computeQuantile(0.95)
    print("quantile=", repr(quantile))
    print("cdf(quantile)=%.6f" % distribution.computeCDF(quantile))
    print("entropy=%.6f" % distribution.computeEntropy())
    mean = distribution.getMean()
    print("mean=", repr(mean))
    standardDeviation = distribution.getStandardDeviation()
    print("standard deviation=", repr(standardDeviation))
    skewness = distribution.getSkewness()
    print("skewness=", repr(skewness))
    kurtosis = distribution.getKurtosis()
    print("kurtosis=", repr(kurtosis))
    covariance = distribution.getCovariance()
    print("covariance=", repr(covariance))
    parameters = distribution.getParametersCollection()
    print("parameters=", repr(parameters))
    for i in range(6):
        print("standard moment n=", i, " value=",
              distribution.getStandardMoment(i))
    print("Standard representative=", distribution.getStandardRepresentative())

except:
    import sys
    print("t_ZipfMandelbrot_std.py", sys.exc_info()[0], sys.exc_info()[1])
