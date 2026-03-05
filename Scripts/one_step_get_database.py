# 该程序用于读取一个文件信息，一键式生成 HypoMtDB 数据库



import os
import sys
import subprocess
import pandas as pd


def README_creat(output):
    readme_content = '''
    # HypoMtDB
    
    # Overview
    
    **`HypoMtDB`** is a comprehensive mitochondrial genome database of Hypocreales Fungi. As a group with high species diversity and unique evolutionary characteristics in the phylum Ascomycota, Hypocreales plays a crucial role in multiple fields, including material cycling in ecosystems, agricultural production, pharmaceutical research and development, and the study of fungal evolutionary mechanisms. This study integrated the mitochondrial genome data of nearly a thousand strains from **`11 families`** of Hypocreales. At the same time, genome assembly was also performed on some species without mitochondrial genomes.<br>
    
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
    │   │           └── Trichoderma_breve_T069.gff                        # Trichoderma breve T069 菌株线粒体基因组 gff3 文件
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
    
    # Meta_information
      Meta_information包含所有样本的基础描述信息，这里我们使用表格文件`Hypocreales_mitogenomes_infor.txt`来展示所有物种线粒体基因组的基础信息。具体信息如下
    | Family | Species | Strain | Abbreviation | Accession | Mitogenome Size (bp) | GC (%) | Complete (Y/N) | Download |Reference | Note. |
    | --- | :---: | :---: |  :---: |  :---: |  :---: | :---: | :---: | :---: | :---: | ---: |
    | Hypocreaceae | Trichoderma breve | T069 | HyTbT069 | PP933710.1 | 26285 | 27.44 | Y | https://www.ncbi.nlm.nih.gov/nuccore/PP933710.1 | https://doi.org/10.3390/ijms252212140 |-- |
    
    # Mitogenomes_data
      In the Mitogenomes_data directory, mitochondrial genome sequence data and the annotation data of 11 families belonging to Hypocreales are presented. The mitochondrial data of each strain is stored in a separate folder named after the family and genus. The mitochondrial data of each strain is presented as an individual FASTA-formatted file, with the filename containing the species name and strain name.`Trichoderma_breve_T069.fasta `;`Trichoderma_breve_T069.gb`;`Trichoderma_breve_T069.gff`.
    
    # Script

    '''
    with open(output, 'w') as WW:
        WW.write(readme_content)


