import ROOT as R
import numpy as np
import argparse
import os

R.gROOT.SetBatch(True)

def set_config() : # Block to configure plots

    config = {}
    config["eta"]   = [0.0]               # To produce the plot for fixed values of eta. Comment out to produce plots for all values of eta.
    config["pt"]    = [9., 10.]                 # To produce the plot for fixed values of pt. Comment out to produce plots for all values of pt

    config["outdir"] = "plot_Flavor_"+args.year+"/"           # Output directory name
    config["sources"] = {                       # JEC uncertainty sources. The numbers in brackers correspond to MarkerStyle and MarkerColor to format the histogram visuals
       "AbsoluteStat"     : [20, 1],
       "AbsoluteScale"    : [20, 2],
#        "AbsoluteFlavMap"  : [20, 1],
       "AbsoluteMPFBias"  : [20, 3],
       "Fragmentation"    : [20, 4],
       "SinglePionECAL"   : [20, 5],
       "SinglePionHCAL"   : [20, 6],
       "FlavorQCD"         : [20, 7],
       "TimePtEta"        : [20, 8],
       "RelativeJEREC1"    : [20, 9],
       "RelativeJEREC2"    : [21, 1],
       "RelativeJERHF"     : [21, 2],
       "RelativePtBB"      : [21, 3],
       "RelativePtEC1"     : [21, 4],
       "RelativePtEC2"     : [21, 5],
       "RelativePtHF"      : [21, 6],
       "RelativeBal"       : [21, 7],
       "RelativeSample"    : [21, 8],
       "RelativeFSR"       : [21, 9],
       "RelativeStatFSR"   : [22, 4],
       "RelativeStatEC"    : [22, 5],
       "RelativeStatHF"    : [22, 6],
        "PileUpDataMC"      : [22, 7],
        "PileUpPtRef"       : [22, 8],
        "PileUpPtBB"        : [22, 9],
        "PileUpPtEC1"       : [23, 2],
        "PileUpPtEC2"       : [23, 3],
        "PileUpPtHF"        : [23, 4],
        # "PileUpMuZero"      : [21, 8],
        # "PileUpEnvelope"    : [21, 9],
       # "SubTotalPileUp"    : [21, 2],
       # "SubTotalRelative"  : [21, 3],
       # "SubTotalPt"        : [21, 4],
       # "SubTotalScale"     : [21, 5],
       # "SubTotalAbsolute"  : [21, 6],
       # "SubTotalMC"        : [21, 7],
       "Total"             : [34, 1],
#        "TotalNoFlavor"    : [0, 1]
#        "TotalNoTime"      : [0, 1]
#        "TotalNoFlavorNoTime" : [0, 1],
#        "FlavorZJet"        : [21, 2],
#        "FlavorPhotonJet"   : [21, 3],
#        "FlavorPureGluon"   : [21, 4],
#        "FlavorPureQuark"   : [21, 5],
#        "FlavorPureCharm"   : [21, 6],
#        "FlavorPureBottom"  : [21, 7],
#        "TimeRunB"         : [21, 7],
#        "TimeRunC"         : [21, 7],
#        "TimeRunDE"        : [21, 7],
#        "TimeRunF"         : [21, 7],
#        "CorrelationGroupMPFInSitu"        : [21, 7],
#        "CorrelationGroupIntercalibration" : [21, 7],
#        "CorrelationGroupbJES"             : [21, 7],
#        "CorrelationGroupFlavor"           : [21, 7],
#        "CorrelationGroupUncorrelated"     : [21, 7],
    }

    config['quad'] = {                          # Sources to add in quadrature
#      "FlavorCombined" : {                     # This is the uncertainty class name which the combined underatainties will be plotted under.
#        "FlavorZJet"        : [21, 2],
#        "FlavorPhotonJet"   : [21, 3],
#        "FlavorPureGluon"   : [21, 4],
#        "FlavorPureQuark"   : [21, 5],
#        "FlavorPureCharm"   : [21, 6],
#        "FlavorPureBottom"  : [21, 7],
#      },
#
#      "RelativeCombined" : {
#        "RelativeJEREC1"    : [21, 2],
#        "RelativeJEREC2"    : [21, 3],
#        "RelativeJERHF"     : [21, 4],
#        "RelativePtBB"      : [21, 5],
#        "RelativePtEC1"     : [21, 6],
#        "RelativePtEC2"     : [21, 7],
#        "RelativePtHF"      : [21, 8],
#        "RelativeBal"       : [21, 9],
#        "RelativeSample"    : [22, 2],
#        "RelativeFSR"       : [22, 3],
#        "RelativeStatFSR"   : [22, 4],
#        "RelativeStatEC"    : [22, 5],
#        "RelativeStatHF"    : [22, 6],
#      },

      # "PileUpCombined" :{
      #   "PileUpDataMC"      : [21, 2],
      #   "PileUpPtRef"       : [21, 3],
      #   "PileUpPtBB"        : [21, 4],
      #   "PileUpPtEC1"       : [21, 5],
      #   "PileUpPtEC2"       : [21, 6],
      #   "PileUpPtHF"        : [21, 7],
      #   "PileUpMuZero"      : [21, 8],
      #   "PileUpEnvelope"    : [21, 9],
      # },
    "TotalFromSources":{
        "AbsoluteStat"     : [20, 1],
        "AbsoluteScale"    : [20, 1],
        "AbsoluteMPFBias"  : [20, 1],
        "Fragmentation"    : [20, 1],
        "SinglePionECAL"   : [20, 1],
        "SinglePionHCAL"   : [20, 1],
        "FlavorQCD"         : [20, 1],
        "TimePtEta"        : [20, 1],
        "RelativeJEREC1"    : [21, 2],
        "RelativeJEREC2"    : [21, 3],
        "RelativeJERHF"     : [21, 4],
        "RelativePtBB"      : [21, 5],
        "RelativePtEC1"     : [21, 6],
        "RelativePtEC2"     : [21, 7],
        "RelativePtHF"      : [21, 8],
        "RelativeBal"       : [21, 9],
        "RelativeSample"    : [22, 2],
        "RelativeFSR"       : [22, 3],
        "RelativeStatFSR"   : [22, 4],
        "RelativeStatEC"    : [22, 5],
        "RelativeStatHF"    : [22, 6],
        "PileUpDataMC"      : [21, 2],
        "PileUpPtRef"       : [21, 3],
        "PileUpPtBB"        : [21, 4],
        "PileUpPtEC1"       : [21, 5],
        "PileUpPtEC2"       : [21, 6],
        "PileUpPtHF"        : [21, 7],
    }

    }

    return config

