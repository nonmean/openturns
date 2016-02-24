//                                               -*- C++ -*-
/**
 *  @brief Abstract top-level view of an monteCarloExperiment plane
 *
 *  Copyright 2005-2015 Airbus-EDF-IMACS-Phimeca
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
 *  You should have received a copy of the GNU Lesser General Public
 *  along with this library.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
#ifndef OPENTURNS_MONTECARLOEXPERIMENT_HXX
#define OPENTURNS_MONTECARLOEXPERIMENT_HXX

#include "openturns/WeightedExperiment.hxx"

BEGIN_NAMESPACE_OPENTURNS



/**
 * @class MonteCarloExperiment
 *
 * The class describes the probabilistic concept of monteCarloExperiment plan
 */
class OT_API MonteCarloExperiment
  : public WeightedExperiment
{
  CLASSNAME;
public:


  /** Default constructor */
  MonteCarloExperiment();

  /** Parameters constructor */
  explicit MonteCarloExperiment(const UnsignedInteger size);

  /** Parameters constructor */
  MonteCarloExperiment(const Distribution & distribution,
                       const UnsignedInteger size);

  /** Virtual constructor */
  virtual MonteCarloExperiment * clone() const;

  /** String converter */
  virtual String __repr__() const;

  /* Here is the interface that all derived class must implement */

  /** Sample generation */
  using WeightedExperiment::generate;
  NumericalSample generate();

protected:

private:

}; /* class MonteCarloExperiment */


END_NAMESPACE_OPENTURNS

#endif /* OPENTURNS_MONTECARLOEXPERIMENT_HXX */