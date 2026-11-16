#!/usr/bin/env python3
"""
Midmak repellent-brick: release-kinetics and effective-radius simulation.

IMPORTANT: every kinetic constant below is an ASSUMED design value (order-of-magnitude, literature-informed),
not a measurement. The purpose is (1) to show which parameter ranges are needed to meet the targets and
(2) to define what the lab must measure (TGA / headspace GC-MS / wind-tunnel dose-response) to replace them.

Run:  python3 release_model.py        (writes CSVs + PNGs next to this file)
"""
import numpy as np, csv, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
R = 8.314                       # J/mol/K
T_REF = 298.15

# ---------------- geometry / loading (per m^2 of exposed wall face) ----------------
L      = 0.010                  # m, functional skin thickness (sealed back, one open face)
RHO    = 1900.0                 # kg/m3, skin bulk density
LOAD   = 0.005                  # 0.5 wt% active blend in the skin
M0     = L * RHO * LOAD * 1000  # g of active per m2  -> 95 g/m2
A_SRC  = 1.0                    # m2 source area
R0     = (A_SRC / (2*np.pi))**0.5   # m, source-size regularisation (~0.40 m)

# ---------------- formulations (ASSUMED parameters) ----------------
# model 'slab': Fickian release from a one-face-open slab, D_app(T)=D25*exp(Ea/R*(1/298.15-1/T))
# model 'reservoir': liquid-core capsules + membrane/sealer: ~zero-order flux Q0 until 10% remains, then first-order tail
FORMS = {
 "F0 neat oil in porous skin":              dict(model="slab", D25=1.0e-11, Ea=45e3),
 "F1 oil on diatomite/zeolite carrier":     dict(model="slab", D25=4.0e-13, Ea=50e3),
 "F2 beta-CD complex + carrier":            dict(model="slab", D25=1.5e-13, Ea=65e3),
 "F3 biopolymer microcapsules + sealer":    dict(model="reservoir", T_dep25=330.0, Ea=55e3),
}
TEMPS = [25, 40, 55]            # deg C  (shaded / hot ambient / sun-heated surface)
T_DAYS = np.unique(np.r_[np.linspace(0.05, 10, 200), np.linspace(10, 730, 1500)])

def arr(Ea, TC):                # Arrhenius acceleration vs 25 C
    return np.exp(Ea/R * (1/T_REF - 1/(TC+273.15)))

def slab_release(D, t_s, nterm=400):
    tau = D * t_s / L**2
    n = np.arange(nterm)[:, None]
    a = (2*n+1)**2 * np.pi**2 / 4
    F = 1 - np.sum(8/((2*n+1)**2*np.pi**2) * np.exp(-a*tau[None, :]), axis=0)
    dF = np.sum(2 * D/L**2 * np.exp(-a*tau[None, :]), axis=0)      # 1/s
    return np.clip(F, 0, 1), dF

def reservoir_release(T_dep_days, t_days, dt=0.05):
    Q0 = 1.0/T_dep_days                                             # fraction/day at constant-activity stage
    t = np.arange(0, t_days.max()+dt, dt); m = np.empty_like(t); m[0] = 1.0
    for i in range(1, len(t)):
        rate = Q0 * min(1.0, m[i-1]/0.10)
        m[i] = max(0.0, m[i-1] - rate*dt)
    F = 1 - np.interp(t_days, t, m)
    rate = Q0*np.minimum(1.0, (1-F)/0.10)
    return F, rate/86400.0                                          # dF/dt in 1/s

def release(name, TC):
    p = FORMS[name]
    if p["model"] == "slab":
        F, dF = slab_release(p["D25"]*arr(p["Ea"], TC), T_DAYS*86400)
    else:
        F, dF = reservoir_release(p["T_dep25"]/arr(p["Ea"], TC), T_DAYS)
    return F, dF*M0*86400.0                                         # F, Q in g/day/m2

def r_eff(Q_g_day, K, Cstar_ug_m3):
    Q = Q_g_day*1e6/86400.0                                         # ug/s
    R = Q/(2*np.pi*K*Cstar_ug_m3)                                   # r at which C = C*  (point source on a plane)
    return np.sqrt(np.maximum(R**2 - R0**2, 0.0))                   # regularised for a 1 m2 source

