// -*- C++ -*-
//
// Package:    HBHETimingValidation/MakeTimingMaps
// Class:      MakeTimingMaps
// 
/**\class MakeTimingMaps MakeTimingMaps.cc HBHETimingValidation/MakeTimingMaps/plugins/MakeTimingMaps.cc

Description: Quick example code for making HBHE timing monitoring plots
*/
//
// Original Author:  Stephanie Brandt
//         Created:  Fri, 21 Aug 2015 11:42:17 GMT
//
//


// system include files
#include <memory>
#include <string>
#include <map>
#include <iostream>
using namespace std;

// user include files
#include "TLine.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TTree.h"
#include "TFile.h"
#include "TProfile.h"
#include "TH1.h"
#include "TH2.h"
#include "TCanvas.h"
#include "TProfile2D.h"
#include "TLatex.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HcalRecHit/interface/HBHERecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"
#include "DataFormats/HcalRecHit/interface/HBHEChannelInfo.h"

#include "SimDataFormats/CaloHit/interface/PCaloHit.h"
#include "SimDataFormats/CaloHit/interface/PCaloHitContainer.h"


#include "CalibCalorimetry/HcalAlgos/interface/HcalPulseContainmentManager.h"
#include "CondFormats/HcalObjects/interface/HcalRecoParams.h"
#include "CondFormats/HcalObjects/interface/HcalRecoParam.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalDbASCIIIO.h"
#include "Geometry/HcalCommonData/interface/HcalHitRelabeller.h"
#include "Geometry/HcalCommonData/interface/HcalDDDRecConstants.h"

#include "Geometry/Records/interface/HcalRecNumberingRecord.h"
#include "CondFormats/HcalObjects/interface/HcalLogicalMap.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalLogicalMapGenerator.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalDbASCIIIO.h"


#include "SimCalorimetry/HcalSimAlgos/interface/HcalSimParameterMap.h"


// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class MakeRun2M3M2Plots : public edm::one::EDAnalyzer<edm::one::SharedResources>  
{
    public:
        explicit MakeRun2M3M2Plots(const edm::ParameterSet&);
        ~MakeRun2M3M2Plots();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


    private:
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;

        std::string int2string(int i);

        void ClearVariables();

        // some variables for storing information
        double Method0Energy;
        double RecHitEnergy;
        double RecHitEnergyCSV;
        double RecHitTime;
        double RecHitChi2;
        double Method0EnergyM3;
        double RecHitEnergyM2;
        double RecHitEnergyM3;
        double RecHitTimeM3;

        int LumiBlock;
        double iEta;
        double iPhi; 
        int depth;
        int RunNumber;
        int EvtNumber;

        // create the output file
        edm::Service<TFileService> FileService;
        // create the token to retrieve hit information
        edm::EDGetTokenT<HBHERecHitCollection>    hRhTokenM2;
        edm::EDGetTokenT<HBHERecHitCollection>    hRhTokenM3;
        edm::EDGetTokenT<HBHERecHitCollection>    hRhTokenM0;
        edm::EDGetTokenT<HBHEChannelInfoCollection> InfoToken;


        edm::EDGetTokenT<std::vector<PCaloHit>>   hSHitToken;

        TH1F *hCheckEnergyM2;
        TH1F *hCheckTimingM2;
        TH1F *hCheckTimingM2_gt5;
        TH1F *hCheckChi2M2_gt5;

        TH2F *hCheckM2SimHit;
        TH2F *hCheckM3SimHit;
        TH2F *hCheckM3M2_HPD;
        TH2F *hCheckM3M2_HPD_zoom;

        TH1F *hCheckM3M2_HPD_1D;
        TH1F *hCheckM2SimHit_1D;
        TH1F *hCheckM3SimHit_1D;

        HcalSimParameterMap simParameterMap_;

        TProfile2D *hHBHEChi2;
        
        TProfile *hCheckM2SimHit_SimHit;
        TProfile *hCheckM2SimHit_iEta;
        
        TProfile *hCheckM3SimHit_SimHit;
        TProfile *hCheckM3SimHit_iEta;
        
        TH2F *hCheckM2SimHit_iEta_TH2;
        TH2F *hCheckM3SimHit_iEta_TH2;

        const HcalDDDRecConstants *hcons;

        bool isData = false;
};