#######################

#Block to read the text file in as lines
def read_file(file_path):
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines

def split_line(line):
    values = [float(num) for num in line.split()]
    return values

parser = argparse.ArgumentParser()

parser.add_argument("--ymax", type = float, default = 20., help = "y axis max")
parser.add_argument("--ymin", type = float, default = 0., help = "y axis min")
parser.add_argument("--logx", action = "store_true", default=False, help = "Set log x axis")
parser.add_argument("--logy", action = "store_true", default=False, help = "Set log y axis")
parser.add_argument("--legdim", nargs = 4, type = float, default = [0.5, 0.5, 0.9, 0.88], help = "legend dimensions")
parser.add_argument("--year", type = str, default = "UL2018", help = "year = UL2016preVFP/UL2016/UL2017/UL2018")

args = parser.parse_args()

if __name__ == "__main__" :

    config = set_config()

### Input file
    file_path = ''
    if args.year == "UL2016preVFP":
        file_path = 'Summer19UL16APV_V9_MC_UncertaintySources_AK4PFchs.txt'
    elif args.year == "UL2016":
        file_path = 'Summer19UL16_V9_MC_UncertaintySources_AK4PFchs.txt'
    elif args.year == "UL2017":
        file_path = 'Summer19UL17_V6_MC_UncertaintySources_AK4PFchs.txt'
    elif args.year == "UL2018":
        file_path = 'Summer19UL18_V5_MC_UncertaintySources_AK4PFchs.txt'
    else:
        raise RuntimeError( "Year %s is not known! Select UL2016preVFP/UL2016/UL2017/UL2018", args.year)
    lines = read_file(file_path)

##### Build a dictionary to store values ####

# the dictionary is indexed by the uncertainty sources. For each eta bin (has a minimum and maximum bin edge), each pt point is saved with the corresponding uncertainty such that the numerical list index is the same for the pt and the uncertainty. This is important because plotting the graphs vs pt is trivial using arrays, but for the histograms vs eta, one needs to loop over each eta bin additionally.

#Structure

