---
status: In progress
reason: 
---

# 2024-02-01 Pilot Plasmid Test

## Purpose
This is a pilot experiment designed to test if the pSKA413 plasmid acts well 
as an optogenetic inducer of sfGFP in NCM3722 *E. coli*. This follows a transformation 
of the plasmid, ordered from Addgene, into our canonical lab strain. While this 
experiment is not being done using the target equipment, it should act as a good 
measure of whether things are working or not. 

## Experiment Design
Wildtype *E. coli* NCM3722 (strain GC001) containing plasmid pSKA413 is grown in
a minimal medium supplemented with acetate and ammonium chloride as carbon and 
nitrogen sources, respectively, and with chloramphenicol, under different red
(660 nm) and green (530 nm) illumination conditions. These are grown in 30 mL
aliquots in a PSI Multicultivator. Without careful preculturing of the cells, 
this is a sanity check to see if we can get a titration curve of sfGFP
fluorescence as 535 nm illumination is titrated, keeping track of illumination
as µE (µmol photons • m^-2 • s^-1).

All eight reaction vessels of the PSI Multicultivator were used in this experiment, 
with the following illumination settings.

| Vessel Number | Wavelength | Illumination |
|:--:|:--:|:--:|
| 1 | 660 nm | 300 µE |
| 2 | 530 nm | 25 µE | 
| 3 | 530 nm | 50 µE |
| 4 | 530 nm | 75 µE |
| 5 | 530 nm | 100 µE |
| 6 | 530 nm | 150 µE |
| 7 | 530 nm | 200 µE | 
| 8 | None | 0 |

Vessel #8 was set at 0 µE illumination intensity, but in reality is very lowly 
illuminated by the neighboring vessel. This is something that needs more careful
control in future experiments if we will still use the PSI Multicultivator for
these experiments.

## Materials 
### Strains
| Strain Identifier | Plasmid | Host Strain | Species | Short-hand |
|:--:|:--:|:--:|:--:|
| GC001 | pSKA413 | NCM3722 | E. coli | WT |

### Media



## Protocol 
1. A seed culture was started by inoculating 3 mL of LB supplemented with 50 µg / mL chloramphenicol
with a colony of GC123 and was grown in a 37° C water bath for 2 - 3 hours until 
visibly turbid. 

2. The culture was diluted 1:2000 into 400 mL of prewarmed N-C- + 30 mM acetate + 10 mM
NH_4_Cl + micronutrients. The culture was well mixed and separated into 50 mL aliquots
into PSI Multicultivator reaction vessels. 

3. The vessels were stationed into the PSI Multicultivator waterbath, set at 37° C. 
Glass tubes were affixed to the sterilized bubbling line and the flow rate was 
adjusted to be vigorous and visually similar across culture tubes. I estimate there are ≈ 100 small bubbles per second. 

4. The OD sensors were zeroed on the dilute medium and the lights were turned on as 
described in the **Experiment Design** section of these notes. 

5. OD_680nm_ measurements were taken every 5 minutes after a 30s cessation in bubbling. These measurements were 
taken for the duration of the experiment. 