# 将 html 文件内容写到 out_file 中
def Index_creat(output_file):
    # 定义 HTML 内容（注意：Python 字符串用三引号包裹，内部双引号无需转义，或用反斜杠转义）
    html_content = '''<!DOCTYPE html>
    <html>
    <head>
    <title>HypoMtDB index</title>
    <style>
    .page-container {
      width: 1200px;
      margin: 0 auto;
      border: 1px solid #ccc;
    }
    .content {
      font-family:times new roman;
      margin: 90px;
    }
    </style>
    </head>
    
    <body class="page-container" style="text-align: justify;border:1px solid;">
    <div class="content">
      <h1>Welcome to HFMtDB!</h1>
    
      <p style="font-family:times new roman;color:rgba(242,14,0,1);font-size:30px;">HFMtDB is a comprehensive mitochondrial genome database of Hypocreales Fungi.</p>
      <p style="font-family:times new roman;font-size:24px; text-align: justify;
              width: 1000px; /* 核心：限制文本宽度（框的宽度），可按需调整 */
              margin: 0 0; /* 让固定宽度的文本框在页面水平居中 */
              margin-top: 10px; margin-bottom: 10px;">
    As a group with high species diversity and unique evolutionary characteristics in the phylum Ascomycota,
    Hypocreales plays a crucial role in multiple fields, including material cycling in ecosystems, agricultural 
    production, pharmaceutical research and development, and the study of fungal evolutionary mechanisms. This 
    database integrated the mitochondrial genome data of nearly a thousand strains from 11 families of Hypocreales. 
    At the same time, genome assembly was also performed on some species without mitochondrial genomes. </p>
    
      <p style="font-size:24px;font-family:times new roman;">The data structure of the database is as follows, and you can click the position you are interested.</p>
    
      <div>
      <ul class="firstdir" style="list-style-type:square;font-family:times new roman;">
        <li style="font-size:20px;"><a href="README.md"><b>  README.md  </b></a><a>-----------------------------------------------------------Database Description Document</a></li>
        <li style="font-size:20px;"><a href="LICENSE"><b>  LICENSE  </b></a><a>----------------------------------------------------------------Open Source License</a></li>
        <li style="font-size:20px;"><a href="metadata"><b>  Meta data  </b></a><a>----------------------------------------------------------------Metadata Folder</a></li>
          <ul style="list-style-type:circle;font-family:times new roman;">
    	    <li style="font-size:20px;"><a href="meta_information/00.mitogenome_infor_Assembly.xlsx">Mitogenome_Meta_information</a></li>
    	  </ul>
      <li style="font-size:20px;"><a href="mitogenomes_sequences"><b>  Mitogenomes sequences  </b></a><a>-----------------------------------------------Mitogenomes Folder</a></li>
        <ul style="list-style-type:circle;font-family:times new roman;">
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Bionectriaceae">Bionectriaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Clavicipitaceae">Clavicipitaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Cordycipitaceae">Cordycipitaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Hypocreaceae">Hypocreaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Nectriaceae">Nectriaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Ophiocordycipitaceae">Ophiocordycipitaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Sarocladiaceae">Sarocladiaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Polycephalomycetaceae">Polycephalomycetaceae/</a></li>
    	  <li style="font-size:20px;"><a href="mitogenomes_data/Pseudodiploosporaceae">Pseudodiploosporaceae/</a></li>
    	</ul>
      <li style="font-size:20px;"><a href="index.html"><b>  Script  </b></a><a>----------------------------------------------------------------------Auxiliary Script</a></li>
      </ul>
      </div>
    </div>
    </body>
    </html>'''
    
    with open(output_file, "w", encoding="utf-8") as TT:
        TT.write(html_content)
    print(f" HTML file has been created successfully!")


def LICENSE_creat(output_file):
    license_content = '''
    还没想好写啥
    '''
    with open(output_file, 'w') as BB:
        BB.write(license_content)


# 根据表头名称获取索引（核心步骤）
# get_header_index('Species', 表头列表），返回值是 int 类型
def get_header_index(header_name, headers_list):
    try:
        return headers_list.index(header_name.strip())  # 去掉表头的空格（避免用户输入时的疏忽）
    except ValueError:
        print(f"警告：表头'{header_name}'不存在！当前表头：{headers_list}")
        return -1


