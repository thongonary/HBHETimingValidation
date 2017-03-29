# Visualize digi and fit pulses of the 10 TS

To visualize the fit, add the following additional codes before running step 3:
- M3: https://github.com/thongonary/cmssw/blob/755ad9cefb6d7c2de9a1df55ec51f6593f38e758/RecoLocalCalo/HcalRecAlgos/src/HcalDeterministicFit.cc#L240-L253
- M2: https://github.com/thongonary/cmssw/blob/755ad9cefb6d7c2de9a1df55ec51f6593f38e758/RecoLocalCalo/HcalRecAlgos/src/PulseShapeFitOOTPileupCorrection.cc#L756-L761
- All the lines with cout in this file https://github.com/thongonary/cmssw/blob/755ad9cefb6d7c2de9a1df55ec51f6593f38e758/RecoLocalCalo/HcalRecAlgos/src/SimpleHBHEPhase1Algo.cc

When running the step 3 (it's recommended to run on ~10 events for visualization purpose), do the following
> cmsRun step3_RAW2DIGI.py >& all.txt

So that the output of all.txt looks like this: https://github.com/thongonary/HBHETimingValidation/blob/master/SubmitData/cfg/PulseVisualization/all.txt

To run the visualization code
> python draw.py all.txt
