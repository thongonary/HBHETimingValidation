from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ttbarpu50_2017mar21'
config.General.workArea = 'crab_ttbarpu50'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_EI_PAT_Phase1_GT.py'
config.JobType.numCores = 8

config.Data.inputDataset = '/RelValTTbar_13/CMSSW_9_0_0_pre5-PU25ns_90X_upgrade2017_realistic_v15_PU50-v1/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/dpg_hcal/comm_hcal/RecoAlgos/crab_ttbarPU50_9_0_0_pre5'
config.Data.publication = False
#config.Data.outputDatasetTag = 'CRAB3'

config.Site.storageSite = 'T2_CH_CERN'