#uncertainty source :
#    [eta0_low, eta0_high] :
#       [pt0,   pt1,    pt2,    pt3,    ...,    pt50]
#       [unc0,  unc1,   unc2,   unc3,   ...,    unc50]
#    [eta1_low, eta1_high] :
#       [pt0,   pt1,    pt2,    pt3,    ...,    pt50]
#       [unc0,  unc1,   unc2,   unc3,   ...,    unc50]
#     .
#     .
#     .
#
#    [etan_low, etan_high] :
#       [pt0,   pt1,    pt2,    pt3,    ...,    pt50]
#       [unc0,  unc1,   unc2,   unc3,   ...,    unc50]

    type_dict = {}

    tempname = None

    for line in lines:
        if "#" in line or "{" in line : continue
        if "[" in line and "]" in line :
            tempname = line.strip("[]")
            type_dict[tempname]={"eta" : [], "pt" : [], "err" : []}
            continue
        values = split_line(line)
        type_dict[tempname]["eta"].append([values[0], values[1]])
        type_dict[tempname]["pt"].append(values[3::3])
        type_dict[tempname]["err"].append(values[4::3])

#############################################
## Definitions useful for binning

    eta_bins = []
    pt_bins = []

    for el in type_dict[tempname]['eta'] :
        eta_bins.append(el)

    for el in type_dict[tempname]['pt'][0] :
        pt_bins.append(el)

    eta_edges = []
    for el in eta_bins :
        eta_edges.append(el[0])
    eta_edges.append(el[1])

############################################

    graphs = {}
    hists = {}

    if not os.path.exists(config['outdir']):
        os.makedirs(config['outdir'])

############################################################
#### Individual TGraphs (vs pt) and histograms (vs eta) for each source in config['sources']

    for name in config['sources'] :

        #### Graphs vs pt #####
        for i in range(len(eta_bins)) :     ## Looping over each eta bin to set the y value as the uncertainty corresponding to each pt point
            graph_name = "pt_{source}_etabin_{val1}_{val2}".format(source=name, val1 = eta_bins[i][0], val2 = eta_bins[i][1])
            xarray = np.array(type_dict[name]['pt'][i], 'd')        # We can easily do this as pt points are set into an array.
            yarray = np.array(type_dict[name]['err'][i], 'd')
            yarray = yarray*100.
            graph = R.TGraph(len(xarray), xarray, yarray)
            graph.SetMarkerStyle(config['sources'][name][0])
            graph.SetMarkerColor(config['sources'][name][1])
            graphs[graph_name] = graph

        ###### Histogram vs eta
        for i in range(len(pt_bins)) :      ## Looping over each pt value
            hist_name = "eta_{source}_pt_{pt}".format(source=name, pt=pt_bins[i])
            xarray = np.array(eta_edges, 'd')
            hist = R.TH1F("h", "h", len(xarray)-1, xarray)
            for j in range(len(eta_bins)) : # Here we loop over each eta bin and set the content of each bin to be the uncertainty value
                hist.SetBinContent(j+1, type_dict[name]['err'][j][i]*100.)
            hist.SetStats(0)
            hist.SetMarkerStyle(config['sources'][name][0])
            hist.SetMarkerColor(config['sources'][name][1])
            hist.SetLineColor(1)
            hists[hist_name] = hist.Clone()

            hist.Delete()

#############################################
#################### Adding uncertainties in quadrature for all sets in in config['quad']
    if len(config["quad"]):
        for i in range(len(eta_bins)) :
            linecol = 2
            for quadname in config['quad'] :
                yarray = np.zeros(len(pt_bins))
                for source in config['quad'][quadname] :
                    yarray_temp = np.array(type_dict[source]['err'][i], 'd')**2
                    yarray = yarray + yarray_temp

                yarray = np.sqrt(yarray)
                graphname = "pt_{source}_etabin_{val1}_{val2}".format(source=quadname, val1 = eta_bins[i][0], val2 = eta_bins[i][1])
                xarray = np.array(pt_bins, 'd')
                yarray = yarray*100.
                graph = R.TGraph(len(xarray), xarray, yarray)
                graphs[graphname] = graph
                graphs[graphname].SetLineColor(linecol)
                linecol+= 1
                graphs[graphname].SetLineWidth(2)


        for i in range(len(pt_bins)) :
            linecol = 2
            xarray = np.array(eta_edges, 'd')
            for quadname in config['quad'] :
                hist = R.TH1F("h", "h", len(xarray)-1, xarray)
                hist_name = "eta_{source}_pt_{pt}".format(source=quadname, pt=pt_bins[i])
                for j in range(len(eta_bins)) :
                    err = 0.
                    for source in config['quad'][quadname] :
                        err += type_dict[source]['err'][j][i]**2
                    err = np.sqrt(err)*100.
                    hist.SetBinContent(j+1, err)
                hist.SetStats(0)
                hist.SetLineColor(linecol)
                linecol+=1
                hist.SetLineWidth(2)
                hists[hist_name] = hist.Clone()
                hist.Delete()