MakeRun2M3M2Plots::MakeRun2M3M2Plots(const edm::ParameterSet& iConfig)
{
    //now do what ever initialization is needed
    usesResource("TFileService");

    // Tell which collection is consumed
    hRhTokenM2 = consumes<HBHERecHitCollection >(iConfig.getUntrackedParameter<string>("HBHERecHits","hbheprerecoM2"));
    hRhTokenM3 = consumes<HBHERecHitCollection >(iConfig.getUntrackedParameter<string>("HBHERecHits","hbheprerecoM3"));
     if(!isData) InfoToken = consumes<HBHEChannelInfoCollection>(iConfig.getUntrackedParameter<string>("HBHEChannelInfo","hbheprereco"));
    if (!isData) hSHitToken = consumes<edm::PCaloHitContainer>(edm::InputTag("g4SimHits","HcalHits"));

    hCheckTimingM2 = FileService->make<TH1F>("TimingM2","TimingM2; M2 Timing",25,-12.5,12.5);
    hCheckTimingM2_gt5 = FileService->make<TH1F>("TimingM2_gt5","TimingM2_gt5; M2 Timing",25,-12.5,12.5);
    hCheckEnergyM2 = FileService->make<TH1F>("EnergyM2","EnergyM2; M2 Energy",20,0.,100.);
    hCheckChi2M2_gt5 = FileService->make<TH1F>("Chi2M2_gt5","Chi2M2_gt5; M2 #chi^{2}",1000,-10,500);
    hHBHEChi2 = FileService->make<TProfile2D>("hHBHEChi2","hHBHEChi2;#eta;#phi;M2 #chi^{2}",59,-29.5,29.5,72,0.5,72.5, 0, 500.,"s");

    hCheckM3M2_HPD = FileService->make<TH2F>("CheckM3M2_HB",";M2;M3/M2",200,0,500,200,0.5,1.5);
    hCheckM3M2_HPD_zoom = FileService->make<TH2F>("CheckM3M2_HB_zoom",";M2;M3/M2",200,0,5,200,0,3);
    hCheckM3M2_HPD_1D = FileService->make<TH1F>("CheckM3M2_HB_1D",";M3/M2",100,0.5,1.5);

    hCheckM2SimHit = FileService->make<TH2F>("CheckM2SimHit",";SimHit;M2/SimHit",200,0,500,200,0.5,1.5);
    hCheckM3SimHit = FileService->make<TH2F>("CheckM3SimHit",";SimHit;M3/SimHit",200,0,500,200,0.5,1.5);

    hCheckM2SimHit_1D = FileService->make<TH1F>("CheckM2SimHit_1D",";M2/SimHit",100,0.5,1.5);
    hCheckM3SimHit_1D = FileService->make<TH1F>("CheckM3SimHit_1D",";M3/SimHit",100,0.5,1.5);

    double binSimHit[] = {0,10,20,30,45,60,80,100,120,150,200,300,500};
    int binnum = sizeof(binSimHit)/sizeof(double) - 1;
    hCheckM2SimHit_SimHit = FileService->make<TProfile>("CheckM2SimHit_SimHit",";SimHit;M2/SimHit",binnum,binSimHit,0.5,1.5,"s");
    hCheckM3SimHit_SimHit = FileService->make<TProfile>("CheckM3SimHit_SimHit",";SimHit;M3/SimHit",binnum,binSimHit,0.5,1.5,"s");

    hCheckM2SimHit_iEta = FileService->make<TProfile>("CheckM2SimHit_iEta",";iEta;M2/SimHit",59,-29.5,29.5,"s");
    hCheckM3SimHit_iEta = FileService->make<TProfile>("CheckM3SimHit_iEta",";iEta;M3/SimHit",59,-29.5,29.5,"s");
    
    hCheckM2SimHit_iEta_TH2 = FileService->make<TH2F>("CheckM2SimHit_iEta_TH2",";iEta;M2/SimHit",59,-29.5,29.5,100,0,2);
    hCheckM3SimHit_iEta_TH2 = FileService->make<TH2F>("CheckM3SimHit_iEta_TH2",";iEta;M3/SimHit",59,-29.5,29.5,100,0,2);
}


MakeRun2M3M2Plots::~MakeRun2M3M2Plots(){} // destructor

