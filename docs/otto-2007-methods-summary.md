# Methods Summary

## Simulations

They use a bioenergetics population model from the Yodiz & Innes style. The model: 

$$ \frac{dB_b}{dt} = r_bG_bB_b - x_iy_iF_{ib}\frac{B_i}{e} $$
$$ \frac{dB_i}{dt} = -x_iB_i + x_iy_iF_{ib}B_i - x_ty_tF_{ti}\frac{B_t}{e} $$
$$ \frac{dB_t}{dt} = -x_tB_t + x_ty_tF_{ti}B_i$$

*Variables:*
 * *e* = assimilation efficiency
 * *$G_b$* = logistic net growth w/ carrying capacity *K*
 * *F* = a type II functional response
 * *r* = growth rate
 * *x* = metabolic rate
 * *y* = maximum consumption rate

All the biological rates scale with body mass, which is *M*. Maximum consumption rate was constant, *x* increased with body-mass ratio to basal species:

$$ x_{i,t} = a(\frac{M_{i,t}}{M_b})^{-0.25} $$

where *a* is a constant. When *R* is varied,

$$ R_{ti} = M_t/M_i $$
$$ R_{ib} = M_i/M_b $$

the consumtion here is *xyF*. The top-down pressure per unit biomass on basal and intermediate species are:

$$ P_{b,i} = \frac{x_{i,t}y_{i,t}F_{ib,ti}B_{i,t}}{B_{b,i}} $$ 

and the energy fluxes per unit biomass to intermediate and top species are:

$$ E_{i,t} = x_{i,t}y_{i,t}F_{ib,ti} $$ 

Note also that:

$$ G_b = 1 \frac{B_b}{K} $$
$$F_{ib} = B_b/(B_0 + B_b) $$
$$F_{ti} = B_i/(B_0 + B_i) $$ 

where $B_0$ is the half saturation density. Here, the fraction of biomass removed from the resource population that is actually eaten is = 1. Production ($W$), metabolism ($X$), and maximum consumption ($Y$) are given by:

$$Y_{i,t} = a_yM_{i,t}^{-0.25} $$
$$X_{i,t} = a_xM_{i,t}^{-0.25} $$
$$W_{b} = a_rM_{b}^{-0.25} $$

where $a_r, a_x,$ and $a_y$ are allometric constants (discussed in Yodiz & Innes). You can define the timescale of the system by setting the mass-specific growth rate to unity ($dB_t/dt$). Then the mass-specific metabolic rates of all species, $x$, are normalized by the timescale ($dBi/dt$) and the maximum consumption rates, $y$, are normalized by the metabolic rates: 

$$ r_i = 1$$
$$x_{i,t} = \frac{X_{i,t}}{W_b} = \frac{a_x}{a_r}(\frac{M_{i,t}}{M_b})^{-0.25} $$
$$y_{i,t} = \frac{Y_{i,t}}{X_{i,t}} = \frac{a_y}{a_x} $$

If you sub in all of these into the $dB/dt$ equations above, you get a population dynamic model with allometrically scaled and normalized parameters. 

Note that the body mass of the basal species $M_b = 1$ and the body masses of all other species, $M_i$ and $M_t$ are expressed relative to the body mass of the basal species. This makes results independent of the body mass of the basal species. 