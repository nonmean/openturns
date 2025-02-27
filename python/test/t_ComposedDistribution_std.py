#! /usr/bin/env python

import openturns as ot

ot.TESTPREAMBLE()
ot.PlatformInfo.SetNumericalPrecision(5)

mean = [1.0, 2.0, 3.0]
sigma = [2.0, 3.0, 4.0]

# Create a collection of distribution attente TUI
aCollection = []
try:
    aCollection[10] = ot.Normal()
except:
    pass
# Create a marginal : distribution 1D
marginal = ot.Normal(mean[0], sigma[0])
marginal.setName("First")
marginal.setDescription(["One"])
# Fill the first marginal of aCollection
aCollection.append(marginal)
aCollection[0].setName("First")
# Create a second marginal : distribution 1D
marginal = ot.Normal(mean[1], sigma[1])
marginal.setName("Second")
marginal.setDescription(["Two"])
# Fill the second marginal of aCollection
aCollection.append(marginal)
aCollection[1].setName("Second")
# Create a third marginal : distribution 1D
marginal = ot.Normal(mean[2], sigma[2])
marginal.setName("Third")
marginal.setDescription(["Three"])
# Fill the third marginal of aCollection
aCollection.append(marginal)
aCollection[2].setName("Third")
# Create a copula : IndependentCopula
dim = len(aCollection)
aCopula = ot.IndependentCopula(dim)
aCopula.setName("Independent copula")
print("Copula = ", repr(aCopula))
print("Copula = ", aCopula)
# Instantiate one distribution object
distribution = ot.ComposedDistribution(aCollection, aCopula)
distribution.setName("myDist")
print("Distribution = ", repr(distribution))
print("Distribution = ", distribution)
print("Parameters = ", repr(distribution.getParametersCollection()))
print("Mean = ", repr(distribution.getMean()))
print("Covariance = ", repr(distribution.getCovariance()))
# Is this distribution elliptical ?
print("Elliptical = ", distribution.isElliptical())
# Has this distribution an elliptical copula?
print("Elliptical copula = ", distribution.hasEllipticalCopula())

# Has this distribution an independent copula?
print("Independent copula = ",  distribution.hasIndependentCopula())

# Test for realization of distribution
oneRealization = distribution.getRealization()
print("oneRealization=", repr(oneRealization))

# Test for sampling
size = 10
oneSample = distribution.getSample(size)
print("oneSample=", repr(oneSample))

# Test for sampling
size = 10000
anotherSample = distribution.getSample(size)
print("anotherSample mean=", repr(anotherSample.computeMean()))
print("anotherSample covariance=", repr(anotherSample.computeCovariance()))

# Define a point
zero = ot.Point(dim, 0.0)

# Show PDF and CDF of zero point
zeroPDF = distribution.computePDF(zero)
zeroCDF = distribution.computeCDF(zero)
print("Zero point= ", repr(zero), " pdf=%.6f" %
      zeroPDF, " cdf=%.6f" % zeroCDF)

# Get 95% quantile
quantile = distribution.computeQuantile(0.95)
print("Quantile=", repr(quantile))
print("CDF(quantile)=%.6f" % distribution.computeCDF(quantile))

# Get 5% quantile
quantile = distribution.computeQuantile(0.95, True)
print("Quantile=", repr(quantile))

# Get 95% survival function
inverseSurvival = ot.Point(distribution.computeInverseSurvivalFunction(0.95))
print("InverseSurvival=", repr(inverseSurvival))
print("Survival(inverseSurvival)=%.6f" %
      distribution.computeSurvivalFunction(inverseSurvival))
print("entropy=%.6f" % distribution.computeEntropy())
# Confidence regions
if distribution.getDimension() <= 2:
    threshold = Point()
    print("Minimum volume interval=",
          distribution.computeMinimumVolumeInterval(0.95, threshold))
    print("threshold=", threshold)
    beta = Point()
    levelSet = distribution.computeMinimumVolumeLevelSet(0.95, beta)
    print("Minimum volume level set=", levelSet)
    print("beta=", beta)
    print("Bilateral confidence interval=",
          distribution.computeBilateralConfidenceInterval(0.95, beta))
    print("beta=", beta)
    print("Unilateral confidence interval (lower tail)=",
          distribution.computeUnilateralConfidenceInterval(0.95, False, beta))
    print("beta=", beta)
    print("Unilateral confidence interval (upper tail)=",
          distribution.computeUnilateralConfidenceInterval(0.95, True, beta))
    print("beta=", beta)

# Reference : Normal nD, correlation matrix = identity
ref = ot.Normal(mean, sigma, ot.CorrelationMatrix(dim))
print("Reference=")
print("Zero point= ", repr(zero), " pdf= %.6f" % ref.computePDF(zero), " cdf= %.6f" %
      ref.computeCDF(zero), " quantile= ", repr(ref.computeQuantile(0.95)))

