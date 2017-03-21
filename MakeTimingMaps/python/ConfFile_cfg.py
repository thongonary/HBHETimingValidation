import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet (wantSummary = cms.untracked.bool(False))

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

#        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_pi1-100_2017_realistic_1Pulse_MCFit.root'
#        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_pi1-100_2017_realistic_1Pulse_defaultFit.root'
#        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_pi1-100_2017_realistic_3Pulse.root'
#        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_pi1-100_2017_realistic_3Pulse_defaultFit.root'
#        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_pi1-100_2017_realistic_switchPulse.root'
        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/phase1/step3_ttbar_PU50_1Pulse_MCFit.root'
#        'root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/RecoAlgos/ttbarPU50_step3_9_0_0_pre5/step3_ttbar_PU50_1Pulse_defaultFit.root'
#        'root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/RecoAlgos/ttbarPU50_step3_9_0_0_pre5/step3_ttbar_PU50_3Pulse_defaultFit.root'
#        'root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/RecoAlgos/ttbarPU50_step3_9_0_0_pre5/step3_ttbar_PU50_3Pulse_MCFit.root'
#        'root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/RecoAlgos/ttbarPU50_step3_9_0_0_pre5/step3_ttbar_PU50_switchPulse_defaultFit.root'

    )
)

process.timingMaps = cms.EDAnalyzer('MakeRun2M3M2Plots')

#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_pi1-100_2017_realistic_1Pulse_MCFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_pi1-100_2017_realistic_1Pulse_defaultFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_pi1-100_2017_realistic_3Pulse.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_pi1-100_2017_realistic_3Pulse_defaultFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_pi1-100_2017_realistic_switchPulse.root') )
process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_ttbar_PU50_1Pulse_MCFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_ttbar_PU50_1Pulse_defaultFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_ttbar_PU50_3Pulse_defaultFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_ttbar_PU50_3Pulse_MCFit.root') )
#process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_ttbar_PU50_switchPulse_defaultFit.root') )

process.p = cms.Path(process.timingMaps)