# 读取excel文件，将每个sheet创建成txt文件，并将内容整理创建数据库。
def excel_to_txt(excel_file_path, main_dir, sep='\t'):
    # 1. 验证 Excel 文件是否存在
    if not os.path.exists(excel_file_path):
        print(f"错误：找不到 Excel 文件 {excel_file_path}")
        sys.exit(1)

    try:
        # 2. 读取 Excel 文件，获取所有 Sheet 名称（sheet_name=None 表示读取所有 Sheet）
        # 根据文件后缀选择解析引擎（.xlsx 用 openpyxl，.xls 用 xlrd）
        file_ext = os.path.splitext(excel_file_path)[1].lower()
        if file_ext == '.xlsx':
            excel_dict = pd.read_excel(excel_file_path, sheet_name=None, engine='openpyxl')
        elif file_ext == '.xls':
            excel_dict = pd.read_excel(excel_file_path, sheet_name=None, engine='xlrd')
        else:
            print(f"错误：不支持的文件格式 {file_ext}，仅支持 .xls/.xlsx")
            sys.exit(1)

        # 3. 遍历所有 Sheet，导出为 TXT
        sheet_names = list(excel_dict.keys())
        print(f"成功识别 {len(sheet_names)} 个 Sheet：{sheet_names}")

        # 创建一个列表，记录所有.txt文件的路径及名称
        all_sheet_txt_list = []

        meta_infor_dir = os.path.join(main_dir, 'meta_information')
        if not os.path.exists(meta_infor_dir):
            os.mkdir(meta_infor_dir)

        for sheet_name, df in excel_dict.items():
            # TXT 文件名 = Sheet 名 + .txt（自动处理 Sheet 名中的空格/特殊字符）
            txt_filename = f"{sheet_name}_mitogenomes_infor.txt"
            txt_file_path = os.path.join(meta_infor_dir, txt_filename)

            all_sheet_txt_list.append(txt_filename)

            # 导出为 TXT（index=False 不保留行索引，header=True 保留列名）,sep: TXT 文件的列分隔符（默认制表符 \t，可改为逗号 , 等）
            df.to_csv(txt_file_path, sep=sep, index=False, header=True, encoding='utf-8')
            print(f"已导出：{txt_file_path}")

        print(f"\n所有 Sheet 已成功导出到：{meta_infor_dir}/")

        Mt_data_dir = os.path.join(main_dir, 'mitogenomes_data')
        if not os.path.exists(Mt_data_dir):
            os.mkdir(Mt_data_dir)
        os.chdir(Mt_data_dir)

        for i in range(0, len(all_sheet_txt_list), 1):
            family_file_all_name = all_sheet_txt_list[i]
            family_name = all_sheet_txt_list[i].split('_mitogenomes_infor.txt')[0]
            family_dir = os.path.join(Mt_data_dir, family_name)
            family_file_all_name_path = os.path.join(meta_infor_dir, family_file_all_name)
            with open(family_file_all_name_path, 'r') as AA:
                if not os.path.exists(family_dir):
                    os.mkdir(family_dir)
                os.chdir(family_dir)
                AA_line = AA.readline()
                line_one = AA_line.split('\n')[0].split('\t')
                species_idx = get_header_index('Species', line_one)
                strain_idx = get_header_index('Strains', line_one)
                accession_idx = get_header_index('Accession', line_one)
                download_idx = get_header_index('Download', line_one)

                AA_line = AA.readline()
                mid_dir = family_dir
                while AA_line:
                    AA_line_list = AA_line.split('\n')[0].split('\t')
                    species_name = AA_line_list[species_idx]
                    strain_name = AA_line_list[strain_idx]
                    genus_name = species_name.split(' ')[0]
                    accession_ID = AA_line_list[accession_idx]
                    genus_dir = os.path.join(mid_dir, genus_name)
                    if not os.path.exists(genus_dir):
                        os.mkdir(genus_dir)
                        os.chdir(genus_dir)
                    else:
                        os.chdir(genus_dir)
                    if strain_name == ' --':
                        species_strain_integrate_name = (species_name + '_' + accession_ID).replace(' ', '_')
                    else:
                        species_strain_integrate_name = (species_name + '_' + strain_name).replace(' ', '_')
                    species_strain_integrate_name = species_strain_integrate_name.replace('(', '_')
                    species_strain_integrate_name = species_strain_integrate_name.replace(')', '_')
                    species_strain_integrate_name = species_strain_integrate_name.replace(',', '_')
                    species_strain_integrate_name = species_strain_integrate_name.replace('/', '_')
                    species_strain_integrate_name = species_strain_integrate_name.replace(':', '_')

                    species_strain_integrate_name_dir = os.path.join(genus_dir, species_strain_integrate_name)
                    if not os.path.exists(species_strain_integrate_name_dir):
                        os.mkdir(species_strain_integrate_name_dir)
                    else:
                        species_strain_integrate_name = species_strain_integrate_name + '_' + accession_ID
                        species_strain_integrate_name_dir = os.path.join(genus_dir, species_strain_integrate_name)
                        os.mkdir(species_strain_integrate_name_dir)
                    os.chdir(species_strain_integrate_name_dir)
                    # 使用 efetch 下载数据
                    mitogenome_output_file = species_strain_integrate_name + '.fasta'
                    # 下载线粒体基因组数据
                    try:
                        # 数据类型：nuccore（核酸）、protein（蛋白）、genome（基因组）等
                        # Accession 号
                        # 输出格式：fasta、gb（GenBank）、gff
                        cmd = f"efetch -db nuccore -id {accession_ID} -format fasta > {mitogenome_output_file}"
                        subprocess.run(cmd, check=True, text=True, shell=True)
                        print(f'{accession_ID}: mitogenomic sequence download successfully!!!')
                    except Exception as e:
                        print(f'efetch {family_name}, {species_strain_integrate_name}, {accession_ID}: '
                              f'mitogenomic sequence download error'
                              f'detailed error：{str(e)}')

                    annotation_genbank_output = species_strain_integrate_name + '.gb'
                    # 下载线粒体基因组genbank注释信息。
                    try:
                        cmd = f"efetch -db nuccore -id {accession_ID} -format gb > {annotation_genbank_output}"
                        subprocess.run(cmd, check=True, text=True, shell=True)
                        print(f'{accession_ID}: mitogenomic gb file download successfully!!!')
                    except Exception as e:
                        print(f'efetch {family_name}, {species_strain_integrate_name}, {accession_ID}: '
                              f'mitogenomic genbank annotation download error'
                              f'detailed error：{str(e)}')

                    fasta_cds_na = species_strain_integrate_name + '_cds.fasta'
                    # 下载线粒体基因组cds序列信息。
                    try:
                        cmd = f"efetch -db nuccore -id {accession_ID} -format fasta_cds_na > {fasta_cds_na}"
                        subprocess.run(cmd, check=True, text=True, shell=True)
                        print(f'{accession_ID}: mitogenomic cds sequence download successfully!!!')
                        
                    except Exception as e:
                        print(f'efetch {family_name}, {species_strain_integrate_name}, {accession_ID}: '
                              f'mitogenomic cds sequence download error'
                              f'detailed error：{str(e)}')

                    fasta_cds_aa = species_strain_integrate_name + '_pep.fasta'
                    # 下载线粒体基因组cds序列信息。
                    try:
                        cmd = f"efetch -db nuccore -id {accession_ID} -format fasta_cds_aa > {fasta_cds_aa}"
                        subprocess.run(cmd, check=True, text=True, shell=True)
                        print(f'{accession_ID}: mitogenomic pep sequence download successfully!!!')
                        
                    except Exception as e:
                        print(f'efetch {family_name}, {species_strain_integrate_name}, {accession_ID}: '
                              f'mitogenomic pep sequence download error'
                              f'detailed error：{str(e)}')
                    print('\n')
                    
                    os.chdir(mid_dir)
                    AA_line = AA.readline()
                os.chdir(Mt_data_dir)
        os.chdir(main_dir)

    except Exception as e:
        print(f"错误：处理 Excel 时失败 - {str(e)}")
        sys.exit(1)


# 主函数：运行脚本时指定 Excel 文件路径
if __name__ == "__main__":
    # 用法1：直接在脚本中指定 Excel 文件路径（适合新手）
    excel_file = "/home/bio02/一键建库/00.mitogenome_infor_NCBI.xlsx"  # 替换为你的 Excel 路径
    main_dir = os.path.abspath("HypoMtDB")  # 绝对路径，避免歧义
    # 先创建主目录（如果不存在）
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)

    # 直接用绝对路径创建文件，不切换工作目录
    index_file = os.path.join(main_dir, "index.html")
    readme_file = os.path.join(main_dir, "README.md")
    license_file = os.path.join(main_dir, "LICENSE")

    Index_creat(index_file)
    README_creat(readme_file)
    LICENSE_creat(license_file)
    excel_to_txt(excel_file, main_dir)

# 运行完之后别忘了检查一下是否都有数据下载了
# du -ah mitogenomes_data | awk '$1 == "0"'           查看mitogenomes_data文件下是否文件都不是空文件
