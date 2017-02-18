import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet (wantSummary = cms.untracked.bool(False))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

        'file:$CMSSW_BASE/src/HBHETimingValidation/SubmitData/cfg/step3_singlepi_M3_Pars3.root'

    )
)

process.timingMaps = cms.EDAnalyzer('MakeRun2M3Plots')

process.TFileService = cms.Service('TFileService', fileName = cms.string('step3_singlepi_M3_Pars3.root') )


process.p = cms.Path(process.timingMaps)
