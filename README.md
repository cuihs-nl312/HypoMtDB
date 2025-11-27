# HypoMtDB

# Overview

**`HypoMtDB`** is a comprehensive mitochondrial genome database of Hypocreales Fungi. As a group with high species diversity and unique evolutionary characteristics in the phylum Ascomycota, Hypocreales plays a crucial role in multiple fields, including material cycling in ecosystems, agricultural production, pharmaceutical research and development, and the study of fungal evolutionary mechanisms. This study integrated the mitochondrial genome data of nearly a thousand strains from **`10 families`** of Hypocreales. At the same time, genome assembly was also performed on some species without mitochondrial genomes.<br>

# Data Structure
```
HypoMtDB/                                                             # 数据库根目录
├── README.md                                                         # 数据库说明文档（核心导航，含目录、使用指南）
├── LICENSE                                                           # 开源许可（如 MIT 协议，明确数据使用、修改规则）
├── meta_information/                                                 # 元信息文件夹（存储所有样本的基础描述信息）
│   ├── Hypocreales_mitogenomes_infor.txt                             # 样本总表：包含物种名、样本ID、Accession、Reference等
│   ├── Clavicipitaceae_mitogenomes_infor.txt                        
│   ├── Cordycipitaceae_mitogenomes_infor.txt
│   ├── Bionectriaceae_mitogenomes_infor.txt
│   ├── Nectriaceae_mitogenomes_infor.txt
│   ├── Niessliaceae_mitogenomes_infor.txt
│   ├── Ophiocordycipitaceae_mitogenomes_infor.txt
│   ├── Pseudodiploosporaceae_mitogenomes_infor.txt
│   ├── Sarocladiaceae_mitogenomes_infor.txt
│   ├── Stcahybotryaceae_mitogenomes_infor.txt
├── mitogenomes_data/                                                 # 基因组相关数据（核心数据，存储 FASTA 格式线粒体序列以及基因组注释文件）
│   ├── Hypocreaceae/                                                 # 科级子文件夹（肉座菌科）
│   │    └──Trichoderma                                               # 属级子文件夹（木霉属）
│   │       └── Trichoderma_breve_T069                                # Trichoderma breve T069 菌株文件夹
│   │           ├── Trichoderma_breve_T069.fasta                      # Trichoderma breve T069 菌株线粒体基因组序列
│   │           ├── Trichoderma_breve_T069.gb                         # Trichoderma breve T069 菌株线粒体基因组 genbank 文件
│   │           ├── Trichoderma_breve_T069_cds.fasta                  # Trichoderma breve T069 菌株线粒体基因组 cds 文件
│   │           └── Trichoderma_breve_T069_pep.fasta                  # Trichoderma breve T069 菌株线粒体基因组 pep 文件
│   ├── Clavicipitaceae/                                              
│   ├── Cordycipitaceae/
│   ├── Bionectriaceae/
│   ├── Nectriaceae/
│   ├── Niessliaceae/
│   ├── Ophiocordycipitaceae/
│   ├── Pseudodiploosporaceae/
│   ├── Sarocladiaceae/
│   ├── Stcahybotryaceae/ 
└── scripts/                                                          # 辅助脚本文件夹（存储数据处理、格式转换工具）
    ├── one_step_to_construct_database.py                             # Python 脚本：处理收集的数据文件，一步搭建数据库
    └── README.md                                                     # 脚本使用说明
```
# How to download HypoMtDB?
## Windows Download
  Go to the HypoMtDB page on GitHub. Click the `Code` button on the page, then select `Download ZIP`. All data from HFMtDB will then be downloaded to your computer.
  
## Linux Download
  Use the following code in the Linux command line. HFMtDB will be downloaded to the Linux directory.
```
git clone https://github.com/cuihs-nl312/HypoMtDB.git
```

# Meta information
  Meta_information包含所有样本的基础描述信息，这里我们使用表格文件`Hypocreales_mitogenomes_infor.txt`来展示所有物种线粒体基因组的基础信息。具体信息如下
| Family | Species | Strain | Abbreviation | Accession | Mitogenome Size (bp) | GC (%) | Complete (Y/N) | Download |Reference |
| --- | :---: | :---: |  :---: |  :---: |  :---: | :---: | :---: | :---: | ---: |
| Hypocreaceae | Trichoderma breve | T069 | HyTbT069 | PP933710.1 | 26285 | 27.44 | Y | https://www.ncbi.nlm.nih.gov/nuccore/PP933710.1 | https://doi.org/10.3390/ijms252212140 |

# Mitogenomes data
  In the Mitogenomes_data directory, mitochondrial genome sequence data and the annotation data of 11 families belonging to Hypocreales are presented. The mitochondrial data of each strain is stored in a separate folder named after the family and genus. The mitochondrial data of each strain is presented as an individual FASTA-formatted file, with the filename containing the species name and strain name.`Trichoderma_breve_T069.fasta `;`Trichoderma_breve_T069.gb`;`Trichoderma_breve_T069.gff`.

# Script

