# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --runUnscheduled --conditions auto:phase1_2017_hcaldev -n 10 --era Run2_2017_HCALdev --eventcontent RECOSIM -s RAW2DIGI,L1Reco,RECO,EI --datatier GEN-SIM-RECO --geometry Extended2017dev -n 100 --nThreads 16
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT3',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                            #'file:step2_pi500_2017_realistic.root'

                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/0C06CBE9-E1FF-E611-B04B-0CC47A7C3430.root',   
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/2810D0F0-E1FF-E611-BE10-0025905A48C0.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/340164F6-E1FF-E611-A29B-0025905A60BC.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/4AF60CF7-E1FF-E611-9F81-0025905B860C.root', 
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/50DDF9D1-E1FF-E611-ABA6-0CC47A7C360E.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/58C63DED-E1FF-E611-B8C5-0025905A60D0.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/64E16CEC-E1FF-E611-B78C-0CC47A78A340.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/6830E3F0-E1FF-E611-B58B-0025905A6138.root',  
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/68D20DDE-E1FF-E611-98C0-0CC47A4D7614.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/700FF2E1-E1FF-E611-9805-0CC47A7C3458.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/8402B1E9-E1FF-E611-BD82-0025905A60DE.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/8E7B03C9-E1FF-E611-A441-0CC47A4D769C.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/B00771CB-E1FF-E611-A78F-0CC47A4C8E82.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/B6B63CF5-E1FF-E611-8FFC-0CC47A7C357E.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/BC6D38C9-E1FF-E611-B316-0CC47A78A360.root',   
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/C4CC19EF-E1FF-E611-BB87-0025905B85BC.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/CE0773F1-E1FF-E611-AA2E-0025905B85A0.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/DC8A96C9-E1FF-E611-B116-0CC47A78A436.root',
                            'root://eoscms.cern.ch//store/relval/CMSSW_9_0_0_pre5/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/00000/EA8F61DC-E1FF-E611-8838-0CC47A4D7602.root',
                                
                                ),

                            secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step3_ttbar_PU50_1Pulse_MCFit.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.RECOSIMoutput.outputCommands.append( "keep *_g4SimHits*_*_*")
process.RECOSIMoutput.outputCommands.append( "keep *_hbheprereco*_*_*")
process.RECOSIMoutput.outputCommands.append( "keep HBHERecHits*_*_*_*")

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')
##process.GlobalTag = GlobalTag(process.GlobalTag, '81X_upgrade2017_realistic_v25', '')

# Save HBHEChannelInfo
process.hbheprereco.saveInfos = cms.bool(True)

process.hbheprerecoM2 = process.hbheprereco.clone()
process.hbheprerecoM2.algorithm.__setattr__('useM2',cms.bool(True))
process.hbheprerecoM2.algorithm.__setattr__('useM3',cms.bool(False))

process.hbheprerecoM3 = process.hbheprereco.clone()
process.hbheprerecoM3.algorithm.__setattr__('useM2',cms.bool(False))
process.hbheprerecoM3.algorithm.__setattr__('useM3',cms.bool(True))

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction*process.hbheprerecoM2*process.hbheprerecoM3)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.eventinterpretaion_step,process.endjob_step,process.RECOSIMoutput_step)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

##from SLHCUpgradeSimulations.Configuration.HCalCustoms import load_HcalHardcode
##process = load_HcalHardcode(process)
##process.es_hardcode.useHEUpgrade = cms.bool(True)
##process.es_hardcode.useHFUpgrade = cms.bool(True)
##process.es_hardcode.heUpgrade.darkCurrent = cms.double(0)
##process.es_hardcode.SiPMCharacteristics[2].crosstalk = cms.double(0.0)
##process.es_hardcode.SiPMCharacteristics[3].crosstalk = cms.double(0.0)
##process.es_hardcode.toGet = cms.untracked.vstring('GainWidths','SiPMParameters','SiPMCharacteristics')

# Customisation from command line

dumpFile  = open("DumpRECO_Phase1_step3_GT.py", "w")
dumpFile.write(process.dumpPython())
dumpFile.close()