# Extract the marginals
for i in range(dim):
    margin = distribution.getMarginal(i)
    print("margin=", repr(margin))
    print("margin PDF=%.6f" % margin.computePDF([0.0]))
    print("margin CDF=%.6f" % margin.computeCDF([0.0]))
    print("margin quantile=", repr(margin.computeQuantile(0.5)))
    print("margin realization=", repr(margin.getRealization()))

# Extract a 2-D marginal
indices = ot.Indices([1, 0])
print("indices=", repr(indices))
margins = distribution.getMarginal(indices)
print("margins=", repr(margins))
print("margins PDF=%.6f" % margins.computePDF([0.0]*2))
print("margins CDF=%.6f" % margins.computeCDF([0.0]*2))
quantile = margins.computeQuantile(0.5)
print("margins quantile=", repr(quantile))
print("margins CDF(qantile)=%.6f" % margins.computeCDF(quantile))
print("margins realization=", repr(margins.getRealization()))
x = 0.6
y = [0.2]
print("conditional PDF=%.6f" % distribution.computeConditionalPDF(x, y))
print("conditional CDF=%.6f" % distribution.computeConditionalCDF(x, y))
print("conditional quantile=%.6f" %
      distribution.computeConditionalQuantile(x, y))
point = [0.6]*dim
print("sequential conditional PDF=",
      distribution.computeSequentialConditionalPDF(point))
print("sequential conditional CDF=",
      distribution.computeSequentialConditionalCDF(point))
print("sequential conditional quantile=",
      distribution.computeSequentialConditionalQuantile(point))

#

# With a Normal copula
correlation = ot.CorrelationMatrix(dim)
for i in range(1, dim):
    correlation[i - 1, i] = 0.25
anotherCopula = ot.NormalCopula(correlation)
anotherCopula.setName("Normal copula")

# Instantiate one distribution object
distribution = ot.ComposedDistribution(aCollection, anotherCopula)
distribution.setName("myDist")
distributionRef = ot.Normal(mean, sigma, correlation)
print("Distribution ", repr(distribution))
print("Parameters ", repr(distribution.getParametersCollection()))

# Show PDF and CDF at point
point = [0.0] * dim
print("PDF      =%.6f" % distribution.computePDF(point))
print("PDF (ref)=%.6f" % distributionRef.computePDF(point))
print("CDF      =%.6f" % distribution.computeCDF(point))
print("CDF (ref)=%.6f" % distributionRef.computeCDF(point))
print("Survival      =%.6f" % distribution.computeSurvivalFunction(point))
print("Survival (ref)=%.6f" %
      distributionRef.computeSurvivalFunction(point))
# 95% quantile
quantile = distribution.computeQuantile(0.95)
print("Quantile      =", repr(quantile))
print("Quantile (ref)=", repr(distributionRef.computeQuantile(0.95)))
print("CDF(quantile)=%.6f" % distribution.computeCDF(quantile))
print("Mean      =", repr(distribution.getMean()))
print("Mean (ref)=", repr(distributionRef.getMean()))
print("Standard deviation      =", repr(
    distribution.getStandardDeviation()))
print("Standard deviation (ref)=", repr(
    distributionRef.getStandardDeviation()))
print("Skewness      =", repr(distribution.getSkewness()))
print("Skewness (ref)=", repr(distributionRef.getSkewness()))
print("Kurtosis      =", repr(distribution.getKurtosis()))
print("Kurtosis (ref)=", repr(distributionRef.getKurtosis()))
print("Covariance      =", repr(distribution.getCovariance()))
print("Covariance (ref)=", repr(distributionRef.getCovariance()))
anotherSample = distribution.getSample(size)
print("anotherSample mean=", repr(anotherSample.computeMean()))
print("anotherSample covariance=", repr(anotherSample.computeCovariance()))

# test transfo
sample = distribution.getSample(10)
print(sample)
sample_iso = distribution.getIsoProbabilisticTransformation()(sample)
print(sample_iso)
sample_inv = distribution.getInverseIsoProbabilisticTransformation()(
    sample_iso)
print(sample_inv)
x = 0.6
y = [0.2]*(dim-1)
print("conditional PDF=%.6f" % distribution.computeConditionalPDF(x, y))
print("conditional CDF=%.6f" % distribution.computeConditionalCDF(x, y))
print("conditional quantile=%.6f" %
      distribution.computeConditionalQuantile(x, y))
pt = ot.Point([i + 1.5 for i in range(dim)])
print("sequential conditional PDF=",
      distribution.computeSequentialConditionalPDF(point))
resCDF = distribution.computeSequentialConditionalCDF(pt)
print("sequential conditional CDF(", pt, ")=", resCDF)
print("sequential conditional quantile(", resCDF, ")=",
      distribution.computeSequentialConditionalQuantile(resCDF))

# comparison
d = ot.ComposedDistribution([ot.Uniform()]*2, ot.ClaytonCopula(2.5))
d1 = ot.MaximumDistribution(d)
d2 = ot.MaximumDistribution(d)
assert d1.getDistribution() == d2.getDistribution(), "comp1"
assert d1 == d2, "comp2"
