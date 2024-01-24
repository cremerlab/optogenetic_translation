# Cloning of pZE31-MBP-sfGFP

## Purpose
This markdown file contains my notes summarizing the cloning steps undertaken to
create pZE31-ccaS/R_MBP-sfGFP, a light-inducible MBP-sfGFP fusion. This acts as a 
longer version of sfGFP, which is needed to account for the transcription, translation,
folding, and maturation time of sfGFP. This is akin ot using the lacZ-alpha isoform 
as described in Dai et al. 2016. 

## Templates

| **Plasmid Name** | **Source** | **Notes**|
|--|--|--|
|pSKA413| [Addgene 80381](https://www.addgene.org/80381/) | Expresses sfGFP from CpcG2d59 promoter. Also constitutively expresses ccaSR|
|pSub-MBP-sfGFP | [Addgene 18757](https://www.addgene.org/185757/) | Expresses MBP-sfGFP with a TEV linker. |


## Primers
| **Primer Name** | **Sequence (5' -> 3')** | **Notes** |
|--|--|--|
|GC125_pZE31-MBP_FWD | `aggcacgtaaggcaccatataatgaaa` `actgaagaaggtaaactggtaatctg` | Anneals to pSub-MBP-sfGFP, with homology to promoter of pSKA413. Amplifies MBP-linker |
|GC126_pZE31-MBP_REV | `gtgaaaagttcttctcctttacg` `catggatccaccggaaccttg`| Anneals to pSub-MBP-sfGFP, with homology to promoter of pSKA413. Amplifies MBP-linker |
|GC127_pZE31-GFP_FWD | `atgcgtaaaggagaagaacttttcac`| Anneals to pSKA413. Amplifies backbone. |
|GC128_pZE31-GFP_REV | `tatatggtgccttacgtgcct` | Anneals to pSKA41. Amplifies backbone. |
|GC129_pZE31-MBP_REV | `atgttgcatcaccttcaccc` | Sequencing primer. Reads reverse strand from beginning of sfGFP to promoter |
GC130_pZE31-MBP_FWD| `cttcaattttactttgttaggatcgcattc` | Sequencing primer. Reads forward strand from CpcG2d59 promoter into insert |


## Strain + Locations 
| **Strain Identifier** | **Notes** | 
|--| --|
| GC001 | WT E. coli (NCM3722) |
| GC121 | pSKA413 in DH5alpha |
| GC122 | pSub-MBP-sfGFP in DH5alpha|


## Cloning Steps

<details>

<summary><b>January 23 - 24, 2024: Amplification of cloning fragments</b></summary>

### First attempt
The first attempt to clone pZE31-ccaS/ccaR_MBP-sfGFP from agar stabs received from 
addgene. I set up two PCR reactions (2 x 50 µL reactions each),

1. GC127 + GC128 + cell debris from pSKA413 agar stab. 
2. GC125 + GC126 + cell debris from pSub-MBP-sfGFP agar stab.

using the following program:

1. Boil @ 98° C for 8m
2. Denaturation @ 95° C for 30s 
3. Annealing @ 60° C for 30s 
4. Elongation @ 72° C for 3m 
5. Return to #2 x 24
6. Final elongation @ 72° C for 5 min
7. Hold @ 4° C

I ran 5 µL of each reaction on a 1% TAE Gel with the following image:

![](gel_images/2024-01-24-gel1.png)

There was some spillage of the MBP-linker insert into the adjacent wells, but that reaction seemed to work. Amplification of the backbone *did not* work. 

### Second attempt
I purified the pSKA413 plasmid from a saturated overnight culture yielding 50 µL of ≈ 160 ng/µL aliquot. Using around 8 ng, I set up an annealing temperature gradient (55° - 68° C) with the following program:

1. Boil @ 98° C for 2m
2. Denaturation @ 95° C for 30s 
3. Annealing @ 60° C for 30s 
4. Elongation @ 72° C for 3m30s 
5. Return to #2 x 24
6. Final elongation @ 72° C for 5 min
7. Hold @ 4° C


</details>