###############################
############### Plotting overlaid histograms vs pt

    for etabin in eta_bins :
        if "eta" in config :
          for etavalue in config["eta"] :
            if etavalue < etabin[0] or etavalue > etabin[1] : continue
            c = R.TCanvas("c", "c", 800, 600)
            legdim = args.legdim
            leg = R.TLegend(legdim[0], legdim[1], legdim[2], legdim[3])
            firstplot = True
            for graphname in graphs :
                eta_range = "{}_{}".format(etabin[0], etabin[1])
                if eta_range in graphname :
                    namelist = graphname.split("_")
                    leg.AddEntry(graphs[graphname], namelist[1])
                    if firstplot is True :
                        graphs[graphname].GetYaxis().SetTitle("JEC uncertainty [%]")
                        graphs[graphname].GetXaxis().SetTitle("p_{T} [GeV]")
                        graphs[graphname].Draw()
                        graphs[graphname].SetMinimum(args.ymin)
                        graphs[graphname].SetMaximum(args.ymax)
                        graphs[graphname].SetTitle("")
                        firstplot = False
                    else :
                        graphs[graphname].Draw("pl same")

            leg.SetLineWidth(0)
            leg.Draw("same")
            if args.logx : c.SetLogx()
            if args.logy : c.SetLogy()
            latex = R.TLatex(15, 16, "{} < #eta < {}".format(etabin[0], etabin[1]))
            if "eta" in config : latex = R.TLatex(15, 16, "#eta = {}".format(etavalue))
            latex.SetTextSize(0.04)
            latex.Draw()
            c.Update()
            plotname = "pt_etabin_{}_{}".format(etabin[0], etabin[1])
            c.SaveAs("{}{}.root".format(config["outdir"], plotname))
            c.SaveAs("{}{}.png".format(config["outdir"], plotname))
            c.SaveAs("{}{}.pdf".format(config["outdir"], plotname))

##############################
####### Plotting overlaid histograms vs eta

    if "pt" in config :
      for ptvalue in config["pt"]:
        if ptvalue not in pt_bins :
            print("Uncertainties not available for pt = {}. Try one of the following".format(ptvalue))
            print(pt_bins)
        for pt in pt_bins :
            if pt != ptvalue : continue
            c = R.TCanvas("c", "c", 800, 600)
            legdim = args.legdim
            leg = R.TLegend(legdim[0], legdim[1], legdim[2], legdim[3])
            firstplot = True
            for histname in hists :
                pt_str = "pt_{}".format(pt)
                if pt_str in histname :
                    namelist = histname.split("_")
                    leg.AddEntry(hists[histname], namelist[1])
                    if firstplot is True :
                        hists[histname].GetYaxis().SetTitle("JEC uncertainty [%]")
                        hists[histname].GetXaxis().SetTitle("#eta")
                        hists[histname].Draw("pl")
                        hists[histname].SetMinimum(args.ymin)
                        hists[histname].SetMaximum(args.ymax)
                        hists[histname].SetTitle("")
                        firstplot = False
                    else :
                        hists[histname].Draw("pl same")

            leg.SetLineWidth(0)
            leg.Draw("same")
            if args.logy : c.SetLogy()
            latex = R.TLatex(-4.5, 18, "p_{{T}} = {}".format(ptvalue))
            latex.SetTextSize(0.04)
            latex.Draw()
            c.Update()
            plotname = "eta_pt_{}".format(pt)
            c.SaveAs("{}{}.root".format(config["outdir"], plotname))
            c.SaveAs("{}{}.png".format(config["outdir"], plotname))
            c.SaveAs("{}{}.pdf".format(config["outdir"], plotname))
