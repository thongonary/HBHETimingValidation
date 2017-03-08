# Description: Visualize different pulse fits with the same digis. 
# Usage: python draw.py pulsePrintout.txt
# -----
# Original Author: Thong Nguyen (Caltech)
# Created: January 12, 2017

import re
import ROOT
import argparse

class Hit:
    def __init__(self,_spot,_pulseType,_fit,_digi):
        self.spot = _spot
        self.pulseType = _pulseType
        self.fit = _fit
        self.digi = _digi

def checkRepeated(spot, allSpots):
    repeated = False
    if len(allSpots) == 0:
        return repeated
    else:
        for index in allSpots:
            if index == spot: repeated = True
    return repeated

def setBinLabel(hist):
    hist.GetXaxis().SetBinLabel(1,"TS0");
    hist.GetXaxis().SetBinLabel(2,"TS1");
    hist.GetXaxis().SetBinLabel(3,"TS2");
    hist.GetXaxis().SetBinLabel(4,"TS3");
    hist.GetXaxis().SetBinLabel(5,"TS4");
    hist.GetXaxis().SetBinLabel(6,"TS5");
    hist.GetXaxis().SetBinLabel(7,"TS6");
    hist.GetXaxis().SetBinLabel(8,"TS7");
    hist.GetXaxis().SetBinLabel(9,"TS8");
    hist.GetXaxis().SetBinLabel(10,"TS9");

def fillHist(hist,val):
    for i in range(0,9):
        hist.SetBinContent(i+1,val[i])


parser = argparse.ArgumentParser()
parser.add_argument('infile',help='Input printout text file of pulses')
args = parser.parse_args()

with open(args.infile) as f:
    allHits = []
    allSpots = []
    allDigis = []
    lines = f.readlines()

    # Dump info into Hit object
    for i in xrange(len(lines)):
        if '(iEta, iPhi, Depth)' in lines[i]:
            spot = [int(s) for s in re.findall(r'-?\d+',lines[i])]
            pulses = []
            digi = []
            fit = []
            for ts in range (2,11):
                pulses.append([float(s) for s in re.findall(r'-?\d+\.\d+',lines[i+ts])])
            for val in pulses:
                digi.append(val[1])
                fit.append(val[0])

            # Store different hits:
            if not checkRepeated(spot,allSpots):
                allSpots.append(spot)
            if not checkRepeated(digi,allDigis):
                allDigis.append(digi)

            pulseType = [int(s) for s in re.findall(r'\b\d+\b',lines[i-1])]

            myHit = Hit(spot,pulseType,fit,digi)
            allHits.append(myHit)

    
    # Iterate by different spots and digis, then draw histograms
    index = 0
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetLegendBorderSize(0);

    for myDigi in allDigis:
        ts0 = myDigi[0]
        for mySpot in allSpots:
            ieta = mySpot[0]
            iphi = mySpot[1]
            depth = mySpot[2]
            index += 1 
            canvas = ROOT.TCanvas('canvas'+str(index),'',800,600)
            canvas.cd()
            plotFilled = False
            drawDigi = False

            for hit in allHits:
                if hit.spot == mySpot and hit.digi == myDigi:
                    plotFilled = True
                    if not drawDigi:    
                        digi = ROOT.TH1F('digi','',10,0.,10.);
                        setBinLabel(digi)
                        digiVal = hit.digi
                        fillHist(digi,digiVal)
                        digi.SetLineWidth(3)
                        digi.SetLineColor(ROOT.kBlack)
                        digi.Draw("hist")
                        drawDigi = True

                    if hit.pulseType == [1]: # standard m2
                        m2 = ROOT.TH1F('m2','',10,0.,10.);
                        setBinLabel(m2)
                        m2Val = hit.fit
                        fillHist(m2,m2Val)
                        m2.SetLineWidth(3)
                        m2.SetLineColor(ROOT.kRed)
                        m2.Draw("hist same")
                    
                    elif hit.pulseType == [2]: # m2csv105
                        m2csv105 = ROOT.TH1F('m2csv105','',10,0.,10.);
                        setBinLabel(m2csv105)
                        m2csv105Val = hit.fit
                        fillHist(m2csv105,m2csv105Val)
                        m2csv105.SetLineWidth(3)
                        m2csv105.SetLineColor(ROOT.kBlue)
                        m2csv105.Draw("hist same")
                    
                    elif hit.pulseType == [3]: # m2csvlag
                        m2csvlag = ROOT.TH1F('m2csvlag','',10,0.,10.);
                        m2csvlagVal = hit.fit
                        fillHist(m2csvlag,m2csvlagVal)
                        m2csvlag.SetLineWidth(3)
                        m2csvlag.SetLineColor(ROOT.kOrange)
                        m2csvlag.Draw("hist same")

            if plotFilled:
                canvas.BuildLegend(0.65,0.6,0.88,0.88)
                text = ROOT.TLatex()
                text.SetTextFont(42)
                text.SetTextColor(1)
                text.SetTextAlign(12)
                text.SetTextSize(0.04)
                text.DrawLatex(0.5,0.95*m2.GetMaximum(),'iEta='+str(ieta));
                text.DrawLatex(0.5,0.85*m2.GetMaximum(),'iPhi='+str(iphi));
                text.DrawLatex(0.5,0.75*m2.GetMaximum(),'Depth='+str(depth));

                canvas.Draw()
                canvas.SaveAs('iEtaiPhiDepth_'+str(ieta)+'_'+str(iphi)+'_'+str(depth)+'_ts0_'+str(ts0)+'.png')
