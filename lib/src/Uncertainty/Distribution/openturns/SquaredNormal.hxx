//                                               -*- C++ -*-
/**
 *  @brief The Squared Normal distribution
 *
 *  Copyright 2005-2022 Airbus-EDF-IMACS-ONERA-Phimeca
 *
 *  This library is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public License
 *  along with this library.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
#ifndef OPENTURNS_SQUAREDNORMAL_HXX
#define OPENTURNS_SQUAREDNORMAL_HXX

#include "openturns/OTprivate.hxx"
#include "openturns/ContinuousDistribution.hxx"
#include "openturns/Normal.hxx"

BEGIN_NAMESPACE_OPENTURNS

/**
 * @class SquaredNormal
 *
 * The SquaredNormal (gaussian) distribution.
 */
class OT_API SquaredNormal
  : public ContinuousDistribution
{

  CLASSNAME
public:

  /** Default constructor */
  SquaredNormal();

  /** Constructor */
  SquaredNormal(Scalar mu, Scalar sigma);

  /** Comparison operator */
  Bool operator ==(const SquaredNormal & other) const;
protected:
  Bool equals(const DistributionImplementation & other) const override;

public:

  /** String converter */
  String __repr__() const override;
  String __str__(const String & offset = "") const override;

  /* Interface inherited from Distribution */

  /** Virtual constructor */
  SquaredNormal * clone() const override;

  /** Get one realization of the SquaredNormal distribution */
  Point getRealization() const override;
  Sample getSample(const UnsignedInteger size) const override;

  /** Get the CDF of the SquaredNormal distribution */
  using ContinuousDistribution::computeCDF;
  Scalar computeCDF(const Point & point) const override;

  /** Get the PDF of the distribution */
  using ContinuousDistribution::computePDF;
  Scalar computePDF(const Point & point) const override;

  /** Get the characteristic function of the distribution */
  Complex computeCharacteristicFunction(const Scalar x) const override;

  /** Parameters value accessor */
  Point getParameter() const override;
  void setParameter(const Point & parameters) override;

  /** Parameters description accessor */
  Description getParameterDescription() const override;

  /* Interface specific to Arcsine */

  /** Mu accessor */
  void setMu(const Scalar mu);
  Scalar getMu() const;

  /** Sigma accessor */
  void setSigma(const Scalar sigma);
  Scalar getSigma() const;

  /** Method save() stores the object through the StorageManager */
  void save(Advocate & adv) const override;

  /** Method load() reloads the object from the StorageManager */
  void load(Advocate & adv) override;

protected:

private:

  /** Compute the mean of the distribution */
  void computeMean() const override;

  /** Compute the covariance of the distribution */
  void computeCovariance() const override;

  /** Compute the range */
  void computeRange() override;

  Scalar mu_;
  Scalar sigma_;

}; /* class SquaredNormal */

END_NAMESPACE_OPENTURNS

#endif /* OPENTURNS_SQUARED_NORMAL_HXX */