// ------------ method called for each event  ------------
void MakeRun2M3M2Plots::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    // Read events
    Handle<HBHERecHitCollection> hRecHits; // create handle
    iEvent.getByToken(hRhTokenM2, hRecHits); // get events based on token

    Handle<HBHERecHitCollection> hRecHitsM3; // create handle
    iEvent.getByToken(hRhTokenM3, hRecHitsM3); // get events based on token

    Handle<HBHEChannelInfoCollection> channelData; // create handle 
    Handle<PCaloHitContainer> hSimHits;      // create handle
    edm::ESHandle<HcalDDDRecConstants> pHRNDC;

    if (!isData)
    {
        iEvent.getByToken(InfoToken, channelData); // get events based on token
        iEvent.getByToken(hSHitToken, hSimHits);   // SimHits
        iSetup.get<HcalRecNumberingRecord>().get( pHRNDC );
        hcons = &(*pHRNDC);
    }

    RunNumber = iEvent.id().run(); // get the run number for the event
    EvtNumber = iEvent.id().event(); // get the event number
    LumiBlock = iEvent.id().luminosityBlock();

    // Loop over all rechits in one event
    for(int i = 0; i < (int)hRecHits->size(); i++) 
    {
        HcalDetId detID_rh = (*hRecHits)[i].id().rawId();

        // ID information can get us detector coordinates
        depth = (*hRecHits)[i].id().depth();
        iEta = detID_rh.ieta();
        iPhi = detID_rh.iphi();

        // get some variables
        Method0Energy = (*hRecHits)[i].eraw();
        RecHitEnergy = (*hRecHits)[i].energy();
        RecHitTime = (*hRecHits)[i].time();
        RecHitChi2 = (*hRecHits)[i].chi2();

        hCheckEnergyM2->Fill(RecHitEnergy);
        hCheckTimingM2->Fill(RecHitTime);
        if(Method0Energy>5) hCheckTimingM2_gt5->Fill(RecHitTime);
        if(Method0Energy>5) hCheckChi2M2_gt5->Fill(RecHitChi2);
        if(Method0Energy>5) hHBHEChi2->Fill(detID_rh.ieta(), detID_rh.iphi(), RecHitChi2);

    } // recHit


    // COMPARE M3/M2
    for(int i = 0; i < (int)hRecHits->size(); i++) 
    {
        for(int j = 0; j < (int)hRecHitsM3->size(); j++) 
        {
            // get ID information for the reconstructed hit
            HcalDetId detID_rh = (*hRecHits)[i].id().rawId();
            HcalDetId detID_rhcsv = (*hRecHitsM3)[j].id().rawId();

            bool HPD=true;
            if (detID_rh.ieta()>=16 && detID_rh.ieta()<=29 && detID_rh.iphi()>=63 && detID_rh.iphi()<=66 ) HPD=false;

            // ID information can get us detector coordinates
            iEta = detID_rh.ieta();
            iPhi = detID_rh.iphi();

            // get some variables
            Method0Energy = (*hRecHits)[i].eraw();
            RecHitEnergy = (*hRecHits)[i].energy();
            RecHitEnergyM3 = (*hRecHitsM3)[j].energy();
            if (detID_rh == detID_rhcsv && HPD) hCheckM3M2_HPD->Fill(RecHitEnergy, RecHitEnergyM3/RecHitEnergy);
            if (detID_rh == detID_rhcsv && HPD) hCheckM3M2_HPD_zoom->Fill(RecHitEnergy, RecHitEnergyM3/RecHitEnergy);
            if (RecHitEnergy>5.0 && detID_rh == detID_rhcsv && HPD) hCheckM3M2_HPD_1D->Fill(RecHitEnergyM3/RecHitEnergy);
        }
    }


    // Comparing M2 with SimHits
    for (int i = 0; i < (int) hRecHits->size(); i++)
    {
        double SHitEn=0;
        HcalDetId detID_rh = (*hRecHits)[i].id().rawId();

        bool HPD=true;
        if (detID_rh.ieta()>=16 && detID_rh.ieta()<=29 && detID_rh.iphi()>=63 && detID_rh.iphi()<=66 ) HPD=false;
        
        RecHitEnergyM2 = (*hRecHits)[i].energy();

        double SamplingFactor = 1;
        if(detID_rh.subdet() == HcalBarrel) 
        {
            SamplingFactor = simParameterMap_.hbParameters().samplingFactor(detID_rh);
        } 
        else if (detID_rh.subdet() == HcalEndcap) 
        {
            SamplingFactor = simParameterMap_.heParameters().samplingFactor(detID_rh);
        }

        for (int j = 0; j < (int) hSimHits->size(); j++)
        {
            HcalDetId simId = HcalHitRelabeller::relabel((*hSimHits)[j].id(), hcons);
            if (simId == detID_rh) SHitEn += SamplingFactor*((*hSimHits)[j].energy());
        }
        if (SHitEn>0 && (*hRecHits)[i].energy()>0 && HPD) hCheckM2SimHit->Fill(SHitEn, RecHitEnergyM2/SHitEn); 
        if (SHitEn>0 && (*hRecHits)[i].energy()>0 && HPD) hCheckM2SimHit_SimHit->Fill(SHitEn, RecHitEnergyM2/SHitEn); 
        if (SHitEn>0 && (*hRecHits)[i].energy()>5 && HPD) hCheckM2SimHit_iEta->Fill(detID_rh.ieta(), RecHitEnergyM2/SHitEn); 
        if (SHitEn>0 && (*hRecHits)[i].energy()>5 && HPD) hCheckM2SimHit_iEta_TH2->Fill(detID_rh.ieta(), RecHitEnergyM2/SHitEn); 
        if (SHitEn>0 && (*hRecHits)[i].energy()>5 && HPD) hCheckM2SimHit_1D->Fill(RecHitEnergyM2/SHitEn); 
    }

    // Comparing M3 with SimHits
    for (int i = 0; i < (int) hRecHitsM3->size(); i++)
    {
        double SHitEn=0;
        HcalDetId detID_rh = (*hRecHitsM3)[i].id().rawId();
        bool HPD=true;
        if (detID_rh.ieta()>=16 && detID_rh.ieta()<=29 && detID_rh.iphi()>=63 && detID_rh.iphi()<=66 ) HPD=false;
        RecHitEnergyM3 = (*hRecHitsM3)[i].energy();

        double SamplingFactor = 1;
        if(detID_rh.subdet() == HcalBarrel) 
        {
            SamplingFactor = simParameterMap_.hbParameters().samplingFactor(detID_rh);
        } 
        else if (detID_rh.subdet() == HcalEndcap) 
        {
            SamplingFactor = simParameterMap_.heParameters().samplingFactor(detID_rh);
        }


        for (int j = 0; j < (int) hSimHits->size(); j++)
        {
            HcalDetId simId = HcalHitRelabeller::relabel((*hSimHits)[j].id(), hcons); 
            if (simId == detID_rh) SHitEn += SamplingFactor*((*hSimHits)[j].energy());
        }
        if (SHitEn>0 && (*hRecHitsM3)[i].energy()>0 && HPD) hCheckM3SimHit->Fill(SHitEn, RecHitEnergyM3/SHitEn); 
        if (SHitEn>0 && (*hRecHitsM3)[i].energy()>0 && HPD) hCheckM3SimHit_SimHit->Fill(SHitEn, RecHitEnergyM3/SHitEn); 
        if (SHitEn>0 && (*hRecHitsM3)[i].energy()>5 && HPD) hCheckM3SimHit_iEta->Fill(detID_rh.ieta(), RecHitEnergyM3/SHitEn); 
        if (SHitEn>0 && (*hRecHitsM3)[i].energy()>5 && HPD) hCheckM3SimHit_iEta_TH2->Fill(detID_rh.ieta(), RecHitEnergyM3/SHitEn); 
        if (SHitEn>0 && (*hRecHitsM3)[i].energy()>5 && HPD) hCheckM3SimHit_1D->Fill(RecHitEnergyM3/SHitEn); 
    }
}

