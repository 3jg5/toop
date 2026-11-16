#!/usr/bin/env python3
"""Screening-level cost and carbon add-on per m2 of wall face for each formulation.
ALL unit prices and emission factors are indicative ranges (low, high) to be replaced by supplier quotes / EPDs."""
import csv, os
HERE=os.path.dirname(os.path.abspath(__file__))
M0=0.095   # kg active per m2 (see release_model.py)
# name: (price USD/kg low, high ; GWP kg CO2e/kg low, high)
MAT={
 "essential-oil blend (cedarwood+lemongrass)":(25,60, 2.0,8.0),
 "diatomite/zeolite carrier (milled)":        (0.4,1.2, 0.3,1.0),
 "beta-cyclodextrin":                         (3,10,   3.0,6.0),
 "gum arabic / maltodextrin shell":           (3,8,    0.5,1.5),
 "encapsulation processing (toll, per kg capsules)":(3,10, 0.5,2.0),
 "lime/silicate sealer coat":                 (3,8,    0.5,1.0),
}
# kg of each material per m2, by formulation
BOM={
 "F0 neat oil in porous skin":            {"essential-oil blend (cedarwood+lemongrass)":M0},
 "F1 oil on diatomite/zeolite carrier":   {"essential-oil blend (cedarwood+lemongrass)":M0,"diatomite/zeolite carrier (milled)":M0/0.40},
 "F2 beta-CD complex + carrier":          {"essential-oil blend (cedarwood+lemongrass)":M0,"beta-cyclodextrin":M0/0.12,"diatomite/zeolite carrier (milled)":0.10},
 "F3 biopolymer microcapsules + sealer":  {"essential-oil blend (cedarwood+lemongrass)":M0,"gum arabic / maltodextrin shell":M0,
                                           "encapsulation processing (toll, per kg capsules)":2*M0,"diatomite/zeolite carrier (milled)":0.05,
                                           "lime/silicate sealer coat":0.2},
}
BASE_GWP=190*0.10*0.85      # kg CO2e per m2 of a 100 mm wall: 190 kg/m2, 10% cement, 0.85 kg CO2e/kg cement
rows=[["formulation","addon_cost_USD_per_m2_low","addon_cost_USD_per_m2_high","addon_GWP_kgCO2e_per_m2_low","addon_GWP_kgCO2e_per_m2_high","addon_GWP_pct_of_baseline_wall_low","addon_GWP_pct_of_baseline_wall_high"]]
for f,b in BOM.items():
    c=[sum(m*MAT[k][0] for k,m in b.items()),sum(m*MAT[k][1] for k,m in b.items())]
    g=[sum(m*MAT[k][2] for k,m in b.items()),sum(m*MAT[k][3] for k,m in b.items())]
    rows.append([f,round(c[0],2),round(c[1],2),round(g[0],2),round(g[1],2),round(100*g[0]/BASE_GWP,1),round(100*g[1]/BASE_GWP,1)])
csv.writer(open(os.path.join(HERE,"cost_lca_screening.csv"),"w",newline="")).writerows(rows)
print("baseline wall GWP %.1f kgCO2e/m2"%BASE_GWP)
for r in rows: print(r)