if __name__ == "__main__":
    rows, rrows, summ = [], [], []
    K_SCEN = {"sheltered courtyard (K=0.005 m2/s)": 0.005, "open/breezy (K=0.05 m2/s)": 0.05}
    CSTARS = [10, 100, 1000]       # ug/m3, ASSUMED effective airborne thresholds -> must be measured (EC50)
    REP_T = [1, 7, 30, 90, 180, 365]
    data = {}
    for name in FORMS:
        for TC in TEMPS:
            F, Q = release(name, TC); data[(name, TC)] = (F, Q)
            for i in range(0, len(T_DAYS), 5):
                rows.append([name, TC, round(T_DAYS[i], 3), round(F[i], 5), round(Q[i], 5)])
            # service life: days with r_eff>=0.5 m (sheltered, C*=100)
            ok = r_eff(Q, 0.005, 100) >= 0.5
            life = T_DAYS[ok].max() if ok.any() else 0.0
            t50 = T_DAYS[np.argmax(F >= 0.5)] if (F >= 0.5).any() else np.nan
            t90 = T_DAYS[np.argmax(F >= 0.9)] if (F >= 0.9).any() else np.nan
            summ.append([name, TC, round(t50, 1), round(t90, 1), round(life, 1)])
            for kn, K in K_SCEN.items():
                for C in CSTARS:
                    for d in REP_T:
                        j = np.argmin(abs(T_DAYS-d))
                        rrows.append([name, TC, kn, C, d, round(Q[j]*1e6/86400, 4), round(float(r_eff(Q[j], K, C)), 3)])
    w = lambda f, h, r: csv.writer(open(os.path.join(HERE, f), "w", newline="")).writerows([h]+r)
    w("release_vs_time.csv", ["formulation","T_C","t_days","fraction_released","flux_g_per_day_per_m2"], rows)
    w("effective_radius.csv", ["formulation","T_C","airflow_scenario","C_star_ug_m3","t_days","emission_ug_per_s","r_eff_m"], rrows)
    w("summary_metrics.csv", ["formulation","T_C","t50_days","t90_days","service_life_days_(r_eff>=0.5m;K=0.005;C*=100)"], summ)

    # ---------------- figures ----------------
    pal = {"F0":"#94A3B8","F1":"#7786A2","F2":"#27CE9B","F3":"#0E8F68"}
    col = lambda n: pal[n[:2]]
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"grid.alpha":.25})
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    for n in FORMS:
        F, Q = data[(n, 25)]; ax[0].plot(T_DAYS, F*100, color=col(n), lw=2, label=n)
        F, Q = data[(n, 40)]; ax[1].plot(T_DAYS, F*100, color=col(n), lw=2, label=n)
    for a, t in zip(ax, ["25 °C (shaded)", "40 °C (hot ambient)"]):
        a.set_xlabel("days"); a.set_ylabel("cumulative release (% of loaded active)"); a.set_title(t); a.set_xlim(0, 730)
    ax[0].legend(fontsize=8, frameon=False); fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig1_cumulative_release.png"), dpi=170); plt.close(fig)

    fig, ax = plt.subplots(1, 4, figsize=(14, 3.6), sharey=True)
    for a, n in zip(ax, FORMS):
        for TC, ls in zip(TEMPS, ["-", "--", ":"]):
            F, Q = data[(n, TC)]; a.semilogy(T_DAYS, np.maximum(Q, 1e-5), ls, color=col(n), lw=2, label=f"{TC} °C")
        a.axhline(0.174, color="#E11D48", lw=1, ls="-."); a.set_title(n, fontsize=8.5); a.set_xlabel("days"); a.set_xlim(0, 400); a.set_ylim(1e-3, 1e3)
    ax[0].set_ylabel("emission (g/day per m² of wall)"); ax[0].legend(fontsize=8, frameon=False)
    ax[0].text(150, 0.26, "min. flux for r_eff ≥ 0.5 m\n(K=0.005, C*=100 µg/m³)", color="#E11D48", fontsize=7.5)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig2_emission_flux.png"), dpi=170); plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for a, (kn, K) in zip(ax, K_SCEN.items()):
        for n in FORMS:
            F, Q = data[(n, 25)]; a.plot(T_DAYS, r_eff(Q, K, 100), color=col(n), lw=2, label=n)
        a.set_title(kn+", C*=100 µg/m³, 25 °C", fontsize=9); a.set_xlabel("days"); a.set_xlim(0, 400)
    ax[0].set_ylabel("effective radius r_eff (m)"); ax[0].set_ylim(0, 3); ax[0].legend(fontsize=7.5, frameon=False)
    ax[1].text(200, 1.5, "r_eff < source radius (0.4 m) for every formulation:\nin open air the effect is limited to the wall's\nimmediate contact/landing zone", ha="center", fontsize=9, color="#475569")
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig3_effective_radius.png"), dpi=170); plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.5, 3.8)); wd = 0.26
    for k, TC in enumerate(TEMPS):
        v = [next(s[4] for s in summ if s[0]==n and s[1]==TC) for n in FORMS]
        ax.bar(np.arange(4)+(k-1)*wd, v, wd, label=f"{TC} °C", color=["#C7D2DC","#7786A2","#27CE9B"][k])
    ax.set_xticks(range(4)); ax.set_xticklabels([n[:2] for n in FORMS]); ax.set_ylabel("service life (days)\nr_eff ≥ 0.5 m, K=0.005, C*=100")
    ax.legend(frameon=False); fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig4_service_life.png"), dpi=170); plt.close(fig)
    print("M0 = %.0f g/m2, R0 = %.2f m" % (M0, R0))
    for s in summ: print(s)