// ------------ method called once each job just before starting event loop  ------------
void MakeRun2M3M2Plots::beginJob(){}

// ------------ method called once each job just after ending the event loop  ------------
void MakeRun2M3M2Plots::endJob()
{
    //    TCanvas *c1 = new TCanvas("c1","",650,600);
    //    c1->cd();
    //    gStyle->SetOptStat(11);
    //    gPad->SetLogz();
    //    gPad->SetGridy();
    //
    //    hCheckM3M2_HPD->Draw("COLZ");
    //    c1->SaveAs("M3M2_HB.png");
    //    
    //    hCheckM3M2_HPD_zoom->Draw("COLZ");
    //    c1->SaveAs("M3M2_HB_zoom.png");
    //    
    //    hCheckM3csvM2_HB->Draw("COLZ");
    //    c1->SaveAs("M3csvM2_HB.png");
    //   
    //    hCheckM3csvM2_HB_zoom->Draw("COLZ");
    //    c1->SaveAs("M3csvM2_HB_zoom.png");
    //   
    //    hCheckM3csv105M2_HB->Draw("COLZ");
    //    c1->SaveAs("M3csv105M2_HB.png");
    //   
    //    hCheckM3csv105M2_HB_zoom->Draw("COLZ");
    //    c1->SaveAs("M3csv105M2_HB_zoom.png");
    //    
    //    gPad->SetGridy(0);
    //    gPad->SetGridx();
    //    
    //    hCheckM3csvM2_HB_1D->Draw();
    //    c1->SaveAs("M3csvM2_HB_1D.png");
    //    
    //    hCheckM3M2_HPD_1D->Draw();
    //    c1->SaveAs("M3M2_HB_1D.png");
    //    
    //    hCheckM3csv105M2_HB_1D->Draw();
    //    c1->SaveAs("M3csv105M2_HB_1D.png");
}

void MakeRun2M3M2Plots::ClearVariables(){
    RecHitEnergy = 0;
    RunNumber = 0;
    depth=0;
    iEta = 0;
    iPhi = 0;
    RecHitTime = 0;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void MakeRun2M3M2Plots::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    // The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MakeRun2M3M2Plots);
