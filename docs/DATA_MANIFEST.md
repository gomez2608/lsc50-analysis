# Data manifest: PLOS One revision PONE-D-26-34021

Every data and result file used or produced during the revision: where it is, size, MD5 and modification time. Generated with `scripts/revision/manifest.py`; regenerate after new runs (see `REVISION_LOG.md` §8). Model weights, checkpoints and Arrow shards are summarized as groups (count, total size), not hashed. The volunteer photos (`WORK/volunteers/`), the landmark-overlay images (`WORK/overlay_check/`, identifiable volunteers, added 2026-10-23; the only Mac files newer than the 2026-10-20 table, checked 2026-10-28) and the local test folder (`WORK/vivit_smoke/`) are deliberately left out.

## 1. Raw data (public LSC50 release, figshare article 27383016)

| File | Where | MD5 | figshare computed MD5 | Match |
|------|-------|-----|-----------------------|-------|
| `IMU.zip` (1,608,738,643 B) | Mac `LSC50_DATA/` | `f94fc68d1ec5da41f9074e77d017a9c8` | `f94fc68d1ec5da41f9074e77d017a9c8` | yes |
| `LANDMARKS.zip` (2,770,068,538 B) | Mac `LSC50_DATA/` | `996d3e9ee1d3fb39866ce395efd23214` | `996d3e9ee1d3fb39866ce395efd23214` | yes |
| `VIDEOS.zip` (6,247,307,413 B) | server `~/lsc-revision/data/` | `26003107442257c7947352b18e3c2597` | `26003107442257c7947352b18e3c2597` | yes |

Only `VIDEOS/COLOR_BODY` (1,000 clips, 200 per subject) was extracted on the server; the IMU `INFO/` and `OUT_OPENSIM/` folders were copied from the Mac's extracted `IMU.zip` to `~/lsc-revision/data/IMU/` (2026-10-19) for the segmentation check. The original authors' workspace on the server (`~/LSC/`, 370 GB) was read but never modified; the files copied from it are under `WORK/original_server/` (§2).

## 2. Mac

### Mac working data: `/Users/sgomezahumada/Desktop/Work/Avances proyecto LSC AV/LSC50_DATA/WORK`

Generated 2026-10-20 08:35. 687 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `general_db.csv` | 56.5 MB | `f9ccff684361ae00e7de53e2c81a3366` | 2026-10-15 11:59 |
| `general_db_imu.csv` | 28.0 MB | `d0de2d81d5b82a2b3538303ea7e8bae3` | 2026-10-15 11:56 |
| `general_db_imu_chronos.csv` | 1.6 MB | `9508c23b05b1d2b440a9221a6d772903` | 2026-10-15 11:58 |
| `general_db_lm_chronos.csv` | 6.3 MB | `6ef547d6f002f8e2391ad782e67513eb` | 2026-10-15 12:00 |
| `temporal.csv` | 698.5 KB | `784c2a5a6f2a5bc1a5c174c1840fa649` | 2026-10-15 11:58 |
| `temporal_features.csv` | 25.7 MB | `7765f9c1ed4a3dddf733de2eafede293` | 2026-10-15 12:00 |
| `SIGNS/Abuelo/nw_Volunteer_1.csv` | 75.4 KB | `51bca77465b18ef5f4652d8cce0e8ba6` | 2026-10-15 11:56 |
| `SIGNS/Abuelo/nw_Volunteer_2.csv` | 92.2 KB | `7293a2b3d925eea597ffdd96ae0688c7` | 2026-10-15 11:56 |
| `SIGNS/Abuelo/nw_Volunteer_3.csv` | 91.3 KB | `0c5261dc1f8f4dec684fe44ee34e9d39` | 2026-10-15 11:56 |
| `SIGNS/Abuelo/nw_Volunteer_4.csv` | 104.8 KB | `40b80a490e550173f3b34bac1ee2a07f` | 2026-10-15 11:56 |
| `SIGNS/Abuelo/nw_Volunteer_5.csv` | 165.5 KB | `aa99bb37d44bed6fddd6756345e9a94f` | 2026-10-15 11:56 |
| `SIGNS/Aburrido/nw_Volunteer_1.csv` | 101.3 KB | `4f47a0e914afe39fcaf1d3fc1e840d6f` | 2026-10-15 11:56 |
| `SIGNS/Aburrido/nw_Volunteer_2.csv` | 113.8 KB | `03149dc95dc2ecf96fae2e7ec71e54db` | 2026-10-15 11:56 |
| `SIGNS/Aburrido/nw_Volunteer_3.csv` | 138.0 KB | `6ff3191cac66a2e844fd665c46dc7586` | 2026-10-15 11:56 |
| `SIGNS/Aburrido/nw_Volunteer_4.csv` | 113.4 KB | `44317060f3d9874a080501043aadd747` | 2026-10-15 11:56 |
| `SIGNS/Aburrido/nw_Volunteer_5.csv` | 185.8 KB | `c5cf5e2cfe729b9e74a50df6719db900` | 2026-10-15 11:56 |
| `SIGNS/Adios/nw_Volunteer_1.csv` | 70.2 KB | `bddabb456cef907a88e253bd24daffd6` | 2026-10-15 11:56 |
| `SIGNS/Adios/nw_Volunteer_2.csv` | 121.1 KB | `56cc41c90bfc860136baf6c2a49a5e7e` | 2026-10-15 11:56 |
| `SIGNS/Adios/nw_Volunteer_3.csv` | 113.2 KB | `bd1f09625508f2adce7348413a3f0c4a` | 2026-10-15 11:56 |
| `SIGNS/Adios/nw_Volunteer_4.csv` | 119.9 KB | `ec14e7143d579d335383bff352116757` | 2026-10-15 11:56 |
| `SIGNS/Adios/nw_Volunteer_5.csv` | 145.7 KB | `2bae776474728a0a8e59f09a9a28d1ca` | 2026-10-15 11:56 |
| `SIGNS/Bien/nw_Volunteer_1.csv` | 73.6 KB | `4ff06d39c79909ec41ef85443294ddd5` | 2026-10-15 11:56 |
| `SIGNS/Bien/nw_Volunteer_2.csv` | 93.1 KB | `32a7107db45cf4c3a4e0eaff4b9332a4` | 2026-10-15 11:56 |
| `SIGNS/Bien/nw_Volunteer_3.csv` | 82.7 KB | `5d56784f19fe9c50494b6241f533ca01` | 2026-10-15 11:56 |
| `SIGNS/Bien/nw_Volunteer_4.csv` | 109.3 KB | `ac2822b0a02de394324e19fc3517feaa` | 2026-10-15 11:56 |
| `SIGNS/Bien/nw_Volunteer_5.csv` | 144.6 KB | `4af57093f206f3d111c6b96439b8cf20` | 2026-10-15 11:56 |
| `SIGNS/Bienvenido/nw_Volunteer_1.csv` | 72.1 KB | `99629e8cedae4497a3c9d5885f2b9e47` | 2026-10-15 11:56 |
| `SIGNS/Bienvenido/nw_Volunteer_2.csv` | 124.5 KB | `cbd8200f6ec4c087b02ca3b4318fd861` | 2026-10-15 11:56 |
| `SIGNS/Bienvenido/nw_Volunteer_3.csv` | 145.9 KB | `c335b05bc594310dcea1a40f8b0c251d` | 2026-10-15 11:56 |
| `SIGNS/Bienvenido/nw_Volunteer_4.csv` | 112.8 KB | `ba5b7aa6dc8088412f0aec6b1404beb6` | 2026-10-15 11:56 |
| `SIGNS/Bienvenido/nw_Volunteer_5.csv` | 165.6 KB | `a0132e0e96afe48f604f2a41ba19381b` | 2026-10-15 11:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_1.csv` | 85.7 KB | `c95a335b3193de0ab0c4f56d69309b5f` | 2026-10-15 11:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_2.csv` | 127.9 KB | `d9376d4692d686e141fc9a6695d86d57` | 2026-10-15 11:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_3.csv` | 166.9 KB | `1b3cf16504532bc844a499caa2177878` | 2026-10-15 11:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_4.csv` | 119.0 KB | `da65f1455b0c6994c637c9619e74cab7` | 2026-10-15 11:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_5.csv` | 138.2 KB | `a84d09a14a757c5af8528beb8362a59b` | 2026-10-15 11:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_1.csv` | 89.0 KB | `393d9548a712d62fc3844baa089d6670` | 2026-10-15 11:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_2.csv` | 108.4 KB | `7c0c45db4085b9b14b2838e2f38b1624` | 2026-10-15 11:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_3.csv` | 111.0 KB | `4ce9760017fa9448454be3e97a015dd6` | 2026-10-15 11:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_4.csv` | 107.2 KB | `082102f3f92a2909bab87fcdbddec061` | 2026-10-15 11:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_5.csv` | 153.3 KB | `630555d368a82846516edc9f330c6416` | 2026-10-15 11:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_1.csv` | 85.2 KB | `4d2c0b0caa7668f98e81501ccb513106` | 2026-10-15 11:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_2.csv` | 104.4 KB | `54a11b95850c1b393fae2275fc508c31` | 2026-10-15 11:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_3.csv` | 129.1 KB | `fa0d8a6bd77d9239f2ec88b93ad37204` | 2026-10-15 11:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_4.csv` | 126.0 KB | `0b6b634dc8d137e9dff3cc49f543d874` | 2026-10-15 11:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_5.csv` | 176.0 KB | `d429d380aa20408067a9596c72bd184b` | 2026-10-15 11:56 |
| `SIGNS/Comer/nw_Volunteer_1.csv` | 85.5 KB | `81fd3bdcd9d679e6e06563b882ec2908` | 2026-10-15 11:56 |
| `SIGNS/Comer/nw_Volunteer_2.csv` | 103.6 KB | `7b4af9e09ce7f3077682c7a4ea992809` | 2026-10-15 11:56 |
| `SIGNS/Comer/nw_Volunteer_3.csv` | 120.1 KB | `2d7bf1b7e0e664b62f2b5f151c42997a` | 2026-10-15 11:56 |
| `SIGNS/Comer/nw_Volunteer_4.csv` | 102.5 KB | `8992a0b212b1f16325887e06ab404761` | 2026-10-15 11:56 |
| `SIGNS/Comer/nw_Volunteer_5.csv` | 142.7 KB | `446bde805528bc0d86e4de98c87e74ad` | 2026-10-15 11:56 |
| `SIGNS/Como estas_q/nw_Volunteer_1.csv` | 90.1 KB | `b99e10e72b2e2298e32e4ef150b8b8a2` | 2026-10-15 11:56 |
| `SIGNS/Como estas_q/nw_Volunteer_2.csv` | 117.1 KB | `09676c889355744f93670fd435e79260` | 2026-10-15 11:56 |
| `SIGNS/Como estas_q/nw_Volunteer_3.csv` | 135.4 KB | `864fa86355b01bc376951633e88fa150` | 2026-10-15 11:56 |
| `SIGNS/Como estas_q/nw_Volunteer_4.csv` | 111.9 KB | `b32bb145b4a14b73bc546cdf53ee263c` | 2026-10-15 11:56 |
| `SIGNS/Como estas_q/nw_Volunteer_5.csv` | 148.6 KB | `825bc0623c9751d8f4b398bbeb1eb422` | 2026-10-15 11:56 |
| `SIGNS/Como_q/nw_Volunteer_1.csv` | 88.5 KB | `60bb538953ab1b948b7d452d796e3456` | 2026-10-15 11:56 |
| `SIGNS/Como_q/nw_Volunteer_2.csv` | 82.0 KB | `d4ad0ccb6afdf89f7833cbf6fde91d51` | 2026-10-15 11:56 |
| `SIGNS/Como_q/nw_Volunteer_3.csv` | 108.0 KB | `acafaf5c9670d58a6330d90171487b6c` | 2026-10-15 11:56 |
| `SIGNS/Como_q/nw_Volunteer_4.csv` | 121.1 KB | `d4b1ec0b9695b4383b2b4976e0697dcb` | 2026-10-15 11:56 |
| `SIGNS/Como_q/nw_Volunteer_5.csv` | 175.1 KB | `e382466e19a51128f084e34cc408781d` | 2026-10-15 11:56 |
| `SIGNS/Con Gusto/nw_Volunteer_1.csv` | 61.3 KB | `4a5637206195feeb0879c4a6043cf0bb` | 2026-10-15 11:56 |
| `SIGNS/Con Gusto/nw_Volunteer_2.csv` | 144.9 KB | `f9aca2b673e3944f2a6b734cc8bb53ec` | 2026-10-15 11:56 |
| `SIGNS/Con Gusto/nw_Volunteer_3.csv` | 129.1 KB | `1f6793dfa21fef8c6b3c3887374e2077` | 2026-10-15 11:56 |
| `SIGNS/Con Gusto/nw_Volunteer_4.csv` | 156.9 KB | `6d9eb34c942fa1b4231b0c30a05d8e02` | 2026-10-15 11:56 |
| `SIGNS/Con Gusto/nw_Volunteer_5.csv` | 161.5 KB | `500862e96a691a9cdde6fa7e5f01a09f` | 2026-10-15 11:56 |
| `SIGNS/Contento/nw_Volunteer_1.csv` | 110.1 KB | `d29122309a740d22cddc11639f6688a9` | 2026-10-15 11:56 |
| `SIGNS/Contento/nw_Volunteer_2.csv` | 97.1 KB | `1e5c29bee56375a8e4689dff62a2f9e5` | 2026-10-15 11:56 |
| `SIGNS/Contento/nw_Volunteer_3.csv` | 78.0 KB | `bbf09c475f8d0e84e7ab19f84ca7835d` | 2026-10-15 11:56 |
| `SIGNS/Contento/nw_Volunteer_4.csv` | 127.8 KB | `6991224391cff7ceb4596ee68a5255a5` | 2026-10-15 11:56 |
| `SIGNS/Contento/nw_Volunteer_5.csv` | 157.5 KB | `1206ea315c1137e80e9edf1fa7d8840f` | 2026-10-15 11:56 |
| `SIGNS/Cuando_q/nw_Volunteer_1.csv` | 89.2 KB | `c968ed01bcc7ba1373e2c8db1564d708` | 2026-10-15 11:56 |
| `SIGNS/Cuando_q/nw_Volunteer_2.csv` | 121.2 KB | `0c6986af6767f5e8ab83ee6ca6f6ae96` | 2026-10-15 11:56 |
| `SIGNS/Cuando_q/nw_Volunteer_3.csv` | 123.4 KB | `4ab4c2036d3b1c746d205a43ccf6e9fa` | 2026-10-15 11:56 |
| `SIGNS/Cuando_q/nw_Volunteer_4.csv` | 125.7 KB | `ebe037ed6ef028b6c401b17d11c069d7` | 2026-10-15 11:56 |
| `SIGNS/Cuando_q/nw_Volunteer_5.csv` | 132.5 KB | `ed2bee15a23b6c0849500a0217b3fdc5` | 2026-10-15 11:56 |
| `SIGNS/Diferente/nw_Volunteer_1.csv` | 102.1 KB | `e5aff1dfccbe2dbd98bbf9aef65207c8` | 2026-10-15 11:56 |
| `SIGNS/Diferente/nw_Volunteer_2.csv` | 139.1 KB | `593092854ffbaf2b6c6ab2bd4b3de6c0` | 2026-10-15 11:56 |
| `SIGNS/Diferente/nw_Volunteer_3.csv` | 119.6 KB | `2b0201ddda4f5d312bdca0d3181d45a9` | 2026-10-15 11:56 |
| `SIGNS/Diferente/nw_Volunteer_4.csv` | 118.1 KB | `4b4199f42fdec14fcf1bfba164490bc7` | 2026-10-15 11:56 |
| `SIGNS/Diferente/nw_Volunteer_5.csv` | 133.6 KB | `a40b844f0d96e51a6521757307a374a0` | 2026-10-15 11:56 |
| `SIGNS/Donde_q/nw_Volunteer_1.csv` | 77.8 KB | `d3bcf166e9c0c7ec8f8fdbe7c580e7b4` | 2026-10-15 11:56 |
| `SIGNS/Donde_q/nw_Volunteer_2.csv` | 128.2 KB | `ad4863fbe21db8ad9e52d55f01e121c2` | 2026-10-15 11:56 |
| `SIGNS/Donde_q/nw_Volunteer_3.csv` | 85.5 KB | `a8a1f29a30f9d3be806fa6aa559115bf` | 2026-10-15 11:56 |
| `SIGNS/Donde_q/nw_Volunteer_4.csv` | 106.2 KB | `ff874ef8a90994b40488c32c76f0968a` | 2026-10-15 11:56 |
| `SIGNS/Donde_q/nw_Volunteer_5.csv` | 131.7 KB | `94b62da9e2ffa9c626e4d6564c84c5c8` | 2026-10-15 11:56 |
| `SIGNS/Familia/nw_Volunteer_1.csv` | 84.5 KB | `3732faa1ad55bc2c0c13612f7addca58` | 2026-10-15 11:56 |
| `SIGNS/Familia/nw_Volunteer_2.csv` | 93.2 KB | `03badd74e4f007999d0069bfc6ceab66` | 2026-10-15 11:56 |
| `SIGNS/Familia/nw_Volunteer_3.csv` | 108.8 KB | `0bba71ea843b991247370d8e331be35c` | 2026-10-15 11:56 |
| `SIGNS/Familia/nw_Volunteer_4.csv` | 143.1 KB | `00e252735ee368153687cbc972212c6b` | 2026-10-15 11:56 |
| `SIGNS/Familia/nw_Volunteer_5.csv` | 139.0 KB | `5ca9ff4b48dda95fbe9892ce19ae3701` | 2026-10-15 11:56 |
| `SIGNS/Feliz/nw_Volunteer_1.csv` | 93.8 KB | `eccfb8d70d623b3bf97f8803f7f1b506` | 2026-10-15 11:56 |
| `SIGNS/Feliz/nw_Volunteer_2.csv` | 92.3 KB | `423f8830432d9bea5fe3482fa02e67c4` | 2026-10-15 11:56 |
| `SIGNS/Feliz/nw_Volunteer_3.csv` | 108.4 KB | `6b7f075e2f7427a68b63506630c20295` | 2026-10-15 11:56 |
| `SIGNS/Feliz/nw_Volunteer_4.csv` | 125.3 KB | `2565601c627397ccefed4865b8e9735b` | 2026-10-15 11:56 |
| `SIGNS/Feliz/nw_Volunteer_5.csv` | 218.6 KB | `2fea14b21b1850b4eb040f3a723e8d42` | 2026-10-15 11:56 |
| `SIGNS/Gracias/nw_Volunteer_1.csv` | 56.9 KB | `d56c2e03b42eb7f5f7efe386ec6e712f` | 2026-10-15 11:56 |
| `SIGNS/Gracias/nw_Volunteer_2.csv` | 91.2 KB | `b231de8b418cae2a0bc55c02e99cad18` | 2026-10-15 11:56 |
| `SIGNS/Gracias/nw_Volunteer_3.csv` | 119.2 KB | `e9966a21220179c7e3013036dc0a1aa8` | 2026-10-15 11:56 |
| `SIGNS/Gracias/nw_Volunteer_4.csv` | 104.0 KB | `a399c802137d81f664cbde083d093d12` | 2026-10-15 11:56 |
| `SIGNS/Gracias/nw_Volunteer_5.csv` | 107.5 KB | `3272796ce2bb0b0582325b707d9e97fe` | 2026-10-15 11:56 |
| `SIGNS/Hambre/nw_Volunteer_1.csv` | 100.3 KB | `b325d632782ff79b11a4eb7e180ee225` | 2026-10-15 11:56 |
| `SIGNS/Hambre/nw_Volunteer_2.csv` | 115.1 KB | `a90b5ffc78a5816f425299af0129cd9e` | 2026-10-15 11:56 |
| `SIGNS/Hambre/nw_Volunteer_3.csv` | 159.2 KB | `0866e0d0b4753f5c6ca153a365018228` | 2026-10-15 11:56 |
| `SIGNS/Hambre/nw_Volunteer_4.csv` | 152.4 KB | `737e8f36f1e13e254e582b709ea80944` | 2026-10-15 11:56 |
| `SIGNS/Hambre/nw_Volunteer_5.csv` | 125.4 KB | `e5797a98e0c0e2c97771f60226046f7a` | 2026-10-15 11:56 |
| `SIGNS/Hermano/nw_Volunteer_1.csv` | 94.3 KB | `76e98fd26e9892debaf1c6c6d0ee68f4` | 2026-10-15 11:56 |
| `SIGNS/Hermano/nw_Volunteer_2.csv` | 105.8 KB | `e44a73a5214d42650b20ec039ba29727` | 2026-10-15 11:56 |
| `SIGNS/Hermano/nw_Volunteer_3.csv` | 120.2 KB | `8d44f49cffb7cce467835a2cce94b997` | 2026-10-15 11:56 |
| `SIGNS/Hermano/nw_Volunteer_4.csv` | 119.7 KB | `ad57c242d29e8354720eea60cbd0f3d1` | 2026-10-15 11:56 |
| `SIGNS/Hermano/nw_Volunteer_5.csv` | 138.8 KB | `e9fdfec7a43e6e18c86f4f5bc149b814` | 2026-10-15 11:56 |
| `SIGNS/Hola/nw_Volunteer_1.csv` | 83.2 KB | `c545a3e000c08950fda93685255f460e` | 2026-10-15 11:56 |
| `SIGNS/Hola/nw_Volunteer_2.csv` | 141.4 KB | `a5e0d74fc53159eccfdb50cfe1017ed3` | 2026-10-15 11:56 |
| `SIGNS/Hola/nw_Volunteer_3.csv` | 132.6 KB | `abc034b6bcd82d7ecb1d2b0af1dc08b3` | 2026-10-15 11:56 |
| `SIGNS/Hola/nw_Volunteer_4.csv` | 102.6 KB | `3c5033ea7ac78b7d294e1e6d1b690992` | 2026-10-15 11:56 |
| `SIGNS/Hola/nw_Volunteer_5.csv` | 207.4 KB | `dac4d34b5003e660023771364aaaedf5` | 2026-10-15 11:56 |
| `SIGNS/Hombre/nw_Volunteer_1.csv` | 62.1 KB | `b7da587e495238b01e3b7fe9282189ca` | 2026-10-15 11:56 |
| `SIGNS/Hombre/nw_Volunteer_2.csv` | 92.4 KB | `f395ab728ab20d1a6ead9acc1ad9bfee` | 2026-10-15 11:56 |
| `SIGNS/Hombre/nw_Volunteer_3.csv` | 132.9 KB | `8e50fbae0ff07c39bd62ea33e3f24e8e` | 2026-10-15 11:56 |
| `SIGNS/Hombre/nw_Volunteer_4.csv` | 147.1 KB | `4b02c0165c14e9a42151dce30bc09b4b` | 2026-10-15 11:56 |
| `SIGNS/Hombre/nw_Volunteer_5.csv` | 176.6 KB | `05b1aa36c51831d80d2bb05856709bad` | 2026-10-15 11:56 |
| `SIGNS/Jucioso/nw_Volunteer_1.csv` | 94.2 KB | `ba622cee8013304616b64df5341a9919` | 2026-10-15 11:56 |
| `SIGNS/Jucioso/nw_Volunteer_2.csv` | 140.9 KB | `990442821d990da8110c551f271d07b8` | 2026-10-15 11:56 |
| `SIGNS/Jucioso/nw_Volunteer_3.csv` | 131.2 KB | `f2e230f45d24b22d8993c58a1db7ff3a` | 2026-10-15 11:56 |
| `SIGNS/Jucioso/nw_Volunteer_4.csv` | 116.8 KB | `baed389c7ae98e40e43d053805d6a88d` | 2026-10-15 11:56 |
| `SIGNS/Jucioso/nw_Volunteer_5.csv` | 162.2 KB | `8c3eb993dc673a83e32e90be1b354ed8` | 2026-10-15 11:56 |
| `SIGNS/Mal/nw_Volunteer_1.csv` | 86.6 KB | `da379adab4f499e6810bf4eec6615f3b` | 2026-10-15 11:56 |
| `SIGNS/Mal/nw_Volunteer_2.csv` | 145.8 KB | `b357206538ce08e50f8a813272085e24` | 2026-10-15 11:56 |
| `SIGNS/Mal/nw_Volunteer_3.csv` | 107.1 KB | `e3d306fb35eaef294cfa5886fcbbd259` | 2026-10-15 11:56 |
| `SIGNS/Mal/nw_Volunteer_4.csv` | 134.7 KB | `c51b906ea5d29a5f73ec57c4fa7ee698` | 2026-10-15 11:56 |
| `SIGNS/Mal/nw_Volunteer_5.csv` | 143.7 KB | `7a0a4ae706bb40c2a844fb78f3aac028` | 2026-10-15 11:56 |
| `SIGNS/Mas o menos/nw_Volunteer_1.csv` | 99.5 KB | `f0999183cb894bea1688319fe08078e3` | 2026-10-15 11:56 |
| `SIGNS/Mas o menos/nw_Volunteer_2.csv` | 125.1 KB | `61fecda54a19d54f7e3977ac4e2040d5` | 2026-10-15 11:56 |
| `SIGNS/Mas o menos/nw_Volunteer_3.csv` | 97.4 KB | `8c0d98bddf58d17923ef8bb621698a2c` | 2026-10-15 11:56 |
| `SIGNS/Mas o menos/nw_Volunteer_4.csv` | 132.8 KB | `0ddc100dfee538c94c7aafbf6294c1af` | 2026-10-15 11:56 |
| `SIGNS/Mas o menos/nw_Volunteer_5.csv` | 190.7 KB | `37b5ba3adef3507f940242953575be11` | 2026-10-15 11:56 |
| `SIGNS/Mucho/nw_Volunteer_1.csv` | 86.2 KB | `bdedb63e007acbfdd2e21f47c2dc4581` | 2026-10-15 11:56 |
| `SIGNS/Mucho/nw_Volunteer_2.csv` | 142.5 KB | `3bc6c157e046bc1aeb907e97912d7922` | 2026-10-15 11:56 |
| `SIGNS/Mucho/nw_Volunteer_3.csv` | 108.8 KB | `d905e4fe657925ccdadaed46447a39f9` | 2026-10-15 11:56 |
| `SIGNS/Mucho/nw_Volunteer_4.csv` | 143.3 KB | `040e2ceba9f726561b1632dfc43c89cd` | 2026-10-15 11:56 |
| `SIGNS/Mucho/nw_Volunteer_5.csv` | 164 B | `60daa8ae672e83d8a02b254f842aa7c2` | 2026-10-15 11:56 |
| `SIGNS/Mujer/nw_Volunteer_1.csv` | 66.7 KB | `ff919ee3132b406a1c4b9a30b926bc5f` | 2026-10-15 11:56 |
| `SIGNS/Mujer/nw_Volunteer_2.csv` | 87.7 KB | `431b80ef24f7b142ce7e7355b1b40d0f` | 2026-10-15 11:56 |
| `SIGNS/Mujer/nw_Volunteer_3.csv` | 121.5 KB | `3c397b7426f2e9d3abd629c4615d3151` | 2026-10-15 11:56 |
| `SIGNS/Mujer/nw_Volunteer_4.csv` | 117.5 KB | `e1423854946df711e36c2fbb0fc480d8` | 2026-10-15 11:56 |
| `SIGNS/Mujer/nw_Volunteer_5.csv` | 171.8 KB | `5fa7071555d45138617f9a297298c5c2` | 2026-10-15 11:56 |
| `SIGNS/Niña/nw_Volunteer_1.csv` | 63.8 KB | `3e447029e92815d4cf8f28826715fc97` | 2026-10-15 11:56 |
| `SIGNS/Niña/nw_Volunteer_2.csv` | 106.0 KB | `2dfaf76ab779d21ce43bff8ce31293de` | 2026-10-15 11:56 |
| `SIGNS/Niña/nw_Volunteer_3.csv` | 140.2 KB | `b63ae006c14db3766c07c6ade278f255` | 2026-10-15 11:56 |
| `SIGNS/Niña/nw_Volunteer_4.csv` | 145.6 KB | `7044a3ce328b73d5999b5f9eabe0a62d` | 2026-10-15 11:56 |
| `SIGNS/Niña/nw_Volunteer_5.csv` | 158.9 KB | `d0d08fb538ce68a3e505024ad906d453` | 2026-10-15 11:56 |
| `SIGNS/Niño/nw_Volunteer_1.csv` | 75.4 KB | `ab42bc4592633a9b8b77457c2a56e746` | 2026-10-15 11:56 |
| `SIGNS/Niño/nw_Volunteer_2.csv` | 99.4 KB | `922b551216cd4a6ba51cc8f4e37b5264` | 2026-10-15 11:56 |
| `SIGNS/Niño/nw_Volunteer_3.csv` | 147.2 KB | `085658399fc1be9c51fe4041acad4428` | 2026-10-15 11:56 |
| `SIGNS/Niño/nw_Volunteer_4.csv` | 135.1 KB | `1da44958f5cc211b6d3b17ff2c374626` | 2026-10-15 11:56 |
| `SIGNS/Niño/nw_Volunteer_5.csv` | 214.4 KB | `d051abdb5c5fb69e178cdf89a59c4332` | 2026-10-15 11:56 |
| `SIGNS/Nombre/nw_Volunteer_1.csv` | 83.8 KB | `95a16df4a279397eb981fcb03574b40d` | 2026-10-15 11:56 |
| `SIGNS/Nombre/nw_Volunteer_2.csv` | 103.9 KB | `72d686900115a2b2f21c8041019f58b4` | 2026-10-15 11:56 |
| `SIGNS/Nombre/nw_Volunteer_3.csv` | 160.1 KB | `8a509f0d317a05d75d92ec0589b828c2` | 2026-10-15 11:56 |
| `SIGNS/Nombre/nw_Volunteer_4.csv` | 113.0 KB | `61e61c180024b6e5c640939e8be1f8cc` | 2026-10-15 11:56 |
| `SIGNS/Nombre/nw_Volunteer_5.csv` | 133.6 KB | `29a9d81369fd4ca7f62685ba2700a3fe` | 2026-10-15 11:56 |
| `SIGNS/Nunca/nw_Volunteer_1.csv` | 91.6 KB | `e5bd0c3eecce30ef50e7f3ddec5e35f2` | 2026-10-15 11:56 |
| `SIGNS/Nunca/nw_Volunteer_2.csv` | 119.3 KB | `8337b0bab710b29d5e74769c40cb968e` | 2026-10-15 11:56 |
| `SIGNS/Nunca/nw_Volunteer_3.csv` | 111.5 KB | `6a987913d97164d6a09b131857cdc926` | 2026-10-15 11:56 |
| `SIGNS/Nunca/nw_Volunteer_4.csv` | 117.2 KB | `347c339b5b0f8dad8708f2e4123c3eae` | 2026-10-15 11:56 |
| `SIGNS/Nunca/nw_Volunteer_5.csv` | 178.0 KB | `f3a70765a5f1bbd65d7e03b8cf36207e` | 2026-10-15 11:56 |
| `SIGNS/Perdon/nw_Volunteer_1.csv` | 91.0 KB | `1eda76f0627895967db251e3b08ccc87` | 2026-10-15 11:56 |
| `SIGNS/Perdon/nw_Volunteer_2.csv` | 107.2 KB | `514c0ef4da1f410e30140b19fd3cde84` | 2026-10-15 11:56 |
| `SIGNS/Perdon/nw_Volunteer_3.csv` | 117.7 KB | `0dab99c0490790187c0821d929b4d2c3` | 2026-10-15 11:56 |
| `SIGNS/Perdon/nw_Volunteer_4.csv` | 129.6 KB | `94daf6dc7f22ed02f5c2ea7467d00b03` | 2026-10-15 11:56 |
| `SIGNS/Perdon/nw_Volunteer_5.csv` | 140.0 KB | `b9b92166088f3d687a9cada78f36fef2` | 2026-10-15 11:56 |
| `SIGNS/Permiso/nw_Volunteer_1.csv` | 75.1 KB | `88ce7e7b8b5091bcb99d9156feb5eb5d` | 2026-10-15 11:56 |
| `SIGNS/Permiso/nw_Volunteer_2.csv` | 105.7 KB | `6d20868e8587db60d528135ed7179c53` | 2026-10-15 11:56 |
| `SIGNS/Permiso/nw_Volunteer_3.csv` | 135.1 KB | `509881f3406c99ace7076fc3c710df4f` | 2026-10-15 11:56 |
| `SIGNS/Permiso/nw_Volunteer_4.csv` | 132.8 KB | `8be2d6eab99096e07d193700dbc3e2ba` | 2026-10-15 11:56 |
| `SIGNS/Permiso/nw_Volunteer_5.csv` | 185.4 KB | `af4afe09a966777e043e8656ca0baae8` | 2026-10-15 11:56 |
| `SIGNS/Personas/nw_Volunteer_1.csv` | 81.3 KB | `ff13449eee7d2ebb57d6666bcfdf1fc9` | 2026-10-15 11:56 |
| `SIGNS/Personas/nw_Volunteer_2.csv` | 104.0 KB | `f9717c559ecadd77cad2bd40acb76375` | 2026-10-15 11:56 |
| `SIGNS/Personas/nw_Volunteer_3.csv` | 144.2 KB | `b69ba0a0523d8dba73f1a4efbdc46d9d` | 2026-10-15 11:56 |
| `SIGNS/Personas/nw_Volunteer_4.csv` | 114.5 KB | `51665c19e20e578bc4a74bc1fa5bd1ab` | 2026-10-15 11:56 |
| `SIGNS/Personas/nw_Volunteer_5.csv` | 130.3 KB | `39dc8456b14c4fc2527b42da49c41760` | 2026-10-15 11:56 |
| `SIGNS/Poco/nw_Volunteer_1.csv` | 85.5 KB | `90b7e15b2dfd8cc75ffc34cdaa757c2c` | 2026-10-15 11:56 |
| `SIGNS/Poco/nw_Volunteer_2.csv` | 98.9 KB | `e75fb0d431936177831c608f8f83b304` | 2026-10-15 11:56 |
| `SIGNS/Poco/nw_Volunteer_3.csv` | 136.1 KB | `d1ebaa5066b35d4ae8966d3c3ffff995` | 2026-10-15 11:56 |
| `SIGNS/Poco/nw_Volunteer_4.csv` | 133.7 KB | `d5b8e323f11ffe30d91f8527e8d3bc18` | 2026-10-15 11:56 |
| `SIGNS/Poco/nw_Volunteer_5.csv` | 161.9 KB | `0f882d326edb471f298adcad3c08ccae` | 2026-10-15 11:56 |
| `SIGNS/Por favor/nw_Volunteer_1.csv` | 78.8 KB | `edef36df2afa71b6fc758ae4938ea4c1` | 2026-10-15 11:56 |
| `SIGNS/Por favor/nw_Volunteer_2.csv` | 141.4 KB | `6d45bf3497cfaaf50f926d08222e4629` | 2026-10-15 11:56 |
| `SIGNS/Por favor/nw_Volunteer_3.csv` | 105.1 KB | `f34381cdb357793d1f35d6ae61741cf9` | 2026-10-15 11:56 |
| `SIGNS/Por favor/nw_Volunteer_4.csv` | 135.4 KB | `420490ba6751e848d64d9ff78eb7aaff` | 2026-10-15 11:56 |
| `SIGNS/Por favor/nw_Volunteer_5.csv` | 131.2 KB | `39297b049a0824a59fa160ec16900e4d` | 2026-10-15 11:56 |
| `SIGNS/Por que_q/nw_Volunteer_1.csv` | 98.9 KB | `446eece351a0b620a4f8e9fb359462fc` | 2026-10-15 11:56 |
| `SIGNS/Por que_q/nw_Volunteer_2.csv` | 121.5 KB | `af5ea7b3f80754e7293eb274e7e89817` | 2026-10-15 11:56 |
| `SIGNS/Por que_q/nw_Volunteer_3.csv` | 134.6 KB | `7f0922ca9da9d163f4f599a229a24e2d` | 2026-10-15 11:56 |
| `SIGNS/Por que_q/nw_Volunteer_4.csv` | 128.6 KB | `5f61ca372368e9d492c2fb35e635c8d2` | 2026-10-15 11:56 |
| `SIGNS/Por que_q/nw_Volunteer_5.csv` | 134.9 KB | `a11249dd0bded54d1962141d9739869e` | 2026-10-15 11:56 |
| `SIGNS/Que_q/nw_Volunteer_1.csv` | 82.7 KB | `f2e02e8a01e82bb06ac89a96bf62e803` | 2026-10-15 11:56 |
| `SIGNS/Que_q/nw_Volunteer_2.csv` | 130.5 KB | `c0cef58376586693a1630db09ea19023` | 2026-10-15 11:56 |
| `SIGNS/Que_q/nw_Volunteer_3.csv` | 89.8 KB | `a6e49c5dce3f554dbd0f8e908829f121` | 2026-10-15 11:56 |
| `SIGNS/Que_q/nw_Volunteer_4.csv` | 122.4 KB | `64ffa6c848d9b5294d1bb340448ecb17` | 2026-10-15 11:56 |
| `SIGNS/Que_q/nw_Volunteer_5.csv` | 148.6 KB | `0993f59b63ced80014c337d03641c3e3` | 2026-10-15 11:56 |
| `SIGNS/Quien_q/nw_Volunteer_1.csv` | 97.2 KB | `e1ce7b90621fdec9e8d6d9cdfaaedef1` | 2026-10-15 11:56 |
| `SIGNS/Quien_q/nw_Volunteer_2.csv` | 162.4 KB | `aa29b6a48c72aee2cb9da68b6cd01fd3` | 2026-10-15 11:56 |
| `SIGNS/Quien_q/nw_Volunteer_3.csv` | 109.5 KB | `de94f5c43026d603d11d1ea4530592b0` | 2026-10-15 11:56 |
| `SIGNS/Quien_q/nw_Volunteer_4.csv` | 124.4 KB | `aa51299cdcc248d8e5ea9bb4b87d5b20` | 2026-10-15 11:56 |
| `SIGNS/Quien_q/nw_Volunteer_5.csv` | 155.3 KB | `c11c5ea2074cf5c3d4412c4f26590f13` | 2026-10-15 11:56 |
| `SIGNS/Sentir/nw_Volunteer_1.csv` | 69.3 KB | `27c114ef150163364fa3a14cc49d1422` | 2026-10-15 11:56 |
| `SIGNS/Sentir/nw_Volunteer_2.csv` | 148.8 KB | `b5bcd30a76a1f119c803a8bc796e0e6b` | 2026-10-15 11:56 |
| `SIGNS/Sentir/nw_Volunteer_3.csv` | 120.1 KB | `41344129b3d6ffe5249f4427b63a8e6c` | 2026-10-15 11:56 |
| `SIGNS/Sentir/nw_Volunteer_4.csv` | 136.8 KB | `2c1a55ad17542c6de458913d602fc219` | 2026-10-15 11:56 |
| `SIGNS/Sentir/nw_Volunteer_5.csv` | 140.0 KB | `b4f1d850cbc8a11b490326cc4c308098` | 2026-10-15 11:56 |
| `SIGNS/Seña/nw_Volunteer_1.csv` | 76.2 KB | `b8a7f5db5ff3ced8d80fbbf5f25b0459` | 2026-10-15 11:56 |
| `SIGNS/Seña/nw_Volunteer_2.csv` | 100.8 KB | `5eb778c02c24055fa5bc6aa819c9b226` | 2026-10-15 11:56 |
| `SIGNS/Seña/nw_Volunteer_3.csv` | 171.0 KB | `af31256a5459e94e7d62f9acd62eb95c` | 2026-10-15 11:56 |
| `SIGNS/Seña/nw_Volunteer_4.csv` | 135.2 KB | `86caa579710f1e1f7b9ca19d7ebf5de9` | 2026-10-15 11:56 |
| `SIGNS/Seña/nw_Volunteer_5.csv` | 175.0 KB | `a3b972ab3a2c4a91f11216309c36323d` | 2026-10-15 11:56 |
| `SIGNS/Tio /nw_Volunteer_1.csv` | 77.9 KB | `b2b5aea42c355ec16274060a9f081bcf` | 2026-10-15 11:56 |
| `SIGNS/Tio /nw_Volunteer_2.csv` | 110.7 KB | `52acb5e6da3fead4c0d3ce3c252f3fd9` | 2026-10-15 11:56 |
| `SIGNS/Tio /nw_Volunteer_3.csv` | 132.0 KB | `14c847096da596e6504126b242069532` | 2026-10-15 11:56 |
| `SIGNS/Tio /nw_Volunteer_4.csv` | 133.6 KB | `af6b9f628e32f2ac1ca3505f4f7bb398` | 2026-10-15 11:56 |
| `SIGNS/Tio /nw_Volunteer_5.csv` | 170.4 KB | `bd192701e6adc5136d9724541e0cb397` | 2026-10-15 11:56 |
| `SIGNS/Todos/nw_Volunteer_1.csv` | 97.3 KB | `f74110bc98ba35368180c7e832425e75` | 2026-10-15 11:56 |
| `SIGNS/Todos/nw_Volunteer_2.csv` | 148.0 KB | `07ad7d6c75c3b66898cf182df2ee137e` | 2026-10-15 11:56 |
| `SIGNS/Todos/nw_Volunteer_3.csv` | 122.7 KB | `9a551567180e7a655dc4c5f5374f5cc9` | 2026-10-15 11:56 |
| `SIGNS/Todos/nw_Volunteer_4.csv` | 125.7 KB | `659c36666230a3475013046641c55fce` | 2026-10-15 11:56 |
| `SIGNS/Todos/nw_Volunteer_5.csv` | 146.2 KB | `04e3e696430825b08a4cc97c2f46767a` | 2026-10-15 11:56 |
| `SIGNS/Trabajar/nw_Volunteer_1.csv` | 86.1 KB | `36e9769548d734fe4758e2222fd61124` | 2026-10-15 11:56 |
| `SIGNS/Trabajar/nw_Volunteer_2.csv` | 119.6 KB | `0556a3a7311185130dedf6c0e712b151` | 2026-10-15 11:56 |
| `SIGNS/Trabajar/nw_Volunteer_3.csv` | 144.5 KB | `6b106af098de26f4cb9507170a3d5ded` | 2026-10-15 11:56 |
| `SIGNS/Trabajar/nw_Volunteer_4.csv` | 125.2 KB | `a10150a76fa8828b15ebe7ecf7b0960d` | 2026-10-15 11:56 |
| `SIGNS/Trabajar/nw_Volunteer_5.csv` | 157.5 KB | `59fa77b84cb15e6db8ac396501bd9402` | 2026-10-15 11:56 |
| `SIGNS/Triste/nw_Volunteer_1.csv` | 99.7 KB | `a4a0d8aba02a4cdad44e16415beea001` | 2026-10-15 11:56 |
| `SIGNS/Triste/nw_Volunteer_2.csv` | 106.1 KB | `cfb601e30123b051c61845dd31442f97` | 2026-10-15 11:56 |
| `SIGNS/Triste/nw_Volunteer_3.csv` | 156.4 KB | `29a2e087a82a9cf62a003f5ac573d9e1` | 2026-10-15 11:56 |
| `SIGNS/Triste/nw_Volunteer_4.csv` | 139.8 KB | `df4d85bfdb92c84017f1e0cd39e6bd35` | 2026-10-15 11:56 |
| `SIGNS/Triste/nw_Volunteer_5.csv` | 141.0 KB | `7e55cb32e90510d486218a62ef3251cb` | 2026-10-15 11:56 |
| `SIGNS/Tu/nw_Volunteer_1.csv` | 68.5 KB | `20b22ecc1a7d543201e207944429f6b9` | 2026-10-15 11:56 |
| `SIGNS/Tu/nw_Volunteer_2.csv` | 128.2 KB | `4251d118ba2b68194e7e9897d8cb71f1` | 2026-10-15 11:56 |
| `SIGNS/Tu/nw_Volunteer_3.csv` | 111.0 KB | `7660b3d134d54e0acf47bc8a7b46606f` | 2026-10-15 11:56 |
| `SIGNS/Tu/nw_Volunteer_4.csv` | 127.0 KB | `04a527dcaf233ff8129c4ef2594b435c` | 2026-10-15 11:56 |
| `SIGNS/Tu/nw_Volunteer_5.csv` | 126.5 KB | `3348e75eb72d0e95a5d472de26a85a27` | 2026-10-15 11:56 |
| `SIGNS/Ustedes/nw_Volunteer_1.csv` | 71.2 KB | `e5378fb7a269edc16e0b54420e7a97f7` | 2026-10-15 11:56 |
| `SIGNS/Ustedes/nw_Volunteer_2.csv` | 118.9 KB | `29d9e1fc7fbd8c911754822598ee172e` | 2026-10-15 11:56 |
| `SIGNS/Ustedes/nw_Volunteer_3.csv` | 122.2 KB | `3d0086904f5bd3b05ce27e9ba091fb2f` | 2026-10-15 11:56 |
| `SIGNS/Ustedes/nw_Volunteer_4.csv` | 97.6 KB | `d0a559abe64a345b99d37ae484cf26f2` | 2026-10-15 11:56 |
| `SIGNS/Ustedes/nw_Volunteer_5.csv` | 141.8 KB | `458d4619ca55282006ca41ff6fff42c0` | 2026-10-15 11:56 |
| `SIGNS/Vivir/nw_Volunteer_1.csv` | 88.6 KB | `f6807ff9762ea7033d9cd6869e187586` | 2026-10-15 11:56 |
| `SIGNS/Vivir/nw_Volunteer_2.csv` | 105.7 KB | `b6b7e7cf82116a61d88a3056127fbfba` | 2026-10-15 11:56 |
| `SIGNS/Vivir/nw_Volunteer_3.csv` | 139.7 KB | `f8cb57515ca6666db9e37dbafc1a912a` | 2026-10-15 11:56 |
| `SIGNS/Vivir/nw_Volunteer_4.csv` | 127.6 KB | `116a88fd0572ae95d7642f27db589f40` | 2026-10-15 11:56 |
| `SIGNS/Vivir/nw_Volunteer_5.csv` | 156.0 KB | `10976c09a18a7fd39a890e66aada04fa` | 2026-10-15 11:56 |
| `SIGNS/Yo/nw_Volunteer_1.csv` | 82.9 KB | `a97c76e4a9a8de99287589eec45c05c7` | 2026-10-15 11:56 |
| `SIGNS/Yo/nw_Volunteer_2.csv` | 87.7 KB | `d9d0934c066b008cc7e2fa2db7348300` | 2026-10-15 11:56 |
| `SIGNS/Yo/nw_Volunteer_3.csv` | 96.5 KB | `17e888aac73a0622b38df8433cb0bece` | 2026-10-15 11:56 |
| `SIGNS/Yo/nw_Volunteer_4.csv` | 98.1 KB | `4a254a6135ab978dde0c3ef762b3743b` | 2026-10-15 11:56 |
| `SIGNS/Yo/nw_Volunteer_5.csv` | 131.7 KB | `7a63fb0b2fe49dd43d347ccd897a17e3` | 2026-10-15 11:56 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed0.pkl` | 19.7 KB | `eb56f0e4414a75f570f6c7e5e0a7ecd2` | 2026-10-17 11:52 |
| `bodynorm/general_db_bodynorm.csv` | 58.8 MB | `f794252fce6e8dc904144851a87da0e5` | 2026-10-17 11:47 |
| `bodynorm/grid.log` | 1.1 KB | `b29bee2383123b4027e853720ef5d15f` | 2026-10-17 11:52 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed0.pkl` | 592.4 KB | `c61afcb53f79abf57a7586f40789ec63` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed1.pkl` | 592.4 KB | `7d8b9067dfa0d0816e7528f45af2a4ba` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed2.pkl` | 592.4 KB | `40616943d9582b0dc575cdad9dcae43a` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed3.pkl` | 592.4 KB | `cc6758d1f2493fa4ee694ac7d5acfabb` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed4.pkl` | 592.4 KB | `9ff13f9ad4580134f8d05b0c8f5604e6` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed0.pkl` | 119.0 KB | `a50c4b96e455cbf13690c182cfbb1ca0` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed1.pkl` | 119.0 KB | `c767f7dfeab1965cc168de860fbf0270` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed2.pkl` | 119.0 KB | `49d297dda2d8db17e956ee59346f99f2` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed3.pkl` | 119.0 KB | `d0041638905c7e9fb6008bc12ac60d63` | 2026-10-18 11:23 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed4.pkl` | 119.0 KB | `5ea8fe5211148d547eefaa76b3bea8d0` | 2026-10-18 11:23 |
| `bodynorm/temporal_features_bodynorm.csv` | 25.2 MB | `e3239f2937d71b4fb0f140db7c903eaa` | 2026-10-17 11:48 |
| `bodynorm/tsfel.log` | 11.2 KB | `ff8d36b1bc78a0883f74f1e35c621781` | 2026-10-17 11:48 |
| `dup_test/temporal_dupv1.csv` | 802.7 KB | `7e8fba3c7495f164d35c3b97b9346afd` | 2026-10-15 14:55 |
| `frames/general_db_f0.csv` | 144.6 MB | `59257694ec71b8f5b874d03c1e15e212` | 2026-10-15 14:34 |
| `frames/general_db_f16.csv` | 37.6 MB | `e9cedfa5f9c64f792aa89ff1fd9d6fed` | 2026-10-15 14:25 |
| `frames/general_db_f32.csv` | 75.3 MB | `83249ad5bef6a9ea9b845662f46eb8b6` | 2026-10-15 14:27 |
| `frames/general_db_f48.csv` | 113.0 MB | `6fe20c23c3e04d6cbdbb9cd451dfb370` | 2026-10-15 14:30 |
| `frames/general_db_lm_chronos_f0.csv` | 6.3 MB | `6c73ac3983af15b393e4fa10eb660319` | 2026-10-15 14:39 |
| `frames/general_db_lm_chronos_f16.csv` | 6.3 MB | `b0b7353dc603e8fea792109d69f2bb9d` | 2026-10-15 14:27 |
| `frames/general_db_lm_chronos_f32.csv` | 6.3 MB | `cf66ee50031d8cbdfaba06b5496e0cc6` | 2026-10-15 14:30 |
| `frames/general_db_lm_chronos_f48.csv` | 6.3 MB | `967617effea7094f68ce8e8c4f7705ac` | 2026-10-15 14:34 |
| `frames/temporal_features_f0.csv` | 25.8 MB | `124e18ba77006ed20a177b110a7cc33e` | 2026-10-15 14:35 |
| `frames/temporal_features_f16.csv` | 25.7 MB | `8bbf1f3b6161494fcf12a7daddc3b6d3` | 2026-10-15 14:26 |
| `frames/temporal_features_f32.csv` | 25.8 MB | `760f313746efde09c2ee40f96d43adfd` | 2026-10-15 14:28 |
| `frames/temporal_features_f48.csv` | 25.8 MB | `e25ca58c66c2f4558ce19130404f1114` | 2026-10-15 14:31 |
| `original_server/IMU/grid_search.py` | 10.3 KB | `eb17c0d1d8de2584b7141a7c026cc907` | 2025-09-07 11:40 |
| `original_server/IMU/grid_search_notebook.ipynb` | 1.1 MB | `8f4a3bbd160f6a9f5bcc5b79f60276bd` | 2025-08-18 14:00 |
| `original_server/IMU/grid_search_results_temporal.pkl` | 699.3 KB | `bea77f16fafe20e7deac11e801366b93` | 2025-08-18 14:44 |
| `original_server/IMU/helper_functions.py` | 3.5 KB | `acd7b27dfc86a501d8a167940d94a82f` | 2024-11-04 20:32 |
| `original_server/IMU/temporal.csv` | 698.5 KB | `db9da5dcbc810d4c1aeb1f71feacf27a` | 2025-02-20 09:55 |
| `original_server/IMU/IMU_FEATURES_NEW_6subjects/temporal.csv` | 838.4 KB | `5b4d1095d3a779bb41e6f895eb3e8c28` | 2024-11-04 20:59 |
| `original_server/IMU/rerun/cm_rf_temporal_balanced_seed42.pkl` | 19.7 KB | `68d19dfe17a8eaf4f21de39ffa912b6b` | 2026-10-17 11:21 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_0_seed42.pkl` | 19.7 KB | `c97f06ec04b40e48e8207deb06c8ef0e` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_1_seed42.pkl` | 19.7 KB | `f7d17b57a0df4c290a006f5e8d00b860` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_2_seed42.pkl` | 19.7 KB | `70188096cd5d6d91778bc6a3bf094783` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_3_seed42.pkl` | 19.7 KB | `df3ae443d4d77575255be13a8bd3baaf` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_4_seed42.pkl` | 19.7 KB | `d7a6f914db26f1ca88384a07758af132` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/errors.log` | 4.0 KB | `efb731fa94b91e47e7e8ffe9048d5b8b` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/grid_search_results_temporal_seed42.pkl` | 576.1 KB | `049e910d1f312e035fa1b7c404b60e18` | 2026-10-17 11:22 |
| `original_server/IMU/rerun/names.txt` | 5.4 KB | `a43e645830e5dd0a79e82342734a3307` | 2026-10-17 11:21 |
| `results/errors.log` | 34.7 KB | `0aa1d79356566e52354d22a24e536bab` | 2026-10-15 16:02 |
| `results/errors_frames.log` | 388.2 KB | `6ff53dcfc2c7c7655bf81e6e71bb3698` | 2026-10-16 13:10 |
| `results/errors_groupcv.log` | 15.4 KB | `c3fbc1e4c1971b75a1418b9bd3697e00` | 2026-10-16 13:51 |
| `results/errors_groupcv_seeds.log` | 50.6 KB | `727f4febb3937aacbdb35943b6c9b1eb` | 2026-10-16 17:26 |
| `results/errors_signant.log` | 24.0 KB | `b79689c54056b19fd7aa5f4504c18027` | 2026-10-16 17:51 |
| `results/run_frames.sh` | 1.7 KB | `2a3d00a62f455ed384d49b6136b019d7` | 2026-10-15 14:25 |
| `results/run_groupcv.sh` | 850 B | `6c4fcdde066988ba0ed55f58e89cafd6` | 2026-10-15 15:24 |
| `results/run_groupcv_seeds.sh` | 727 B | `af151a152bb5e3afff796c53ba1be899` | 2026-10-16 14:29 |
| `results/run_signant.sh` | 1.0 KB | `700e37b818b3bdf66afee1c7cca7a3c9` | 2026-10-16 14:43 |
| `results/run_slr.sh` | 1.1 KB | `91eeefee22445e57a56b4250ec6555d4` | 2026-10-15 12:00 |
| `results/summary_stage1.csv` | 1.9 KB | `4935c703c5589092ecd21651d0632b3f` | 2026-10-15 14:08 |
| `results/dup_test/cm_rf_temporal_dupv1_balanced_seed0.pkl` | 19.7 KB | `ab35bcd026151dfea4d33a535d0c4f9c` | 2026-10-15 14:57 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_0_seed0.pkl` | 19.7 KB | `f9b5563e3934e94bcf724a4bf26a3805` | 2026-10-15 14:59 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_1_seed0.pkl` | 19.7 KB | `ca3ac1de85b9f53f111a290dca98bd79` | 2026-10-15 15:00 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_2_seed0.pkl` | 19.7 KB | `6bcf91865b9197419191bcac5f829eeb` | 2026-10-15 15:01 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_3_seed0.pkl` | 19.7 KB | `65f5ccd8e59116daf20b3db865a5d7fe` | 2026-10-15 15:02 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_4_seed0.pkl` | 19.7 KB | `d3a3cadc595d9414c530098c84cab388` | 2026-10-15 15:02 |
| `results/dup_test/err.log` | 3.7 KB | `5d34b2eea9b58a3253aeb76e7c966f70` | 2026-10-15 15:02 |
| `results/dup_test/grid_search_results_temporal_dupv1_seed0.pkl` | 576.4 KB | `9c986792591df11d5b1f39e5f0af33d3` | 2026-10-15 15:02 |
| `results/dup_test/names.txt` | 5.4 KB | `a43e645830e5dd0a79e82342734a3307` | 2026-10-15 14:56 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_balanced_seed0.pkl` | 19.7 KB | `dcfb4d2d08dd4754584e51588ef70867` | 2026-10-16 12:48 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_0_seed0.pkl` | 19.7 KB | `c915397bbbf3cbd995d48c74c1827c5d` | 2026-10-16 12:54 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_1_seed0.pkl` | 19.7 KB | `f53f3b6a8a11617b557e7372bebd4456` | 2026-10-16 13:01 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_2_seed0.pkl` | 19.7 KB | `15ae9f4d93035ff1e1700de3ba477347` | 2026-10-16 13:04 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_3_seed0.pkl` | 19.7 KB | `136a27b9acb89fa6d529520d07370089` | 2026-10-16 13:07 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_4_seed0.pkl` | 19.7 KB | `301459fc58270cd5e319d22ac97af266` | 2026-10-16 13:10 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_balanced_seed0.pkl` | 19.7 KB | `b799124d7c87e44895958c6a3694631f` | 2026-10-16 10:17 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_0_seed0.pkl` | 19.7 KB | `0abd840badb772c6cb9cb186b44092ec` | 2026-10-16 10:21 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_1_seed0.pkl` | 19.7 KB | `6c7d2365224e6a771acaf09790704b7c` | 2026-10-16 10:24 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_2_seed0.pkl` | 19.7 KB | `180836ef68cb17751fd6cb8e3067930b` | 2026-10-16 10:27 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_3_seed0.pkl` | 19.7 KB | `62a9a30b95f16da1b804abe1c50b691a` | 2026-10-16 10:31 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_4_seed0.pkl` | 19.7 KB | `0048e42f5c47f30fe41f3d7d30578bce` | 2026-10-16 10:34 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_balanced_seed0.pkl` | 19.7 KB | `57a1126e3f57ce2794071cd48001cbfc` | 2026-10-16 11:05 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_0_seed0.pkl` | 19.7 KB | `40931453ef78b6918db8b3c86c2ef048` | 2026-10-16 11:08 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_1_seed0.pkl` | 19.7 KB | `a129c4ee272951cdc4fcf2bfe2fdc1cc` | 2026-10-16 11:12 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_2_seed0.pkl` | 19.7 KB | `3366c0ab73118ebea6429a7bd299461f` | 2026-10-16 11:16 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_3_seed0.pkl` | 19.7 KB | `ae9a246dbab3f00903c878c7bd634567` | 2026-10-16 11:19 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_4_seed0.pkl` | 19.7 KB | `10057a59ec76c475b5974f3c9265fd81` | 2026-10-16 11:23 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_balanced_seed0.pkl` | 19.7 KB | `84fe1f1d38c9b73ec2d1b3360cab0b08` | 2026-10-16 11:55 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_0_seed0.pkl` | 19.7 KB | `5f2c0768a5724065348d22e32e8960ed` | 2026-10-16 11:59 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_1_seed0.pkl` | 19.7 KB | `c9756d0aca0613c18ded72078eb3d6f1` | 2026-10-16 12:02 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_2_seed0.pkl` | 19.7 KB | `8a4048f1ce3306ffca77f7e655cf037c` | 2026-10-16 12:06 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_3_seed0.pkl` | 19.7 KB | `3ca5d17cb9746c2afb5b69a47436e092` | 2026-10-16 12:10 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_4_seed0.pkl` | 19.7 KB | `4b5d121682912dcf4189416524093615` | 2026-10-16 12:13 |
| `results/frames/cm_rf_temporal_features_f0_balanced_seed0.pkl` | 19.7 KB | `96df6d305c4fdbd6f9bc1bfc9b85ea3d` | 2026-10-16 12:19 |
| `results/frames/cm_rf_temporal_features_f0_loso_0_seed0.pkl` | 19.7 KB | `19539eadec5e2220ff53632a521d5269` | 2026-10-16 12:24 |
| `results/frames/cm_rf_temporal_features_f0_loso_1_seed0.pkl` | 19.7 KB | `8c038694a5ee54e875cc52496790b3f8` | 2026-10-16 12:29 |
| `results/frames/cm_rf_temporal_features_f0_loso_2_seed0.pkl` | 19.7 KB | `de17c55280d92599f3918a83afe92c33` | 2026-10-16 12:35 |
| `results/frames/cm_rf_temporal_features_f0_loso_3_seed0.pkl` | 19.7 KB | `49dca09be587b58137ee9b6a190f8dde` | 2026-10-16 12:40 |
| `results/frames/cm_rf_temporal_features_f0_loso_4_seed0.pkl` | 19.7 KB | `28256b947f2c6ca579e8fed2d08f59a5` | 2026-10-16 12:45 |
| `results/frames/cm_rf_temporal_features_f16_balanced_seed0.pkl` | 19.7 KB | `c5dee017bf4d9bdd0ba5b0797816e8ba` | 2026-10-16 03:40 |
| `results/frames/cm_rf_temporal_features_f16_loso_0_seed0.pkl` | 19.7 KB | `aaf39157c6c72a653c897c4e755cb04e` | 2026-10-16 09:57 |
| `results/frames/cm_rf_temporal_features_f16_loso_1_seed0.pkl` | 19.7 KB | `6febd188e37a6a2c4b63e2f6821013ef` | 2026-10-16 10:01 |
| `results/frames/cm_rf_temporal_features_f16_loso_2_seed0.pkl` | 19.7 KB | `bd1414596275bbb69c82b8b485a76f53` | 2026-10-16 10:05 |
| `results/frames/cm_rf_temporal_features_f16_loso_3_seed0.pkl` | 19.7 KB | `f46713fb488fa4eff0942fc5ae60c63e` | 2026-10-16 10:09 |
| `results/frames/cm_rf_temporal_features_f16_loso_4_seed0.pkl` | 19.7 KB | `6d5342c019ee38ed3e935f6796ae7108` | 2026-10-16 10:14 |
| `results/frames/cm_rf_temporal_features_f32_balanced_seed0.pkl` | 19.7 KB | `2d8b9fad8ae4bf9a8fe6c63d85ec71d3` | 2026-10-16 10:39 |
| `results/frames/cm_rf_temporal_features_f32_loso_0_seed0.pkl` | 19.7 KB | `41a4cb0cff40e607abb8fd8ec58fcf25` | 2026-10-16 10:43 |
| `results/frames/cm_rf_temporal_features_f32_loso_1_seed0.pkl` | 19.7 KB | `91023999bc89e44a3377316fd035aaf3` | 2026-10-16 10:47 |
| `results/frames/cm_rf_temporal_features_f32_loso_2_seed0.pkl` | 19.7 KB | `a408e34087a6a7f61691aa32ca36fc3a` | 2026-10-16 10:52 |
| `results/frames/cm_rf_temporal_features_f32_loso_3_seed0.pkl` | 19.7 KB | `e511f0a60ec75f78ba13cec2fdfc6320` | 2026-10-16 10:56 |
| `results/frames/cm_rf_temporal_features_f32_loso_4_seed0.pkl` | 19.7 KB | `9c7531e7ae51b1110b53417c23655c10` | 2026-10-16 11:01 |
| `results/frames/cm_rf_temporal_features_f48_balanced_seed0.pkl` | 19.7 KB | `f33915c5ee284228d53d3a689f799434` | 2026-10-16 11:28 |
| `results/frames/cm_rf_temporal_features_f48_loso_0_seed0.pkl` | 19.7 KB | `bacc3469de9964cc03b1b0ea61250e42` | 2026-10-16 11:32 |
| `results/frames/cm_rf_temporal_features_f48_loso_1_seed0.pkl` | 19.7 KB | `f358005cb69522916b5b8aa28ae545c6` | 2026-10-16 11:37 |
| `results/frames/cm_rf_temporal_features_f48_loso_2_seed0.pkl` | 19.7 KB | `7ff2a809d90c24d5b945df2826c9d77b` | 2026-10-16 11:41 |
| `results/frames/cm_rf_temporal_features_f48_loso_3_seed0.pkl` | 19.7 KB | `be4f6d1e0aa26884088813f5af47a714` | 2026-10-16 11:46 |
| `results/frames/cm_rf_temporal_features_f48_loso_4_seed0.pkl` | 19.7 KB | `f0ed4e005366d20510aae135621b8734` | 2026-10-16 11:51 |
| `results/frames/grid_search_results_general_db_lm_chronos_f0_chronos_seed0.pkl` | 649.6 KB | `1235f9e6889b521c9b4bf50a1833e82f` | 2026-10-16 13:10 |
| `results/frames/grid_search_results_general_db_lm_chronos_f16_chronos_seed0.pkl` | 649.6 KB | `374c91614b3f54a06f2b2ee3bd36851b` | 2026-10-16 10:34 |
| `results/frames/grid_search_results_general_db_lm_chronos_f32_chronos_seed0.pkl` | 649.6 KB | `4ee7ab79dd794d2232a4f41a19c46d1d` | 2026-10-16 11:23 |
| `results/frames/grid_search_results_general_db_lm_chronos_f48_chronos_seed0.pkl` | 649.6 KB | `459ad7ef3333192679123389e6d1600d` | 2026-10-16 12:13 |
| `results/frames/grid_search_results_temporal_features_f0_chronos_seed0.pkl` | 710.9 KB | `0e53ae4b6fa0dcd5b88277e9b59e7018` | 2026-10-16 12:45 |
| `results/frames/grid_search_results_temporal_features_f16_chronos_seed0.pkl` | 710.9 KB | `23bc878ee607ba64f172883d4bc2879e` | 2026-10-16 10:14 |
| `results/frames/grid_search_results_temporal_features_f32_chronos_seed0.pkl` | 710.9 KB | `bbfe782b2499af878557adabc9ff5709` | 2026-10-16 11:01 |
| `results/frames/grid_search_results_temporal_features_f48_chronos_seed0.pkl` | 710.9 KB | `05ba832978f84547917052a4c6c6925d` | 2026-10-16 11:51 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed0.pkl` | 19.7 KB | `eda66360710feee8a2f87e6c23e7eafc` | 2026-10-15 13:05 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed1.pkl` | 19.7 KB | `273cc2d2b2307bb810a5065b8f901112` | 2026-10-15 16:05 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed2.pkl` | 19.7 KB | `ee888b2a80f85d202e2cfb1269a8a9d0` | 2026-10-15 16:10 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed3.pkl` | 19.7 KB | `c5928370f85bfdf9303f063f1e4d03c9` | 2026-10-15 16:15 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed4.pkl` | 19.7 KB | `b0679787a3da4e40fdace33c01f43d6c` | 2026-10-15 16:35 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_shuffled_seed0.pkl` | 19.7 KB | `5d438d4bdd62b3c2961c85558cd5b534` | 2026-10-15 15:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed0.pkl` | 19.7 KB | `75a788923bf67f2451679ef8c149033a` | 2026-10-16 13:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed1.pkl` | 19.7 KB | `0612bdd7b2936f6987cdae4aff677ce4` | 2026-10-16 14:32 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed2.pkl` | 19.7 KB | `ecbe5f9a5193fb4cc95b8232d92e64dc` | 2026-10-16 14:37 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed3.pkl` | 19.7 KB | `3698633cffddcec06abbfc611721bacf` | 2026-10-16 14:43 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed4.pkl` | 19.7 KB | `e9f6db27e1a5d845128b7097835e71ce` | 2026-10-16 14:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed0.pkl` | 19.7 KB | `705d735d2180347ef73f35593914c5b1` | 2026-10-15 13:05 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed1.pkl` | 19.7 KB | `f3bf10e34407595b52b3272b99177afc` | 2026-10-15 16:05 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed2.pkl` | 19.7 KB | `a241225dfb26535262c51d3904069f14` | 2026-10-15 16:10 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed3.pkl` | 19.7 KB | `67113b3af56de49a9f7003a8cb120d9a` | 2026-10-15 16:15 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed4.pkl` | 19.7 KB | `a35f98df34aa5004a69d6d940d1cc23d` | 2026-10-15 16:35 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_shuffled_seed0.pkl` | 19.7 KB | `5402c748ad2d18211b179165efd0cd77` | 2026-10-15 15:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed0.pkl` | 19.7 KB | `ece8d31d6875af45082931854eb9cb33` | 2026-10-16 13:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed1.pkl` | 19.7 KB | `aa407c04e2fa8d1fe386deb7c298ab1f` | 2026-10-16 14:33 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed2.pkl` | 19.7 KB | `ba1786ccc009f9c36a973bab43d1ae87` | 2026-10-16 14:38 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed3.pkl` | 19.7 KB | `5aa3093770608a1e74a135863eefdbbd` | 2026-10-16 14:44 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed4.pkl` | 19.7 KB | `d274dcf73cc8f105c206aca9594b60a1` | 2026-10-16 14:50 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed0.pkl` | 19.7 KB | `49a9634dfcbab78d71a168005a5f1a8a` | 2026-10-15 13:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed1.pkl` | 19.7 KB | `6536d8397c09e00395070588f0f14872` | 2026-10-15 16:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed2.pkl` | 19.7 KB | `523e4fd755a46e297ed44e44dd78c3c7` | 2026-10-15 16:11 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed3.pkl` | 19.7 KB | `d8a690aa1fe132fd03a3e6916462de55` | 2026-10-15 16:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed4.pkl` | 19.7 KB | `38edd144374cda930a5dde411ee9facc` | 2026-10-15 16:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_shuffled_seed0.pkl` | 19.7 KB | `07d83fc5aea171675f251085e05064e6` | 2026-10-15 15:18 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed0.pkl` | 19.7 KB | `7a2dcce783ceba81aefef4b351d1f66b` | 2026-10-16 13:50 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed1.pkl` | 19.7 KB | `e114c446c06ff9d6102ea571445ae17d` | 2026-10-16 14:33 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed2.pkl` | 19.7 KB | `2fb07cf23056542b9033788d6704000d` | 2026-10-16 14:39 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed3.pkl` | 19.7 KB | `c64f1a0d47659eed11e153eec04e21fd` | 2026-10-16 14:45 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed4.pkl` | 19.7 KB | `932c9f272d944ad3e0de7ca47dfff1ad` | 2026-10-16 14:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed0.pkl` | 19.7 KB | `c10a032190e111d00ccd0e911f6d4ebd` | 2026-10-15 13:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed1.pkl` | 19.7 KB | `4dbb24736a85107496d044062915697f` | 2026-10-15 16:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed2.pkl` | 19.7 KB | `0925bf0d40b05fc4045ecf96b52b14bb` | 2026-10-15 16:11 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed3.pkl` | 19.7 KB | `3a6692439ec8186caaa521f3baebba12` | 2026-10-15 16:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed4.pkl` | 19.7 KB | `20bf2c780df57551787742e3cdaa10ec` | 2026-10-15 16:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_shuffled_seed0.pkl` | 19.7 KB | `9a66f41b368cf5df355da266052ce497` | 2026-10-15 15:19 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed0.pkl` | 19.7 KB | `319be95cf9076a10ae38c9fb3e388461` | 2026-10-16 13:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed1.pkl` | 19.7 KB | `752be20b2c6d3f50174cd970d376da73` | 2026-10-16 14:34 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed2.pkl` | 19.7 KB | `f7a1b1715faf2c5f3fe956214837acde` | 2026-10-16 14:39 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed3.pkl` | 19.7 KB | `2dcc7bcec2f52562972a78d2336b37ce` | 2026-10-16 14:45 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed4.pkl` | 19.7 KB | `d72dbb805ae9320e648836485fb77aad` | 2026-10-16 14:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed0.pkl` | 19.7 KB | `e034a799b56ade60c1b847e7098e9be1` | 2026-10-15 13:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed1.pkl` | 19.7 KB | `45f2154eee2cb01820a6ccc679dba74b` | 2026-10-15 16:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed2.pkl` | 19.7 KB | `d4327274bffc0ea7f2582dcc45b83cda` | 2026-10-15 16:12 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed3.pkl` | 19.7 KB | `17c44f31a3a6c268212e72d2f01ac087` | 2026-10-15 16:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed4.pkl` | 19.7 KB | `d602cdb54d060cde962535ded8fa95a3` | 2026-10-15 17:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_shuffled_seed0.pkl` | 19.7 KB | `6221eee535dbe42e496148cd854143c4` | 2026-10-15 15:20 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed0.pkl` | 18.9 KB | `fceec78dcdc406f6f3cf0c7aed57a5ae` | 2026-10-16 13:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed1.pkl` | 18.9 KB | `5f273e2534a7a60fcec03907eae01d56` | 2026-10-16 14:35 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed2.pkl` | 18.9 KB | `1ec890a72497d1b27d0ffc3166fa1c91` | 2026-10-16 14:40 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed3.pkl` | 18.9 KB | `bd15985069f04924f3703a2528f89b5f` | 2026-10-16 14:46 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed4.pkl` | 18.9 KB | `8604bdd319ed5d70d295c50da413cfcd` | 2026-10-16 14:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed0.pkl` | 18.9 KB | `b3356aeedff1a8f9ffffaa771f2967c5` | 2026-10-15 13:08 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed1.pkl` | 18.9 KB | `80be15af6056a745902d0de5f5673a03` | 2026-10-15 16:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed2.pkl` | 18.9 KB | `04e9633c72bf11c0bf07d1d832d47e67` | 2026-10-15 16:12 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed3.pkl` | 19.7 KB | `0f62d510f4be7da58dae23ad706855f2` | 2026-10-15 16:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed4.pkl` | 19.7 KB | `118cee778030f4e9e760cd73ec81c7f1` | 2026-10-15 18:56 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_shuffled_seed0.pkl` | 19.7 KB | `c63aa90076757f622a0f1b8edce1b93c` | 2026-10-15 15:22 |
| `results/imu/cm_rf_temporal_balanced_seed0.pkl` | 19.7 KB | `a3e15d0124fd342ea14ddf8556ccb8ee` | 2026-10-15 13:02 |
| `results/imu/cm_rf_temporal_balanced_seed1.pkl` | 19.7 KB | `a75c315680e7197ccf1057f4b781bf2a` | 2026-10-15 16:02 |
| `results/imu/cm_rf_temporal_balanced_seed2.pkl` | 19.7 KB | `5b7b8b39d4cc2e7997843455f5216a9e` | 2026-10-15 16:08 |
| `results/imu/cm_rf_temporal_balanced_seed3.pkl` | 19.7 KB | `22c76aa13d14372e685a6f80a3860d51` | 2026-10-15 16:13 |
| `results/imu/cm_rf_temporal_balanced_seed4.pkl` | 19.7 KB | `6ad7f32e5b8ec1ea2bbbd319bd26a62d` | 2026-10-15 16:17 |
| `results/imu/cm_rf_temporal_balanced_shuffled_seed0.pkl` | 19.7 KB | `75e330b6b618847cd9acc8ad4dd4bb28` | 2026-10-15 15:14 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed0.pkl` | 19.7 KB | `01f63586bc14ee749a7f1636cc9dccfb` | 2026-10-16 13:46 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed1.pkl` | 19.7 KB | `967f29b43a7bb86153b26a29ce8f783d` | 2026-10-16 14:30 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed2.pkl` | 19.7 KB | `fbeca6c1466ed62b70a5981845998c82` | 2026-10-16 14:35 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed3.pkl` | 19.7 KB | `126b47f83e35bd445ff9bb9792d939af` | 2026-10-16 14:41 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed4.pkl` | 19.7 KB | `2575b93ee55d8466f125477a3d83e43c` | 2026-10-16 14:47 |
| `results/imu/cm_rf_temporal_loso_0_seed0.pkl` | 19.7 KB | `6538c2671309f3e5440d96795658697d` | 2026-10-15 13:02 |
| `results/imu/cm_rf_temporal_loso_0_seed1.pkl` | 19.7 KB | `23b5dba511ff673af7e2c81168fe0c0a` | 2026-10-15 16:03 |
| `results/imu/cm_rf_temporal_loso_0_seed2.pkl` | 19.7 KB | `77882a90e959648cb29b1d8a2dc4425b` | 2026-10-15 16:08 |
| `results/imu/cm_rf_temporal_loso_0_seed3.pkl` | 19.7 KB | `55a1400d3c1af4ce195ace00ce9f6c04` | 2026-10-15 16:13 |
| `results/imu/cm_rf_temporal_loso_0_seed4.pkl` | 19.7 KB | `eb530387a305b6d3d044861446d129a4` | 2026-10-15 16:18 |
| `results/imu/cm_rf_temporal_loso_0_shuffled_seed0.pkl` | 19.7 KB | `21e58ed257083baff89210fbf9c72103` | 2026-10-15 15:15 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed0.pkl` | 19.7 KB | `fd67f2956cc3e2729e6aee3f499f461a` | 2026-10-16 13:47 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed1.pkl` | 19.7 KB | `3718fd83cd162b12feb14e3a9c037525` | 2026-10-16 14:30 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed2.pkl` | 19.7 KB | `f48185386a64b045f798bc8c3e8dff43` | 2026-10-16 14:35 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed3.pkl` | 19.7 KB | `fc6aee7fd172e7b24e48487ed63cf6d2` | 2026-10-16 14:41 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed4.pkl` | 19.7 KB | `5b7dc0a6d324649e2a7d453a88dc87b3` | 2026-10-16 14:47 |
| `results/imu/cm_rf_temporal_loso_1_seed0.pkl` | 19.7 KB | `6aea8e7e3cb492323b7e0aeae1c7e3db` | 2026-10-15 13:03 |
| `results/imu/cm_rf_temporal_loso_1_seed1.pkl` | 19.7 KB | `0d4b3628c9c2fcf78e27c58bdfe546ba` | 2026-10-15 16:03 |
| `results/imu/cm_rf_temporal_loso_1_seed2.pkl` | 19.7 KB | `bfd8135529231231abdd26eee266c27d` | 2026-10-15 16:08 |
| `results/imu/cm_rf_temporal_loso_1_seed3.pkl` | 19.7 KB | `daacccd946262fabdd28090415535204` | 2026-10-15 16:13 |
| `results/imu/cm_rf_temporal_loso_1_seed4.pkl` | 19.7 KB | `3ef9bf3d58174e61757d4faba032f79b` | 2026-10-15 16:18 |
| `results/imu/cm_rf_temporal_loso_1_shuffled_seed0.pkl` | 19.7 KB | `23dc25a6ca622171a252521408757440` | 2026-10-15 15:15 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed0.pkl` | 19.7 KB | `8f6b033acb0bca6e3322c3e8c14f41ca` | 2026-10-16 13:47 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed1.pkl` | 19.7 KB | `12fbf8687581fe1bafe7ffbb83b13bc6` | 2026-10-16 14:31 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed2.pkl` | 19.7 KB | `97133ea3c9bfbeaff1553eaae5efffbb` | 2026-10-16 14:36 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed3.pkl` | 19.7 KB | `26a50c8df4a1221b29985ff18b71c112` | 2026-10-16 14:42 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed4.pkl` | 19.7 KB | `6621003f29d8199b94e1871d3c975d2d` | 2026-10-16 14:48 |
| `results/imu/cm_rf_temporal_loso_2_seed0.pkl` | 19.7 KB | `2c2302e65148f611cbaf0bf84ded75fd` | 2026-10-15 13:03 |
| `results/imu/cm_rf_temporal_loso_2_seed1.pkl` | 19.7 KB | `12fbf8687581fe1bafe7ffbb83b13bc6` | 2026-10-15 16:03 |
| `results/imu/cm_rf_temporal_loso_2_seed2.pkl` | 19.7 KB | `0f8aad5c26a0a3d02b0766ad5c55c39b` | 2026-10-15 16:09 |
| `results/imu/cm_rf_temporal_loso_2_seed3.pkl` | 19.7 KB | `7509f9212b006c71d07d0be0ca1eadbf` | 2026-10-15 16:14 |
| `results/imu/cm_rf_temporal_loso_2_seed4.pkl` | 19.7 KB | `3903e8fc5d6367519a612f46a4807536` | 2026-10-15 16:18 |
| `results/imu/cm_rf_temporal_loso_2_shuffled_seed0.pkl` | 19.7 KB | `3792c8233384f46e62a3d566f19ef7f8` | 2026-10-15 15:15 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed0.pkl` | 19.7 KB | `738c367c82e53a83a12dc2ceb14dcc6a` | 2026-10-16 13:47 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed1.pkl` | 19.7 KB | `0be87c4601a7c9210d18682255c5a8c7` | 2026-10-16 14:31 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed2.pkl` | 19.7 KB | `159db6dbdcce4840e3fc161701a1c837` | 2026-10-16 14:36 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed3.pkl` | 19.7 KB | `d8e9698860105b1b4e696938b01cfe98` | 2026-10-16 14:42 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed4.pkl` | 19.7 KB | `b4460afb89548d60d55530b16fb79ace` | 2026-10-16 14:48 |
| `results/imu/cm_rf_temporal_loso_3_seed0.pkl` | 19.7 KB | `b58b2ac3732602ea161068295cdf549f` | 2026-10-15 13:04 |
| `results/imu/cm_rf_temporal_loso_3_seed1.pkl` | 19.7 KB | `76d93b2656d7cee5413744c322ec4dcc` | 2026-10-15 16:04 |
| `results/imu/cm_rf_temporal_loso_3_seed2.pkl` | 19.7 KB | `1f21637df598d2d4ea344e37eb4143ee` | 2026-10-15 16:09 |
| `results/imu/cm_rf_temporal_loso_3_seed3.pkl` | 19.7 KB | `86b2545b07a46cb51e557fcd022d5f1f` | 2026-10-15 16:14 |
| `results/imu/cm_rf_temporal_loso_3_seed4.pkl` | 19.7 KB | `775986a0f6b1467e85bcf2e47ab28dad` | 2026-10-15 16:19 |
| `results/imu/cm_rf_temporal_loso_3_shuffled_seed0.pkl` | 19.7 KB | `af5a1c94c30ed64d413cf09e306877e0` | 2026-10-15 15:16 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed0.pkl` | 19.7 KB | `287ab4543f103dbd25381b8ec1e17ca6` | 2026-10-16 13:48 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed1.pkl` | 18.9 KB | `5a6f9850cce4a23daf3615dc20e1a055` | 2026-10-16 14:31 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed2.pkl` | 18.9 KB | `3da3806d73aa84acbe8c00a3c9e2d542` | 2026-10-16 14:37 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed3.pkl` | 19.7 KB | `fe71ad0312adef6a88aa11cf988d47b4` | 2026-10-16 14:42 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed4.pkl` | 18.9 KB | `b6bf29c802436b2d8dcb7d20a7a0aa47` | 2026-10-16 14:48 |
| `results/imu/cm_rf_temporal_loso_4_seed0.pkl` | 19.7 KB | `638c4fd4e9d4e71ede5ce2c967c127ac` | 2026-10-15 13:04 |
| `results/imu/cm_rf_temporal_loso_4_seed1.pkl` | 18.9 KB | `f5776271172c991d1c10b11477c8e03c` | 2026-10-15 16:04 |
| `results/imu/cm_rf_temporal_loso_4_seed2.pkl` | 18.9 KB | `6dd162aa4890cf40e4ef8e16b6b95344` | 2026-10-15 16:09 |
| `results/imu/cm_rf_temporal_loso_4_seed3.pkl` | 18.9 KB | `4e2fb39038a1ecddfbba86695c5eaa18` | 2026-10-15 16:14 |
| `results/imu/cm_rf_temporal_loso_4_seed4.pkl` | 19.7 KB | `53d3774c8fa295add131647de5ff261e` | 2026-10-15 16:19 |
| `results/imu/cm_rf_temporal_loso_4_shuffled_seed0.pkl` | 18.9 KB | `776f211a9af37ec5ac3bc09bdffc885c` | 2026-10-15 15:16 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed0.pkl` | 517.9 KB | `3fde5b9a4824e04759f4bc29681228ec` | 2026-10-16 13:51 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed1.pkl` | 517.9 KB | `67e903515702d428ddff26b852cf4185` | 2026-10-16 14:35 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed2.pkl` | 517.9 KB | `e3de0f1db68dab7f4937d1a657f9b1c6` | 2026-10-16 14:40 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed3.pkl` | 517.9 KB | `3f11a2ae27dff06365e3696351e41584` | 2026-10-16 14:46 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed4.pkl` | 517.9 KB | `088d2f212bbe316c9f3e4e456c29a81e` | 2026-10-16 14:52 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed0.pkl` | 590.9 KB | `a3026e7bc60c3c3f2da60fb6040919bc` | 2026-10-15 13:08 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed1.pkl` | 590.9 KB | `b18434cff3f19f8a36c2c7e7553e5dc5` | 2026-10-15 16:07 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed2.pkl` | 590.9 KB | `e3a1342891b6a5ce5a68d07abb5c6fa3` | 2026-10-15 16:12 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed3.pkl` | 590.9 KB | `78aac20fb663bb57aa826361e52cedab` | 2026-10-15 16:17 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed4.pkl` | 590.9 KB | `bc056e386fc0d4ef31ddd626fab68286` | 2026-10-15 18:56 |
| `results/imu/grid_search_results_general_db_imu_chronos_shuffled_seed0.pkl` | 590.9 KB | `66dccb120d50d3397781fc928ef7471a` | 2026-10-15 15:22 |
| `results/imu/grid_search_results_temporal_groupcv_seed0.pkl` | 505.6 KB | `e7443aae932f18473aeec310b05678cc` | 2026-10-16 13:48 |
| `results/imu/grid_search_results_temporal_groupcv_seed1.pkl` | 505.6 KB | `db64b698d57559a4777befdb1c17a689` | 2026-10-16 14:31 |
| `results/imu/grid_search_results_temporal_groupcv_seed2.pkl` | 505.6 KB | `36c04d870e143ca9dcfbda8f291d0a90` | 2026-10-16 14:37 |
| `results/imu/grid_search_results_temporal_groupcv_seed3.pkl` | 505.6 KB | `a0a2307c1466c777d786fc052d689a6c` | 2026-10-16 14:42 |
| `results/imu/grid_search_results_temporal_groupcv_seed4.pkl` | 505.6 KB | `44b164d0d55211b46748573ea4181e62` | 2026-10-16 14:48 |
| `results/imu/grid_search_results_temporal_seed0.pkl` | 576.1 KB | `599bec5364bf88c8edc35dd42999bdc1` | 2026-10-15 13:04 |
| `results/imu/grid_search_results_temporal_seed1.pkl` | 576.1 KB | `a3d61ce0c99e612989faaa2e4bb292a4` | 2026-10-15 16:04 |
| `results/imu/grid_search_results_temporal_seed2.pkl` | 576.1 KB | `a16f8da27638d2aae9776b6c14b6ba57` | 2026-10-15 16:09 |
| `results/imu/grid_search_results_temporal_seed3.pkl` | 576.1 KB | `b6b0f0bc9baaa77f797eb8dcddca0c90` | 2026-10-15 16:14 |
| `results/imu/grid_search_results_temporal_seed4.pkl` | 576.1 KB | `d10a83b46c824964a84a589b14f2bdae` | 2026-10-15 16:19 |
| `results/imu/grid_search_results_temporal_shuffled_seed0.pkl` | 576.1 KB | `f6cf6e9eb646b52d202a9724977b9783` | 2026-10-15 15:16 |
| `results/imu/names.txt` | 6.4 KB | `32986c9e41e77beb22be4b089e243b00` | 2026-10-15 16:19 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed0.pkl` | 19.7 KB | `97aa078022fc612e96811841256b161f` | 2026-10-15 12:38 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed1.pkl` | 19.7 KB | `266252a8fcf816655653162469afb0a0` | 2026-10-15 15:33 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed2.pkl` | 19.7 KB | `3eb3191ba42d76687f0d1151a672a7e0` | 2026-10-15 15:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed3.pkl` | 19.7 KB | `3bf7f29b0d144cc607d6549e702a1737` | 2026-10-15 15:52 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed4.pkl` | 19.7 KB | `452a6d2b51687796159d95551baac961` | 2026-10-15 16:02 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_shuffled_seed0.pkl` | 19.7 KB | `f5642c91417a599f6295ab1fb040ddfa` | 2026-10-15 14:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed0.pkl` | 19.7 KB | `1f0835c2b5eb536b387ab2b78f4254ba` | 2026-10-16 13:33 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed1.pkl` | 19.7 KB | `8b210e89eb2be0972224ce5789dd2112` | 2026-10-16 15:18 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed2.pkl` | 19.7 KB | `78ab98bbdb8be785ebbf66594446726c` | 2026-10-16 15:58 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed3.pkl` | 19.7 KB | `33d0df6cc86f0f21b61f5fd62b4c21b0` | 2026-10-16 16:37 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed4.pkl` | 19.7 KB | `8574b83a9c23bd408c753276cb25d060` | 2026-10-16 17:14 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_seed0.pkl` | 19.7 KB | `92d57eedbc12dcc1546b014b66f6724b` | 2026-10-15 12:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_shuffled_seed0.pkl` | 19.7 KB | `e3c87cb92c54d286af3677320b9a8ef5` | 2026-10-15 14:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed0.pkl` | 19.7 KB | `9fd80a5c6559a8df41c3050eb7bad97d` | 2026-10-16 13:36 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed1.pkl` | 19.7 KB | `1401270ef141c21dc9e4a87a91db2adb` | 2026-10-16 15:21 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed2.pkl` | 19.7 KB | `565502c2b1df55e5deedc872038b39ee` | 2026-10-16 16:01 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed3.pkl` | 19.7 KB | `8d6d18f0c9298e7603d6fbf1f30ce059` | 2026-10-16 16:40 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed4.pkl` | 19.7 KB | `ea1b3ada68e29b06190f723bd42f2124` | 2026-10-16 17:17 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_seed0.pkl` | 19.7 KB | `828d74648d72496151b933ff10321c5d` | 2026-10-15 12:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_shuffled_seed0.pkl` | 19.7 KB | `0308445de78e229ff834653f2bf8a03f` | 2026-10-15 14:53 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed0.pkl` | 19.7 KB | `38345285798c1a25f3b597b0d9fd5e12` | 2026-10-16 13:40 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed1.pkl` | 19.7 KB | `daa959e38cb70aec6ee9dd3c3be5e776` | 2026-10-16 15:25 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed2.pkl` | 19.7 KB | `47e665af43c7b295fddaa11666bfcee3` | 2026-10-16 16:05 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed3.pkl` | 19.7 KB | `47e069b6b71b3101ccb26cf32d145ef7` | 2026-10-16 16:44 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed4.pkl` | 19.7 KB | `e7a6ebba2ac6410db8e85e79a21ec955` | 2026-10-16 17:20 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_seed0.pkl` | 19.7 KB | `3a956da9989f51ae68fe8d002a074834` | 2026-10-15 12:51 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_shuffled_seed0.pkl` | 19.7 KB | `878c75441cad02aff385048a6b0b99d7` | 2026-10-15 15:03 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed0.pkl` | 19.7 KB | `adc1e1b5271ab5121e83a795eca40f71` | 2026-10-16 13:43 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed1.pkl` | 19.7 KB | `eb316144042a2b5bfb560755c7635c4f` | 2026-10-16 15:28 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed2.pkl` | 19.7 KB | `85b2d32c4d21b1c39691614a435d9802` | 2026-10-16 16:08 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed3.pkl` | 19.7 KB | `d3f0a9a9598c79e73e499d93d2a9dfa1` | 2026-10-16 16:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed4.pkl` | 19.7 KB | `f44d7e571d0191b90316dc8bb3a16740` | 2026-10-16 17:23 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_seed0.pkl` | 19.7 KB | `f3961212c4eceb06e09d9b3565e57194` | 2026-10-15 12:56 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_shuffled_seed0.pkl` | 19.7 KB | `c7554c1f9cdcf2944c50354618d1628f` | 2026-10-15 15:08 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed0.pkl` | 19.7 KB | `f04d5bcd581df25b85d2ec46c210efb0` | 2026-10-16 13:46 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed1.pkl` | 19.7 KB | `dfc5083325f2d5dc3c3062008a2a3030` | 2026-10-16 15:32 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed2.pkl` | 19.7 KB | `a1ba34854b3abfe4face62f95ae5d2d5` | 2026-10-16 16:12 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed3.pkl` | 19.7 KB | `1fecc94b15847639ce5bdfb62ec8faab` | 2026-10-16 16:50 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed4.pkl` | 19.7 KB | `831f3fbe2e3406e5f06be1d177d5858e` | 2026-10-16 17:26 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_seed0.pkl` | 19.7 KB | `5f51b139f106360af0376763c6ee08f4` | 2026-10-15 13:01 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_shuffled_seed0.pkl` | 19.7 KB | `7543ce7a764d6a98d043f00e9420b5a8` | 2026-10-15 15:14 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed0.pkl` | 19.7 KB | `729a75bd541412b52acc00f87c45349b` | 2026-10-15 12:07 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed1.pkl` | 19.7 KB | `0c34d489c8bb3591ff1a4fd0c29d916d` | 2026-10-15 15:28 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed2.pkl` | 19.7 KB | `8a6c8aa44850db879d0f9e58bb5f81ef` | 2026-10-15 15:38 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed3.pkl` | 19.7 KB | `b992da4fb98ee98a3e281ab3dcf8f99f` | 2026-10-15 15:48 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed4.pkl` | 19.7 KB | `3bdb0d5881f71c0852812494f52f6dea` | 2026-10-15 15:58 |
| `results/landmarks/cm_rf_temporal_features_balanced_shuffled_seed0.pkl` | 19.7 KB | `66452328d9698d00c072f4928b2f50b1` | 2026-10-15 13:16 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed0.pkl` | 19.7 KB | `bf732032d9ecdaa8fd5dad416b4c344a` | 2026-10-16 13:14 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed1.pkl` | 19.7 KB | `e8d37b4787bf4f46fc3d5008b9a28347` | 2026-10-16 14:57 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed2.pkl` | 19.7 KB | `294761e5b393bea51f2bb89b4486f29f` | 2026-10-16 15:36 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed3.pkl` | 19.7 KB | `6a431bf6743756f92e4e3faf2f891625` | 2026-10-16 16:16 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed4.pkl` | 19.7 KB | `649f3874d6de0c127e48ec8a48153f80` | 2026-10-16 16:55 |
| `results/landmarks/cm_rf_temporal_features_loso_0_seed0.pkl` | 19.7 KB | `d2a88fa926072324a5034e0dff9c676f` | 2026-10-15 12:12 |
| `results/landmarks/cm_rf_temporal_features_loso_0_shuffled_seed0.pkl` | 19.7 KB | `392f36fa87178c4d27464bdaddeef4dd` | 2026-10-15 14:02 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed0.pkl` | 19.7 KB | `42644aebbe621c99d0aa7fc234d4bb9d` | 2026-10-16 13:18 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed1.pkl` | 19.7 KB | `132726b6958a907cff5ee69c46731ed2` | 2026-10-16 15:01 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed2.pkl` | 19.7 KB | `0b493f5df7fda4ec06c58cd7596bb687` | 2026-10-16 15:40 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed3.pkl` | 19.7 KB | `1878cd54e9727f5465e97e72fb47ffa4` | 2026-10-16 16:20 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed4.pkl` | 19.7 KB | `703e4dad4df5bb886e3bf8c879ebd753` | 2026-10-16 16:59 |
| `results/landmarks/cm_rf_temporal_features_loso_1_seed0.pkl` | 19.7 KB | `1b555f3035f65d4e7aef3dce5a6afd2c` | 2026-10-15 12:17 |
| `results/landmarks/cm_rf_temporal_features_loso_1_shuffled_seed0.pkl` | 19.7 KB | `af26a00687c4c632a37cdb36eab1271a` | 2026-10-15 14:08 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed0.pkl` | 19.7 KB | `c7f9b40af049f289c24565383d34ac87` | 2026-10-16 13:22 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed1.pkl` | 19.7 KB | `2655e27e5d03cd0d8d3f47056322ce44` | 2026-10-16 15:05 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed2.pkl` | 19.7 KB | `faa8ec7b5f354718660e7907444fd8e7` | 2026-10-16 15:45 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed3.pkl` | 19.7 KB | `46c81dd8a5472cd9379fef14e65126fb` | 2026-10-16 16:25 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed4.pkl` | 19.7 KB | `411f32e99d7a6c04ea9fff94811e08ac` | 2026-10-16 17:03 |
| `results/landmarks/cm_rf_temporal_features_loso_2_seed0.pkl` | 19.7 KB | `18a9e7d2367204110861cb6dcb3bb227` | 2026-10-15 12:23 |
| `results/landmarks/cm_rf_temporal_features_loso_2_shuffled_seed0.pkl` | 19.7 KB | `6d49befa917305431308c7865d48c74e` | 2026-10-15 14:15 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed0.pkl` | 19.7 KB | `99576579638013435ec7e245b5af737f` | 2026-10-16 13:26 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed1.pkl` | 19.7 KB | `1e634c4ef7b918cb25e8ec2f104c5f16` | 2026-10-16 15:10 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed2.pkl` | 19.7 KB | `92012a8fe5648001c470b3520b59747e` | 2026-10-16 15:50 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed3.pkl` | 19.7 KB | `68b959eb3ce351c6eb40ad53fc2bbda0` | 2026-10-16 16:29 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed4.pkl` | 19.7 KB | `616b1a5545d1beea7acc065213ca4831` | 2026-10-16 17:07 |
| `results/landmarks/cm_rf_temporal_features_loso_3_seed0.pkl` | 19.7 KB | `6fd62dfcd2b2d4021f38d82af30c0454` | 2026-10-15 12:28 |
| `results/landmarks/cm_rf_temporal_features_loso_3_shuffled_seed0.pkl` | 19.7 KB | `72d12253d926f62a675430355e71a72a` | 2026-10-15 14:22 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed0.pkl` | 19.7 KB | `f411e9cdd04f1182c4a1cc3955598f26` | 2026-10-16 13:30 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed1.pkl` | 19.7 KB | `48e2fff2c4501d10fd5ea4df22b2e901` | 2026-10-16 15:15 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed2.pkl` | 19.7 KB | `11b0645d47d5b242a2dc5be76d25605c` | 2026-10-16 15:55 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed3.pkl` | 19.7 KB | `dd364efd11a023e159899b489964a62b` | 2026-10-16 16:34 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed4.pkl` | 19.7 KB | `c861afa2b47765be9f54870c3504cc54` | 2026-10-16 17:11 |
| `results/landmarks/cm_rf_temporal_features_loso_4_seed0.pkl` | 19.7 KB | `5d55e763a7374d2f5b0bd78c7efbd011` | 2026-10-15 12:34 |
| `results/landmarks/cm_rf_temporal_features_loso_4_shuffled_seed0.pkl` | 19.7 KB | `5f3b82addf735f6098bef1505552ad8a` | 2026-10-15 14:32 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed0.pkl` | 541.3 KB | `51c297d71ace0caab1971815a4d93fe3` | 2026-10-16 13:46 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed1.pkl` | 541.3 KB | `cda69a0a6a11b282c0d71802e402da9e` | 2026-10-16 15:32 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed2.pkl` | 541.3 KB | `0468eb2195051b098dcad4a18819a575` | 2026-10-16 16:12 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed3.pkl` | 541.3 KB | `4e7402b20f72d915dc371d38aa74a47c` | 2026-10-16 16:50 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed4.pkl` | 541.3 KB | `404a0bda84d11c06fae4b62ef243d2f4` | 2026-10-16 17:26 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed0.pkl` | 649.6 KB | `a98bd7632d1f3439ccaad534648dca6a` | 2026-10-15 13:01 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed1.pkl` | 108.8 KB | `27c220c1523a2f75caab065c647d7821` | 2026-10-15 15:33 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed2.pkl` | 108.8 KB | `2939065cfda48692963cb3edaa4dc0bb` | 2026-10-15 15:42 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed3.pkl` | 108.8 KB | `7dead5a7e7d236a84f9f4e684ac67180` | 2026-10-15 15:52 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed4.pkl` | 108.8 KB | `e6a73490abc40746d39c65a250b72f8b` | 2026-10-15 16:02 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_shuffled_seed0.pkl` | 649.6 KB | `3247f938e049ec8ed45ae17846d41978` | 2026-10-15 15:14 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed0.pkl` | 592.4 KB | `814e2748e6c36250bc2f253382574748` | 2026-10-16 13:30 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed1.pkl` | 592.4 KB | `89f5d203e7442cc3bb982f25e5665919` | 2026-10-16 15:15 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed2.pkl` | 592.4 KB | `c507a6f58f2568a29141bc82bc2eb520` | 2026-10-16 15:55 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed3.pkl` | 592.4 KB | `378fcaeae27e166e0ac34583db9cd7c5` | 2026-10-16 16:34 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed4.pkl` | 592.4 KB | `d0ede19468e218bb048543925c66c2bb` | 2026-10-16 17:11 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed0.pkl` | 710.9 KB | `93993bb47b46b7c9a4be823bbcee9135` | 2026-10-15 12:34 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed1.pkl` | 119.0 KB | `0df827b22732912f3bf4140721b826a3` | 2026-10-15 15:28 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed2.pkl` | 119.0 KB | `d3b8d5ff36d96246d3649ed0c763654f` | 2026-10-15 15:38 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed3.pkl` | 119.0 KB | `7fc864df2af82d7206f571cd4818191c` | 2026-10-15 15:48 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed4.pkl` | 119.0 KB | `f8db3ace788690bce9b4cfc5b9c74325` | 2026-10-15 15:58 |
| `results/landmarks/grid_search_results_temporal_features_chronos_shuffled_seed0.pkl` | 710.9 KB | `c89924b40748f30e3fbc09a90b761452` | 2026-10-15 14:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed0.pkl` | 181 B | `533f6c91afef98724eed87404879fa18` | 2026-10-16 17:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 17:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed0.pkl` | 181 B | `9fd41059324d3455b2e4f96854f42d13` | 2026-10-16 17:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed0.pkl` | 181 B | `84aefbb7540243c594d022f96e97afba` | 2026-10-16 17:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed0.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-16 17:34 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed0.pkl` | 181 B | `216083e92903b0f87bfa3affc5a1e2fe` | 2026-10-16 17:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed0.pkl` | 19.7 KB | `705d735d2180347ef73f35593914c5b1` | 2026-10-16 17:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed0.pkl` | 19.7 KB | `49a9634dfcbab78d71a168005a5f1a8a` | 2026-10-16 17:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed0.pkl` | 19.7 KB | `c10a032190e111d00ccd0e911f6d4ebd` | 2026-10-16 17:31 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed0.pkl` | 19.7 KB | `e034a799b56ade60c1b847e7098e9be1` | 2026-10-16 17:31 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed0.pkl` | 18.9 KB | `b3356aeedff1a8f9ffffaa771f2967c5` | 2026-10-16 17:32 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 17:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 17:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed0.pkl` | 181 B | `1be56a5254bd6f759ec365f659caced0` | 2026-10-16 17:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed0.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-16 17:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed0.pkl` | 181 B | `ae9a4c2e68166bf8b19979616c24cf32` | 2026-10-16 17:29 |
| `results/signant_imu/cm_rf_temporal_deaf_seed0.pkl` | 181 B | `38f79d5ba058dd77837f39a28191069d` | 2026-10-16 17:28 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed0.pkl` | 19.7 KB | `6538c2671309f3e5440d96795658697d` | 2026-10-16 17:27 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed0.pkl` | 19.7 KB | `6aea8e7e3cb492323b7e0aeae1c7e3db` | 2026-10-16 17:27 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed0.pkl` | 19.7 KB | `2c2302e65148f611cbaf0bf84ded75fd` | 2026-10-16 17:28 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed0.pkl` | 19.7 KB | `b58b2ac3732602ea161068295cdf549f` | 2026-10-16 17:28 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed0.pkl` | 19.7 KB | `638c4fd4e9d4e71ede5ce2c967c127ac` | 2026-10-16 17:28 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed0.pkl` | 1.1 MB | `27f87e2a6f55ba094f84389ca531370a` | 2026-10-16 17:34 |
| `results/signant_imu/grid_search_results_temporal_seed0.pkl` | 1.1 MB | `6aa33e684d82e243449bec6ffe4746ae` | 2026-10-16 17:29 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed0.pkl` | 181 B | `6793b535246503f4d1d35c0348180183` | 2026-10-16 17:44 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed0.pkl` | 181 B | `22d34d30dd17424302a8a3d162e42427` | 2026-10-16 17:45 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed0.pkl` | 181 B | `6f5002acb17fe5ba6421fe8232c7cc00` | 2026-10-16 17:47 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed0.pkl` | 181 B | `b6f22e292ef66dae268ebbdab26991f6` | 2026-10-16 17:48 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed0.pkl` | 181 B | `2ee0dfce6957cbb7ff0dd9c973ac6053` | 2026-10-16 17:49 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed0.pkl` | 181 B | `7dbac3765dfe5dd9df61ef7d598f952a` | 2026-10-16 17:43 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed0.pkl` | 181 B | `146eaa99e871945ab17ce699db3942d3` | 2026-10-16 17:51 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed0.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-16 17:36 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed0.pkl` | 181 B | `12b59d2030363b89520a21ec67b0589c` | 2026-10-16 17:37 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed0.pkl` | 181 B | `d3d7eaa6625738b34b1a9173c7135bcc` | 2026-10-16 17:38 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed0.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-16 17:39 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed0.pkl` | 181 B | `3143dbffadd95421ff4cb9d5f98cb94d` | 2026-10-16 17:40 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed0.pkl` | 181 B | `9a033c73c921e4c3cc64a9b7e8535e84` | 2026-10-16 17:35 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed0.pkl` | 181 B | `d9bfe1b48f7662f4851d792b15a69e85` | 2026-10-16 17:41 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed0.pkl` | 113.8 KB | `367ecd4b4b4b76da9d87c64196dd7921` | 2026-10-16 17:51 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed0.pkl` | 680.1 KB | `61f04b2b95f8a783526f6b311c6af80b` | 2026-10-16 17:49 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed0.pkl` | 124.0 KB | `cfc9fe76fe85ef1dd087bfc9dd3f4cb1` | 2026-10-16 17:41 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed0.pkl` | 741.4 KB | `e125db6f577a47f5cfe94642dfe4f487` | 2026-10-16 17:40 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_groupcv_seed0.pkl` | 551.4 KB | `7145665cadd6521d465f9e0267ff4362` | 2026-10-18 11:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed0.pkl` | 110.8 KB | `bc226d3a17ddcd0fb6e61a7b5a4bbc59` | 2026-10-18 11:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed1.pkl` | 110.8 KB | `7bbfec38ad7931f0d8a96757226aeac2` | 2026-10-18 11:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed2.pkl` | 110.8 KB | `de1ddeee5a909e4460444cb47908c7aa` | 2026-10-18 11:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed3.pkl` | 110.8 KB | `f440a29ee0d943dc602ebffed61b1780` | 2026-10-18 11:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed4.pkl` | 110.8 KB | `f96fe7cb5bf1c055231666d81f4710f3` | 2026-10-18 11:23 |
| `vivit_results/run_vivit.log` | 1.1 KB | `b480487d220fc0e32df28a44f9c9a3f2` | 2026-10-18 11:08 |
| `vivit_results/vivit-8020-seed0/log_history.csv` | 2.5 KB | `58a57193da1d98d5350a4ec21a136a3b` | 2026-10-18 06:26 |
| `vivit_results/vivit-8020-seed0/results.json` | 2.7 KB | `97a6976490364c935138c3b565348c57` | 2026-10-18 06:27 |
| `vivit_results/vivit-s0-seed0/log_history.csv` | 5.4 KB | `78cd3c022a1665bdf151f4f29870c750` | 2026-10-18 01:36 |
| `vivit_results/vivit-s0-seed0/results.json` | 2.8 KB | `a0a48781e0a22a6df1e31d59d430c942` | 2026-10-18 01:37 |
| `vivit_results/vivit-s0-seed1/log_history.csv` | 5.5 KB | `b1e43b6230ca163d35bb41be63989604` | 2026-10-18 11:08 |
| `vivit_results/vivit-s0-seed1/results.json` | 2.8 KB | `7112e07bbf03665b427c9fbfeee7a832` | 2026-10-18 11:08 |
| `vivit_results/vivit-s1-seed0/log_history.csv` | 5.4 KB | `a2e5734ddd9e3b2b8fa03158e223da56` | 2026-10-18 02:01 |
| `vivit_results/vivit-s1-seed0/results.json` | 2.8 KB | `5e59b6cf85080123e4e4ab7ac1af9910` | 2026-10-18 02:02 |
| `vivit_results/vivit-s2-seed0/log_history.csv` | 5.4 KB | `c2f7a5c32a3bd514811fbf1691b2f458` | 2026-10-18 01:53 |
| `vivit_results/vivit-s2-seed0/results.json` | 2.8 KB | `b850f99899a725866c6d2c580bdb908b` | 2026-10-18 01:54 |
| `vivit_results/vivit-s3-seed0/log_history.csv` | 5.4 KB | `b4c7966a1362403f8aea42bfbdc3a1ee` | 2026-10-18 01:48 |
| `vivit_results/vivit-s3-seed0/results.json` | 2.8 KB | `695107916ca15ff8143de8f1ca7bff8f` | 2026-10-18 01:48 |
| `vivit_results/vivit-s4-seed0/log_history.csv` | 5.5 KB | `8749c84aff5c4b2f8f668077f17b8431` | 2026-10-18 10:36 |
| `vivit_results/vivit-s4-seed0/results.json` | 2.8 KB | `57ce9fd9aaf81eb23c12778267dba9aa` | 2026-10-18 10:37 |

## 3. Server (<gpu-server>, ~/lsc-revision)

### Server raw data (~/lsc-revision/data): `data`

Generated 2026-10-20 13:36. 16 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `VIDEOS.zip` | 5.8 GB | `26003107442257c7947352b18e3c2597` | 2024-10-31 17:49 |
| `VIDEOS.zip.md5` | 45 B | `002b6da88a45c61b8c56f5832df3f0eb` | 2026-10-17 16:41 |
| `download.done` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-17 16:42 |
| `n_clips.txt` | 5 B | `ad865d2f63b9feb2552c220385fbb7e3` | 2026-10-17 16:42 |
| `IMU/INFO/OpenSim_Model.osim` | 869.7 KB | `0bf2a1a001e0c409caa18e852daa2cbc` | 2024-10-31 21:49 |
| `IMU/INFO/Timestamps.xlsx` | 21.3 KB | `2585a8541e5d17e1bc39f3c1dc0a7724` | 2024-10-31 21:49 |
| `IMU/INFO/Volunteer_1.txt` | 122 B | `da3f7e52befcb5e487d31ca9ef70c384` | 2024-10-31 21:49 |
| `IMU/INFO/Volunteer_2.txt` | 122 B | `b3125a2d7199840419ff2f5d427aeab0` | 2024-10-31 21:49 |
| `IMU/INFO/Volunteer_3.txt` | 122 B | `64b45ba17c1464162a98e23d0af32ba0` | 2024-10-31 21:49 |
| `IMU/INFO/Volunteer_4.txt` | 122 B | `7c5ec77e68103f8446791399070d1284` | 2024-10-31 21:49 |
| `IMU/INFO/Volunteer_5.txt` | 122 B | `b7c8e76c7014f5446a5f4668aadbc572` | 2024-10-31 21:49 |
| `IMU/OUT_OPENSIM/Volunteer_1.mot` | 37.5 MB | `670d5e35f2c7ed887e56cc8a4d6b58aa` | 2024-10-31 21:49 |
| `IMU/OUT_OPENSIM/Volunteer_2.mot` | 89.9 MB | `5acdb20aec9ea1d82712871a182d5259` | 2024-10-31 21:49 |
| `IMU/OUT_OPENSIM/Volunteer_3.mot` | 89.1 MB | `a7e43f532fccd631ef461ae3e86c906b` | 2024-10-31 21:49 |
| `IMU/OUT_OPENSIM/Volunteer_4.mot` | 89.5 MB | `28cb2d3559dd62ba5fed9b7fded24800` | 2024-10-31 21:49 |
| `IMU/OUT_OPENSIM/Volunteer_5.mot` | 83.3 MB | `4359617e8d903b5b4090f5cbb4dd9955` | 2024-10-31 21:49 |

VIDEOS/COLOR_BODY: 1000 clips, 2.5G

Server tables regenerated 2026-10-28 (`WORK` again at 23:52 UTC, after the prediction-metrics and sign-name runs; times are server time, UTC; the Mac tables use Mac local time, UTC−5). `WORK` now includes the DTW normalization check (`WORK/dtw_pathnorm/`, listed separately until 2026-10-20), the fusion retraining (`WORK/fusion/`, weights summarized), SPOTER, ST-GCN v2, sequence importance, the final signer intervals and the final figures (`WORK/figures_final/`). `WORK/overlay_check/` on the server holds only the frame-count CSVs and the script; the overlay images are on the Mac only.

### Server working data (~/lsc-revision/WORK): `WORK`

Generated 2026-10-28 23:52. 2660 files listed; 2 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `controls.commit` | 109 B | `7c0c3c974949f1e1c3017b04403f48f1` | 2026-10-20 15:31 |
| `controls.log` | 10.0 KB | `6df9121cdadeb81cfd1b7d0ae8ede56f` | 2026-10-20 18:58 |
| `general_db.csv` | 56.5 MB | `f9ccff684361ae00e7de53e2c81a3366` | 2026-10-15 16:59 |
| `general_db_imu.csv` | 28.0 MB | `d0de2d81d5b82a2b3538303ea7e8bae3` | 2026-10-15 16:56 |
| `general_db_imu_chronos.csv` | 1.6 MB | `9508c23b05b1d2b440a9221a6d772903` | 2026-10-15 16:58 |
| `general_db_lm_chronos.csv` | 6.3 MB | `6ef547d6f002f8e2391ad782e67513eb` | 2026-10-15 17:00 |
| `importance_stability_imu.csv` | 380 B | `f50b260e8d0b3be6b8d67ba6776e1dcd` | 2026-10-20 16:16 |
| `importance_stability_landmarks_bodynorm.csv` | 482 B | `7f7d24e6e092cfc9a2e37a97db1a6ab4` | 2026-10-20 16:16 |
| `signer_ci_v2.out` | 6.0 KB | `258630af024221775652638f77cd6548` | 2026-10-21 15:37 |
| `signer_ci_v3.out` | 6.0 KB | `d5841d4aca54cbfd22d90fef45d3af2f` | 2026-10-22 02:31 |
| `temporal.csv` | 698.5 KB | `784c2a5a6f2a5bc1a5c174c1840fa649` | 2026-10-15 16:58 |
| `temporal_features.csv` | 25.7 MB | `7765f9c1ed4a3dddf733de2eafede293` | 2026-10-15 17:00 |
| `vivit_runs.csv` | 2.7 KB | `c29e8537ebb5a63de3049f693fe939f7` | 2026-10-22 02:02 |
| `SIGNS/Abuelo/nw_Volunteer_1.csv` | 75.4 KB | `51bca77465b18ef5f4652d8cce0e8ba6` | 2026-10-15 16:56 |
| `SIGNS/Abuelo/nw_Volunteer_2.csv` | 92.2 KB | `7293a2b3d925eea597ffdd96ae0688c7` | 2026-10-15 16:56 |
| `SIGNS/Abuelo/nw_Volunteer_3.csv` | 91.3 KB | `0c5261dc1f8f4dec684fe44ee34e9d39` | 2026-10-15 16:56 |
| `SIGNS/Abuelo/nw_Volunteer_4.csv` | 104.8 KB | `40b80a490e550173f3b34bac1ee2a07f` | 2026-10-15 16:56 |
| `SIGNS/Abuelo/nw_Volunteer_5.csv` | 165.5 KB | `aa99bb37d44bed6fddd6756345e9a94f` | 2026-10-15 16:56 |
| `SIGNS/Aburrido/nw_Volunteer_1.csv` | 101.3 KB | `4f47a0e914afe39fcaf1d3fc1e840d6f` | 2026-10-15 16:56 |
| `SIGNS/Aburrido/nw_Volunteer_2.csv` | 113.8 KB | `03149dc95dc2ecf96fae2e7ec71e54db` | 2026-10-15 16:56 |
| `SIGNS/Aburrido/nw_Volunteer_3.csv` | 138.0 KB | `6ff3191cac66a2e844fd665c46dc7586` | 2026-10-15 16:56 |
| `SIGNS/Aburrido/nw_Volunteer_4.csv` | 113.4 KB | `44317060f3d9874a080501043aadd747` | 2026-10-15 16:56 |
| `SIGNS/Aburrido/nw_Volunteer_5.csv` | 185.8 KB | `c5cf5e2cfe729b9e74a50df6719db900` | 2026-10-15 16:56 |
| `SIGNS/Adios/nw_Volunteer_1.csv` | 70.2 KB | `bddabb456cef907a88e253bd24daffd6` | 2026-10-15 16:56 |
| `SIGNS/Adios/nw_Volunteer_2.csv` | 121.1 KB | `56cc41c90bfc860136baf6c2a49a5e7e` | 2026-10-15 16:56 |
| `SIGNS/Adios/nw_Volunteer_3.csv` | 113.2 KB | `bd1f09625508f2adce7348413a3f0c4a` | 2026-10-15 16:56 |
| `SIGNS/Adios/nw_Volunteer_4.csv` | 119.9 KB | `ec14e7143d579d335383bff352116757` | 2026-10-15 16:56 |
| `SIGNS/Adios/nw_Volunteer_5.csv` | 145.7 KB | `2bae776474728a0a8e59f09a9a28d1ca` | 2026-10-15 16:56 |
| `SIGNS/Bien/nw_Volunteer_1.csv` | 73.6 KB | `4ff06d39c79909ec41ef85443294ddd5` | 2026-10-15 16:56 |
| `SIGNS/Bien/nw_Volunteer_2.csv` | 93.1 KB | `32a7107db45cf4c3a4e0eaff4b9332a4` | 2026-10-15 16:56 |
| `SIGNS/Bien/nw_Volunteer_3.csv` | 82.7 KB | `5d56784f19fe9c50494b6241f533ca01` | 2026-10-15 16:56 |
| `SIGNS/Bien/nw_Volunteer_4.csv` | 109.3 KB | `ac2822b0a02de394324e19fc3517feaa` | 2026-10-15 16:56 |
| `SIGNS/Bien/nw_Volunteer_5.csv` | 144.6 KB | `4af57093f206f3d111c6b96439b8cf20` | 2026-10-15 16:56 |
| `SIGNS/Bienvenido/nw_Volunteer_1.csv` | 72.1 KB | `99629e8cedae4497a3c9d5885f2b9e47` | 2026-10-15 16:56 |
| `SIGNS/Bienvenido/nw_Volunteer_2.csv` | 124.5 KB | `cbd8200f6ec4c087b02ca3b4318fd861` | 2026-10-15 16:56 |
| `SIGNS/Bienvenido/nw_Volunteer_3.csv` | 145.9 KB | `c335b05bc594310dcea1a40f8b0c251d` | 2026-10-15 16:56 |
| `SIGNS/Bienvenido/nw_Volunteer_4.csv` | 112.8 KB | `ba5b7aa6dc8088412f0aec6b1404beb6` | 2026-10-15 16:56 |
| `SIGNS/Bienvenido/nw_Volunteer_5.csv` | 165.6 KB | `a0132e0e96afe48f604f2a41ba19381b` | 2026-10-15 16:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_1.csv` | 85.7 KB | `c95a335b3193de0ab0c4f56d69309b5f` | 2026-10-15 16:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_2.csv` | 127.9 KB | `d9376d4692d686e141fc9a6695d86d57` | 2026-10-15 16:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_3.csv` | 166.9 KB | `1b3cf16504532bc844a499caa2177878` | 2026-10-15 16:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_4.csv` | 119.0 KB | `da65f1455b0c6994c637c9619e74cab7` | 2026-10-15 16:56 |
| `SIGNS/Buenas Noches/nw_Volunteer_5.csv` | 138.2 KB | `a84d09a14a757c5af8528beb8362a59b` | 2026-10-15 16:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_1.csv` | 89.0 KB | `393d9548a712d62fc3844baa089d6670` | 2026-10-15 16:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_2.csv` | 108.4 KB | `7c0c45db4085b9b14b2838e2f38b1624` | 2026-10-15 16:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_3.csv` | 111.0 KB | `4ce9760017fa9448454be3e97a015dd6` | 2026-10-15 16:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_4.csv` | 107.2 KB | `082102f3f92a2909bab87fcdbddec061` | 2026-10-15 16:56 |
| `SIGNS/Buenas Tardes/nw_Volunteer_5.csv` | 153.3 KB | `630555d368a82846516edc9f330c6416` | 2026-10-15 16:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_1.csv` | 85.2 KB | `4d2c0b0caa7668f98e81501ccb513106` | 2026-10-15 16:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_2.csv` | 104.4 KB | `54a11b95850c1b393fae2275fc508c31` | 2026-10-15 16:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_3.csv` | 129.1 KB | `fa0d8a6bd77d9239f2ec88b93ad37204` | 2026-10-15 16:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_4.csv` | 126.0 KB | `0b6b634dc8d137e9dff3cc49f543d874` | 2026-10-15 16:56 |
| `SIGNS/Buenos Dias/nw_Volunteer_5.csv` | 176.0 KB | `d429d380aa20408067a9596c72bd184b` | 2026-10-15 16:56 |
| `SIGNS/Comer/nw_Volunteer_1.csv` | 85.5 KB | `81fd3bdcd9d679e6e06563b882ec2908` | 2026-10-15 16:56 |
| `SIGNS/Comer/nw_Volunteer_2.csv` | 103.6 KB | `7b4af9e09ce7f3077682c7a4ea992809` | 2026-10-15 16:56 |
| `SIGNS/Comer/nw_Volunteer_3.csv` | 120.1 KB | `2d7bf1b7e0e664b62f2b5f151c42997a` | 2026-10-15 16:56 |
| `SIGNS/Comer/nw_Volunteer_4.csv` | 102.5 KB | `8992a0b212b1f16325887e06ab404761` | 2026-10-15 16:56 |
| `SIGNS/Comer/nw_Volunteer_5.csv` | 142.7 KB | `446bde805528bc0d86e4de98c87e74ad` | 2026-10-15 16:56 |
| `SIGNS/Como estas_q/nw_Volunteer_1.csv` | 90.1 KB | `b99e10e72b2e2298e32e4ef150b8b8a2` | 2026-10-15 16:56 |
| `SIGNS/Como estas_q/nw_Volunteer_2.csv` | 117.1 KB | `09676c889355744f93670fd435e79260` | 2026-10-15 16:56 |
| `SIGNS/Como estas_q/nw_Volunteer_3.csv` | 135.4 KB | `864fa86355b01bc376951633e88fa150` | 2026-10-15 16:56 |
| `SIGNS/Como estas_q/nw_Volunteer_4.csv` | 111.9 KB | `b32bb145b4a14b73bc546cdf53ee263c` | 2026-10-15 16:56 |
| `SIGNS/Como estas_q/nw_Volunteer_5.csv` | 148.6 KB | `825bc0623c9751d8f4b398bbeb1eb422` | 2026-10-15 16:56 |
| `SIGNS/Como_q/nw_Volunteer_1.csv` | 88.5 KB | `60bb538953ab1b948b7d452d796e3456` | 2026-10-15 16:56 |
| `SIGNS/Como_q/nw_Volunteer_2.csv` | 82.0 KB | `d4ad0ccb6afdf89f7833cbf6fde91d51` | 2026-10-15 16:56 |
| `SIGNS/Como_q/nw_Volunteer_3.csv` | 108.0 KB | `acafaf5c9670d58a6330d90171487b6c` | 2026-10-15 16:56 |
| `SIGNS/Como_q/nw_Volunteer_4.csv` | 121.1 KB | `d4b1ec0b9695b4383b2b4976e0697dcb` | 2026-10-15 16:56 |
| `SIGNS/Como_q/nw_Volunteer_5.csv` | 175.1 KB | `e382466e19a51128f084e34cc408781d` | 2026-10-15 16:56 |
| `SIGNS/Con Gusto/nw_Volunteer_1.csv` | 61.3 KB | `4a5637206195feeb0879c4a6043cf0bb` | 2026-10-15 16:56 |
| `SIGNS/Con Gusto/nw_Volunteer_2.csv` | 144.9 KB | `f9aca2b673e3944f2a6b734cc8bb53ec` | 2026-10-15 16:56 |
| `SIGNS/Con Gusto/nw_Volunteer_3.csv` | 129.1 KB | `1f6793dfa21fef8c6b3c3887374e2077` | 2026-10-15 16:56 |
| `SIGNS/Con Gusto/nw_Volunteer_4.csv` | 156.9 KB | `6d9eb34c942fa1b4231b0c30a05d8e02` | 2026-10-15 16:56 |
| `SIGNS/Con Gusto/nw_Volunteer_5.csv` | 161.5 KB | `500862e96a691a9cdde6fa7e5f01a09f` | 2026-10-15 16:56 |
| `SIGNS/Contento/nw_Volunteer_1.csv` | 110.1 KB | `d29122309a740d22cddc11639f6688a9` | 2026-10-15 16:56 |
| `SIGNS/Contento/nw_Volunteer_2.csv` | 97.1 KB | `1e5c29bee56375a8e4689dff62a2f9e5` | 2026-10-15 16:56 |
| `SIGNS/Contento/nw_Volunteer_3.csv` | 78.0 KB | `bbf09c475f8d0e84e7ab19f84ca7835d` | 2026-10-15 16:56 |
| `SIGNS/Contento/nw_Volunteer_4.csv` | 127.8 KB | `6991224391cff7ceb4596ee68a5255a5` | 2026-10-15 16:56 |
| `SIGNS/Contento/nw_Volunteer_5.csv` | 157.5 KB | `1206ea315c1137e80e9edf1fa7d8840f` | 2026-10-15 16:56 |
| `SIGNS/Cuando_q/nw_Volunteer_1.csv` | 89.2 KB | `c968ed01bcc7ba1373e2c8db1564d708` | 2026-10-15 16:56 |
| `SIGNS/Cuando_q/nw_Volunteer_2.csv` | 121.2 KB | `0c6986af6767f5e8ab83ee6ca6f6ae96` | 2026-10-15 16:56 |
| `SIGNS/Cuando_q/nw_Volunteer_3.csv` | 123.4 KB | `4ab4c2036d3b1c746d205a43ccf6e9fa` | 2026-10-15 16:56 |
| `SIGNS/Cuando_q/nw_Volunteer_4.csv` | 125.7 KB | `ebe037ed6ef028b6c401b17d11c069d7` | 2026-10-15 16:56 |
| `SIGNS/Cuando_q/nw_Volunteer_5.csv` | 132.5 KB | `ed2bee15a23b6c0849500a0217b3fdc5` | 2026-10-15 16:56 |
| `SIGNS/Diferente/nw_Volunteer_1.csv` | 102.1 KB | `e5aff1dfccbe2dbd98bbf9aef65207c8` | 2026-10-15 16:56 |
| `SIGNS/Diferente/nw_Volunteer_2.csv` | 139.1 KB | `593092854ffbaf2b6c6ab2bd4b3de6c0` | 2026-10-15 16:56 |
| `SIGNS/Diferente/nw_Volunteer_3.csv` | 119.6 KB | `2b0201ddda4f5d312bdca0d3181d45a9` | 2026-10-15 16:56 |
| `SIGNS/Diferente/nw_Volunteer_4.csv` | 118.1 KB | `4b4199f42fdec14fcf1bfba164490bc7` | 2026-10-15 16:56 |
| `SIGNS/Diferente/nw_Volunteer_5.csv` | 133.6 KB | `a40b844f0d96e51a6521757307a374a0` | 2026-10-15 16:56 |
| `SIGNS/Donde_q/nw_Volunteer_1.csv` | 77.8 KB | `d3bcf166e9c0c7ec8f8fdbe7c580e7b4` | 2026-10-15 16:56 |
| `SIGNS/Donde_q/nw_Volunteer_2.csv` | 128.2 KB | `ad4863fbe21db8ad9e52d55f01e121c2` | 2026-10-15 16:56 |
| `SIGNS/Donde_q/nw_Volunteer_3.csv` | 85.5 KB | `a8a1f29a30f9d3be806fa6aa559115bf` | 2026-10-15 16:56 |
| `SIGNS/Donde_q/nw_Volunteer_4.csv` | 106.2 KB | `ff874ef8a90994b40488c32c76f0968a` | 2026-10-15 16:56 |
| `SIGNS/Donde_q/nw_Volunteer_5.csv` | 131.7 KB | `94b62da9e2ffa9c626e4d6564c84c5c8` | 2026-10-15 16:56 |
| `SIGNS/Familia/nw_Volunteer_1.csv` | 84.5 KB | `3732faa1ad55bc2c0c13612f7addca58` | 2026-10-15 16:56 |
| `SIGNS/Familia/nw_Volunteer_2.csv` | 93.2 KB | `03badd74e4f007999d0069bfc6ceab66` | 2026-10-15 16:56 |
| `SIGNS/Familia/nw_Volunteer_3.csv` | 108.8 KB | `0bba71ea843b991247370d8e331be35c` | 2026-10-15 16:56 |
| `SIGNS/Familia/nw_Volunteer_4.csv` | 143.1 KB | `00e252735ee368153687cbc972212c6b` | 2026-10-15 16:56 |
| `SIGNS/Familia/nw_Volunteer_5.csv` | 139.0 KB | `5ca9ff4b48dda95fbe9892ce19ae3701` | 2026-10-15 16:56 |
| `SIGNS/Feliz/nw_Volunteer_1.csv` | 93.8 KB | `eccfb8d70d623b3bf97f8803f7f1b506` | 2026-10-15 16:56 |
| `SIGNS/Feliz/nw_Volunteer_2.csv` | 92.3 KB | `423f8830432d9bea5fe3482fa02e67c4` | 2026-10-15 16:56 |
| `SIGNS/Feliz/nw_Volunteer_3.csv` | 108.4 KB | `6b7f075e2f7427a68b63506630c20295` | 2026-10-15 16:56 |
| `SIGNS/Feliz/nw_Volunteer_4.csv` | 125.3 KB | `2565601c627397ccefed4865b8e9735b` | 2026-10-15 16:56 |
| `SIGNS/Feliz/nw_Volunteer_5.csv` | 218.6 KB | `2fea14b21b1850b4eb040f3a723e8d42` | 2026-10-15 16:56 |
| `SIGNS/Gracias/nw_Volunteer_1.csv` | 56.9 KB | `d56c2e03b42eb7f5f7efe386ec6e712f` | 2026-10-15 16:56 |
| `SIGNS/Gracias/nw_Volunteer_2.csv` | 91.2 KB | `b231de8b418cae2a0bc55c02e99cad18` | 2026-10-15 16:56 |
| `SIGNS/Gracias/nw_Volunteer_3.csv` | 119.2 KB | `e9966a21220179c7e3013036dc0a1aa8` | 2026-10-15 16:56 |
| `SIGNS/Gracias/nw_Volunteer_4.csv` | 104.0 KB | `a399c802137d81f664cbde083d093d12` | 2026-10-15 16:56 |
| `SIGNS/Gracias/nw_Volunteer_5.csv` | 107.5 KB | `3272796ce2bb0b0582325b707d9e97fe` | 2026-10-15 16:56 |
| `SIGNS/Hambre/nw_Volunteer_1.csv` | 100.3 KB | `b325d632782ff79b11a4eb7e180ee225` | 2026-10-15 16:56 |
| `SIGNS/Hambre/nw_Volunteer_2.csv` | 115.1 KB | `a90b5ffc78a5816f425299af0129cd9e` | 2026-10-15 16:56 |
| `SIGNS/Hambre/nw_Volunteer_3.csv` | 159.2 KB | `0866e0d0b4753f5c6ca153a365018228` | 2026-10-15 16:56 |
| `SIGNS/Hambre/nw_Volunteer_4.csv` | 152.4 KB | `737e8f36f1e13e254e582b709ea80944` | 2026-10-15 16:56 |
| `SIGNS/Hambre/nw_Volunteer_5.csv` | 125.4 KB | `e5797a98e0c0e2c97771f60226046f7a` | 2026-10-15 16:56 |
| `SIGNS/Hermano/nw_Volunteer_1.csv` | 94.3 KB | `76e98fd26e9892debaf1c6c6d0ee68f4` | 2026-10-15 16:56 |
| `SIGNS/Hermano/nw_Volunteer_2.csv` | 105.8 KB | `e44a73a5214d42650b20ec039ba29727` | 2026-10-15 16:56 |
| `SIGNS/Hermano/nw_Volunteer_3.csv` | 120.2 KB | `8d44f49cffb7cce467835a2cce94b997` | 2026-10-15 16:56 |
| `SIGNS/Hermano/nw_Volunteer_4.csv` | 119.7 KB | `ad57c242d29e8354720eea60cbd0f3d1` | 2026-10-15 16:56 |
| `SIGNS/Hermano/nw_Volunteer_5.csv` | 138.8 KB | `e9fdfec7a43e6e18c86f4f5bc149b814` | 2026-10-15 16:56 |
| `SIGNS/Hola/nw_Volunteer_1.csv` | 83.2 KB | `c545a3e000c08950fda93685255f460e` | 2026-10-15 16:56 |
| `SIGNS/Hola/nw_Volunteer_2.csv` | 141.4 KB | `a5e0d74fc53159eccfdb50cfe1017ed3` | 2026-10-15 16:56 |
| `SIGNS/Hola/nw_Volunteer_3.csv` | 132.6 KB | `abc034b6bcd82d7ecb1d2b0af1dc08b3` | 2026-10-15 16:56 |
| `SIGNS/Hola/nw_Volunteer_4.csv` | 102.6 KB | `3c5033ea7ac78b7d294e1e6d1b690992` | 2026-10-15 16:56 |
| `SIGNS/Hola/nw_Volunteer_5.csv` | 207.4 KB | `dac4d34b5003e660023771364aaaedf5` | 2026-10-15 16:56 |
| `SIGNS/Hombre/nw_Volunteer_1.csv` | 62.1 KB | `b7da587e495238b01e3b7fe9282189ca` | 2026-10-15 16:56 |
| `SIGNS/Hombre/nw_Volunteer_2.csv` | 92.4 KB | `f395ab728ab20d1a6ead9acc1ad9bfee` | 2026-10-15 16:56 |
| `SIGNS/Hombre/nw_Volunteer_3.csv` | 132.9 KB | `8e50fbae0ff07c39bd62ea33e3f24e8e` | 2026-10-15 16:56 |
| `SIGNS/Hombre/nw_Volunteer_4.csv` | 147.1 KB | `4b02c0165c14e9a42151dce30bc09b4b` | 2026-10-15 16:56 |
| `SIGNS/Hombre/nw_Volunteer_5.csv` | 176.6 KB | `05b1aa36c51831d80d2bb05856709bad` | 2026-10-15 16:56 |
| `SIGNS/Jucioso/nw_Volunteer_1.csv` | 94.2 KB | `ba622cee8013304616b64df5341a9919` | 2026-10-15 16:56 |
| `SIGNS/Jucioso/nw_Volunteer_2.csv` | 140.9 KB | `990442821d990da8110c551f271d07b8` | 2026-10-15 16:56 |
| `SIGNS/Jucioso/nw_Volunteer_3.csv` | 131.2 KB | `f2e230f45d24b22d8993c58a1db7ff3a` | 2026-10-15 16:56 |
| `SIGNS/Jucioso/nw_Volunteer_4.csv` | 116.8 KB | `baed389c7ae98e40e43d053805d6a88d` | 2026-10-15 16:56 |
| `SIGNS/Jucioso/nw_Volunteer_5.csv` | 162.2 KB | `8c3eb993dc673a83e32e90be1b354ed8` | 2026-10-15 16:56 |
| `SIGNS/Mal/nw_Volunteer_1.csv` | 86.6 KB | `da379adab4f499e6810bf4eec6615f3b` | 2026-10-15 16:56 |
| `SIGNS/Mal/nw_Volunteer_2.csv` | 145.8 KB | `b357206538ce08e50f8a813272085e24` | 2026-10-15 16:56 |
| `SIGNS/Mal/nw_Volunteer_3.csv` | 107.1 KB | `e3d306fb35eaef294cfa5886fcbbd259` | 2026-10-15 16:56 |
| `SIGNS/Mal/nw_Volunteer_4.csv` | 134.7 KB | `c51b906ea5d29a5f73ec57c4fa7ee698` | 2026-10-15 16:56 |
| `SIGNS/Mal/nw_Volunteer_5.csv` | 143.7 KB | `7a0a4ae706bb40c2a844fb78f3aac028` | 2026-10-15 16:56 |
| `SIGNS/Mas o menos/nw_Volunteer_1.csv` | 99.5 KB | `f0999183cb894bea1688319fe08078e3` | 2026-10-15 16:56 |
| `SIGNS/Mas o menos/nw_Volunteer_2.csv` | 125.1 KB | `61fecda54a19d54f7e3977ac4e2040d5` | 2026-10-15 16:56 |
| `SIGNS/Mas o menos/nw_Volunteer_3.csv` | 97.4 KB | `8c0d98bddf58d17923ef8bb621698a2c` | 2026-10-15 16:56 |
| `SIGNS/Mas o menos/nw_Volunteer_4.csv` | 132.8 KB | `0ddc100dfee538c94c7aafbf6294c1af` | 2026-10-15 16:56 |
| `SIGNS/Mas o menos/nw_Volunteer_5.csv` | 190.7 KB | `37b5ba3adef3507f940242953575be11` | 2026-10-15 16:56 |
| `SIGNS/Mucho/nw_Volunteer_1.csv` | 86.2 KB | `bdedb63e007acbfdd2e21f47c2dc4581` | 2026-10-15 16:56 |
| `SIGNS/Mucho/nw_Volunteer_2.csv` | 142.5 KB | `3bc6c157e046bc1aeb907e97912d7922` | 2026-10-15 16:56 |
| `SIGNS/Mucho/nw_Volunteer_3.csv` | 108.8 KB | `d905e4fe657925ccdadaed46447a39f9` | 2026-10-15 16:56 |
| `SIGNS/Mucho/nw_Volunteer_4.csv` | 143.3 KB | `040e2ceba9f726561b1632dfc43c89cd` | 2026-10-15 16:56 |
| `SIGNS/Mucho/nw_Volunteer_5.csv` | 164 B | `60daa8ae672e83d8a02b254f842aa7c2` | 2026-10-15 16:56 |
| `SIGNS/Mujer/nw_Volunteer_1.csv` | 66.7 KB | `ff919ee3132b406a1c4b9a30b926bc5f` | 2026-10-15 16:56 |
| `SIGNS/Mujer/nw_Volunteer_2.csv` | 87.7 KB | `431b80ef24f7b142ce7e7355b1b40d0f` | 2026-10-15 16:56 |
| `SIGNS/Mujer/nw_Volunteer_3.csv` | 121.5 KB | `3c397b7426f2e9d3abd629c4615d3151` | 2026-10-15 16:56 |
| `SIGNS/Mujer/nw_Volunteer_4.csv` | 117.5 KB | `e1423854946df711e36c2fbb0fc480d8` | 2026-10-15 16:56 |
| `SIGNS/Mujer/nw_Volunteer_5.csv` | 171.8 KB | `5fa7071555d45138617f9a297298c5c2` | 2026-10-15 16:56 |
| `SIGNS/Niña/nw_Volunteer_1.csv` | 63.8 KB | `3e447029e92815d4cf8f28826715fc97` | 2026-10-15 16:56 |
| `SIGNS/Niña/nw_Volunteer_2.csv` | 106.0 KB | `2dfaf76ab779d21ce43bff8ce31293de` | 2026-10-15 16:56 |
| `SIGNS/Niña/nw_Volunteer_3.csv` | 140.2 KB | `b63ae006c14db3766c07c6ade278f255` | 2026-10-15 16:56 |
| `SIGNS/Niña/nw_Volunteer_4.csv` | 145.6 KB | `7044a3ce328b73d5999b5f9eabe0a62d` | 2026-10-15 16:56 |
| `SIGNS/Niña/nw_Volunteer_5.csv` | 158.9 KB | `d0d08fb538ce68a3e505024ad906d453` | 2026-10-15 16:56 |
| `SIGNS/Niño/nw_Volunteer_1.csv` | 75.4 KB | `ab42bc4592633a9b8b77457c2a56e746` | 2026-10-15 16:56 |
| `SIGNS/Niño/nw_Volunteer_2.csv` | 99.4 KB | `922b551216cd4a6ba51cc8f4e37b5264` | 2026-10-15 16:56 |
| `SIGNS/Niño/nw_Volunteer_3.csv` | 147.2 KB | `085658399fc1be9c51fe4041acad4428` | 2026-10-15 16:56 |
| `SIGNS/Niño/nw_Volunteer_4.csv` | 135.1 KB | `1da44958f5cc211b6d3b17ff2c374626` | 2026-10-15 16:56 |
| `SIGNS/Niño/nw_Volunteer_5.csv` | 214.4 KB | `d051abdb5c5fb69e178cdf89a59c4332` | 2026-10-15 16:56 |
| `SIGNS/Nombre/nw_Volunteer_1.csv` | 83.8 KB | `95a16df4a279397eb981fcb03574b40d` | 2026-10-15 16:56 |
| `SIGNS/Nombre/nw_Volunteer_2.csv` | 103.9 KB | `72d686900115a2b2f21c8041019f58b4` | 2026-10-15 16:56 |
| `SIGNS/Nombre/nw_Volunteer_3.csv` | 160.1 KB | `8a509f0d317a05d75d92ec0589b828c2` | 2026-10-15 16:56 |
| `SIGNS/Nombre/nw_Volunteer_4.csv` | 113.0 KB | `61e61c180024b6e5c640939e8be1f8cc` | 2026-10-15 16:56 |
| `SIGNS/Nombre/nw_Volunteer_5.csv` | 133.6 KB | `29a9d81369fd4ca7f62685ba2700a3fe` | 2026-10-15 16:56 |
| `SIGNS/Nunca/nw_Volunteer_1.csv` | 91.6 KB | `e5bd0c3eecce30ef50e7f3ddec5e35f2` | 2026-10-15 16:56 |
| `SIGNS/Nunca/nw_Volunteer_2.csv` | 119.3 KB | `8337b0bab710b29d5e74769c40cb968e` | 2026-10-15 16:56 |
| `SIGNS/Nunca/nw_Volunteer_3.csv` | 111.5 KB | `6a987913d97164d6a09b131857cdc926` | 2026-10-15 16:56 |
| `SIGNS/Nunca/nw_Volunteer_4.csv` | 117.2 KB | `347c339b5b0f8dad8708f2e4123c3eae` | 2026-10-15 16:56 |
| `SIGNS/Nunca/nw_Volunteer_5.csv` | 178.0 KB | `f3a70765a5f1bbd65d7e03b8cf36207e` | 2026-10-15 16:56 |
| `SIGNS/Perdon/nw_Volunteer_1.csv` | 91.0 KB | `1eda76f0627895967db251e3b08ccc87` | 2026-10-15 16:56 |
| `SIGNS/Perdon/nw_Volunteer_2.csv` | 107.2 KB | `514c0ef4da1f410e30140b19fd3cde84` | 2026-10-15 16:56 |
| `SIGNS/Perdon/nw_Volunteer_3.csv` | 117.7 KB | `0dab99c0490790187c0821d929b4d2c3` | 2026-10-15 16:56 |
| `SIGNS/Perdon/nw_Volunteer_4.csv` | 129.6 KB | `94daf6dc7f22ed02f5c2ea7467d00b03` | 2026-10-15 16:56 |
| `SIGNS/Perdon/nw_Volunteer_5.csv` | 140.0 KB | `b9b92166088f3d687a9cada78f36fef2` | 2026-10-15 16:56 |
| `SIGNS/Permiso/nw_Volunteer_1.csv` | 75.1 KB | `88ce7e7b8b5091bcb99d9156feb5eb5d` | 2026-10-15 16:56 |
| `SIGNS/Permiso/nw_Volunteer_2.csv` | 105.7 KB | `6d20868e8587db60d528135ed7179c53` | 2026-10-15 16:56 |
| `SIGNS/Permiso/nw_Volunteer_3.csv` | 135.1 KB | `509881f3406c99ace7076fc3c710df4f` | 2026-10-15 16:56 |
| `SIGNS/Permiso/nw_Volunteer_4.csv` | 132.8 KB | `8be2d6eab99096e07d193700dbc3e2ba` | 2026-10-15 16:56 |
| `SIGNS/Permiso/nw_Volunteer_5.csv` | 185.4 KB | `af4afe09a966777e043e8656ca0baae8` | 2026-10-15 16:56 |
| `SIGNS/Personas/nw_Volunteer_1.csv` | 81.3 KB | `ff13449eee7d2ebb57d6666bcfdf1fc9` | 2026-10-15 16:56 |
| `SIGNS/Personas/nw_Volunteer_2.csv` | 104.0 KB | `f9717c559ecadd77cad2bd40acb76375` | 2026-10-15 16:56 |
| `SIGNS/Personas/nw_Volunteer_3.csv` | 144.2 KB | `b69ba0a0523d8dba73f1a4efbdc46d9d` | 2026-10-15 16:56 |
| `SIGNS/Personas/nw_Volunteer_4.csv` | 114.5 KB | `51665c19e20e578bc4a74bc1fa5bd1ab` | 2026-10-15 16:56 |
| `SIGNS/Personas/nw_Volunteer_5.csv` | 130.3 KB | `39dc8456b14c4fc2527b42da49c41760` | 2026-10-15 16:56 |
| `SIGNS/Poco/nw_Volunteer_1.csv` | 85.5 KB | `90b7e15b2dfd8cc75ffc34cdaa757c2c` | 2026-10-15 16:56 |
| `SIGNS/Poco/nw_Volunteer_2.csv` | 98.9 KB | `e75fb0d431936177831c608f8f83b304` | 2026-10-15 16:56 |
| `SIGNS/Poco/nw_Volunteer_3.csv` | 136.1 KB | `d1ebaa5066b35d4ae8966d3c3ffff995` | 2026-10-15 16:56 |
| `SIGNS/Poco/nw_Volunteer_4.csv` | 133.7 KB | `d5b8e323f11ffe30d91f8527e8d3bc18` | 2026-10-15 16:56 |
| `SIGNS/Poco/nw_Volunteer_5.csv` | 161.9 KB | `0f882d326edb471f298adcad3c08ccae` | 2026-10-15 16:56 |
| `SIGNS/Por favor/nw_Volunteer_1.csv` | 78.8 KB | `edef36df2afa71b6fc758ae4938ea4c1` | 2026-10-15 16:56 |
| `SIGNS/Por favor/nw_Volunteer_2.csv` | 141.4 KB | `6d45bf3497cfaaf50f926d08222e4629` | 2026-10-15 16:56 |
| `SIGNS/Por favor/nw_Volunteer_3.csv` | 105.1 KB | `f34381cdb357793d1f35d6ae61741cf9` | 2026-10-15 16:56 |
| `SIGNS/Por favor/nw_Volunteer_4.csv` | 135.4 KB | `420490ba6751e848d64d9ff78eb7aaff` | 2026-10-15 16:56 |
| `SIGNS/Por favor/nw_Volunteer_5.csv` | 131.2 KB | `39297b049a0824a59fa160ec16900e4d` | 2026-10-15 16:56 |
| `SIGNS/Por que_q/nw_Volunteer_1.csv` | 98.9 KB | `446eece351a0b620a4f8e9fb359462fc` | 2026-10-15 16:56 |
| `SIGNS/Por que_q/nw_Volunteer_2.csv` | 121.5 KB | `af5ea7b3f80754e7293eb274e7e89817` | 2026-10-15 16:56 |
| `SIGNS/Por que_q/nw_Volunteer_3.csv` | 134.6 KB | `7f0922ca9da9d163f4f599a229a24e2d` | 2026-10-15 16:56 |
| `SIGNS/Por que_q/nw_Volunteer_4.csv` | 128.6 KB | `5f61ca372368e9d492c2fb35e635c8d2` | 2026-10-15 16:56 |
| `SIGNS/Por que_q/nw_Volunteer_5.csv` | 134.9 KB | `a11249dd0bded54d1962141d9739869e` | 2026-10-15 16:56 |
| `SIGNS/Que_q/nw_Volunteer_1.csv` | 82.7 KB | `f2e02e8a01e82bb06ac89a96bf62e803` | 2026-10-15 16:56 |
| `SIGNS/Que_q/nw_Volunteer_2.csv` | 130.5 KB | `c0cef58376586693a1630db09ea19023` | 2026-10-15 16:56 |
| `SIGNS/Que_q/nw_Volunteer_3.csv` | 89.8 KB | `a6e49c5dce3f554dbd0f8e908829f121` | 2026-10-15 16:56 |
| `SIGNS/Que_q/nw_Volunteer_4.csv` | 122.4 KB | `64ffa6c848d9b5294d1bb340448ecb17` | 2026-10-15 16:56 |
| `SIGNS/Que_q/nw_Volunteer_5.csv` | 148.6 KB | `0993f59b63ced80014c337d03641c3e3` | 2026-10-15 16:56 |
| `SIGNS/Quien_q/nw_Volunteer_1.csv` | 97.2 KB | `e1ce7b90621fdec9e8d6d9cdfaaedef1` | 2026-10-15 16:56 |
| `SIGNS/Quien_q/nw_Volunteer_2.csv` | 162.4 KB | `aa29b6a48c72aee2cb9da68b6cd01fd3` | 2026-10-15 16:56 |
| `SIGNS/Quien_q/nw_Volunteer_3.csv` | 109.5 KB | `de94f5c43026d603d11d1ea4530592b0` | 2026-10-15 16:56 |
| `SIGNS/Quien_q/nw_Volunteer_4.csv` | 124.4 KB | `aa51299cdcc248d8e5ea9bb4b87d5b20` | 2026-10-15 16:56 |
| `SIGNS/Quien_q/nw_Volunteer_5.csv` | 155.3 KB | `c11c5ea2074cf5c3d4412c4f26590f13` | 2026-10-15 16:56 |
| `SIGNS/Sentir/nw_Volunteer_1.csv` | 69.3 KB | `27c114ef150163364fa3a14cc49d1422` | 2026-10-15 16:56 |
| `SIGNS/Sentir/nw_Volunteer_2.csv` | 148.8 KB | `b5bcd30a76a1f119c803a8bc796e0e6b` | 2026-10-15 16:56 |
| `SIGNS/Sentir/nw_Volunteer_3.csv` | 120.1 KB | `41344129b3d6ffe5249f4427b63a8e6c` | 2026-10-15 16:56 |
| `SIGNS/Sentir/nw_Volunteer_4.csv` | 136.8 KB | `2c1a55ad17542c6de458913d602fc219` | 2026-10-15 16:56 |
| `SIGNS/Sentir/nw_Volunteer_5.csv` | 140.0 KB | `b4f1d850cbc8a11b490326cc4c308098` | 2026-10-15 16:56 |
| `SIGNS/Seña/nw_Volunteer_1.csv` | 76.2 KB | `b8a7f5db5ff3ced8d80fbbf5f25b0459` | 2026-10-15 16:56 |
| `SIGNS/Seña/nw_Volunteer_2.csv` | 100.8 KB | `5eb778c02c24055fa5bc6aa819c9b226` | 2026-10-15 16:56 |
| `SIGNS/Seña/nw_Volunteer_3.csv` | 171.0 KB | `af31256a5459e94e7d62f9acd62eb95c` | 2026-10-15 16:56 |
| `SIGNS/Seña/nw_Volunteer_4.csv` | 135.2 KB | `86caa579710f1e1f7b9ca19d7ebf5de9` | 2026-10-15 16:56 |
| `SIGNS/Seña/nw_Volunteer_5.csv` | 175.0 KB | `a3b972ab3a2c4a91f11216309c36323d` | 2026-10-15 16:56 |
| `SIGNS/Tio /nw_Volunteer_1.csv` | 77.9 KB | `b2b5aea42c355ec16274060a9f081bcf` | 2026-10-15 16:56 |
| `SIGNS/Tio /nw_Volunteer_2.csv` | 110.7 KB | `52acb5e6da3fead4c0d3ce3c252f3fd9` | 2026-10-15 16:56 |
| `SIGNS/Tio /nw_Volunteer_3.csv` | 132.0 KB | `14c847096da596e6504126b242069532` | 2026-10-15 16:56 |
| `SIGNS/Tio /nw_Volunteer_4.csv` | 133.6 KB | `af6b9f628e32f2ac1ca3505f4f7bb398` | 2026-10-15 16:56 |
| `SIGNS/Tio /nw_Volunteer_5.csv` | 170.4 KB | `bd192701e6adc5136d9724541e0cb397` | 2026-10-15 16:56 |
| `SIGNS/Todos/nw_Volunteer_1.csv` | 97.3 KB | `f74110bc98ba35368180c7e832425e75` | 2026-10-15 16:56 |
| `SIGNS/Todos/nw_Volunteer_2.csv` | 148.0 KB | `07ad7d6c75c3b66898cf182df2ee137e` | 2026-10-15 16:56 |
| `SIGNS/Todos/nw_Volunteer_3.csv` | 122.7 KB | `9a551567180e7a655dc4c5f5374f5cc9` | 2026-10-15 16:56 |
| `SIGNS/Todos/nw_Volunteer_4.csv` | 125.7 KB | `659c36666230a3475013046641c55fce` | 2026-10-15 16:56 |
| `SIGNS/Todos/nw_Volunteer_5.csv` | 146.2 KB | `04e3e696430825b08a4cc97c2f46767a` | 2026-10-15 16:56 |
| `SIGNS/Trabajar/nw_Volunteer_1.csv` | 86.1 KB | `36e9769548d734fe4758e2222fd61124` | 2026-10-15 16:56 |
| `SIGNS/Trabajar/nw_Volunteer_2.csv` | 119.6 KB | `0556a3a7311185130dedf6c0e712b151` | 2026-10-15 16:56 |
| `SIGNS/Trabajar/nw_Volunteer_3.csv` | 144.5 KB | `6b106af098de26f4cb9507170a3d5ded` | 2026-10-15 16:56 |
| `SIGNS/Trabajar/nw_Volunteer_4.csv` | 125.2 KB | `a10150a76fa8828b15ebe7ecf7b0960d` | 2026-10-15 16:56 |
| `SIGNS/Trabajar/nw_Volunteer_5.csv` | 157.5 KB | `59fa77b84cb15e6db8ac396501bd9402` | 2026-10-15 16:56 |
| `SIGNS/Triste/nw_Volunteer_1.csv` | 99.7 KB | `a4a0d8aba02a4cdad44e16415beea001` | 2026-10-15 16:56 |
| `SIGNS/Triste/nw_Volunteer_2.csv` | 106.1 KB | `cfb601e30123b051c61845dd31442f97` | 2026-10-15 16:56 |
| `SIGNS/Triste/nw_Volunteer_3.csv` | 156.4 KB | `29a2e087a82a9cf62a003f5ac573d9e1` | 2026-10-15 16:56 |
| `SIGNS/Triste/nw_Volunteer_4.csv` | 139.8 KB | `df4d85bfdb92c84017f1e0cd39e6bd35` | 2026-10-15 16:56 |
| `SIGNS/Triste/nw_Volunteer_5.csv` | 141.0 KB | `7e55cb32e90510d486218a62ef3251cb` | 2026-10-15 16:56 |
| `SIGNS/Tu/nw_Volunteer_1.csv` | 68.5 KB | `20b22ecc1a7d543201e207944429f6b9` | 2026-10-15 16:56 |
| `SIGNS/Tu/nw_Volunteer_2.csv` | 128.2 KB | `4251d118ba2b68194e7e9897d8cb71f1` | 2026-10-15 16:56 |
| `SIGNS/Tu/nw_Volunteer_3.csv` | 111.0 KB | `7660b3d134d54e0acf47bc8a7b46606f` | 2026-10-15 16:56 |
| `SIGNS/Tu/nw_Volunteer_4.csv` | 127.0 KB | `04a527dcaf233ff8129c4ef2594b435c` | 2026-10-15 16:56 |
| `SIGNS/Tu/nw_Volunteer_5.csv` | 126.5 KB | `3348e75eb72d0e95a5d472de26a85a27` | 2026-10-15 16:56 |
| `SIGNS/Ustedes/nw_Volunteer_1.csv` | 71.2 KB | `e5378fb7a269edc16e0b54420e7a97f7` | 2026-10-15 16:56 |
| `SIGNS/Ustedes/nw_Volunteer_2.csv` | 118.9 KB | `29d9e1fc7fbd8c911754822598ee172e` | 2026-10-15 16:56 |
| `SIGNS/Ustedes/nw_Volunteer_3.csv` | 122.2 KB | `3d0086904f5bd3b05ce27e9ba091fb2f` | 2026-10-15 16:56 |
| `SIGNS/Ustedes/nw_Volunteer_4.csv` | 97.6 KB | `d0a559abe64a345b99d37ae484cf26f2` | 2026-10-15 16:56 |
| `SIGNS/Ustedes/nw_Volunteer_5.csv` | 141.8 KB | `458d4619ca55282006ca41ff6fff42c0` | 2026-10-15 16:56 |
| `SIGNS/Vivir/nw_Volunteer_1.csv` | 88.6 KB | `f6807ff9762ea7033d9cd6869e187586` | 2026-10-15 16:56 |
| `SIGNS/Vivir/nw_Volunteer_2.csv` | 105.7 KB | `b6b7e7cf82116a61d88a3056127fbfba` | 2026-10-15 16:56 |
| `SIGNS/Vivir/nw_Volunteer_3.csv` | 139.7 KB | `f8cb57515ca6666db9e37dbafc1a912a` | 2026-10-15 16:56 |
| `SIGNS/Vivir/nw_Volunteer_4.csv` | 127.6 KB | `116a88fd0572ae95d7642f27db589f40` | 2026-10-15 16:56 |
| `SIGNS/Vivir/nw_Volunteer_5.csv` | 156.0 KB | `10976c09a18a7fd39a890e66aada04fa` | 2026-10-15 16:56 |
| `SIGNS/Yo/nw_Volunteer_1.csv` | 82.9 KB | `a97c76e4a9a8de99287589eec45c05c7` | 2026-10-15 16:56 |
| `SIGNS/Yo/nw_Volunteer_2.csv` | 87.7 KB | `d9d0934c066b008cc7e2fa2db7348300` | 2026-10-15 16:56 |
| `SIGNS/Yo/nw_Volunteer_3.csv` | 96.5 KB | `17e888aac73a0622b38df8433cb0bece` | 2026-10-15 16:56 |
| `SIGNS/Yo/nw_Volunteer_4.csv` | 98.1 KB | `4a254a6135ab978dde0c3ef762b3743b` | 2026-10-15 16:56 |
| `SIGNS/Yo/nw_Volunteer_5.csv` | 131.7 KB | `7a63fb0b2fe49dd43d347ccd897a17e3` | 2026-10-15 16:56 |
| `analysis/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-18 16:56 |
| `analysis/dtw_all.log` | 1.9 KB | `8f4f902ae3438a8f44948599dae6e738` | 2026-10-18 16:51 |
| `analysis/dtw_all_pairs.csv` | 486.9 KB | `dc6cab5e6cd718c3db54843141b41544` | 2026-10-18 16:51 |
| `analysis/dtw_all_signer_matrix.csv` | 493 B | `eac3572a7efae2ce7001a53663429e7c` | 2026-10-18 16:51 |
| `analysis/dtw_hands.log` | 1.9 KB | `8ae43455b5708b8cd092a078972ce0d9` | 2026-10-18 16:51 |
| `analysis/dtw_hands_pairs.csv` | 487.4 KB | `f90fa515482df3471959641469f0cc82` | 2026-10-18 16:51 |
| `analysis/dtw_hands_signer_matrix.csv` | 499 B | `7d8380a6ca0c10e0c610d010bc4843e7` | 2026-10-18 16:51 |
| `analysis/importance_imu.csv` | 11.6 KB | `a21c55d143049e08e507c266566b8357` | 2026-10-18 16:56 |
| `analysis/importance_imu.log` | 3.1 KB | `d2a4421a4f3b777c765bb50a3393cb3a` | 2026-10-18 16:56 |
| `analysis/importance_landmarks.log` | 3.5 KB | `07706e6c2d6ca100ab0ed15a30ecc620` | 2026-10-18 16:55 |
| `analysis/importance_landmarks_bodynorm.csv` | 32.2 KB | `b0f81693d360d38271b1d2a7472dba75` | 2026-10-18 16:55 |
| `analysis/run.log` | 207 B | `6cd3a77a829b5942e1e6a65e3bdd767d` | 2026-10-18 16:50 |
| `analysis/run.sh` | 1.6 KB | `14507525e8bace395e4b7da6342f0b23` | 2026-10-18 16:50 |
| `analysis/signer_ci.csv` | 5.4 KB | `a5e1c5f2e2dedcf1316489f4f098120f` | 2026-10-19 17:58 |
| `audit/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-18 19:41 |
| `audit/imu_reproduce.log` | 1.3 KB | `e010a2b5462766effbde277c483f6505` | 2026-10-18 19:40 |
| `audit/imu_segmentation_check.csv` | 48.6 KB | `44354fdf9c3881629d7f4ddd4af6e226` | 2026-10-19 17:25 |
| `audit/vivit_duplicates.log` | 172 B | `aa6d900a82ee227ad7b474b6c9ab8f91` | 2026-10-18 19:41 |
| `bodynorm/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-17 17:27 |
| `bodynorm/DONE2` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-17 20:26 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_seed0.pkl` | 19.7 KB | `cf74636be77409a52cc7ab51572e7504` | 2026-10-17 19:57 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_seed1.pkl` | 19.7 KB | `76239447fa017a1a3595a279f643c4d9` | 2026-10-17 20:04 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_seed2.pkl` | 19.7 KB | `61e9e51d51e67ba348a41e050e4d0207` | 2026-10-17 20:11 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_seed3.pkl` | 19.7 KB | `5ef726ef00b601c7443632862316eb95` | 2026-10-17 20:19 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_seed4.pkl` | 19.7 KB | `f9b2b65a256a1cc22347a458505f229d` | 2026-10-17 20:26 |
| `bodynorm/cm_rf_temporal_features_bodynorm_balanced_shuffled_seed0.pkl` | 19.7 KB | `e47741d6da72cdc29d99c5712cf05f8f` | 2026-10-20 17:01 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed0.pkl` | 19.7 KB | `9df4db31cc3d27b8d26266d9b3a1f22e` | 2026-10-17 17:03 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed1.pkl` | 19.7 KB | `8ff3dcee9cf1538651ebbdcaf23f5414` | 2026-10-17 17:39 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed2.pkl` | 19.7 KB | `1e703212194975de374a386447e83ed2` | 2026-10-17 18:11 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed3.pkl` | 19.7 KB | `2fa382a1f69271a0fed34ac2b63b5084` | 2026-10-17 18:45 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_seed4.pkl` | 19.7 KB | `bb0a4ef9892128897a45b5d2c78efc60` | 2026-10-17 19:21 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_0_groupcv_shuffled_seed0.pkl` | 19.7 KB | `2b77821714bf552e55a4bdd5caa4a641` | 2026-10-20 15:41 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_seed0.pkl` | 19.7 KB | `c8c8e137adb4df15c0099824dde6f964` | 2026-10-17 17:09 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_seed1.pkl` | 19.7 KB | `a1e89bb16182ddacbda9bbec1cdd9e9b` | 2026-10-17 17:45 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_seed2.pkl` | 19.7 KB | `9a6318e6542fabc5a2df2a347e9d261b` | 2026-10-17 18:17 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_seed3.pkl` | 19.7 KB | `23bb96d4c3989b90a594122a6a7340f4` | 2026-10-17 18:52 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_seed4.pkl` | 19.7 KB | `14e4f421bc1ab15b854c670497401843` | 2026-10-17 19:28 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_1_groupcv_shuffled_seed0.pkl` | 19.7 KB | `750d475456115fb9cc76c9b6151a3efe` | 2026-10-20 15:51 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_seed0.pkl` | 19.7 KB | `307ff267515614c7b887194e00f328b4` | 2026-10-17 17:15 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_seed1.pkl` | 19.7 KB | `55e5a75aa3c03c9f3f6f902919a4099b` | 2026-10-17 17:51 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_seed2.pkl` | 19.7 KB | `2d5d90750f08e82f737e16bab5343ffa` | 2026-10-17 18:24 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_seed3.pkl` | 19.7 KB | `eef64881726bc6969945801ab9dc9c13` | 2026-10-17 19:00 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_seed4.pkl` | 19.7 KB | `bf490487c5ec7bdb7d66787ddc37f30d` | 2026-10-17 19:35 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_2_groupcv_shuffled_seed0.pkl` | 19.7 KB | `f41c463cfc4b59619c2a4258476b0b8d` | 2026-10-20 16:06 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_seed0.pkl` | 19.7 KB | `9faf144f47b0eb1469e7e0ec214f77a1` | 2026-10-17 17:21 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_seed1.pkl` | 19.7 KB | `9b91686ea88b716d2283b30adccd5034` | 2026-10-17 17:57 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_seed2.pkl` | 19.7 KB | `481b4da69f8bf37195ab5604f125289d` | 2026-10-17 18:31 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_seed3.pkl` | 19.7 KB | `ed24affbed9f543eebdffae4c41d4768` | 2026-10-17 19:07 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_seed4.pkl` | 19.7 KB | `673731181672a1c06c5dc92ef2c91228` | 2026-10-17 19:42 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_3_groupcv_shuffled_seed0.pkl` | 19.7 KB | `375bb8eedec8f21d918437540fd1777f` | 2026-10-20 16:25 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_seed0.pkl` | 19.7 KB | `1dceb3dca98585ce815b5730a9482f34` | 2026-10-17 17:27 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_seed1.pkl` | 19.7 KB | `812b50ec6cc709a65637f7aa966e135a` | 2026-10-17 18:04 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_seed2.pkl` | 19.7 KB | `46952cc8cf751cf0e763bc1a63c173ad` | 2026-10-17 18:38 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_seed3.pkl` | 19.7 KB | `1df779ac70809798db7681f75b3b75ce` | 2026-10-17 19:14 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_seed4.pkl` | 19.7 KB | `0d34ddf75c66404c7bb3ce161e0e2ff1` | 2026-10-17 19:49 |
| `bodynorm/cm_rf_temporal_features_bodynorm_loso_4_groupcv_shuffled_seed0.pkl` | 19.7 KB | `4658ccbf93ef60c884c9b4e99ccd74bd` | 2026-10-20 16:42 |
| `bodynorm/general_db_bodynorm.csv` | 58.8 MB | `f794252fce6e8dc904144851a87da0e5` | 2026-10-17 16:47 |
| `bodynorm/general_db_f0_bodynorm.csv` | 151.3 MB | `039458aae6fb7d4d36f7816438e12909` | 2026-10-18 16:50 |
| `bodynorm/general_db_f16_bodynorm.csv` | 39.2 MB | `550e74e1c4f228503e433e551337d763` | 2026-10-22 02:32 |
| `bodynorm/general_db_f32_bodynorm.csv` | 78.4 MB | `22aa37460a8ddf67d280791c55c691b4` | 2026-10-22 02:32 |
| `bodynorm/general_db_f48_bodynorm.csv` | 117.6 MB | `78fa6092e641be154f3e006e687e8156` | 2026-10-22 02:32 |
| `bodynorm/grid.log` | 2.9 KB | `124fbfe913eb38bb78fb3ab7947a9836` | 2026-10-17 17:27 |
| `bodynorm/grid_8020.log` | 2.6 KB | `8dfe2a33fa30ae65e81c6816f6de25ca` | 2026-10-17 20:26 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed0.pkl` | 592.4 KB | `c61afcb53f79abf57a7586f40789ec63` | 2026-10-17 17:27 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed1.pkl` | 592.4 KB | `7d8b9067dfa0d0816e7528f45af2a4ba` | 2026-10-17 18:04 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed2.pkl` | 592.4 KB | `40616943d9582b0dc575cdad9dcae43a` | 2026-10-17 18:38 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed3.pkl` | 592.4 KB | `cc6758d1f2493fa4ee694ac7d5acfabb` | 2026-10-17 19:14 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed4.pkl` | 592.4 KB | `9ff13f9ad4580134f8d05b0c8f5604e6` | 2026-10-17 19:49 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_shuffled_seed0.pkl` | 592.4 KB | `96e178dd920d604494df4a38ad347a55` | 2026-10-20 16:42 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed0.pkl` | 119.0 KB | `a50c4b96e455cbf13690c182cfbb1ca0` | 2026-10-17 19:57 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed1.pkl` | 119.0 KB | `c767f7dfeab1965cc168de860fbf0270` | 2026-10-17 20:04 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed2.pkl` | 119.0 KB | `49d297dda2d8db17e956ee59346f99f2` | 2026-10-17 20:11 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed3.pkl` | 119.0 KB | `d0041638905c7e9fb6008bc12ac60d63` | 2026-10-17 20:19 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed4.pkl` | 119.0 KB | `5ea8fe5211148d547eefaa76b3bea8d0` | 2026-10-17 20:26 |
| `bodynorm/grid_search_results_temporal_features_bodynorm_chronos_shuffled_seed0.pkl` | 119.0 KB | `208144738e203ebb1ddbc402afb1bba6` | 2026-10-20 17:01 |
| `bodynorm/grid_seeds.log` | 11.6 KB | `728099866e64e3100290ea3a2963f3c9` | 2026-10-17 19:49 |
| `bodynorm/run2.commit` | 90 B | `b4397920fd9ad3a7b3d027bf598dcec1` | 2026-10-17 17:33 |
| `bodynorm/temporal_features_bodynorm.csv` | 25.2 MB | `699188e971daf9a3975ad138ba648811` | 2026-10-17 16:57 |
| `bodynorm/tsfel.log` | 33.1 KB | `e3ef17f9ff87519f48c5c5ea6a9140b4` | 2026-10-17 16:57 |
| `controls_summary/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-20 19:51 |
| `controls_summary/controls.commit` | 109 B | `7c0c3c974949f1e1c3017b04403f48f1` | 2026-10-20 19:51 |
| `controls_summary/controls.log` | 10.0 KB | `6df9121cdadeb81cfd1b7d0ae8ede56f` | 2026-10-20 19:51 |
| `controls_summary/controls_shuffled.csv` | 1.2 KB | `d1e6be384e69dffedbd8979269ac86d5` | 2026-10-20 19:51 |
| `controls_summary/probe_cls_shuffled.csv` | 425 B | `07a9a022736518eec325cd7176e28705` | 2026-10-20 19:51 |
| `dtw_pathnorm/dtw_all_pathnorm.log` | 1.4 KB | `31cf1c29ac4c7cda29bda487baad9ca1` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_all_pathnorm_pairs.csv` | 909.4 KB | `c31e4f9af2e28bcd90f466a6efbcc526` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_all_pathnorm_per_sign_matrix.csv` | 36.7 KB | `bddc2fb41bccd47e178b2e81f0a3e884` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_all_pathnorm_per_sign_summary.csv` | 15.4 KB | `18853fa64f3fe0c9dabc334e7fddac6d` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_hands_pathnorm.log` | 1.4 KB | `09da44c06c188dc956c6a904d54f76df` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_hands_pathnorm_pairs.csv` | 910.3 KB | `6259498c2d21b158af8f1e863f742b36` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_hands_pathnorm_per_sign_matrix.csv` | 36.8 KB | `f6ff3aacc9364880a5865310f06582c5` | 2026-10-20 15:13 |
| `dtw_pathnorm/dtw_hands_pathnorm_per_sign_summary.csv` | 15.4 KB | `562ab37bb78e9d994febc43f18bd6dd5` | 2026-10-20 15:14 |
| `dtw_signer/dtw_all_pathnorm_signer_level_all_signers.csv` | 395 B | `521c30eaa1b98b149305589fb0885955` | 2026-10-20 15:58 |
| `dtw_signer/dtw_all_pathnorm_signer_level_summary.csv` | 589 B | `dd2e03b86a3f95cacd7912f402891f6a` | 2026-10-20 15:58 |
| `dtw_signer/dtw_all_pathnorm_signer_level_without_V1.csv` | 318 B | `66052f038e617ac938665f29cb3070bd` | 2026-10-20 15:58 |
| `dtw_signer/dtw_all_signer_level_all_signers.csv` | 392 B | `129889053d37e6a30e70a5b161bf6c4d` | 2026-10-20 15:58 |
| `dtw_signer/dtw_all_signer_level_summary.csv` | 586 B | `015720633dff81160424aade401b7040` | 2026-10-20 15:58 |
| `dtw_signer/dtw_all_signer_level_without_V1.csv` | 316 B | `5330572c06a1ed5fafddfd5f1a938712` | 2026-10-20 15:58 |
| `dtw_signer/dtw_hands_signer_level_all_signers.csv` | 392 B | `efd58307402d06377384ef35f3881097` | 2026-10-20 15:58 |
| `dtw_signer/dtw_hands_signer_level_summary.csv` | 587 B | `72d4d3fef1d0cedfdfdc3c2323a51d89` | 2026-10-20 15:58 |
| `dtw_signer/dtw_hands_signer_level_without_V1.csv` | 318 B | `5a23a902365c6e796b65fcfb0f8e5e92` | 2026-10-20 15:58 |
| `dup_test/temporal_dupv1.csv` | 802.7 KB | `7e8fba3c7495f164d35c3b97b9346afd` | 2026-10-15 19:55 |
| `figures/fig_dtw_matrix.png` | 95.7 KB | `f155b5e84f99df75ab29db108261f629` | 2026-10-19 17:59 |
| `figures/fig_dtw_matrix.tiff` | 197.4 KB | `89346b088bc71b41f0cd0f11df0ca8b2` | 2026-10-19 17:59 |
| `figures/fig_importance.png` | 163.3 KB | `b2d96fb7abd5d042186c9c72f193c79d` | 2026-10-19 17:59 |
| `figures/fig_importance.tiff` | 247.1 KB | `3e48fb61ee75639f844ca79e8e449f34` | 2026-10-19 17:59 |
| `figures/fig_learning_curves.png` | 191.7 KB | `1aee41d4111da4f2ac0c195264dd7935` | 2026-10-19 17:59 |
| `figures/fig_learning_curves.tiff` | 278.3 KB | `9e2d1814f3b47fefbf2bd3a9f8ef0602` | 2026-10-19 17:59 |
| `figures/fig_loso_models.png` | 398.4 KB | `6bc9e208892d08a21407d9dd598ff009` | 2026-10-19 17:59 |
| `figures/fig_loso_models.tiff` | 497.5 KB | `044c7d147d71a047c292a7dfffbc0383` | 2026-10-19 17:59 |
| `figures/fig_loso_per_signer.png` | 89.8 KB | `e63cbaa55b98b07aad187dd1786b7c9d` | 2026-10-19 17:59 |
| `figures/fig_loso_per_signer.tiff` | 120.5 KB | `dc1d399b4b301643253e0ea976366606` | 2026-10-19 17:59 |
| `figures_final/fig_confusion_fusion.png` | 287.1 KB | `31194dd8d1d8c71ced86308cf65f0e0b` | 2026-10-28 23:46 |
| `figures_final/fig_confusion_fusion.tiff` | 533.4 KB | `1092f7abf591abc67c320fb8bf18c1b8` | 2026-10-28 23:46 |
| `figures_final/fig_dtw_matrix.png` | 95.7 KB | `f155b5e84f99df75ab29db108261f629` | 2026-10-28 23:46 |
| `figures_final/fig_dtw_matrix.tiff` | 197.4 KB | `89346b088bc71b41f0cd0f11df0ca8b2` | 2026-10-28 23:46 |
| `figures_final/fig_importance.png` | 163.3 KB | `b2d96fb7abd5d042186c9c72f193c79d` | 2026-10-28 23:46 |
| `figures_final/fig_importance.tiff` | 247.1 KB | `3e48fb61ee75639f844ca79e8e449f34` | 2026-10-28 23:46 |
| `figures_final/fig_importance_pose.png` | 65.9 KB | `ff24d3ed778af14ac94c91f30f5427d1` | 2026-10-28 23:46 |
| `figures_final/fig_importance_pose.tiff` | 136.2 KB | `f169e3008286e2b33846a0330cd1584d` | 2026-10-28 23:46 |
| `figures_final/fig_learning_curves.png` | 245.8 KB | `36021dc939a0d4de314c25510ef51ac9` | 2026-10-28 23:46 |
| `figures_final/fig_learning_curves.tiff` | 321.8 KB | `70726afebda0c0f3d61bb7e81228d659` | 2026-10-28 23:46 |
| `figures_final/fig_loso_models.png` | 488.9 KB | `ad9110d11780f4b0ca4d2353810b987f` | 2026-10-28 23:46 |
| `figures_final/fig_loso_models.tiff` | 602.2 KB | `44cac6ff875d9d1bdecb6a4dd3a9aa76` | 2026-10-28 23:46 |
| `figures_final/fig_loso_per_signer.png` | 96.6 KB | `a681080b512c29393e6f8aaa5378905d` | 2026-10-28 23:46 |
| `figures_final/fig_loso_per_signer.tiff` | 137.4 KB | `342982c56bf5d1ecb3c418e788650e8d` | 2026-10-28 23:46 |
| `figures_final/fig_per_sign_f1.png` | 255.9 KB | `e0ddf95113ac0ef5e14342dcbae358db` | 2026-10-28 23:46 |
| `figures_final/fig_per_sign_f1.tiff` | 349.8 KB | `94edec4ad94930fda27edf5cbb7196f3` | 2026-10-28 23:46 |
| `frames/general_db_f0.csv` | 144.6 MB | `59257694ec71b8f5b874d03c1e15e212` | 2026-10-15 19:34 |
| `frames/general_db_f16.csv` | 37.6 MB | `e9cedfa5f9c64f792aa89ff1fd9d6fed` | 2026-10-15 19:25 |
| `frames/general_db_f32.csv` | 75.3 MB | `83249ad5bef6a9ea9b845662f46eb8b6` | 2026-10-15 19:27 |
| `frames/general_db_f48.csv` | 113.0 MB | `6fe20c23c3e04d6cbdbb9cd451dfb370` | 2026-10-15 19:30 |
| `frames/general_db_lm_chronos_f0.csv` | 6.3 MB | `6c73ac3983af15b393e4fa10eb660319` | 2026-10-15 19:39 |
| `frames/general_db_lm_chronos_f16.csv` | 6.3 MB | `b0b7353dc603e8fea792109d69f2bb9d` | 2026-10-15 19:27 |
| `frames/general_db_lm_chronos_f32.csv` | 6.3 MB | `cf66ee50031d8cbdfaba06b5496e0cc6` | 2026-10-15 19:30 |
| `frames/general_db_lm_chronos_f48.csv` | 6.3 MB | `967617effea7094f68ce8e8c4f7705ac` | 2026-10-15 19:34 |
| `frames/temporal_features_f0.csv` | 25.8 MB | `124e18ba77006ed20a177b110a7cc33e` | 2026-10-15 19:35 |
| `frames/temporal_features_f16.csv` | 25.7 MB | `8bbf1f3b6161494fcf12a7daddc3b6d3` | 2026-10-15 19:26 |
| `frames/temporal_features_f32.csv` | 25.8 MB | `760f313746efde09c2ee40f96d43adfd` | 2026-10-15 19:28 |
| `frames/temporal_features_f48.csv` | 25.8 MB | `e25ca58c66c2f4558ce19130404f1114` | 2026-10-15 19:31 |
| `fusion/DONE_fuse` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 18:28 |
| `fusion/DONE_slowfast` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 14:51 |
| `fusion/DONE_spoter` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 02:55 |
| `fusion/commit_fuse.txt` | 101 B | `44c36749adc12bd95b8a1f50387a896f` | 2026-10-27 18:28 |
| `fusion/commit_slowfast.txt` | 96 B | `654d2c8ee23a6b94c657faa47c734eeb` | 2026-10-27 11:05 |
| `fusion/commit_spoter.txt` | 540 B | `c53abc0e3f4a4c6281e63953d4f3b582` | 2026-10-26 17:37 |
| `fusion/fuse.log` | 7.5 KB | `dbf87d9308e676e3958c8e7afd5b4459` | 2026-10-27 18:28 |
| `fusion/fuse_err.log` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 18:28 |
| `fusion/fuse_first.log` | 4.0 KB | `259faf55742e2ae826f52e11367fbaae` | 2026-10-27 14:52 |
| `fusion/fusion_runs.commit.txt` | 101 B | `44c36749adc12bd95b8a1f50387a896f` | 2026-10-27 18:28 |
| `fusion/fusion_runs.csv` | 9.2 KB | `1a6a6be8aba62ca2d339d3b2e5830ab8` | 2026-10-27 18:28 |
| `fusion/fusion_runs_summary.csv` | 1.9 KB | `2d30f50880cb5f750f3321bd151741d1` | 2026-10-27 18:28 |
| `fusion/importance_spoter_per_signer.csv` | 897 B | `500efa0f56af3e5be3758b86d2bcb758` | 2026-10-27 18:28 |
| `fusion/importance_spoter_runs.csv` | 4.6 KB | `590ad975e32ce405d129bf4abcf53d69` | 2026-10-27 18:28 |
| `fusion/importance_spoter_stability.csv` | 110 B | `7394ef101bfd2a8cec26db091a2e7e0a` | 2026-10-27 18:28 |
| `fusion/importance_spoter_summary.csv` | 572 B | `5aa589a2ad38b6afc62bc3e0cb002707` | 2026-10-27 18:28 |
| `fusion/retry_then_fuse.sh` | 940 B | `d70af92d792214a3833ec56af6346ff5` | 2026-10-26 17:40 |
| `fusion/slowfast.log` | 5.1 KB | `7ae86715cafa66f2576b4251a62de854` | 2026-10-27 14:51 |
| `fusion/slowfast_jobs.txt` | 952 B | `239579966ffc9b9c05a418d72dbedcc3` | 2026-10-27 11:05 |
| `fusion/spoter.log` | 2.6 KB | `d8d9912ef4df442e4b2d3cc8e82e39c9` | 2026-10-27 02:55 |
| `fusion/spoter_jobs.txt` | 2.8 KB | `443199c4e6c4e71984e02749bf5dfe89` | 2026-10-26 17:37 |
| `fusion/fused/fusion-8020-seed0-shuffled.json` | 4.1 KB | `d7ade5a52f8bbef2543437a3533a32f8` | 2026-10-27 18:28 |
| `fusion/fused/fusion-8020-seed0.json` | 4.2 KB | `1a82a2ad557497c1f7427bb5ac67b9d0` | 2026-10-27 18:28 |
| `fusion/fused/fusion-8020-seed1.json` | 4.2 KB | `c8234c1139afca1331551441fffbb9d6` | 2026-10-27 18:28 |
| `fusion/fused/fusion-8020-seed2.json` | 4.2 KB | `f6ec0182b5eac0d33d7325e95d40159e` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s0-seed0-shuffled.json` | 4.2 KB | `fbe7ccf9c42c73fd02c362f674b30fe9` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s0-seed0.json` | 4.2 KB | `6fbe93b86b4f682b915773a19d19531d` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s0-seed1.json` | 4.2 KB | `66eb14587bd3398d1126eb9eebab80fe` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s0-seed2.json` | 4.2 KB | `307dd0913d1a0a281217b9608633a80c` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s1-seed0.json` | 4.2 KB | `123c2c9780f913eac882e9cf9fc235ae` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s1-seed1.json` | 4.2 KB | `2ab7fe12edf1709f594b5f0e14f47eaf` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s1-seed2.json` | 4.2 KB | `56ea166e99dc846c2f6b84a746365579` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s2-seed0.json` | 4.1 KB | `b6fd75ec6465a096ecdd2aa903a7868c` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s2-seed1.json` | 4.1 KB | `7f932cb4ce960f8ac7e0df82e3a2b62a` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s2-seed2.json` | 4.1 KB | `b7487d8d78df6690fa80ae5c994871df` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s3-seed0.json` | 4.2 KB | `2144bf389b31648c0d6d6068c05cb9aa` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s3-seed1.json` | 4.2 KB | `c35314e4a0c657a7348ed9be593bb8ca` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s3-seed2.json` | 4.2 KB | `fb3bb03ccbae177e6f1218cdd3258863` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s4-seed0.json` | 4.2 KB | `0c91b1c07310e6621712e795577057ab` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s4-seed1.json` | 4.2 KB | `6f828daf5b95ec0739603e75e709cba1` | 2026-10-27 18:28 |
| `fusion/fused/fusion-loso-s4-seed2.json` | 4.2 KB | `4c1a541a7e3614e3a4b54de85a7076a2` | 2026-10-27 18:28 |
| `fusion/fused_first/fusion-8020-seed0-shuffled.json` | 4.1 KB | `9c000b9afe4407d6c88240a4cd5bf580` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-8020-seed0.json` | 4.2 KB | `bdb686e3bab04b6bc2fe2b61be0ec59d` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-8020-seed1.json` | 4.2 KB | `8224fb76ac162c7be89d4e8394473a68` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-8020-seed2.json` | 4.2 KB | `ee276b2577c0f86f166e1665cc52898c` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s0-seed0-shuffled.json` | 4.2 KB | `513e3873d9adec8f3f31126fd778ec09` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s0-seed0.json` | 4.2 KB | `cf12c29a2bafff2cf7996c3c7e0289ad` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s0-seed1.json` | 4.2 KB | `f20333d08586199113381367b545272f` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s0-seed2.json` | 4.2 KB | `6e285a1970334f08a2161195665f05ad` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s1-seed0.json` | 4.1 KB | `16f81ebaa0d1c420b466fc185e5a69c5` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s1-seed1.json` | 4.1 KB | `8971461681bdad4de4b6dc7a52c12063` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s1-seed2.json` | 4.1 KB | `c293dcd710ba9646de4d58db7ef9532f` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s2-seed0.json` | 4.1 KB | `d620fdfdbc6eb6245d545a69ea69b71d` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s2-seed1.json` | 4.1 KB | `b89e3cc02c364acc572707fbebb1c520` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s2-seed2.json` | 4.1 KB | `64047607be8e029e5ad40727f8641640` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s3-seed0.json` | 4.2 KB | `45e733fd541ffce008265e0c396590a7` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s3-seed1.json` | 4.2 KB | `39b7a197bb22eef54b3f58a0c053c8d0` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s3-seed2.json` | 4.2 KB | `3be6164c6a21a17e1bde922e19216200` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s4-seed0.json` | 4.1 KB | `19ee2cb32077f6de24315fe32e31ac69` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s4-seed1.json` | 4.2 KB | `9bfdd2d9415918b925e749f18dfa5369` | 2026-10-27 14:52 |
| `fusion/fused_first/fusion-loso-s4-seed2.json` | 4.2 KB | `27324d7d1b7755fa7e29f21c22010709` | 2026-10-27 14:52 |
| `fusion/logs/slowfast-8020-seed0-shuffled.log` | 1.2 KB | `bd3398918214545f4c5cb11f2473a415` | 2026-10-27 11:04 |
| `fusion/logs/slowfast-8020-seed0.log` | 1.2 KB | `1a7036aaedafe17e54066e9036a93d01` | 2026-10-26 21:49 |
| `fusion/logs/slowfast-8020-seed1.log` | 1.2 KB | `39cfc887e35637fc3e938308053ffad0` | 2026-10-27 03:32 |
| `fusion/logs/slowfast-8020-seed2.log` | 1.2 KB | `a60e826dc8f32b8312842e85b5d44686` | 2026-10-27 09:12 |
| `fusion/logs/slowfast-loso-s0-seed0-shuffled.log` | 1.2 KB | `f964271f7aaaa99cdfccb4bfd84b216a` | 2026-10-27 09:15 |
| `fusion/logs/slowfast-loso-s0-seed0.log` | 1.2 KB | `aaf9325989c927bafd08245d92604948` | 2026-10-27 12:59 |
| `fusion/logs/slowfast-loso-s0-seed1.log` | 1.2 KB | `89b1d154c5fa138a0c5dc31d33ee1a60` | 2026-10-26 21:53 |
| `fusion/logs/slowfast-loso-s0-seed2.log` | 1.2 KB | `64bd73ac294341df943754ded7bc71c8` | 2026-10-27 03:33 |
| `fusion/logs/slowfast-loso-s1-seed0.log` | 1.2 KB | `8e7ecc9a8f90c2fbe507446f3ef55657` | 2026-10-27 12:59 |
| `fusion/logs/slowfast-loso-s1-seed1.log` | 1.2 KB | `7eba22c5d8563543e1e945cf452942eb` | 2026-10-26 23:43 |
| `fusion/logs/slowfast-loso-s1-seed2.log` | 1.2 KB | `47b2f6ba43492690e32e3d65a986bc5c` | 2026-10-27 05:27 |
| `fusion/logs/slowfast-loso-s2-seed0.log` | 1.2 KB | `551fe8ce80f1f557d2363eed13ccf20c` | 2026-10-27 14:51 |
| `fusion/logs/slowfast-loso-s2-seed1.log` | 1.2 KB | `5c9fc1e83a220cef8b7f6cf500472a50` | 2026-10-26 23:47 |
| `fusion/logs/slowfast-loso-s2-seed2.log` | 1.2 KB | `e59138289c5df10464e510b29d64a5c8` | 2026-10-27 05:26 |
| `fusion/logs/slowfast-loso-s3-seed0.log` | 1.2 KB | `1eedf76491993ac811bf17afa8c4e8bd` | 2026-10-26 19:54 |
| `fusion/logs/slowfast-loso-s3-seed1.log` | 1.2 KB | `154613f05c88350061d9e0345e8a882c` | 2026-10-27 01:38 |
| `fusion/logs/slowfast-loso-s3-seed2.log` | 1.2 KB | `937622b4ff9803c97a459b92f70e592b` | 2026-10-27 07:19 |
| `fusion/logs/slowfast-loso-s4-seed0.log` | 1.2 KB | `83f08393ac1c0ba219d8d8723fe9e180` | 2026-10-26 20:00 |
| `fusion/logs/slowfast-loso-s4-seed1.log` | 1.2 KB | `e3c641db9164255484a49f533f935d63` | 2026-10-27 01:40 |
| `fusion/logs/slowfast-loso-s4-seed2.log` | 1.2 KB | `bb969673213584c1745ff6579c6d7b7a` | 2026-10-27 07:21 |
| `fusion/logs/spoter-8020-seed0-shuffled.log` | 108 B | `b0d1f9f943ae6ed95c2308d496ef8bce` | 2026-10-27 02:55 |
| `fusion/logs/spoter-8020-seed0.log` | 99 B | `c9c832e07a32c5ff24e43dbe45204063` | 2026-10-26 20:03 |
| `fusion/logs/spoter-8020-seed1.log` | 99 B | `e64f87b2399e9723922d73efd64df359` | 2026-10-26 22:30 |
| `fusion/logs/spoter-8020-seed2.log` | 99 B | `a0819f7ef76be5a06dce7cb2248050a4` | 2026-10-27 01:02 |
| `fusion/logs/spoter-loso-s0-seed0-shuffled.log` | 111 B | `6d2b39e50ee7ef6cd0a6318669b196f6` | 2026-10-27 02:51 |
| `fusion/logs/spoter-loso-s0-seed0.log` | 102 B | `1a966f2c9d669244d32a7066c984dc77` | 2026-10-26 20:13 |
| `fusion/logs/spoter-loso-s0-seed1.log` | 102 B | `603c27d7f5231e820e859b8ff7d8e7f0` | 2026-10-26 22:28 |
| `fusion/logs/spoter-loso-s0-seed2.log` | 102 B | `082d307d6f5d7259825f1924ef8b6beb` | 2026-10-27 00:57 |
| `fusion/logs/spoter-loso-s1-seed0.log` | 102 B | `e985e5ebb006032e64717dc8a035d6b1` | 2026-10-26 20:16 |
| `fusion/logs/spoter-loso-s1-seed1.log` | 102 B | `aeb0385c47b00fb38f991d6b68fc51f8` | 2026-10-26 22:36 |
| `fusion/logs/spoter-loso-s1-seed2.log` | 102 B | `7ee9a2b0d48d44d3f0227df5bf061d1a` | 2026-10-27 00:59 |
| `fusion/logs/spoter-loso-s2-seed0.log` | 102 B | `efa2146f5106b0567d80ebf091f5bd7f` | 2026-10-26 20:13 |
| `fusion/logs/spoter-loso-s2-seed1.log` | 102 B | `5619ae4e002fa23fe9fd01d9e222dfac` | 2026-10-26 22:40 |
| `fusion/logs/spoter-loso-s2-seed2.log` | 102 B | `a50ed590ed3b919c190f52b1372a7248` | 2026-10-27 01:08 |
| `fusion/logs/spoter-loso-s3-seed0.log` | 102 B | `c16bd101fc240a4704618a1b7109165b` | 2026-10-26 20:14 |
| `fusion/logs/spoter-loso-s3-seed1.log` | 102 B | `1c87e97878cc3e21d09af22a45d3af08` | 2026-10-26 22:42 |
| `fusion/logs/spoter-loso-s3-seed2.log` | 102 B | `fb1ec61fbd8add4188ac0fa5ce37d60c` | 2026-10-27 01:07 |
| `fusion/logs/spoter-loso-s4-seed0.log` | 102 B | `982f5fbf01ed074b1d66da6257f44eff` | 2026-10-26 20:11 |
| `fusion/logs/spoter-loso-s4-seed1.log` | 102 B | `77508785f08b65a6118a989eaae2b9cd` | 2026-10-26 22:38 |
| `fusion/logs/spoter-loso-s4-seed2.log` | 102 B | `4ca0215a2a69d1cab33bc60d3151015f` | 2026-10-27 01:03 |
| `fusion/slowfast/slowfast-8020-seed0-shuffled.json` | 201.3 KB | `dbb27e08a748f1b5500124bd569d8bb5` | 2026-10-27 11:04 |
| `fusion/slowfast/slowfast-8020-seed0.json` | 97.4 KB | `88083cfb0ea710c105eec189f612259b` | 2026-10-26 21:49 |
| `fusion/slowfast/slowfast-8020-seed1.json` | 94.2 KB | `fd5f414b8d47095f5d0e0d00096fcf74` | 2026-10-27 03:32 |
| `fusion/slowfast/slowfast-8020-seed2.json` | 98.9 KB | `5b14df05bd6065a605e1d8a56d12ea7b` | 2026-10-27 09:12 |
| `fusion/slowfast/slowfast-loso-s0-seed0-shuffled.json` | 201.7 KB | `b7573d910d574c223c2060ab7c11e0fd` | 2026-10-27 09:15 |
| `fusion/slowfast/slowfast-loso-s0-seed0.json` | 141.0 KB | `35c59c14b9b33df117ee44306559e7bb` | 2026-10-27 12:59 |
| `fusion/slowfast/slowfast-loso-s0-seed1.json` | 146.6 KB | `cbe3204440cdbb4e59e4179f402110ad` | 2026-10-26 21:53 |
| `fusion/slowfast/slowfast-loso-s0-seed2.json` | 142.0 KB | `a05d573843a082c4db2cca78fea90265` | 2026-10-27 03:33 |
| `fusion/slowfast/slowfast-loso-s1-seed0.json` | 123.9 KB | `7f473a936827a1465c6697fc4189ba11` | 2026-10-27 12:59 |
| `fusion/slowfast/slowfast-loso-s1-seed1.json` | 128.5 KB | `2f9362ab9c1ec2e8ebd4e7af8073e58a` | 2026-10-26 23:43 |
| `fusion/slowfast/slowfast-loso-s1-seed2.json` | 133.5 KB | `ddf9df453f03e3d78ad81bc363f913d8` | 2026-10-27 05:27 |
| `fusion/slowfast/slowfast-loso-s2-seed0.json` | 118.7 KB | `f0738951306ef0d9ecdb11fd17d649fe` | 2026-10-27 14:51 |
| `fusion/slowfast/slowfast-loso-s2-seed1.json` | 118.3 KB | `9025d2c36835ffa383cfe45aba6d1248` | 2026-10-26 23:47 |
| `fusion/slowfast/slowfast-loso-s2-seed2.json` | 126.9 KB | `3c5a913847a7c4dc319d15736ac65794` | 2026-10-27 05:26 |
| `fusion/slowfast/slowfast-loso-s3-seed0.json` | 105.8 KB | `daaed17ffb4ae9c048961efb6779bce1` | 2026-10-26 19:54 |
| `fusion/slowfast/slowfast-loso-s3-seed1.json` | 110.4 KB | `fed7f59399f4d671895182ed874810ab` | 2026-10-27 01:38 |
| `fusion/slowfast/slowfast-loso-s3-seed2.json` | 109.4 KB | `bcf3ec1f5918794e4c3ae9dc39faed14` | 2026-10-27 07:19 |
| `fusion/slowfast/slowfast-loso-s4-seed0.json` | 106.4 KB | `dbc7c0bc9f07e88a033dfac4e63bd207` | 2026-10-26 20:00 |
| `fusion/slowfast/slowfast-loso-s4-seed1.json` | 110.4 KB | `e80d601cdfd5189804ccf5dc7c715ba6` | 2026-10-27 01:40 |
| `fusion/slowfast/slowfast-loso-s4-seed2.json` | 121.5 KB | `472e0907316ba40491a6d7d5b61706cf` | 2026-10-27 07:21 |
| `fusion/spoter/spoter-8020-seed0-shuffled.json` | 233.3 KB | `77f118d6d17c25d08499884c78a61cb1` | 2026-10-27 02:55 |
| `fusion/spoter/spoter-8020-seed0.json` | 240.0 KB | `8b383181878ac9e5de6f08289e9aebc3` | 2026-10-26 20:03 |
| `fusion/spoter/spoter-8020-seed1.json` | 240.3 KB | `52425d5285c9ac6d842b4d6512960dc6` | 2026-10-26 22:30 |
| `fusion/spoter/spoter-8020-seed2.json` | 240.2 KB | `b5f45021395995c3673da929a95a27b5` | 2026-10-27 01:02 |
| `fusion/spoter/spoter-loso-s0-seed0-shuffled.json` | 231.1 KB | `cefec7d5808e8b31c8eb4c8ee22d45de` | 2026-10-27 02:51 |
| `fusion/spoter/spoter-loso-s0-seed0.json` | 239.1 KB | `72702bc8c1da2233c9e7184f3649deca` | 2026-10-26 20:13 |
| `fusion/spoter/spoter-loso-s0-seed1.json` | 239.5 KB | `ebf6074786f617796f08aa7b1556d85e` | 2026-10-26 22:28 |
| `fusion/spoter/spoter-loso-s0-seed2.json` | 238.9 KB | `ac31fbabfbd4e149d9740aa49f221285` | 2026-10-27 00:57 |
| `fusion/spoter/spoter-loso-s1-seed0.json` | 238.6 KB | `3b4e2c62f6361850ae027feca864a2a3` | 2026-10-26 20:16 |
| `fusion/spoter/spoter-loso-s1-seed1.json` | 238.5 KB | `d13a12d7d35580bee37e8625cc01b3e2` | 2026-10-26 22:36 |
| `fusion/spoter/spoter-loso-s1-seed2.json` | 238.8 KB | `a5aff042365e319ac3a42e7d333be09f` | 2026-10-27 00:59 |
| `fusion/spoter/spoter-loso-s2-seed0.json` | 237.7 KB | `cfe50ce1625b6820fb8e2f9748d63b63` | 2026-10-26 20:13 |
| `fusion/spoter/spoter-loso-s2-seed1.json` | 238.1 KB | `dfe9cdfe38ec89fdd54ca36c9a7cb6dd` | 2026-10-26 22:40 |
| `fusion/spoter/spoter-loso-s2-seed2.json` | 238.0 KB | `8953b630d2c9c24ce50a2ac70ac35e5d` | 2026-10-27 01:08 |
| `fusion/spoter/spoter-loso-s3-seed0.json` | 240.0 KB | `1dace8113c40132dd88667a6ac56c0f7` | 2026-10-26 20:14 |
| `fusion/spoter/spoter-loso-s3-seed1.json` | 240.4 KB | `fe6953af28d1944610b54b181423795a` | 2026-10-26 22:42 |
| `fusion/spoter/spoter-loso-s3-seed2.json` | 240.3 KB | `f32d981e8f29e18b850d3219344f1912` | 2026-10-27 01:07 |
| `fusion/spoter/spoter-loso-s4-seed0.json` | 240.7 KB | `c96593dd1c7a1feee3640f21a0bd853d` | 2026-10-26 20:11 |
| `fusion/spoter/spoter-loso-s4-seed1.json` | 240.8 KB | `8e7830aab13984520fc1303c790631e3` | 2026-10-26 22:38 |
| `fusion/spoter/spoter-loso-s4-seed2.json` | 240.6 KB | `761ae634bb54c458856b1e998934ae9e` | 2026-10-27 01:03 |
| `fusion_smoke/slowfast.log` | 140 B | `6d8b9f045a9a62313f04f4030ff572b8` | 2026-10-26 17:37 |
| `fusion_smoke/spoter.log` | 100 B | `24febf36ec6d2c518ebeb8c7ecfe2415` | 2026-10-26 17:27 |
| `fusion_smoke/fused/fusion-loso-s1-seed0.json` | 4.2 KB | `83e2982ae605f18bad534bfeb5f58b10` | 2026-10-26 17:37 |
| `fusion_smoke/slowfast/slowfast-loso-s1-seed0.json` | 215.3 KB | `20878ea5cb4f194b21dd237b192d7408` | 2026-10-26 17:37 |
| `fusion_smoke/spoter/spoter-loso-s1-seed0.json` | 215.8 KB | `57d2e7b58c1dd74892a442843c5b172d` | 2026-10-26 17:27 |
| `importance_sequence/pose/DONE_pose` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-23 19:27 |
| `importance_sequence/pose/commit.txt` | 386 B | `dd68075a51485e14ebe415fb4e965068` | 2026-10-23 17:16 |
| `importance_sequence/pose/importance_pose_per_signer.csv` | 17.6 KB | `2023b0edb49fbdb2b7be4f7f6aabb84c` | 2026-10-23 19:27 |
| `importance_sequence/pose/importance_pose_runs.csv` | 161.5 KB | `caa5f170f7f55ebb297148fe831b6215` | 2026-10-23 19:27 |
| `importance_sequence/pose/importance_pose_stability.csv` | 262 B | `6b5ee589329d94208decfa572374a687` | 2026-10-23 19:27 |
| `importance_sequence/pose/importance_pose_summary.csv` | 11.8 KB | `d2173c6553d3a91a6a0597335b9b8d42` | 2026-10-23 19:27 |
| `importance_sequence/pose/run.log` | 4.8 KB | `077d4e6c5995f48c76463b219f1ac113` | 2026-10-23 19:27 |
| `importance_sequence/pose/logs/pose-loso-s0-seed0.log` | 339 B | `f9e791377c019e7a0d9e2f28135cf37e` | 2026-10-23 17:21 |
| `importance_sequence/pose/logs/pose-loso-s0-seed1.log` | 339 B | `0c3de0ecb8e97f1ec1ddef16d6518863` | 2026-10-23 17:48 |
| `importance_sequence/pose/logs/pose-loso-s0-seed2.log` | 339 B | `129b441ee8fcc224fff99e93f1cc2a7c` | 2026-10-23 18:14 |
| `importance_sequence/pose/logs/pose-loso-s0-seed3.log` | 339 B | `7d95355830ee65b0afeb33f4c70e3055` | 2026-10-23 18:40 |
| `importance_sequence/pose/logs/pose-loso-s0-seed4.log` | 339 B | `278a47c20a27d9612dc4bff125693ac6` | 2026-10-23 19:06 |
| `importance_sequence/pose/logs/pose-loso-s1-seed0.log` | 339 B | `b90b164581d22a6767aa38284c80cc1d` | 2026-10-23 17:27 |
| `importance_sequence/pose/logs/pose-loso-s1-seed1.log` | 339 B | `ce88be41213a5b2c0a2ee92e475f7212` | 2026-10-23 17:53 |
| `importance_sequence/pose/logs/pose-loso-s1-seed2.log` | 339 B | `fc0e8cc9aae4985b5ee4d7ab159b4bc3` | 2026-10-23 18:19 |
| `importance_sequence/pose/logs/pose-loso-s1-seed3.log` | 339 B | `ad94ab167aca4c6439796ab747287969` | 2026-10-23 18:45 |
| `importance_sequence/pose/logs/pose-loso-s1-seed4.log` | 339 B | `14cbc27faf9a03459812d94e68511884` | 2026-10-23 19:12 |
| `importance_sequence/pose/logs/pose-loso-s2-seed0.log` | 339 B | `5ec0471e11e0255eef6fbe44e59308b8` | 2026-10-23 17:32 |
| `importance_sequence/pose/logs/pose-loso-s2-seed1.log` | 339 B | `5a6fd1899a55e62558c635a4c96d3def` | 2026-10-23 17:58 |
| `importance_sequence/pose/logs/pose-loso-s2-seed2.log` | 339 B | `7e5b4400be86297f495fb15f06ffb171` | 2026-10-23 18:24 |
| `importance_sequence/pose/logs/pose-loso-s2-seed3.log` | 339 B | `ab4df8ae623346839d6b892af7a1182a` | 2026-10-23 18:51 |
| `importance_sequence/pose/logs/pose-loso-s2-seed4.log` | 339 B | `d98cd5f1ef8805539bf2e54675016edd` | 2026-10-23 19:17 |
| `importance_sequence/pose/logs/pose-loso-s3-seed0.log` | 339 B | `6cbe393d9b35d97eefbbd224be2b2ba5` | 2026-10-23 17:37 |
| `importance_sequence/pose/logs/pose-loso-s3-seed1.log` | 339 B | `8b3a7620714a5bde5203890664e850a4` | 2026-10-23 18:04 |
| `importance_sequence/pose/logs/pose-loso-s3-seed2.log` | 339 B | `39b052b3cbfc4492da1ae8c8d1689f4c` | 2026-10-23 18:30 |
| `importance_sequence/pose/logs/pose-loso-s3-seed3.log` | 339 B | `264c6bf8b9bca45e6e878e7c995fe5e5` | 2026-10-23 18:56 |
| `importance_sequence/pose/logs/pose-loso-s3-seed4.log` | 339 B | `c9bcf0a878b1cc48e239bdf36ccbaa00` | 2026-10-23 19:22 |
| `importance_sequence/pose/logs/pose-loso-s4-seed0.log` | 339 B | `f40bb7969bdcaae35ae5a0a9544810ed` | 2026-10-23 17:43 |
| `importance_sequence/pose/logs/pose-loso-s4-seed1.log` | 339 B | `219908de4256cd682c3fc8b7c881b7ea` | 2026-10-23 18:09 |
| `importance_sequence/pose/logs/pose-loso-s4-seed2.log` | 339 B | `ac98eed7bd52001c50e7a19759ef8326` | 2026-10-23 18:35 |
| `importance_sequence/pose/logs/pose-loso-s4-seed3.log` | 339 B | `cdaa038abfb574c892dda36feb5b695a` | 2026-10-23 19:01 |
| `importance_sequence/pose/logs/pose-loso-s4-seed4.log` | 339 B | `e77e0761985ff878d8843ff97483ee29` | 2026-10-23 19:27 |
| `importance_sequence/pose/runs/pose-loso-s0-seed0.json` | 20.6 KB | `372228ade28623182b0fa38879d76945` | 2026-10-23 17:21 |
| `importance_sequence/pose/runs/pose-loso-s0-seed1.json` | 20.6 KB | `fd81e4ad9df070e2edef5517f1ca2baf` | 2026-10-23 17:48 |
| `importance_sequence/pose/runs/pose-loso-s0-seed2.json` | 20.6 KB | `bd6cf8c032ff5a2bc6f7236d4d1af0f6` | 2026-10-23 18:14 |
| `importance_sequence/pose/runs/pose-loso-s0-seed3.json` | 20.6 KB | `54676994e1dea921f89c825997052c9a` | 2026-10-23 18:40 |
| `importance_sequence/pose/runs/pose-loso-s0-seed4.json` | 20.6 KB | `4e4cbff35b0bf2d8a8febb4f80bbb9cd` | 2026-10-23 19:06 |
| `importance_sequence/pose/runs/pose-loso-s1-seed0.json` | 20.6 KB | `ef21c7ee7a2e0a7c0f92e703d3204d42` | 2026-10-23 17:27 |
| `importance_sequence/pose/runs/pose-loso-s1-seed1.json` | 20.6 KB | `14eb321f11078cf7fd90dcd71cf16b59` | 2026-10-23 17:53 |
| `importance_sequence/pose/runs/pose-loso-s1-seed2.json` | 20.7 KB | `02f5ddee2bd0c7bd79a84e100de8a046` | 2026-10-23 18:19 |
| `importance_sequence/pose/runs/pose-loso-s1-seed3.json` | 20.6 KB | `78ea7bb5257170543cc4877c986cbcdf` | 2026-10-23 18:45 |
| `importance_sequence/pose/runs/pose-loso-s1-seed4.json` | 20.6 KB | `cec874a5fbda3a20c9e0e06c05c4c217` | 2026-10-23 19:12 |
| `importance_sequence/pose/runs/pose-loso-s2-seed0.json` | 20.6 KB | `30ab3279569f3b4547c7cae562da5bad` | 2026-10-23 17:32 |
| `importance_sequence/pose/runs/pose-loso-s2-seed1.json` | 20.6 KB | `6358088c405c53f9229867f23b8cf092` | 2026-10-23 17:58 |
| `importance_sequence/pose/runs/pose-loso-s2-seed2.json` | 20.5 KB | `0a8486de3f42499b0327bc5acaa4b816` | 2026-10-23 18:24 |
| `importance_sequence/pose/runs/pose-loso-s2-seed3.json` | 20.6 KB | `d2c01409faf2e129a7e14943f6d33647` | 2026-10-23 18:51 |
| `importance_sequence/pose/runs/pose-loso-s2-seed4.json` | 20.6 KB | `2ea180c1896dc49bfe16de6713018c6b` | 2026-10-23 19:17 |
| `importance_sequence/pose/runs/pose-loso-s3-seed0.json` | 20.6 KB | `69264348d25b741b801b5840321006d3` | 2026-10-23 17:37 |
| `importance_sequence/pose/runs/pose-loso-s3-seed1.json` | 20.6 KB | `71cec5d07eb2d2662f3b0f15d665b2dc` | 2026-10-23 18:04 |
| `importance_sequence/pose/runs/pose-loso-s3-seed2.json` | 20.6 KB | `fa0b0dc636fb8440e7983d77dd9de62e` | 2026-10-23 18:30 |
| `importance_sequence/pose/runs/pose-loso-s3-seed3.json` | 20.6 KB | `80dce0f5b265cfcf76fcaabb772b40a1` | 2026-10-23 18:56 |
| `importance_sequence/pose/runs/pose-loso-s3-seed4.json` | 20.6 KB | `de050ea24f2518cc2e4a2c6c7fa92020` | 2026-10-23 19:22 |
| `importance_sequence/pose/runs/pose-loso-s4-seed0.json` | 20.5 KB | `43d03906a56d898d8964466ae5a2b7e8` | 2026-10-23 17:43 |
| `importance_sequence/pose/runs/pose-loso-s4-seed1.json` | 20.6 KB | `795049cf7a42da4cea00ab4aa947455a` | 2026-10-23 18:09 |
| `importance_sequence/pose/runs/pose-loso-s4-seed2.json` | 20.6 KB | `d0095e08115d2c9b31e1017516561562` | 2026-10-23 18:35 |
| `importance_sequence/pose/runs/pose-loso-s4-seed3.json` | 20.5 KB | `6814a6f3e662903bd77d5a10e9e4b2fc` | 2026-10-23 19:01 |
| `importance_sequence/pose/runs/pose-loso-s4-seed4.json` | 20.6 KB | `4d9eaeba35c521420e6a0fb495c8ea97` | 2026-10-23 19:27 |
| `importance_sequence/pose_subregion/DONE_pose` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/commit.txt` | 369 B | `27b133b0c4ee17584ee57d8b484c14e8` | 2026-10-26 13:51 |
| `importance_sequence/pose_subregion/importance_pose_per_signer.csv` | 5.9 KB | `d102869e285b1e4fd86486b1ca6a2fd9` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/importance_pose_runs.csv` | 51.0 KB | `5a7abcdf000c18e31404832fd6d10036` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/importance_pose_stability.csv` | 268 B | `638bb8d1ebafd11f0e94b74bb5c6732d` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/importance_pose_summary.csv` | 3.6 KB | `2d701acee371b5e6e00ada1ea39b9781` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/run.log` | 4.8 KB | `5046b484f88b4365ffe91a67a641edeb` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed0.log` | 339 B | `08d23c79645d992ae66ee731e0159ef3` | 2026-10-26 13:55 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed1.log` | 339 B | `4ef4d7673e6048fc7d8cc523107e43f3` | 2026-10-26 14:10 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed2.log` | 339 B | `9d1025c0b47006c7a6cdc9daf034bc20` | 2026-10-26 14:26 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed3.log` | 339 B | `4fc52171302d89b1f9378d1f5f35df65` | 2026-10-26 14:41 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed4.log` | 339 B | `aca24b4c326588433cf311f1933bfedd` | 2026-10-26 14:57 |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed0.log` | 339 B | `6ecbe5f03c3d2c64209d916bdd1773df` | 2026-10-26 13:58 |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed1.log` | 339 B | `0886216b6b2256da9bcbef00227dd68c` | 2026-10-26 14:14 |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed2.log` | 339 B | `cc129e785510f9bfbcdfb306be2c3c05` | 2026-10-26 14:29 |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed3.log` | 339 B | `286f2bf827b6d27f7cec28870659efb4` | 2026-10-26 14:44 |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed4.log` | 339 B | `c625216c0bd903723b313368abe71c5b` | 2026-10-26 14:59 |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed0.log` | 339 B | `5d60883db0cca40be56b298eab9a747a` | 2026-10-26 14:01 |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed1.log` | 339 B | `56fc9713647f2d67cb565f1761b81ae0` | 2026-10-26 14:17 |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed2.log` | 339 B | `5b6534e9dec26e84a8807358d5f1294d` | 2026-10-26 14:32 |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed3.log` | 339 B | `2dcecbb0d985ff1ff5f9b1b53a7256cd` | 2026-10-26 14:47 |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed4.log` | 339 B | `2cfee61e661364adaf5ff2823ddea528` | 2026-10-26 15:02 |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed0.log` | 339 B | `6a5707de11b1d822bef4dc26e044829d` | 2026-10-26 14:04 |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed1.log` | 339 B | `c5657d2c582f3bb9095d3bc25f684a73` | 2026-10-26 14:20 |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed2.log` | 339 B | `58b66693d4169267e276a7722bc0d615` | 2026-10-26 14:35 |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed3.log` | 339 B | `7647725ce762516f8699048f6d7b9217` | 2026-10-26 14:50 |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed4.log` | 339 B | `155d0a1b6c81bb2ae6385ec9af51510b` | 2026-10-26 15:05 |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed0.log` | 339 B | `f3015b265874155c3dcacaf8d164f6c8` | 2026-10-26 14:07 |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed1.log` | 339 B | `3a716437bdf6473f282081a5f51ca538` | 2026-10-26 14:23 |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed2.log` | 339 B | `ac392a3328bfe3a3f0947e4380b0aed8` | 2026-10-26 14:38 |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed3.log` | 339 B | `ff728de000a53bd0afeba09f7db19a33` | 2026-10-26 14:53 |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed4.log` | 339 B | `7986d6e7867d40c2d5a3877467c126de` | 2026-10-26 15:08 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed0.json` | 13.0 KB | `0f6fe86b50f8a0829eed9d8aecc581e1` | 2026-10-26 13:55 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed1.json` | 13.0 KB | `0d1bdb48e1aac0192ea15ffff48c596f` | 2026-10-26 14:10 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed2.json` | 13.0 KB | `0f071371f806a227835697c2100e54f4` | 2026-10-26 14:26 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed3.json` | 13.0 KB | `05195001980d5b43360f8f9cd5ed6ae7` | 2026-10-26 14:41 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed4.json` | 12.9 KB | `5093d1afc87be6a37eb47661612e635f` | 2026-10-26 14:57 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed0.json` | 13.0 KB | `b04eb3106bff3a1c470833a00526f186` | 2026-10-26 13:58 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed1.json` | 13.0 KB | `1643c3672a004e6ddf4e81280059e28e` | 2026-10-26 14:14 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed2.json` | 13.0 KB | `c32be6e952c1182eb9a06f2a8599dfe5` | 2026-10-26 14:29 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed3.json` | 13.0 KB | `78c55bd689c211b8228fdd65b36c529a` | 2026-10-26 14:44 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed4.json` | 13.0 KB | `d563ba13afc29ba0b9663c5a7dae776d` | 2026-10-26 14:59 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed0.json` | 12.9 KB | `5efb02024c578c89b57c8783b5c154a3` | 2026-10-26 14:01 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed1.json` | 12.9 KB | `30a998bc960acacd6aae29d1539ea556` | 2026-10-26 14:17 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed2.json` | 12.9 KB | `bdcf9ad7a6b97abf0d278c7b87529161` | 2026-10-26 14:32 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed3.json` | 13.0 KB | `6b0bbb853fee7909829b74f95643ec90` | 2026-10-26 14:47 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed4.json` | 12.9 KB | `1b7e93b23bac4c7c92a0e1b97b5f33f8` | 2026-10-26 15:02 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed0.json` | 12.9 KB | `884220d76fc0342eb8de77746b69f323` | 2026-10-26 14:04 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed1.json` | 12.9 KB | `b9c184f326dc5497bb46500e687c2a91` | 2026-10-26 14:20 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed2.json` | 12.9 KB | `aa578b6c73eedf7ff5194234ed9e66bf` | 2026-10-26 14:35 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed3.json` | 12.9 KB | `a231c15a70c6d93579b10bd78ba64ccc` | 2026-10-26 14:50 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed4.json` | 13.0 KB | `63ccf2c2a506fbbc4cc4ebd748f88b6e` | 2026-10-26 15:05 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed0.json` | 12.9 KB | `909cd5c5c9f1e3cde8bf9d6defac19a0` | 2026-10-26 14:07 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed1.json` | 13.0 KB | `6aaf8b07bcfba8321254d6b7d9961af8` | 2026-10-26 14:23 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed2.json` | 13.0 KB | `bc9097a895914725e8dd11081386d380` | 2026-10-26 14:38 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed3.json` | 13.0 KB | `9663012a7d6bd016f9af871b54d11432` | 2026-10-26 14:53 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed4.json` | 12.9 KB | `ca832f73e3c8f52b3524fe8eec0899ac` | 2026-10-26 15:08 |
| `importance_sequence/stgcn/DONE_stgcn` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/commit.txt` | 386 B | `dd68075a51485e14ebe415fb4e965068` | 2026-10-23 17:24 |
| `importance_sequence/stgcn/importance_stgcn_per_signer.csv` | 18.1 KB | `06870542d3f78de5826578e38511edd8` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/importance_stgcn_runs.csv` | 165.0 KB | `1b2badddc4c5d5e119b37c8599e03996` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/importance_stgcn_stability.csv` | 263 B | `aa678c31a034c65938b862c5dd33f5db` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/importance_stgcn_summary.csv` | 12.2 KB | `848f9080a4064624e85288dd2ed8b7b9` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/run.log` | 6.2 KB | `84565cfe5dc18dce45e15bf1305f1ab3` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed0.log` | 122 B | `7bd2babf7c6d2eacee80b2856ad0a6a0` | 2026-10-24 11:21 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed1.log` | 122 B | `e765055c8741931114aa044e9a52676a` | 2026-10-24 11:35 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed2.log` | 122 B | `889bf6f24914c87836ac643dd5499819` | 2026-10-24 11:49 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed3.log` | 122 B | `2d687f55fe4b251a3f71f4c8a220df90` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed4.log` | 122 B | `c259413060ff14f033863b0b23575799` | 2026-10-24 12:25 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed0.log` | 122 B | `e08e3063a4f5f691afa484ccb45eb7ab` | 2026-10-24 11:22 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed1.log` | 122 B | `cdaf71d8971201b53e8cd0e944f83ae4` | 2026-10-24 11:36 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed2.log` | 122 B | `26d5d43c43996a5af7bdfa618cebaed8` | 2026-10-24 11:49 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed3.log` | 122 B | `e0aa8ef0dfc2726a58a77b15025c0297` | 2026-10-24 12:12 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed4.log` | 122 B | `cb85d7fa9cd3635c08e1ea6746e555f0` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed0.log` | 122 B | `79e532e14c32440ae5edf61938fa837c` | 2026-10-24 11:23 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed1.log` | 122 B | `eaccee72336b374e07aedf11d2817631` | 2026-10-24 11:36 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed2.log` | 122 B | `63e3a58178fce5cabd1d19a1641c524d` | 2026-10-24 12:00 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed3.log` | 122 B | `29cf21d311f72411084271b5592e6b9d` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed4.log` | 122 B | `6e8871338b2d3e0d6850d4da073952c6` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed0.log` | 122 B | `782d1ffed356e9173d207bab3b094251` | 2026-10-24 11:23 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed1.log` | 122 B | `033faf86409b1a6d25dac41e9459fe14` | 2026-10-24 11:47 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed2.log` | 122 B | `3ecef520ecc85fab63e0d867b3a17876` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed3.log` | 122 B | `18a99dc58a489c7d9dca1684e65f9832` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed4.log` | 122 B | `41027470848397945fc25e84c2c5ff82` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed0.log` | 122 B | `fcf42fd5c9e5cd7b4c3dc1765c41f0e7` | 2026-10-24 11:34 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed1.log` | 122 B | `1c68bf9274655675a015bb91c54fd933` | 2026-10-24 11:48 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed2.log` | 122 B | `bca02271cb7a9fc4a1e2168362f81319` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed3.log` | 122 B | `8b2408950a00e01e6b1b4c270d1f39b6` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed4.log` | 122 B | `f68765da3f8603d3d97a89ae4aa3c010` | 2026-10-24 12:38 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed0.json` | 28.3 KB | `d36e072c1d66d68ec06f6d956cf7b8f3` | 2026-10-24 11:21 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed1.json` | 28.3 KB | `64f3e6555dfa1fb10f2481379a6aee49` | 2026-10-24 11:35 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed2.json` | 28.4 KB | `8fcf9710ec28e616f1d7d8f657140477` | 2026-10-24 11:49 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed3.json` | 28.4 KB | `11bb1daa9ae8f9f4aa0e4ee7dd33b6db` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed4.json` | 28.3 KB | `38b62ded7722da7d4bd7a398a60ae8c8` | 2026-10-24 12:25 |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed0.json` | 28.4 KB | `0d606a3aaa95eacd77fe6d20c03ecb72` | 2026-10-24 11:22 |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed1.json` | 28.4 KB | `8d47da522eb6cf5b4cfa9c09ba0a3d42` | 2026-10-24 11:36 |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed2.json` | 28.4 KB | `9b33ea6465feb40b0f77944dc8b17aeb` | 2026-10-24 11:49 |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed3.json` | 28.4 KB | `41548df6d52047d82976666a6a9ec264` | 2026-10-24 12:12 |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed4.json` | 28.4 KB | `cdc6be9c2fc559472d25b9cc28c3aa17` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed0.json` | 28.3 KB | `10bf8ab942eb61b5639e5527113cfecb` | 2026-10-24 11:23 |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed1.json` | 28.3 KB | `c81441288398191ab62e30e37cf5dd68` | 2026-10-24 11:36 |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed2.json` | 28.2 KB | `fed3b1c8ab4f4a8a8ac15bc3d15124de` | 2026-10-24 12:00 |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed3.json` | 28.2 KB | `da0cfccbb4a0c7c4ec82256c5dca5043` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed4.json` | 28.2 KB | `04ab3635ecc3cdd0244e891ebae7f8d0` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed0.json` | 28.4 KB | `e5973ca1f7ff63457ac637efdeb22974` | 2026-10-24 11:23 |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed1.json` | 28.2 KB | `ec1ef4ee701a3af656cba0a050a53d41` | 2026-10-24 11:47 |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed2.json` | 28.2 KB | `c5fd7dc7fdc0e5d68636f213c026f5e5` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed3.json` | 28.2 KB | `d85f7f95a06442fffda41404afc2206c` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed4.json` | 28.3 KB | `e15403a75b71f10c87c596192a9b3799` | 2026-10-24 12:27 |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed0.json` | 28.4 KB | `5c296670954a31115b6afa39de062f14` | 2026-10-24 11:34 |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed1.json` | 28.3 KB | `f5289bebbda7a3aff9e0b646bc080d73` | 2026-10-24 11:48 |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed2.json` | 28.4 KB | `745444705ffa6aa4fa03d87340d9068e` | 2026-10-24 12:01 |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed3.json` | 28.3 KB | `8066e9d1891b75d27d1535f39eb4e9fc` | 2026-10-24 12:14 |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed4.json` | 28.3 KB | `02ca23e06c6cfc922dac239fbf6d374a` | 2026-10-24 12:38 |
| `importance_sequence/stgcn_subregion/DONE_stgcn` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/commit.txt` | 369 B | `27b133b0c4ee17584ee57d8b484c14e8` | 2026-10-26 13:51 |
| `importance_sequence/stgcn_subregion/importance_stgcn_per_signer.csv` | 6.0 KB | `f7091f35651383dcd94a546cd690a983` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_runs.csv` | 52.2 KB | `130662c5ddbcddc231041b115642004c` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_stability.csv` | 269 B | `ebc714ec947a3b9663dfe9b1d54b4652` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_summary.csv` | 3.7 KB | `6eb600272b9932eb29fae817d5e8337c` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/run.log` | 6.2 KB | `2c0a8b43aa59c14140002e14da246a5e` | 2026-10-26 15:09 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed0.log` | 122 B | `44a4b7ca8b25807423f648ff96c10c55` | 2026-10-26 14:02 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed1.log` | 122 B | `31dc2b79cdd06ec148930d84d6acd092` | 2026-10-26 14:14 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed2.log` | 122 B | `463b6a578345ed99c1f503581d270eee` | 2026-10-26 14:26 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed3.log` | 122 B | `d60b49313b4b216c7c4e22a59852a61e` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed4.log` | 122 B | `b58cc01753d6fd4af7aa5431efa6bfb5` | 2026-10-26 14:57 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed0.log` | 122 B | `bb367d2febf9d8168bd4162c19b285d3` | 2026-10-26 14:03 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed1.log` | 122 B | `83cdd2d628a5c12a1ece6a9166d9966b` | 2026-10-26 14:14 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed2.log` | 122 B | `9e33b282b766a7647ccb4bccff4496b8` | 2026-10-26 14:26 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed3.log` | 122 B | `1ea0fb969167c24ad76757b2955f5143` | 2026-10-26 14:46 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed4.log` | 122 B | `938bfa47a3d0a31457ce2a6815d12b7f` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed0.log` | 122 B | `598bf4ecc52c38985e1622ca8f898e9a` | 2026-10-26 14:03 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed1.log` | 122 B | `8b8d2adb7207dbb34a36476f0153abb7` | 2026-10-26 14:15 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed2.log` | 122 B | `e2211a85e23f2f820e5c4c1d3f41b476` | 2026-10-26 14:35 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed3.log` | 122 B | `46036827082ece363f4b4c77f7fbe6d2` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed4.log` | 122 B | `1da954cf26fc2e4da8483afe064606fc` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed0.log` | 122 B | `c33e813e34c37e66dcd14d71d0127707` | 2026-10-26 14:04 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed1.log` | 122 B | `41f8816ff83628243a055173204b272d` | 2026-10-26 14:24 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed2.log` | 122 B | `4818faa2aaa073e05cfd249c2c49bff9` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed3.log` | 122 B | `b4f9ae92cc905834ebf7b9d20f0d8787` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed4.log` | 122 B | `30e700c08fc5854c7930323aae7235bf` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed0.log` | 122 B | `536b774f687c51f30adc4a8b4cbeb6ca` | 2026-10-26 14:13 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed1.log` | 122 B | `d571819dd93d9e080ca2f93b6bb1db4b` | 2026-10-26 14:25 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed2.log` | 122 B | `6e08437c1f82059ab15dbf71e1e256fc` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed3.log` | 122 B | `7b99d3cc10db92c394d5421e2f2baf0b` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed4.log` | 122 B | `709dc5f398bb0b16dcafa78383238b1e` | 2026-10-26 15:08 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed0.json` | 20.6 KB | `00ddbbeea65205df753067f090906cef` | 2026-10-26 14:02 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed1.json` | 20.7 KB | `d3ac0cb1a38437636586e3421c32e563` | 2026-10-26 14:14 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed2.json` | 20.6 KB | `cd33b4ec01878217b56b963f82c4a55c` | 2026-10-26 14:26 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed3.json` | 20.7 KB | `40a9b639a8d2904e01a5aeacd557fdaf` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed4.json` | 20.6 KB | `9f65181ce920638880c83616df1fe5a1` | 2026-10-26 14:57 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed0.json` | 20.7 KB | `6b046a80f54dc991125bd0146d41cc51` | 2026-10-26 14:03 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed1.json` | 20.7 KB | `558981ad585af8f4c56e6c0cc38c7391` | 2026-10-26 14:14 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed2.json` | 20.7 KB | `cc9c36d74932a6edf721edce0846b2d2` | 2026-10-26 14:26 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed3.json` | 20.7 KB | `eab5fe6a07cfde20717f39077cccf875` | 2026-10-26 14:46 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed4.json` | 20.7 KB | `dce801e1fe01af136527a62f291c2df7` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed0.json` | 20.6 KB | `777077f4ceb2612c7d80b86ea2674990` | 2026-10-26 14:03 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed1.json` | 20.6 KB | `30f9c3aad3583818d12d71eb35daee18` | 2026-10-26 14:15 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed2.json` | 20.6 KB | `30251ac0b5685ba41241e92a37d9e004` | 2026-10-26 14:35 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed3.json` | 20.6 KB | `e3a2a74926c16c92d04407970d900cf1` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed4.json` | 20.6 KB | `3808a271d0723a1d7cc13e5d14d2b214` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed0.json` | 20.6 KB | `035586c310b7054e6e46bcd6ce910efa` | 2026-10-26 14:04 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed1.json` | 20.6 KB | `e8fe01532303b4cf048de937b16416d1` | 2026-10-26 14:24 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed2.json` | 20.6 KB | `8a366e906b002933e1cd5a0115218487` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed3.json` | 20.6 KB | `d1d307528b15c36c62bfdca73fdca28b` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed4.json` | 20.6 KB | `bc9774d4b51d72877842161032f65c0a` | 2026-10-26 14:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed0.json` | 20.6 KB | `6c2fe10acff06f797f0d011f91a44986` | 2026-10-26 14:13 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed1.json` | 20.6 KB | `2c3ddb4c589ff71c0ef8b7d258b0614d` | 2026-10-26 14:25 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed2.json` | 20.7 KB | `934f85e84f4c462057d9c3570ba63de5` | 2026-10-26 14:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed3.json` | 20.7 KB | `e43f7eefafe7085069fbf080058be751` | 2026-10-26 14:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed4.json` | 20.6 KB | `53cbba50b809cc2b85e422239b6f8a5d` | 2026-10-26 15:08 |
| `importance_smoke/pose-loso-s1-seed0.json` | 13.7 KB | `9dda33b7ded0723ff4be466778ec0d41` | 2026-10-23 16:56 |
| `importance_smoke/stgcn-loso-s1-seed0.json` | 11.3 KB | `208ad17b94ed2805a0a94f14d0678705` | 2026-10-23 17:24 |
| `importance_smoke_subregion/stgcn-loso-s1-seed0.json` | 5.2 KB | `c52fc1ee835d9bcbf842e66b73928cd6` | 2026-10-26 13:51 |
| `importance_smoke_subregion/stgcn.log` | 121 B | `c93227c38e6fed9c671fd37780ba2cee` | 2026-10-26 13:51 |
| `original_server/IMU/grid_search.py` | 10.3 KB | `eb17c0d1d8de2584b7141a7c026cc907` | 2025-09-07 16:40 |
| `original_server/IMU/grid_search_notebook.ipynb` | 1.1 MB | `8f4a3bbd160f6a9f5bcc5b79f60276bd` | 2025-08-18 19:00 |
| `original_server/IMU/grid_search_results_temporal.pkl` | 699.3 KB | `bea77f16fafe20e7deac11e801366b93` | 2025-08-18 19:44 |
| `original_server/IMU/helper_functions.py` | 3.5 KB | `acd7b27dfc86a501d8a167940d94a82f` | 2024-11-05 01:32 |
| `original_server/IMU/temporal.csv` | 698.5 KB | `db9da5dcbc810d4c1aeb1f71feacf27a` | 2025-02-20 14:55 |
| `original_server/IMU/IMU_FEATURES_NEW_6subjects/temporal.csv` | 838.4 KB | `5b4d1095d3a779bb41e6f895eb3e8c28` | 2024-11-05 01:59 |
| `original_server/IMU/rerun/cm_rf_temporal_balanced_seed42.pkl` | 19.7 KB | `68d19dfe17a8eaf4f21de39ffa912b6b` | 2026-10-17 16:21 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_0_seed42.pkl` | 19.7 KB | `c97f06ec04b40e48e8207deb06c8ef0e` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_1_seed42.pkl` | 19.7 KB | `f7d17b57a0df4c290a006f5e8d00b860` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_2_seed42.pkl` | 19.7 KB | `70188096cd5d6d91778bc6a3bf094783` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_3_seed42.pkl` | 19.7 KB | `df3ae443d4d77575255be13a8bd3baaf` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/cm_rf_temporal_loso_4_seed42.pkl` | 19.7 KB | `d7a6f914db26f1ca88384a07758af132` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/errors.log` | 4.0 KB | `efb731fa94b91e47e7e8ffe9048d5b8b` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/grid_search_results_temporal_seed42.pkl` | 576.1 KB | `049e910d1f312e035fa1b7c404b60e18` | 2026-10-17 16:22 |
| `original_server/IMU/rerun/names.txt` | 5.4 KB | `a43e645830e5dd0a79e82342734a3307` | 2026-10-17 16:21 |
| `overlay_check/frame_count_gap.csv` | 11.7 KB | `864fef135c95e1f116385c50d8a8c19c` | 2026-10-23 21:09 |
| `overlay_check/landmark_overlay.py` | 6.4 KB | `276a67fc8680fc62b57c477d93c33ac0` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0001_0000_0000.csv` | 111.0 KB | `5cbf96ee322759651bd8b2309d061b93` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0001_0001_0000.csv` | 122.5 KB | `ac52706f827e30f3613b0ae7153b2b4f` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0001_0002_0000.csv` | 124.4 KB | `41feb6f50fd625244fb9284f863929e2` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0001_0003_0000.csv` | 120.8 KB | `663f55b4f79d4206f1f59890f3d03ce5` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0001_0004_0000.csv` | 177.2 KB | `6f49a6e8788af87858d41c6dfd80c9ec` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0030_0000_0000.csv` | 254.8 KB | `804a84c664d24b93ee09d4eb59517ac8` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0030_0001_0000.csv` | 114.8 KB | `302b1778fce990b0a649678c0b2fb068` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0030_0002_0000.csv` | 101.8 KB | `72c3423581712a7ef5568de1691c1206` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0030_0003_0000.csv` | 105.5 KB | `732c10b4ae64c48287809369d9cbb875` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/BODY_LANDMARKS/0030_0004_0000.csv` | 112.9 KB | `abb85446b0ba8b85e0978d4e0f1c9489` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0001_0000_0000.csv` | 72.3 KB | `cb068b7594a9c933d3acad05c2fab382` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0001_0001_0000.csv` | 79.5 KB | `4dacc6d784dae3f6ce4c47486263beb3` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0001_0002_0000.csv` | 81.2 KB | `a268b8ea17b86042af8ee22ae5a8c504` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0001_0003_0000.csv` | 78.8 KB | `90a0b3fc50ac2bb5cd7124892ae042e9` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0001_0004_0000.csv` | 115.8 KB | `6f71516a6bd56677c1ced08ae646de40` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0030_0000_0000.csv` | 166.1 KB | `301fadd9118861627a77c64517300651` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0030_0001_0000.csv` | 74.4 KB | `8d832c4ad4486bee3c5c5a07fe24d506` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0030_0002_0000.csv` | 66.3 KB | `60c59110410bf0d07bff7543b76dc248` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0030_0003_0000.csv` | 68.6 KB | `2a712d31af4ce12c21a0545a901ba96b` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/0030_0004_0000.csv` | 73.5 KB | `195a2feb1e6b8c6508b270fbe61f8a9e` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0001_0000_0000.csv` | 72.7 KB | `eb0749ee5062ca463ce4cb78bf69b006` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0001_0001_0000.csv` | 79.9 KB | `8a89434066fa99bcace2f1d28fcb2429` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0001_0002_0000.csv` | 80.9 KB | `b26663b6ed7615b8486f2a6c1905af01` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0001_0003_0000.csv` | 79.0 KB | `0fd646cd98ea639e716553f81d380aa4` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0001_0004_0000.csv` | 115.4 KB | `30e5cb4a13e22f36d752feb2cc0380f1` | 2026-10-23 21:07 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0030_0000_0000.csv` | 167.2 KB | `6933328c00e33f8acbca8f0e7a841408` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0030_0001_0000.csv` | 74.8 KB | `87c7e55a4b90b9e1ef4e061e17d6b6cc` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0030_0002_0000.csv` | 66.0 KB | `6793d41c4d4f4179d9a57d849557c6a6` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0030_0003_0000.csv` | 68.7 KB | `4fb1db524d52981d23a2064976cf5827` | 2026-10-23 21:08 |
| `overlay_check/LANDMARKS/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/0030_0004_0000.csv` | 73.4 KB | `60d4f3adb5dc61722f8b9f474a77035d` | 2026-10-23 21:08 |
| `pose/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-19 15:07 |
| `pose/commit.txt` | 117 B | `c039de8b8e0dd71a3ea15947051c1929` | 2026-10-19 14:25 |
| `pose/run.log` | 6.1 KB | `f166f090a4995067598d9d4b43beef83` | 2026-10-19 15:07 |
| `pose/bodynorm/pose-8020-seed0.json` | 9.2 KB | `066b32f0a31d4fd793024c684f6a42d1` | 2026-10-19 14:31 |
| `pose/bodynorm/pose-8020-seed1.json` | 9.2 KB | `f4e34c4655f65997c6d1024ab704eb1a` | 2026-10-19 14:37 |
| `pose/bodynorm/pose-8020-seed2.json` | 9.2 KB | `995a7b8584639a96fb253e6bbdbc458b` | 2026-10-19 14:43 |
| `pose/bodynorm/pose-8020-seed3.json` | 9.2 KB | `abf46ca28863a88f580e2dd936cb82c2` | 2026-10-19 14:45 |
| `pose/bodynorm/pose-8020-seed4.json` | 9.2 KB | `d72ae0e5baf9be2e3fc77be25640cd55` | 2026-10-19 14:49 |
| `pose/bodynorm/pose-loso-s0-seed0.json` | 9.2 KB | `dec2b7624113f34716b7c3d39ecfccdd` | 2026-10-19 14:33 |
| `pose/bodynorm/pose-loso-s0-seed1.json` | 9.2 KB | `999c8506864b091a65274f9d268f6500` | 2026-10-19 14:30 |
| `pose/bodynorm/pose-loso-s0-seed2.json` | 9.2 KB | `3600cb3e7a027dee3e122ff461c8463c` | 2026-10-19 14:37 |
| `pose/bodynorm/pose-loso-s0-seed3.json` | 9.2 KB | `717f6c1cf15d96bb4fc62010b258dea7` | 2026-10-19 14:42 |
| `pose/bodynorm/pose-loso-s0-seed4.json` | 9.2 KB | `d36f3cf2c98226434480689be958e04d` | 2026-10-19 14:47 |
| `pose/bodynorm/pose-loso-s1-seed0.json` | 9.2 KB | `a9cec35f07ae22baae37d7f704168ef4` | 2026-10-19 14:34 |
| `pose/bodynorm/pose-loso-s1-seed1.json` | 9.2 KB | `ba0a11bdcb6c5f7fa35343b7db722466` | 2026-10-19 14:31 |
| `pose/bodynorm/pose-loso-s1-seed2.json` | 9.2 KB | `6085c2186477667479001ca0d3426351` | 2026-10-19 14:38 |
| `pose/bodynorm/pose-loso-s1-seed3.json` | 9.2 KB | `69b62ea125668fa81d20371b41202ac8` | 2026-10-19 14:42 |
| `pose/bodynorm/pose-loso-s1-seed4.json` | 9.2 KB | `2b8b6cfce5e783760441b6ce060e367e` | 2026-10-19 14:47 |
| `pose/bodynorm/pose-loso-s2-seed0.json` | 9.2 KB | `c75757268d1aa5eead19eedf8211ebf2` | 2026-10-19 14:31 |
| `pose/bodynorm/pose-loso-s2-seed1.json` | 9.2 KB | `875994bbaa4f4d9a48cf5ed7b830e694` | 2026-10-19 14:36 |
| `pose/bodynorm/pose-loso-s2-seed2.json` | 9.2 KB | `e2971a70ca526c86fd440780f15422e4` | 2026-10-19 14:40 |
| `pose/bodynorm/pose-loso-s2-seed3.json` | 9.2 KB | `ed522c65d40138f0c71947b1e0a459a5` | 2026-10-19 14:42 |
| `pose/bodynorm/pose-loso-s2-seed4.json` | 9.2 KB | `55bcb43a0e27a529a20fc71ac72d2f8f` | 2026-10-19 14:47 |
| `pose/bodynorm/pose-loso-s3-seed0.json` | 9.2 KB | `08377977deb417cbac19553034fa3407` | 2026-10-19 14:34 |
| `pose/bodynorm/pose-loso-s3-seed1.json` | 9.2 KB | `9cfaa4106b31a7ef0903cf5a6a700a92` | 2026-10-19 14:36 |
| `pose/bodynorm/pose-loso-s3-seed2.json` | 9.2 KB | `6d5ac412c3a4710880b4d709dab4c0c1` | 2026-10-19 14:40 |
| `pose/bodynorm/pose-loso-s3-seed3.json` | 9.2 KB | `1158e3180adbb0530be735f914bdf77b` | 2026-10-19 14:43 |
| `pose/bodynorm/pose-loso-s3-seed4.json` | 9.2 KB | `692b36d65650e45f1f3e85a5bfd472de` | 2026-10-19 14:48 |
| `pose/bodynorm/pose-loso-s4-seed0.json` | 9.2 KB | `d3f35d9b7b11f9fdcf2b195b85ab4365` | 2026-10-19 14:30 |
| `pose/bodynorm/pose-loso-s4-seed1.json` | 9.2 KB | `67f2b891d5a0b0d8f07be55691f6c180` | 2026-10-19 14:37 |
| `pose/bodynorm/pose-loso-s4-seed2.json` | 9.2 KB | `6714dac8112a04ab51f74627b76d94b1` | 2026-10-19 14:42 |
| `pose/bodynorm/pose-loso-s4-seed3.json` | 9.2 KB | `c14927e56c76514bce08692c7760c4ab` | 2026-10-19 14:45 |
| `pose/bodynorm/pose-loso-s4-seed4.json` | 9.2 KB | `79f057cd4f573d440f2ab684b05b3155` | 2026-10-19 14:48 |
| `pose/image/pose-8020-seed0.json` | 9.2 KB | `b58d8789123db02899cca1cc6e8e03ed` | 2026-10-19 14:53 |
| `pose/image/pose-8020-seed1.json` | 9.2 KB | `f97f38b4145a3636986d1eedcffad4d2` | 2026-10-19 14:57 |
| `pose/image/pose-8020-seed2.json` | 9.2 KB | `26a49c2482e77ea36b515f636a7db8a4` | 2026-10-19 15:00 |
| `pose/image/pose-8020-seed3.json` | 9.2 KB | `a862776db2faa814aabd31b117924469` | 2026-10-19 15:04 |
| `pose/image/pose-8020-seed4.json` | 9.2 KB | `27594c58f4e94d6c36555abfcfcc9629` | 2026-10-19 15:06 |
| `pose/image/pose-loso-s0-seed0.json` | 9.2 KB | `020aa32f6474993af0ea8ca18ddb957f` | 2026-10-19 14:50 |
| `pose/image/pose-loso-s0-seed1.json` | 9.2 KB | `c9e612e1df83c1c45993fef72f8b37a3` | 2026-10-19 14:54 |
| `pose/image/pose-loso-s0-seed2.json` | 9.2 KB | `e532001fae963317b391246297f292ce` | 2026-10-19 14:58 |
| `pose/image/pose-loso-s0-seed3.json` | 9.2 KB | `b389c3d47b7681ea217f9a957824ede1` | 2026-10-19 15:02 |
| `pose/image/pose-loso-s0-seed4.json` | 9.2 KB | `60c908a031ae8f253148bfb9335ecd34` | 2026-10-19 15:04 |
| `pose/image/pose-loso-s1-seed0.json` | 9.2 KB | `511355b1a0e196ce715a62f0938f7371` | 2026-10-19 14:51 |
| `pose/image/pose-loso-s1-seed1.json` | 9.2 KB | `8140d1600c5da5d0c4056b37c3d55e48` | 2026-10-19 14:54 |
| `pose/image/pose-loso-s1-seed2.json` | 9.2 KB | `6425e32a0040e8c622ef257f208131b8` | 2026-10-19 14:58 |
| `pose/image/pose-loso-s1-seed3.json` | 9.2 KB | `995e1b442234c509a33c893bf086628c` | 2026-10-19 15:02 |
| `pose/image/pose-loso-s1-seed4.json` | 9.2 KB | `0c314fbab68c0cb0ea163c5428b7354c` | 2026-10-19 15:05 |
| `pose/image/pose-loso-s2-seed0.json` | 9.2 KB | `e4b6cecac95dd59c04a785d9ee71bf72` | 2026-10-19 14:52 |
| `pose/image/pose-loso-s2-seed1.json` | 9.2 KB | `f43e1ab8de5c2e88f4198f2e1f4425c0` | 2026-10-19 14:55 |
| `pose/image/pose-loso-s2-seed2.json` | 9.2 KB | `0afb63637ba826786fdc7424d510d903` | 2026-10-19 14:58 |
| `pose/image/pose-loso-s2-seed3.json` | 9.2 KB | `5a2b485d8326e009cfa97058fe5586c9` | 2026-10-19 15:03 |
| `pose/image/pose-loso-s2-seed4.json` | 9.2 KB | `ad7d5c29c4a231ab74a69eada1e1d769` | 2026-10-19 15:06 |
| `pose/image/pose-loso-s3-seed0.json` | 9.2 KB | `1e06db9814814bcf14ca2fff1832fb64` | 2026-10-19 14:52 |
| `pose/image/pose-loso-s3-seed1.json` | 9.2 KB | `5ff4fac9229e19d4f01c3ecf25c0f69c` | 2026-10-19 14:55 |
| `pose/image/pose-loso-s3-seed2.json` | 9.2 KB | `6abdf34c7be8272ad31831b87eb5d9d8` | 2026-10-19 14:59 |
| `pose/image/pose-loso-s3-seed3.json` | 9.2 KB | `b77a8600a2b92234ee869a2a419975ec` | 2026-10-19 15:03 |
| `pose/image/pose-loso-s3-seed4.json` | 9.2 KB | `fcc9029551a9523b570eba2773e96f9d` | 2026-10-19 15:06 |
| `pose/image/pose-loso-s4-seed0.json` | 9.2 KB | `56a5986afdcda2467343067e942d1427` | 2026-10-19 14:53 |
| `pose/image/pose-loso-s4-seed1.json` | 9.2 KB | `2a69ee76870fd2e7661d007f7eb1e31c` | 2026-10-19 14:57 |
| `pose/image/pose-loso-s4-seed2.json` | 9.2 KB | `85046106c0453a648c981616614d5da8` | 2026-10-19 15:00 |
| `pose/image/pose-loso-s4-seed3.json` | 9.2 KB | `e6bceb8f59f457f5ac32c77e1e098298` | 2026-10-19 15:03 |
| `pose/image/pose-loso-s4-seed4.json` | 9.2 KB | `31d6c3d470d6277eec123ee62d8ec18a` | 2026-10-19 15:06 |
| `pose_control/commit.txt` | 83 B | `1648df2067e2115ab72f0c81bb4c65c6` | 2026-10-19 15:08 |
| `pose_control/bodynorm/pose-8020-seed0-shuffled.json` | 9.2 KB | `236cf29b19d681c06965d75b7bc08e02` | 2026-10-19 15:17 |
| `pose_control/bodynorm/pose-loso-s0-seed0-shuffled.json` | 9.3 KB | `874893f9981d23206a0411806b0621ff` | 2026-10-19 15:17 |
| `pose_control/bodynorm/pose-loso-s1-seed0-shuffled.json` | 9.3 KB | `faa61398ad3cc8296d87b6bdaa5baca4` | 2026-10-19 15:17 |
| `pose_control/bodynorm/pose-loso-s2-seed0-shuffled.json` | 9.3 KB | `e47458dacad6cafd9bfdea563cfaa515` | 2026-10-19 15:16 |
| `pose_control/bodynorm/pose-loso-s3-seed0-shuffled.json` | 9.2 KB | `ec3263a3ac5badb376614342eb00f185` | 2026-10-19 15:16 |
| `pose_control/bodynorm/pose-loso-s4-seed0-shuffled.json` | 9.2 KB | `16e68e1cf19f742eb0ad89aecbc31169` | 2026-10-19 15:16 |
| `pose_control/image/pose-8020-seed0-shuffled.json` | 9.2 KB | `0630cfd17cec5b59b9a1fee57a03efd5` | 2026-10-19 15:16 |
| `pose_control/image/pose-loso-s0-seed0-shuffled.json` | 9.2 KB | `c2c044954b03159f8db7a1c2e55dcd8c` | 2026-10-19 15:16 |
| `pose_control/image/pose-loso-s1-seed0-shuffled.json` | 9.2 KB | `0661e3f9329a73cc406a804c72553c12` | 2026-10-19 15:17 |
| `pose_control/image/pose-loso-s2-seed0-shuffled.json` | 9.2 KB | `19f3141f9169f63bd215d17cff519067` | 2026-10-19 15:16 |
| `pose_control/image/pose-loso-s3-seed0-shuffled.json` | 9.2 KB | `263183b447fc7ae59e21162751366b32` | 2026-10-19 15:16 |
| `pose_control/image/pose-loso-s4-seed0-shuffled.json` | 9.2 KB | `114fc58039a595d7ff772290d10c4837` | 2026-10-19 15:18 |
| `pose_regress/pose-loso-s1-seed0.json` | 9.5 KB | `62a112c3807514b49ebac0229ac774ac` | 2026-10-22 02:35 |
| `pose_study/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-22 12:08 |
| `pose_study/commit.txt` | 208 B | `4f0f6b7226e541798dec2f9d5f4f3cbe` | 2026-10-22 02:38 |
| `pose_study/errors.log` | 184.0 KB | `5d1ad675b3f95d5b3dbef9e396d800d8` | 2026-10-22 11:59 |
| `pose_study/jobs_phase1.txt` | 182.1 KB | `3b037198408eabbe4348d712692e5f33` | 2026-10-22 02:38 |
| `pose_study/jobs_phase2.txt` | 5.3 KB | `b9d7044d88ba6566071c10ca479437c7` | 2026-10-22 11:31 |
| `pose_study/nested_selection.csv` | 373 B | `25186ce5544be3b61a6d15388494c77e` | 2026-10-22 11:31 |
| `pose_study/nested_selection_grid.csv` | 3.8 KB | `10d923001e94bc70df4cb3724152142f` | 2026-10-22 11:31 |
| `pose_study/run.log` | 668 B | `75a8c7db6e5e0609e9bdf9f37ce1fc55` | 2026-10-22 12:08 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s0-seed0.json` | 9.5 KB | `3a9a81449f17157254b8e6fdb65cf438` | 2026-10-22 08:05 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s0-seed1.json` | 9.5 KB | `ee4139428fc90e273b717fda0d6ced79` | 2026-10-22 08:11 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s0-seed2.json` | 9.5 KB | `c49c2f81d0854b93c9c725b7e0b86155` | 2026-10-22 08:15 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s0-seed3.json` | 9.5 KB | `dd9b85127d9f6e042cb91409db0d6b06` | 2026-10-22 08:20 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s0-seed4.json` | 9.5 KB | `188575f27b81114cbf607b2dfb741bc3` | 2026-10-22 08:21 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s1-seed0.json` | 9.5 KB | `714554f4dc4b4e9765fbeda90cddf35a` | 2026-10-22 08:06 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s1-seed1.json` | 9.5 KB | `da0c76109ce1dcefe2856de80a367a06` | 2026-10-22 08:11 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s1-seed2.json` | 9.5 KB | `27fdbde7cbc146f487d35bea936aa969` | 2026-10-22 08:16 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s1-seed3.json` | 9.5 KB | `64d39b52bd6612c27a0986c9d61f602d` | 2026-10-22 08:20 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s1-seed4.json` | 9.5 KB | `ea34d6a1a84d4f2966c9c588061f6636` | 2026-10-22 08:21 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s2-seed0.json` | 9.5 KB | `bd8b97569525773e1b38e2977f5f0ce6` | 2026-10-22 08:09 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s2-seed1.json` | 9.5 KB | `752d2cb78193e03e08e0505d4cc871e7` | 2026-10-22 08:14 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s2-seed2.json` | 9.5 KB | `790de87bf28a5baf0dab704ae8a5140e` | 2026-10-22 08:16 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s2-seed3.json` | 9.5 KB | `68e11dc47cfcfb8cbd58ce1733604bcf` | 2026-10-22 08:20 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s2-seed4.json` | 9.5 KB | `5010995087e3f05cf5ced95d421df407` | 2026-10-22 08:24 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s3-seed0.json` | 9.5 KB | `dd3d8cfd68149c6fb37e812cffcb1edf` | 2026-10-22 08:10 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s3-seed1.json` | 9.5 KB | `d495338b0828b63de3363f6ad20c36f5` | 2026-10-22 08:14 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s3-seed2.json` | 9.5 KB | `0893f597232fcce4cb6af4bc994b852f` | 2026-10-22 08:16 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s3-seed3.json` | 9.5 KB | `2924d6d3e368f01d07e896c584d769a9` | 2026-10-22 08:20 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s3-seed4.json` | 9.5 KB | `c33efaf48dbc3d76ead3ad4dee5259b9` | 2026-10-22 08:25 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s4-seed0.json` | 9.5 KB | `350d30cd247cf0cd0ec7bd9f817f0faf` | 2026-10-22 08:11 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s4-seed1.json` | 9.5 KB | `2a576e924ef4fc0f9dffa39116ee490b` | 2026-10-22 08:15 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s4-seed2.json` | 9.5 KB | `999d295c5de935c20dc352dcdced8d79` | 2026-10-22 08:19 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s4-seed3.json` | 9.5 KB | `81cf830b2ef82a453c2140dad7a40def` | 2026-10-22 08:21 |
| `pose_study/ablation/A1_no_augmentation/pose-loso-s4-seed4.json` | 9.5 KB | `379abec97a7d1e92f81c7d8ae078125f` | 2026-10-22 08:25 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s0-seed0.json` | 9.8 KB | `ddf7ef60437ba73e481495482fcb2576` | 2026-10-22 09:30 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s0-seed1.json` | 9.8 KB | `5eeb34d27f44e8178143c48d5258aceb` | 2026-10-22 09:34 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s0-seed2.json` | 9.8 KB | `1e272056c21de8fa8aade000f0aff01e` | 2026-10-22 09:38 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s0-seed3.json` | 9.8 KB | `9fa1ca324ccfca6b8fc8cb01ebcec0c5` | 2026-10-22 09:40 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s0-seed4.json` | 9.8 KB | `4d81bb40cfd611e24f645ea2b1587569` | 2026-10-22 09:45 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s1-seed0.json` | 9.8 KB | `a2832a7937a313acee2254fdba8c0a21` | 2026-10-22 09:33 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s1-seed1.json` | 9.8 KB | `198ebc23f0ee4366eb5e0f9df55eb0e0` | 2026-10-22 09:35 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s1-seed2.json` | 9.9 KB | `71211c47067420cdd4fd0af4e92fe3b8` | 2026-10-22 09:39 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s1-seed3.json` | 9.8 KB | `9ccdb7ab2829445ee193ba456fd58e2a` | 2026-10-22 09:40 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s1-seed4.json` | 9.8 KB | `76cd43fb3ca6ceea9899fa8e626d90fd` | 2026-10-22 09:45 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s2-seed0.json` | 9.8 KB | `bf4c0810c9c8af1985c72b67fae58fa3` | 2026-10-22 09:33 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s2-seed1.json` | 9.8 KB | `bcd1ce6b94dcb9f6fb774276470bb954` | 2026-10-22 09:35 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s2-seed2.json` | 9.8 KB | `ea29b7dbfb498f7d2d12e1197735469c` | 2026-10-22 09:39 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s2-seed3.json` | 9.8 KB | `257b13fdfe70a498bc3dbc92aa107fc2` | 2026-10-22 09:44 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s2-seed4.json` | 9.8 KB | `bf9576720fd5efdc51a198953aa264f7` | 2026-10-22 09:45 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s3-seed0.json` | 9.8 KB | `51e98405f72c2d4efd40a0d4e75e174b` | 2026-10-22 09:33 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s3-seed1.json` | 9.8 KB | `e0a147b5b9e955ba8b207413c3ceab9d` | 2026-10-22 09:35 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s3-seed2.json` | 9.8 KB | `23abadd0ab8698c3690ebf62ec24a884` | 2026-10-22 09:40 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s3-seed3.json` | 9.8 KB | `54cfdc53bef1398748ebf50438afb3b4` | 2026-10-22 09:44 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s3-seed4.json` | 9.8 KB | `a0c93e08ef34b10d2066055663c9ae03` | 2026-10-22 09:45 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s4-seed0.json` | 9.8 KB | `afcfa81581ac906eb1b4f3b2896c33d7` | 2026-10-22 09:34 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s4-seed1.json` | 9.8 KB | `52737e4de8becdbd9a0fe2f54ec39ec6` | 2026-10-22 09:38 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s4-seed2.json` | 9.8 KB | `af990d160a9244758e0be45f6217720c` | 2026-10-22 09:40 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s4-seed3.json` | 9.8 KB | `e7a88ccdd29a0cee14166bf686c2eae5` | 2026-10-22 09:44 |
| `pose_study/ablation/A2_no_label_smoothing/pose-loso-s4-seed4.json` | 9.8 KB | `4d553fbc8f7585802da7916af58b6513` | 2026-10-22 09:46 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s0-seed0.json` | 9.9 KB | `ab398fd8d6a8e714169fd4642a97baca` | 2026-10-22 08:42 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s0-seed1.json` | 9.9 KB | `feeae29a7012a810a2d9b140c27fce1a` | 2026-10-22 08:46 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s0-seed2.json` | 9.9 KB | `18d45d704997c05c0d08226dbd4fbe06` | 2026-10-22 08:47 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s0-seed3.json` | 9.9 KB | `d8b47dc1d365aa082dabe715b80bd99e` | 2026-10-22 08:52 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s0-seed4.json` | 9.9 KB | `54ba1854b1a1f09caeaa8b1919cd36c0` | 2026-10-22 08:56 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s1-seed0.json` | 9.9 KB | `061ba256deee9162d9f8912bc782c2b5` | 2026-10-22 08:42 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s1-seed1.json` | 9.9 KB | `f599ed029d0408fe3ef175045eb550ae` | 2026-10-22 08:46 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s1-seed2.json` | 9.9 KB | `d31e0ac773dea180d2948428eb67eefd` | 2026-10-22 08:47 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s1-seed3.json` | 9.9 KB | `aed212343078dd8fa9045a3083f1f77a` | 2026-10-22 08:52 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s1-seed4.json` | 9.9 KB | `f69f4108a3e7c34293cf6bccfcbad612` | 2026-10-22 08:56 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s2-seed0.json` | 9.9 KB | `aaf22a5db780b52a243818b941e6d857` | 2026-10-22 08:42 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s2-seed1.json` | 9.9 KB | `0e2373cc0dca6a36186c84450de0c694` | 2026-10-22 08:46 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s2-seed2.json` | 9.9 KB | `565bdc9dd8d4f38a678962958b152e69` | 2026-10-22 08:50 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s2-seed3.json` | 9.8 KB | `54cd819887e61ee98e10b8b362c92e50` | 2026-10-22 08:52 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s2-seed4.json` | 9.9 KB | `717f8deba789e906dfdefd53013b62d2` | 2026-10-22 08:56 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s3-seed0.json` | 9.8 KB | `47a030c974dcda603b3cc5852691ef0f` | 2026-10-22 08:42 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s3-seed1.json` | 9.8 KB | `0f70924522379b83bbcce81fd0afc38c` | 2026-10-22 08:47 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s3-seed2.json` | 9.8 KB | `e8dc22ec5239d2125cb3cadcbcbc4643` | 2026-10-22 08:51 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s3-seed3.json` | 9.9 KB | `a3e02f4f5aa98a13f3d3f38c2df910f4` | 2026-10-22 08:52 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s3-seed4.json` | 9.8 KB | `134f875f8325b0309994ba729d3709af` | 2026-10-22 08:57 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s4-seed0.json` | 9.8 KB | `4414850efe618160abd9e47bc6a82831` | 2026-10-22 08:45 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s4-seed1.json` | 9.8 KB | `6a9cbc830692457a2ca42b70fe177b55` | 2026-10-22 08:47 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s4-seed2.json` | 9.8 KB | `0721f1a277b6273525c2d203c73e4980` | 2026-10-22 08:51 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s4-seed3.json` | 9.8 KB | `fdac4dfbb060a391e6e3dd6cae7185c8` | 2026-10-22 08:52 |
| `pose_study/ablation/A3_plain_recipe/pose-loso-s4-seed4.json` | 9.8 KB | `b0758c0a32ca3a3a97197c5195df6a12` | 2026-10-22 08:57 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s0-seed0.json` | 9.5 KB | `971504bf08433f59fcaf03224f11a1b3` | 2026-10-22 09:49 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s0-seed1.json` | 9.5 KB | `6bb92fa7a8033f57fb69ee8aafa335d4` | 2026-10-22 09:51 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s0-seed2.json` | 9.5 KB | `347f6632443b7de7c3e28e649b315c45` | 2026-10-22 09:55 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s0-seed3.json` | 9.5 KB | `6a2ff900c6a767e60b818cf5f66d62b8` | 2026-10-22 09:57 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s0-seed4.json` | 9.5 KB | `27eb5b4a32469fa0bc950de378184b79` | 2026-10-22 10:01 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s1-seed0.json` | 9.5 KB | `0db770488647415fe6d6c6db35735135` | 2026-10-22 09:49 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s1-seed1.json` | 9.5 KB | `b6d65aababfe1d0b184f5670152810b7` | 2026-10-22 09:51 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s1-seed2.json` | 9.5 KB | `f24f58ad7cd23c748396e9de210689d0` | 2026-10-22 09:56 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s1-seed3.json` | 9.5 KB | `d60971c510d46236f4793f39b5d6d795` | 2026-10-22 10:00 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s1-seed4.json` | 9.5 KB | `db323c48efcb5234ea36c9410a0b04cd` | 2026-10-22 10:01 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s2-seed0.json` | 9.5 KB | `9e23077daad33a05ee1cc1077b5a9ba8` | 2026-10-22 09:50 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s2-seed1.json` | 9.5 KB | `eae02890f6e3eae68bc1a117834f2d68` | 2026-10-22 09:51 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s2-seed2.json` | 9.5 KB | `aa4f7628f7cd3419b58ff7e19306e275` | 2026-10-22 09:56 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s2-seed3.json` | 9.5 KB | `8ea8680aa97d4504f7f1d2cd906b792c` | 2026-10-22 10:00 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s2-seed4.json` | 9.5 KB | `6582602c20c4391f0273052e5000e4ac` | 2026-10-22 10:02 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s3-seed0.json` | 9.5 KB | `ec3ad775c4749101e217957fc3140307` | 2026-10-22 09:50 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s3-seed1.json` | 9.5 KB | `39c345631f66a81558f591f1b868cec6` | 2026-10-22 09:55 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s3-seed2.json` | 9.5 KB | `3ff266e4a907c0cbf3e89dbfd822c881` | 2026-10-22 09:56 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s3-seed3.json` | 9.5 KB | `6505a5ff748fdf6bc65009cbfd0e470f` | 2026-10-22 10:01 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s3-seed4.json` | 9.5 KB | `0f165a9adaaf8dff55c15197e001e2d2` | 2026-10-22 10:02 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s4-seed0.json` | 9.5 KB | `049973330561fb6f7ddadf42f73130bd` | 2026-10-22 09:50 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s4-seed1.json` | 9.5 KB | `e9a30bfcacd3582d91f876e8ac3012e6` | 2026-10-22 09:55 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s4-seed2.json` | 9.5 KB | `749416878e10df25c5b7b20213a10162` | 2026-10-22 09:56 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s4-seed3.json` | 9.5 KB | `46650ffcc3f279915644abdb68b185e8` | 2026-10-22 10:01 |
| `pose_study/ablation/A4_mean_pooling/pose-loso-s4-seed4.json` | 9.5 KB | `87a16b3c7521bc51f994447ee32b18a3` | 2026-10-22 10:05 |
| `pose_study/ablation/A5_hands_only/pose-loso-s0-seed0.json` | 9.5 KB | `b96e3f668ab063b9b30ec41368cd69b3` | 2026-10-22 08:57 |
| `pose_study/ablation/A5_hands_only/pose-loso-s0-seed1.json` | 9.5 KB | `50b704be39855ec22aaaa964abedc4b6` | 2026-10-22 09:01 |
| `pose_study/ablation/A5_hands_only/pose-loso-s0-seed2.json` | 9.5 KB | `3c39299dd8e212385dc380a5c3d3f94c` | 2026-10-22 09:03 |
| `pose_study/ablation/A5_hands_only/pose-loso-s0-seed3.json` | 9.5 KB | `b008dbb258ca07a0106a551bd2919362` | 2026-10-22 09:08 |
| `pose_study/ablation/A5_hands_only/pose-loso-s0-seed4.json` | 9.5 KB | `2005a4fc5fe4993385df38bcf3dc0c75` | 2026-10-22 09:12 |
| `pose_study/ablation/A5_hands_only/pose-loso-s1-seed0.json` | 9.5 KB | `236abd78eed34a28ac3256e04aa2e538` | 2026-10-22 08:58 |
| `pose_study/ablation/A5_hands_only/pose-loso-s1-seed1.json` | 9.5 KB | `9c2961bf0e72cc17cc44f0784108713e` | 2026-10-22 09:02 |
| `pose_study/ablation/A5_hands_only/pose-loso-s1-seed2.json` | 9.5 KB | `87aca7786073fac0f37bd5680d0b7ee3` | 2026-10-22 09:07 |
| `pose_study/ablation/A5_hands_only/pose-loso-s1-seed3.json` | 9.5 KB | `cbe4b45972ff542c43e64b63481c7a35` | 2026-10-22 09:08 |
| `pose_study/ablation/A5_hands_only/pose-loso-s1-seed4.json` | 9.5 KB | `6524aff6de094a8ab47546b445fdeb29` | 2026-10-22 09:12 |
| `pose_study/ablation/A5_hands_only/pose-loso-s2-seed0.json` | 9.5 KB | `4814ef1d186c21022136a8eacc50964f` | 2026-10-22 08:58 |
| `pose_study/ablation/A5_hands_only/pose-loso-s2-seed1.json` | 9.5 KB | `1a52609d43750d0574b0b20be63d043a` | 2026-10-22 09:03 |
| `pose_study/ablation/A5_hands_only/pose-loso-s2-seed2.json` | 9.5 KB | `e0e1fe665737cb13645a2d4311923fe4` | 2026-10-22 09:07 |
| `pose_study/ablation/A5_hands_only/pose-loso-s2-seed3.json` | 9.5 KB | `cc05f8673aad9465fe2a4d71169f2b30` | 2026-10-22 09:08 |
| `pose_study/ablation/A5_hands_only/pose-loso-s2-seed4.json` | 9.5 KB | `09128c0f094c352e3e79c0267d55f228` | 2026-10-22 09:13 |
| `pose_study/ablation/A5_hands_only/pose-loso-s3-seed0.json` | 9.5 KB | `396be97477ec0fc61386694323b5f786` | 2026-10-22 09:01 |
| `pose_study/ablation/A5_hands_only/pose-loso-s3-seed1.json` | 9.5 KB | `d123a78cc16de4b2cca8baffbbeacc3b` | 2026-10-22 09:03 |
| `pose_study/ablation/A5_hands_only/pose-loso-s3-seed2.json` | 9.5 KB | `a6c28a217e137369754c5104b39c8038` | 2026-10-22 09:07 |
| `pose_study/ablation/A5_hands_only/pose-loso-s3-seed3.json` | 9.5 KB | `6e4223ebb355d68e787da243d27b937b` | 2026-10-22 09:08 |
| `pose_study/ablation/A5_hands_only/pose-loso-s3-seed4.json` | 9.5 KB | `652d30a3176163d2b81956c1c04dc92d` | 2026-10-22 09:13 |
| `pose_study/ablation/A5_hands_only/pose-loso-s4-seed0.json` | 9.5 KB | `6a973450b5796eafdcc985d13f486894` | 2026-10-22 09:01 |
| `pose_study/ablation/A5_hands_only/pose-loso-s4-seed1.json` | 9.5 KB | `fa089f3cc48bdd7e8796d575e6ab3724` | 2026-10-22 09:03 |
| `pose_study/ablation/A5_hands_only/pose-loso-s4-seed2.json` | 9.5 KB | `eeb68d5bc1cb1c3e6a1d1d4f85e4a249` | 2026-10-22 09:07 |
| `pose_study/ablation/A5_hands_only/pose-loso-s4-seed3.json` | 9.5 KB | `95fe0b4c72fff0f3b9f74c523a47049a` | 2026-10-22 09:12 |
| `pose_study/ablation/A5_hands_only/pose-loso-s4-seed4.json` | 9.5 KB | `e82f5a409b55e7911860309788cd9d6c` | 2026-10-22 09:13 |
| `pose_study/ablation/A6_body_only/pose-loso-s0-seed0.json` | 9.5 KB | `7c790ed7a26d2e35fa51a01613ed4cf6` | 2026-10-22 09:14 |
| `pose_study/ablation/A6_body_only/pose-loso-s0-seed1.json` | 9.5 KB | `2fd6740ef3fa74cf1210ca42c88cb87f` | 2026-10-22 09:18 |
| `pose_study/ablation/A6_body_only/pose-loso-s0-seed2.json` | 9.5 KB | `3621a3675a63717deebe2bb6fd895946` | 2026-10-22 09:22 |
| `pose_study/ablation/A6_body_only/pose-loso-s0-seed3.json` | 9.5 KB | `142bcf729b82aadf115c3f7385734d40` | 2026-10-22 09:24 |
| `pose_study/ablation/A6_body_only/pose-loso-s0-seed4.json` | 9.5 KB | `6bfed9444ff305e941827c8b813579e4` | 2026-10-22 09:28 |
| `pose_study/ablation/A6_body_only/pose-loso-s1-seed0.json` | 9.5 KB | `e5091da5548bb2ee09da2ebf2603cebb` | 2026-10-22 09:14 |
| `pose_study/ablation/A6_body_only/pose-loso-s1-seed1.json` | 9.5 KB | `b9b8891c99083657aa4663c7c58294b0` | 2026-10-22 09:19 |
| `pose_study/ablation/A6_body_only/pose-loso-s1-seed2.json` | 9.5 KB | `464bb6278843de07de2ec35dd198138a` | 2026-10-22 09:22 |
| `pose_study/ablation/A6_body_only/pose-loso-s1-seed3.json` | 9.5 KB | `7987794feb0bf869ec559907e9cdf1cc` | 2026-10-22 09:24 |
| `pose_study/ablation/A6_body_only/pose-loso-s1-seed4.json` | 9.5 KB | `89661bb52a4173153a5ab78f623f768b` | 2026-10-22 09:29 |
| `pose_study/ablation/A6_body_only/pose-loso-s2-seed0.json` | 9.5 KB | `c91947d1a98185d4c7ce83d863cb0012` | 2026-10-22 09:17 |
| `pose_study/ablation/A6_body_only/pose-loso-s2-seed1.json` | 9.5 KB | `2f1ce82e726a0931bae3ffe5757c2fda` | 2026-10-22 09:19 |
| `pose_study/ablation/A6_body_only/pose-loso-s2-seed2.json` | 9.5 KB | `b2fc84cdc054c9ac89f31b6d43994b6d` | 2026-10-22 09:23 |
| `pose_study/ablation/A6_body_only/pose-loso-s2-seed3.json` | 9.5 KB | `52b830c34099542148a00a4685b4e875` | 2026-10-22 09:24 |
| `pose_study/ablation/A6_body_only/pose-loso-s2-seed4.json` | 9.6 KB | `10043bd1a94c3c40a0924ca2099e8f93` | 2026-10-22 09:29 |
| `pose_study/ablation/A6_body_only/pose-loso-s3-seed0.json` | 9.5 KB | `28707dfa96578ffaaea6563f57f9d1a9` | 2026-10-22 09:17 |
| `pose_study/ablation/A6_body_only/pose-loso-s3-seed1.json` | 9.5 KB | `285754a2c6230da7dfaca24ba8f4f3a8` | 2026-10-22 09:19 |
| `pose_study/ablation/A6_body_only/pose-loso-s3-seed2.json` | 9.5 KB | `4ad86e8d462087a347cbcad4ff463c47` | 2026-10-22 09:23 |
| `pose_study/ablation/A6_body_only/pose-loso-s3-seed3.json` | 9.5 KB | `468737bbbf7beb6a6fb6c78641110ce4` | 2026-10-22 09:28 |
| `pose_study/ablation/A6_body_only/pose-loso-s3-seed4.json` | 9.5 KB | `1879f9dc560a7ad95960b4c65e1281d5` | 2026-10-22 09:29 |
| `pose_study/ablation/A6_body_only/pose-loso-s4-seed0.json` | 9.5 KB | `39be12a3a38ceb6129b189d7a93c67e2` | 2026-10-22 09:17 |
| `pose_study/ablation/A6_body_only/pose-loso-s4-seed1.json` | 9.5 KB | `6c8b6610c0b0450edbcdd62d517cf790` | 2026-10-22 09:19 |
| `pose_study/ablation/A6_body_only/pose-loso-s4-seed2.json` | 9.5 KB | `0a349634691436584e7fa28a3affb310` | 2026-10-22 09:24 |
| `pose_study/ablation/A6_body_only/pose-loso-s4-seed3.json` | 9.5 KB | `5d5bc973708e9982019c2a9218bb9b1a` | 2026-10-22 09:28 |
| `pose_study/ablation/A6_body_only/pose-loso-s4-seed4.json` | 9.5 KB | `3ceb0ea88fd6b5e21b273948cd8cfee8` | 2026-10-22 09:29 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed0.json` | 9.5 KB | `174bc2aabcea41d3b6aaf374427895e5` | 2026-10-22 08:25 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed1.json` | 9.5 KB | `c5ab3040da6dcb2b6630411fac4b518a` | 2026-10-22 08:30 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed2.json` | 9.5 KB | `04e1c664e507093d164ec2efefdd3ca5` | 2026-10-22 08:32 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed3.json` | 9.5 KB | `052fc28c10c1ab67fbe924b80babc288` | 2026-10-22 08:35 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed4.json` | 9.5 KB | `5d5893e56066707bff822fc60ddd9029` | 2026-10-22 08:37 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed0.json` | 9.5 KB | `e3c85557d82cc01e75516e5f0ad99837` | 2026-10-22 08:26 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed1.json` | 9.5 KB | `b56e664de7e677ed74f87b39a9c8f783` | 2026-10-22 08:30 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed2.json` | 9.5 KB | `9621dcfd14f5029c0991ee23e15b7ad0` | 2026-10-22 08:31 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed3.json` | 9.5 KB | `576c88c020724455ee16a4a5a57f4c11` | 2026-10-22 08:36 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed4.json` | 9.5 KB | `8b342b36d11c27993f92939ecb7d5723` | 2026-10-22 08:40 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed0.json` | 9.5 KB | `68135347b6e3d913175893d1c0e76ef0` | 2026-10-22 08:26 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed1.json` | 9.5 KB | `0be9476b8b3fa377408a5cafb5b7346e` | 2026-10-22 08:30 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed2.json` | 9.5 KB | `902298ff9f0dfcd4d081ca0687487e0e` | 2026-10-22 08:32 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed3.json` | 9.5 KB | `6cb48defe62587ae88d95dcca5745a1a` | 2026-10-22 08:37 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed4.json` | 9.5 KB | `19b2f7489eff4d253772bef544bba707` | 2026-10-22 08:41 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed0.json` | 9.5 KB | `1fc92010f4913c70083086f2af72f41a` | 2026-10-22 08:26 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed1.json` | 9.5 KB | `39de90a92c0fe45888c45706580d13ec` | 2026-10-22 08:31 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed2.json` | 9.5 KB | `a51b698f06a1ef0e14402341306a645c` | 2026-10-22 08:35 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed3.json` | 9.5 KB | `d32f48b59d95bd05eec023fa51be6f6c` | 2026-10-22 08:37 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed4.json` | 9.5 KB | `9a4a3d421b2dbe02501e3c5ec51fb07b` | 2026-10-22 08:41 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed0.json` | 9.5 KB | `ec20f31df9061e18a140f28a58eb1474` | 2026-10-22 08:26 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed1.json` | 9.5 KB | `f145a37c7506fc480bbc921118e57fe7` | 2026-10-22 08:31 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed2.json` | 9.5 KB | `f7850a55de93ea0b52ae615744118ccd` | 2026-10-22 08:35 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed3.json` | 9.5 KB | `2a078de86f77414394a860b45b8b7b00` | 2026-10-22 08:37 |
| `pose_study/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed4.json` | 9.5 KB | `111329590553f547367de94dc58dc181` | 2026-10-22 08:41 |
| `pose_study/curve/k1-s0-train1.json` | 9.5 KB | `4a9c0f1b72ea64eaf853900ba70a2841` | 2026-10-22 11:05 |
| `pose_study/curve/k1-s0-train2.json` | 9.5 KB | `71c5a998f1a2bbba630eaa92346d3f7c` | 2026-10-22 11:05 |
| `pose_study/curve/k1-s0-train3.json` | 9.5 KB | `55738715cfd1d15adc3d3687b50933b1` | 2026-10-22 11:06 |
| `pose_study/curve/k1-s0-train4.json` | 9.5 KB | `10d97db1f70c6a67da288c8f069e32f6` | 2026-10-22 11:06 |
| `pose_study/curve/k1-s1-train0.json` | 9.5 KB | `0ba533be633ccf421c76189a6077da53` | 2026-10-22 11:11 |
| `pose_study/curve/k1-s1-train2.json` | 9.5 KB | `1e907933a64282ee3a6b37fb081c09c1` | 2026-10-22 11:11 |
| `pose_study/curve/k1-s1-train3.json` | 9.5 KB | `dca047214ee58221ee097dbe91ecc2bd` | 2026-10-22 11:12 |
| `pose_study/curve/k1-s1-train4.json` | 9.5 KB | `06f37b69ad12eadd732c79f1c217ae61` | 2026-10-22 11:12 |
| `pose_study/curve/k1-s2-train0.json` | 9.5 KB | `b458df63ca67719094f0797270fcc2cd` | 2026-10-22 11:16 |
| `pose_study/curve/k1-s2-train1.json` | 9.5 KB | `77583a187b83c3ee244c2c02c8d7ac93` | 2026-10-22 11:16 |
| `pose_study/curve/k1-s2-train3.json` | 9.5 KB | `e5b0759877493f97eb96eec944d282a4` | 2026-10-22 11:17 |
| `pose_study/curve/k1-s2-train4.json` | 9.5 KB | `ebe6101e27d75eb8443e09c83695d48b` | 2026-10-22 11:17 |
| `pose_study/curve/k1-s3-train0.json` | 9.5 KB | `ae64d6874187133cf5d48f9ed3254607` | 2026-10-22 11:21 |
| `pose_study/curve/k1-s3-train1.json` | 9.5 KB | `c4b26bf1a3b725d8f14379a3fe418387` | 2026-10-22 11:21 |
| `pose_study/curve/k1-s3-train2.json` | 9.5 KB | `70fdc752e8ea9517ecf7a99ba3f6371e` | 2026-10-22 11:21 |
| `pose_study/curve/k1-s3-train4.json` | 9.5 KB | `c040e2b1622f116a8c4ef06d627edf1a` | 2026-10-22 11:21 |
| `pose_study/curve/k1-s4-train0.json` | 9.5 KB | `a4971c92937b455387ff2e63192f0a9b` | 2026-10-22 11:25 |
| `pose_study/curve/k1-s4-train1.json` | 9.5 KB | `dc6f5f25f12217d2be0bda616a89a82d` | 2026-10-22 11:25 |
| `pose_study/curve/k1-s4-train2.json` | 9.5 KB | `68a467c8acad150308cc0b83be090d67` | 2026-10-22 11:26 |
| `pose_study/curve/k1-s4-train3.json` | 9.5 KB | `99d68a8b55bcd6187b85db902398f927` | 2026-10-22 11:27 |
| `pose_study/curve/k2-s0-train12.json` | 9.5 KB | `7a4e741a9ba5dc9e62a7c7e9c183e027` | 2026-10-22 11:08 |
| `pose_study/curve/k2-s0-train13.json` | 9.5 KB | `d10796c6bc41d2413116235bf6a3b736` | 2026-10-22 11:08 |
| `pose_study/curve/k2-s0-train14.json` | 9.5 KB | `e6c30495350aaf2c64f78bc31a145555` | 2026-10-22 11:08 |
| `pose_study/curve/k2-s0-train23.json` | 9.5 KB | `36b6e1c89cf883d3c4c7d60459ef25b0` | 2026-10-22 11:09 |
| `pose_study/curve/k2-s0-train24.json` | 9.5 KB | `4b4309e8afeaa969be368008c093b9cd` | 2026-10-22 11:09 |
| `pose_study/curve/k2-s0-train34.json` | 9.5 KB | `1ac483c2bdb9c52ad988a81fb6343d6f` | 2026-10-22 11:09 |
| `pose_study/curve/k2-s1-train02.json` | 9.5 KB | `388ef7fd3cd07721fee48b1d010b5040` | 2026-10-22 11:14 |
| `pose_study/curve/k2-s1-train03.json` | 9.5 KB | `bdcaeb87b9550febd9b88b1d1a063b42` | 2026-10-22 11:14 |
| `pose_study/curve/k2-s1-train04.json` | 9.5 KB | `23485c0b3243a6e6631e3b271db51ec7` | 2026-10-22 11:15 |
| `pose_study/curve/k2-s1-train23.json` | 9.5 KB | `a0d39871d3e59fa3a9b501120afa35b7` | 2026-10-22 11:15 |
| `pose_study/curve/k2-s1-train24.json` | 9.6 KB | `fd32b7cd1a38343c399e938d2d904196` | 2026-10-22 11:15 |
| `pose_study/curve/k2-s1-train34.json` | 9.5 KB | `b645f21beec504b689b81da68556e8d9` | 2026-10-22 11:15 |
| `pose_study/curve/k2-s2-train01.json` | 9.5 KB | `48238a4483db897f320d5145f77ab9c9` | 2026-10-22 11:19 |
| `pose_study/curve/k2-s2-train03.json` | 9.5 KB | `8342bce55035b862a42028d289814d63` | 2026-10-22 11:19 |
| `pose_study/curve/k2-s2-train04.json` | 9.5 KB | `5f07f8eb8dc1a2c02f8588fb7f71d617` | 2026-10-22 11:19 |
| `pose_study/curve/k2-s2-train13.json` | 9.5 KB | `adf7b24ca9b6537ea3e9124d20b20afe` | 2026-10-22 11:19 |
| `pose_study/curve/k2-s2-train14.json` | 9.5 KB | `f4009fd23cb1c2d8e2d0526c44e3d937` | 2026-10-22 11:20 |
| `pose_study/curve/k2-s2-train34.json` | 9.5 KB | `a9fb01ad322f516e2985b4f75487072d` | 2026-10-22 11:20 |
| `pose_study/curve/k2-s3-train01.json` | 9.5 KB | `81f95f997641bc9f9b0bb30203ab163d` | 2026-10-22 11:24 |
| `pose_study/curve/k2-s3-train02.json` | 9.5 KB | `820529c51a66a51e928c8641ce365354` | 2026-10-22 11:24 |
| `pose_study/curve/k2-s3-train04.json` | 9.5 KB | `57ee4ebbacb78c7b954c870e1adc5459` | 2026-10-22 11:24 |
| `pose_study/curve/k2-s3-train12.json` | 9.5 KB | `11c64d1c431a8f0ecd5a87021cbe950a` | 2026-10-22 11:24 |
| `pose_study/curve/k2-s3-train14.json` | 9.5 KB | `b66bd19e450845e57e89b564d34fc0d3` | 2026-10-22 11:25 |
| `pose_study/curve/k2-s3-train24.json` | 9.5 KB | `3c37ea500afabce3f6a0dd543734be08` | 2026-10-22 11:25 |
| `pose_study/curve/k2-s4-train01.json` | 9.5 KB | `500a6a15ece688447cfcdcc3ff6ececf` | 2026-10-22 11:28 |
| `pose_study/curve/k2-s4-train02.json` | 9.5 KB | `9be7dc78441a0bdde22b0eccd9e966b3` | 2026-10-22 11:28 |
| `pose_study/curve/k2-s4-train03.json` | 9.5 KB | `c283fb363142c35dca43e418abf0028b` | 2026-10-22 11:29 |
| `pose_study/curve/k2-s4-train12.json` | 9.5 KB | `fc216b334c0f955b5099a7eb93d17ebc` | 2026-10-22 11:30 |
| `pose_study/curve/k2-s4-train13.json` | 9.5 KB | `704a118dc60d91b42e1ed6ff25517d70` | 2026-10-22 11:30 |
| `pose_study/curve/k2-s4-train23.json` | 9.5 KB | `b6088e4d13bca51623b22018de3b2a30` | 2026-10-22 11:30 |
| `pose_study/curve/k3-s0-train123.json` | 9.5 KB | `937b5470ff1615c97b0d3c5dd032f80e` | 2026-10-22 11:12 |
| `pose_study/curve/k3-s0-train124.json` | 9.5 KB | `e5a21566391bd40f929769c94e8dce21` | 2026-10-22 11:12 |
| `pose_study/curve/k3-s0-train134.json` | 9.5 KB | `50098379ed9eb1a610f0ab27e4a626ce` | 2026-10-22 11:12 |
| `pose_study/curve/k3-s0-train234.json` | 9.5 KB | `f0e8ef16285a9f8049b533dd33ba68c3` | 2026-10-22 11:13 |
| `pose_study/curve/k3-s1-train023.json` | 9.5 KB | `0db8b003b4bb0cff51dc121126dde314` | 2026-10-22 11:17 |
| `pose_study/curve/k3-s1-train024.json` | 9.5 KB | `f493dda0870c0c52055c6d1f503a3a5a` | 2026-10-22 11:17 |
| `pose_study/curve/k3-s1-train034.json` | 9.5 KB | `4e9f8d388f4efeaf313d020797f35d99` | 2026-10-22 11:18 |
| `pose_study/curve/k3-s1-train234.json` | 9.5 KB | `a3d92164675bdaf960916fa80d2494c7` | 2026-10-22 11:18 |
| `pose_study/curve/k3-s2-train013.json` | 9.5 KB | `3b8012ea120b3ed33ea9b7f5ad261bf0` | 2026-10-22 11:22 |
| `pose_study/curve/k3-s2-train014.json` | 9.5 KB | `32812d5c316b743a3e37a19bffc19ed2` | 2026-10-22 11:22 |
| `pose_study/curve/k3-s2-train034.json` | 9.5 KB | `1b475d040f0106b6c7f4f1f961cc8aa2` | 2026-10-22 11:23 |
| `pose_study/curve/k3-s2-train134.json` | 9.5 KB | `7963a44aac98b0048b9a1377c01e2c33` | 2026-10-22 11:23 |
| `pose_study/curve/k3-s3-train012.json` | 9.5 KB | `bc0b81accea6a46091e5cbad191a7235` | 2026-10-22 11:27 |
| `pose_study/curve/k3-s3-train014.json` | 9.5 KB | `d533ab9e138ba7f02ee51f9b429cdf64` | 2026-10-22 11:27 |
| `pose_study/curve/k3-s3-train024.json` | 9.5 KB | `ab477e5e9c0c77dfe27ddce46b10a7a4` | 2026-10-22 11:28 |
| `pose_study/curve/k3-s3-train124.json` | 9.5 KB | `2eaf77760413f7d21c8b221ff81c1794` | 2026-10-22 11:28 |
| `pose_study/curve/k3-s4-train012.json` | 9.5 KB | `9224179a8336142fd6e5f6efc42de9ab` | 2026-10-22 11:31 |
| `pose_study/curve/k3-s4-train013.json` | 9.5 KB | `2d387ae1c13dc3b3df412bb9f33db081` | 2026-10-22 11:31 |
| `pose_study/curve/k3-s4-train023.json` | 9.5 KB | `19998040584eeea44075a2990e9fc351` | 2026-10-22 11:31 |
| `pose_study/curve/k3-s4-train123.json` | 9.5 KB | `207f5fd04fce7b072c3deb8ac4630670` | 2026-10-22 11:31 |
| `pose_study/frames/f16/pose-loso-s0-seed0.json` | 9.5 KB | `ca46f4c57db77931e1a2d240f69e5d38` | 2026-10-22 10:04 |
| `pose_study/frames/f16/pose-loso-s0-seed1.json` | 9.5 KB | `d125b763bac7037ea3ffd81504e00375` | 2026-10-22 10:06 |
| `pose_study/frames/f16/pose-loso-s0-seed2.json` | 9.5 KB | `b5240a26140a216a323bcafe4733d63a` | 2026-10-22 10:09 |
| `pose_study/frames/f16/pose-loso-s0-seed3.json` | 9.5 KB | `1f9b7e22eff8556c2ae2a9ed390c173a` | 2026-10-22 10:12 |
| `pose_study/frames/f16/pose-loso-s0-seed4.json` | 9.5 KB | `803a6b55f12becd4d6b33350702840ed` | 2026-10-22 10:14 |
| `pose_study/frames/f16/pose-loso-s1-seed0.json` | 9.5 KB | `cd51492c2ee62072d4e2731ebd891c2b` | 2026-10-22 10:05 |
| `pose_study/frames/f16/pose-loso-s1-seed1.json` | 9.5 KB | `5de2f761ce47e2a95a17b662118b0508` | 2026-10-22 10:06 |
| `pose_study/frames/f16/pose-loso-s1-seed2.json` | 9.5 KB | `1a32831b5175a3c745c41083f6e1c4ee` | 2026-10-22 10:09 |
| `pose_study/frames/f16/pose-loso-s1-seed3.json` | 9.5 KB | `6c4283ac529d7268e7d16f865cf3eec8` | 2026-10-22 10:13 |
| `pose_study/frames/f16/pose-loso-s1-seed4.json` | 9.5 KB | `ab3a086df9be49aadb86201f7054cc2e` | 2026-10-22 10:14 |
| `pose_study/frames/f16/pose-loso-s2-seed0.json` | 9.5 KB | `ea1cdd15bf9aa3b403cb3a29afe42dde` | 2026-10-22 10:05 |
| `pose_study/frames/f16/pose-loso-s2-seed1.json` | 9.5 KB | `83172b3b38a902dd71d7ddb3b976a60c` | 2026-10-22 10:08 |
| `pose_study/frames/f16/pose-loso-s2-seed2.json` | 9.5 KB | `29ddf5db4dea11f5c64989114811f7cc` | 2026-10-22 10:09 |
| `pose_study/frames/f16/pose-loso-s2-seed3.json` | 9.5 KB | `56a8a53cf06a65ca0eb8ff1c78d77e55` | 2026-10-22 10:13 |
| `pose_study/frames/f16/pose-loso-s2-seed4.json` | 9.5 KB | `9183277394b91760ab518128c1be185e` | 2026-10-22 10:14 |
| `pose_study/frames/f16/pose-loso-s3-seed0.json` | 9.5 KB | `fb1c184d6ea30c1f4e06d6ab20e42108` | 2026-10-22 10:05 |
| `pose_study/frames/f16/pose-loso-s3-seed1.json` | 9.5 KB | `d8a1ba707385c15a9262c86596b5f3ac` | 2026-10-22 10:09 |
| `pose_study/frames/f16/pose-loso-s3-seed2.json` | 9.5 KB | `ba7a513321d7d17614d415ab636fcab2` | 2026-10-22 10:10 |
| `pose_study/frames/f16/pose-loso-s3-seed3.json` | 9.5 KB | `c67268cf9166f132c50f80ba4f808838` | 2026-10-22 10:13 |
| `pose_study/frames/f16/pose-loso-s3-seed4.json` | 9.5 KB | `0569d157e6c21a9f99864d3aa3f431ed` | 2026-10-22 10:17 |
| `pose_study/frames/f16/pose-loso-s4-seed0.json` | 9.5 KB | `f5f579558f952b9a27ecb91bf7952909` | 2026-10-22 10:05 |
| `pose_study/frames/f16/pose-loso-s4-seed1.json` | 9.5 KB | `49a3d907e8870b556bdbc95a3f04d78a` | 2026-10-22 10:09 |
| `pose_study/frames/f16/pose-loso-s4-seed2.json` | 9.5 KB | `111e791369eb271c257202d5d144748a` | 2026-10-22 10:10 |
| `pose_study/frames/f16/pose-loso-s4-seed3.json` | 9.5 KB | `d403c3fe0f64df3d58be9f82b88be3ab` | 2026-10-22 10:13 |
| `pose_study/frames/f16/pose-loso-s4-seed4.json` | 9.5 KB | `acf89146a75b3b908c57b55daba759dc` | 2026-10-22 10:17 |
| `pose_study/frames/f32/pose-loso-s0-seed0.json` | 9.5 KB | `be6d54c1019431587f8db0b84f9ff742` | 2026-10-22 10:20 |
| `pose_study/frames/f32/pose-loso-s0-seed1.json` | 9.5 KB | `1be285eb455dc0d57daf547023aa355d` | 2026-10-22 10:21 |
| `pose_study/frames/f32/pose-loso-s0-seed2.json` | 9.5 KB | `f90d6a70f177090a6eaef5b2d19bd4cb` | 2026-10-22 10:27 |
| `pose_study/frames/f32/pose-loso-s0-seed3.json` | 9.5 KB | `52d4b503313fd6756494cd343bebde18` | 2026-10-22 10:31 |
| `pose_study/frames/f32/pose-loso-s0-seed4.json` | 9.5 KB | `d089c4297cba7a62922e78a16f66fa7e` | 2026-10-22 10:34 |
| `pose_study/frames/f32/pose-loso-s1-seed0.json` | 9.5 KB | `65de47d62c67413c896fd14973e0afea` | 2026-10-22 10:20 |
| `pose_study/frames/f32/pose-loso-s1-seed1.json` | 9.5 KB | `51e8028c1193cd977ca0595ba8d7b13e` | 2026-10-22 10:23 |
| `pose_study/frames/f32/pose-loso-s1-seed2.json` | 9.5 KB | `f9b9a60b8b096319d652891b070b329a` | 2026-10-22 10:27 |
| `pose_study/frames/f32/pose-loso-s1-seed3.json` | 9.5 KB | `8ce1dab023ef4cc67f673f6f5d353168` | 2026-10-22 10:34 |
| `pose_study/frames/f32/pose-loso-s1-seed4.json` | 9.5 KB | `9f7f3110f07a71f60e56d45de58ba8bf` | 2026-10-22 10:35 |
| `pose_study/frames/f32/pose-loso-s2-seed0.json` | 9.5 KB | `6d93d01a21700b76dea3bfff62685591` | 2026-10-22 10:20 |
| `pose_study/frames/f32/pose-loso-s2-seed1.json` | 9.5 KB | `3ec8b4ad1691fe72ab0a4f9310c89c52` | 2026-10-22 10:24 |
| `pose_study/frames/f32/pose-loso-s2-seed2.json` | 9.5 KB | `88adf40bcf59226cce631f9cb9a3c13c` | 2026-10-22 10:27 |
| `pose_study/frames/f32/pose-loso-s2-seed3.json` | 9.5 KB | `627b7fc171593eca87520ced85a0d8e3` | 2026-10-22 10:34 |
| `pose_study/frames/f32/pose-loso-s2-seed4.json` | 9.5 KB | `e1892932a0a5d82894b2fb32f8895e9d` | 2026-10-22 10:37 |
| `pose_study/frames/f32/pose-loso-s3-seed0.json` | 9.5 KB | `0d50302c729171f3d6d24242d1397384` | 2026-10-22 10:20 |
| `pose_study/frames/f32/pose-loso-s3-seed1.json` | 9.5 KB | `3cf0e5f1803582351aa0eb3470f3bf6b` | 2026-10-22 10:27 |
| `pose_study/frames/f32/pose-loso-s3-seed2.json` | 9.5 KB | `e5926a65ca3ebdfacffb3de56b96c862` | 2026-10-22 10:28 |
| `pose_study/frames/f32/pose-loso-s3-seed3.json` | 9.5 KB | `b79b01f82cdf78411e1102c352a38aab` | 2026-10-22 10:34 |
| `pose_study/frames/f32/pose-loso-s3-seed4.json` | 9.5 KB | `3cd379619fb3c7dafa6d0ee7e21263fe` | 2026-10-22 10:37 |
| `pose_study/frames/f32/pose-loso-s4-seed0.json` | 9.5 KB | `63694b1b57546bcff87af444969f3fcf` | 2026-10-22 10:21 |
| `pose_study/frames/f32/pose-loso-s4-seed1.json` | 9.5 KB | `6d6dcd954bf5fa0c55f4bfbbce5612be` | 2026-10-22 10:27 |
| `pose_study/frames/f32/pose-loso-s4-seed2.json` | 9.5 KB | `d405e7cd5bfafc35303bfaf0bbbf49a3` | 2026-10-22 10:30 |
| `pose_study/frames/f32/pose-loso-s4-seed3.json` | 9.5 KB | `ef3e2a9af2aaf422cf0351e27695a0cb` | 2026-10-22 10:34 |
| `pose_study/frames/f32/pose-loso-s4-seed4.json` | 9.5 KB | `27958462fb32dd73021ce5cd69cc87c3` | 2026-10-22 10:41 |
| `pose_study/frames/f48/pose-loso-s0-seed0.json` | 9.5 KB | `c645a43b553e96ec91406cdc8da37fb3` | 2026-10-22 10:44 |
| `pose_study/frames/f48/pose-loso-s0-seed1.json` | 9.5 KB | `d0f39a8bed607136363a7d491d2a8064` | 2026-10-22 10:47 |
| `pose_study/frames/f48/pose-loso-s0-seed2.json` | 9.5 KB | `ee03fbf86c7c442118f1292c92728e01` | 2026-10-22 10:54 |
| `pose_study/frames/f48/pose-loso-s0-seed3.json` | 9.5 KB | `edeab66490d38c0679521a661d3e8a2a` | 2026-10-22 11:00 |
| `pose_study/frames/f48/pose-loso-s0-seed4.json` | 9.5 KB | `e1e24597bfa7c3b93c9afebc311e6230` | 2026-10-22 11:04 |
| `pose_study/frames/f48/pose-loso-s1-seed0.json` | 9.5 KB | `48313cd7bb2fa34b6813ab77ad462ec3` | 2026-10-22 10:44 |
| `pose_study/frames/f48/pose-loso-s1-seed1.json` | 9.5 KB | `7ff5cd196074d36f0e91a0009404e086` | 2026-10-22 10:47 |
| `pose_study/frames/f48/pose-loso-s1-seed2.json` | 9.5 KB | `8303ead63e30230cacf753025a80f972` | 2026-10-22 10:54 |
| `pose_study/frames/f48/pose-loso-s1-seed3.json` | 9.5 KB | `bcd75ae4ba0c03f9af5f2b95467fcf1a` | 2026-10-22 11:03 |
| `pose_study/frames/f48/pose-loso-s1-seed4.json` | 9.5 KB | `a02dcdc9fc0754dd846e32a275d863df` | 2026-10-22 11:06 |
| `pose_study/frames/f48/pose-loso-s2-seed0.json` | 9.5 KB | `da429ff3be36f2fb3e673ebb76f54b02` | 2026-10-22 10:44 |
| `pose_study/frames/f48/pose-loso-s2-seed1.json` | 9.5 KB | `7e8a9face756beb3b9e4a00dda4ea644` | 2026-10-22 10:51 |
| `pose_study/frames/f48/pose-loso-s2-seed2.json` | 9.5 KB | `c97820e8301123859b338365b64cb878` | 2026-10-22 10:54 |
| `pose_study/frames/f48/pose-loso-s2-seed3.json` | 9.5 KB | `d78b5ffee8201e808723fc498e1b3667` | 2026-10-22 11:03 |
| `pose_study/frames/f48/pose-loso-s2-seed4.json` | 9.5 KB | `f75b73c261da83a397b9abaf89ff05ad` | 2026-10-22 11:07 |
| `pose_study/frames/f48/pose-loso-s3-seed0.json` | 9.5 KB | `039aba9c6f321b5ee9ba8218357548ca` | 2026-10-22 10:44 |
| `pose_study/frames/f48/pose-loso-s3-seed1.json` | 9.5 KB | `c1fd6624ecdd41c31d3eb89edf9bfdbd` | 2026-10-22 10:53 |
| `pose_study/frames/f48/pose-loso-s3-seed2.json` | 9.5 KB | `5eb121d8bbfc7783c836cbc0ed00118b` | 2026-10-22 10:57 |
| `pose_study/frames/f48/pose-loso-s3-seed3.json` | 9.5 KB | `2649a936e50805e0642fc34d1dd6755e` | 2026-10-22 11:04 |
| `pose_study/frames/f48/pose-loso-s3-seed4.json` | 9.5 KB | `5b5bbec7376c512dd6a5323e0ec2b623` | 2026-10-22 11:10 |
| `pose_study/frames/f48/pose-loso-s4-seed0.json` | 9.5 KB | `21ecb4477f325ea3cfb76635bdfb6f10` | 2026-10-22 10:44 |
| `pose_study/frames/f48/pose-loso-s4-seed1.json` | 9.5 KB | `5945b54d1ffd0165695ace63c25b6e76` | 2026-10-22 10:54 |
| `pose_study/frames/f48/pose-loso-s4-seed2.json` | 9.5 KB | `2996ac71b34abed00735ceda5926d7a3` | 2026-10-22 10:57 |
| `pose_study/frames/f48/pose-loso-s4-seed3.json` | 9.5 KB | `63c6dcd51220aae10290b5b533aa3126` | 2026-10-22 11:04 |
| `pose_study/frames/f48/pose-loso-s4-seed4.json` | 9.5 KB | `706ad81dec0d760b3c953f524342ab03` | 2026-10-22 11:13 |
| `pose_study/inner/d128-L2-lr1e-3-out0-val1.json` | 9.6 KB | `eeeeb884ac5fe2687708abd20c4b5093` | 2026-10-22 03:34 |
| `pose_study/inner/d128-L2-lr1e-3-out0-val2.json` | 9.5 KB | `3a62d45d801f4749c771e32e3b5e2837` | 2026-10-22 03:34 |
| `pose_study/inner/d128-L2-lr1e-3-out0-val3.json` | 9.5 KB | `8e742ac1cc1cb0504d7c30e099e16887` | 2026-10-22 03:35 |
| `pose_study/inner/d128-L2-lr1e-3-out0-val4.json` | 9.5 KB | `d2e4b0b78bad20115298ae910bbd0959` | 2026-10-22 03:35 |
| `pose_study/inner/d128-L2-lr1e-3-out1-val0.json` | 9.5 KB | `26146309a588d551526cb2c063b2fc0a` | 2026-10-22 03:35 |
| `pose_study/inner/d128-L2-lr1e-3-out1-val2.json` | 9.5 KB | `86b932c92ddeb84f441e1dd83b312de4` | 2026-10-22 03:36 |
| `pose_study/inner/d128-L2-lr1e-3-out1-val3.json` | 9.5 KB | `4f289096efcda6243f145f3ffbdb5005` | 2026-10-22 03:36 |
| `pose_study/inner/d128-L2-lr1e-3-out1-val4.json` | 9.5 KB | `bba12179ab7d87bad521bd0a6ec6dd60` | 2026-10-22 03:37 |
| `pose_study/inner/d128-L2-lr1e-3-out2-val0.json` | 9.5 KB | `45d82abf3bfcbfdc9cd966709a64658a` | 2026-10-22 03:38 |
| `pose_study/inner/d128-L2-lr1e-3-out2-val1.json` | 9.5 KB | `7dd16750fb0776d30f55e0b648acfd35` | 2026-10-22 03:38 |
| `pose_study/inner/d128-L2-lr1e-3-out2-val3.json` | 9.5 KB | `38906b3c3308943abdfe306953d6cc76` | 2026-10-22 03:38 |
| `pose_study/inner/d128-L2-lr1e-3-out2-val4.json` | 9.5 KB | `7b7b3ffc258fb1c378d40ae893708e5a` | 2026-10-22 03:39 |
| `pose_study/inner/d128-L2-lr1e-3-out3-val0.json` | 9.5 KB | `5b4bab59a7adae1dbca437e296c99c4d` | 2026-10-22 03:39 |
| `pose_study/inner/d128-L2-lr1e-3-out3-val1.json` | 9.5 KB | `cbf547bf231ee5eeded93a710177ce74` | 2026-10-22 03:40 |
| `pose_study/inner/d128-L2-lr1e-3-out3-val2.json` | 9.5 KB | `97937d7caa38cd3b08e2c6e10ff08ac9` | 2026-10-22 03:41 |
| `pose_study/inner/d128-L2-lr1e-3-out3-val4.json` | 9.5 KB | `d9bfa5578a80842739bd0974e9291a5f` | 2026-10-22 03:41 |
| `pose_study/inner/d128-L2-lr1e-3-out4-val0.json` | 9.5 KB | `0e92b926204810a0be860cd8312734fc` | 2026-10-22 03:41 |
| `pose_study/inner/d128-L2-lr1e-3-out4-val1.json` | 9.5 KB | `55e2159f8f8c6994be716941b4f1d012` | 2026-10-22 03:42 |
| `pose_study/inner/d128-L2-lr1e-3-out4-val2.json` | 9.5 KB | `9270aa3bb5076c66ab1b4c27b33caf46` | 2026-10-22 03:42 |
| `pose_study/inner/d128-L2-lr1e-3-out4-val3.json` | 9.5 KB | `b0b21d623e85af7f5280bd9b4141e9aa` | 2026-10-22 03:43 |
| `pose_study/inner/d128-L2-lr5e-4-out0-val1.json` | 9.6 KB | `e5ce6800a909e6c9a2c4cd266cf5c1a4` | 2026-10-22 03:24 |
| `pose_study/inner/d128-L2-lr5e-4-out0-val2.json` | 9.5 KB | `e637351f18ba84d47dedc71fc1e29651` | 2026-10-22 03:24 |
| `pose_study/inner/d128-L2-lr5e-4-out0-val3.json` | 9.5 KB | `d613496e7b56889fe19db7844d776164` | 2026-10-22 03:25 |
| `pose_study/inner/d128-L2-lr5e-4-out0-val4.json` | 9.5 KB | `da63f73ed2df74bb579957ad2dba8fdb` | 2026-10-22 03:26 |
| `pose_study/inner/d128-L2-lr5e-4-out1-val0.json` | 9.5 KB | `c52e13db66c77293aabb424cd58de240` | 2026-10-22 03:27 |
| `pose_study/inner/d128-L2-lr5e-4-out1-val2.json` | 9.5 KB | `97f83fb5144785df80d7e7243fc64c40` | 2026-10-22 03:27 |
| `pose_study/inner/d128-L2-lr5e-4-out1-val3.json` | 9.5 KB | `a2435b746c620039db894abdd3796f30` | 2026-10-22 03:27 |
| `pose_study/inner/d128-L2-lr5e-4-out1-val4.json` | 9.5 KB | `adcd6e93b3eedb3ec23e79672aa7e2f4` | 2026-10-22 03:27 |
| `pose_study/inner/d128-L2-lr5e-4-out2-val0.json` | 9.5 KB | `bff2c0902892a4ef94d15a1ad081ddb0` | 2026-10-22 03:28 |
| `pose_study/inner/d128-L2-lr5e-4-out2-val1.json` | 9.6 KB | `42c1a47c55ff2d34d5d13d8c13a08b69` | 2026-10-22 03:28 |
| `pose_study/inner/d128-L2-lr5e-4-out2-val3.json` | 9.5 KB | `86eeb247f47d20f89cde309dad6011e1` | 2026-10-22 03:29 |
| `pose_study/inner/d128-L2-lr5e-4-out2-val4.json` | 9.5 KB | `f6f199372c6cfd65a6bc10326de006ec` | 2026-10-22 03:30 |
| `pose_study/inner/d128-L2-lr5e-4-out3-val0.json` | 9.5 KB | `236cfc58038eba2b661910c435760197` | 2026-10-22 03:30 |
| `pose_study/inner/d128-L2-lr5e-4-out3-val1.json` | 9.5 KB | `97a693faa350df93475e62daa3905768` | 2026-10-22 03:30 |
| `pose_study/inner/d128-L2-lr5e-4-out3-val2.json` | 9.5 KB | `9ea11f312a2e9dd16b29e6ed9e93cb94` | 2026-10-22 03:31 |
| `pose_study/inner/d128-L2-lr5e-4-out3-val4.json` | 9.5 KB | `09c90d61357c450054ca09ab169833c5` | 2026-10-22 03:31 |
| `pose_study/inner/d128-L2-lr5e-4-out4-val0.json` | 9.5 KB | `d958391e1a9038d15dc42accc020c580` | 2026-10-22 03:32 |
| `pose_study/inner/d128-L2-lr5e-4-out4-val1.json` | 9.6 KB | `e360520b13c0acf30c142ee841084e94` | 2026-10-22 03:32 |
| `pose_study/inner/d128-L2-lr5e-4-out4-val2.json` | 9.5 KB | `4c635001f1add0a4992417cff226ce24` | 2026-10-22 03:33 |
| `pose_study/inner/d128-L2-lr5e-4-out4-val3.json` | 9.5 KB | `e731ab26a4d68531249d8f7fb1583423` | 2026-10-22 03:33 |
| `pose_study/inner/d128-L3-lr1e-3-out0-val1.json` | 9.5 KB | `b8c976ffab31e6e2359f79081c310f16` | 2026-10-22 03:58 |
| `pose_study/inner/d128-L3-lr1e-3-out0-val2.json` | 9.5 KB | `1c7ba9cb6dd628ea51c53fa028837a8e` | 2026-10-22 03:58 |
| `pose_study/inner/d128-L3-lr1e-3-out0-val3.json` | 9.5 KB | `c69daa5b2bb1d52151eefefa40d10e93` | 2026-10-22 03:59 |
| `pose_study/inner/d128-L3-lr1e-3-out0-val4.json` | 9.5 KB | `ad2b9f6134937b28b69ead8be2dafad0` | 2026-10-22 03:59 |
| `pose_study/inner/d128-L3-lr1e-3-out1-val0.json` | 9.5 KB | `b4ea254ecdd8f358cd61460fca3374f0` | 2026-10-22 04:00 |
| `pose_study/inner/d128-L3-lr1e-3-out1-val2.json` | 9.5 KB | `b0f0d9a23d192cade9021062fcbd0c00` | 2026-10-22 04:01 |
| `pose_study/inner/d128-L3-lr1e-3-out1-val3.json` | 9.5 KB | `eee0a17c6baf22bc409cd5354cd2425c` | 2026-10-22 04:02 |
| `pose_study/inner/d128-L3-lr1e-3-out1-val4.json` | 9.5 KB | `65eef03175109296998565d5c71ae4f8` | 2026-10-22 04:02 |
| `pose_study/inner/d128-L3-lr1e-3-out2-val0.json` | 9.5 KB | `007e6a088bf7ffb65b06858065f2ce01` | 2026-10-22 04:03 |
| `pose_study/inner/d128-L3-lr1e-3-out2-val1.json` | 9.5 KB | `b2efd796f5b44a3abc8806deeacb3e83` | 2026-10-22 04:03 |
| `pose_study/inner/d128-L3-lr1e-3-out2-val3.json` | 9.5 KB | `797d7f4b361e4ef48dcd28ff186f3d43` | 2026-10-22 04:04 |
| `pose_study/inner/d128-L3-lr1e-3-out2-val4.json` | 9.5 KB | `d31f4086ca7b06a7d3e4d0f096912608` | 2026-10-22 04:05 |
| `pose_study/inner/d128-L3-lr1e-3-out3-val0.json` | 9.5 KB | `8d64c7a303fc15642079ee925cc71392` | 2026-10-22 04:06 |
| `pose_study/inner/d128-L3-lr1e-3-out3-val1.json` | 9.5 KB | `b4a2d66e9aeac53ccf2eb1efdb6ab87c` | 2026-10-22 04:06 |
| `pose_study/inner/d128-L3-lr1e-3-out3-val2.json` | 9.5 KB | `5a8c9283d4315a58c3b7192512e23e57` | 2026-10-22 04:07 |
| `pose_study/inner/d128-L3-lr1e-3-out3-val4.json` | 9.5 KB | `91667b8bcd5c876e5e06cc22d610a150` | 2026-10-22 04:08 |
| `pose_study/inner/d128-L3-lr1e-3-out4-val0.json` | 9.5 KB | `f1ad8bd0263dad76bfc01cf9adc0ba05` | 2026-10-22 04:08 |
| `pose_study/inner/d128-L3-lr1e-3-out4-val1.json` | 9.6 KB | `5094feafdd7e516cce2584748dd8dfa3` | 2026-10-22 04:09 |
| `pose_study/inner/d128-L3-lr1e-3-out4-val2.json` | 9.5 KB | `34b5767165419394947d1bef237826b6` | 2026-10-22 04:10 |
| `pose_study/inner/d128-L3-lr1e-3-out4-val3.json` | 9.5 KB | `fc3481b95080d5734c336f47413596f6` | 2026-10-22 04:10 |
| `pose_study/inner/d128-L3-lr5e-4-out0-val1.json` | 9.5 KB | `57c97d24b00f723313bd35952cf8b70e` | 2026-10-22 03:45 |
| `pose_study/inner/d128-L3-lr5e-4-out0-val2.json` | 9.5 KB | `d3d17130604750ab04bdebaac0165ded` | 2026-10-22 03:45 |
| `pose_study/inner/d128-L3-lr5e-4-out0-val3.json` | 9.5 KB | `9a687a951404a1e5217817bbd1929254` | 2026-10-22 03:45 |
| `pose_study/inner/d128-L3-lr5e-4-out0-val4.json` | 9.5 KB | `84ccb0671442fe787cdce939f528c859` | 2026-10-22 03:46 |
| `pose_study/inner/d128-L3-lr5e-4-out1-val0.json` | 9.5 KB | `95b75d502c7a64a805244625d5b4cb9d` | 2026-10-22 03:46 |
| `pose_study/inner/d128-L3-lr5e-4-out1-val2.json` | 9.5 KB | `bc412be825dc796f934bb42e22643723` | 2026-10-22 03:47 |
| `pose_study/inner/d128-L3-lr5e-4-out1-val3.json` | 9.5 KB | `961a51a512fdccaf6d28ecc5ea7d3d8d` | 2026-10-22 03:48 |
| `pose_study/inner/d128-L3-lr5e-4-out1-val4.json` | 9.5 KB | `67d1f561c0a2b6fe79a8d00156bebfcc` | 2026-10-22 03:49 |
| `pose_study/inner/d128-L3-lr5e-4-out2-val0.json` | 9.5 KB | `f14c1bd2815002daa8ed58cb609312d5` | 2026-10-22 03:49 |
| `pose_study/inner/d128-L3-lr5e-4-out2-val1.json` | 9.5 KB | `d1160236eceb39c65d8f8f3b0ebec973` | 2026-10-22 03:50 |
| `pose_study/inner/d128-L3-lr5e-4-out2-val3.json` | 9.5 KB | `3cca36e7d159ed7ebbadeced0586cb41` | 2026-10-22 03:50 |
| `pose_study/inner/d128-L3-lr5e-4-out2-val4.json` | 9.5 KB | `1575befa56e86ff0e2c70e535d5a17fd` | 2026-10-22 03:51 |
| `pose_study/inner/d128-L3-lr5e-4-out3-val0.json` | 9.5 KB | `b4cf8519b2f37d84e22c7dc97654301d` | 2026-10-22 03:52 |
| `pose_study/inner/d128-L3-lr5e-4-out3-val1.json` | 9.5 KB | `355872d81e05d377ee83451082e171da` | 2026-10-22 03:53 |
| `pose_study/inner/d128-L3-lr5e-4-out3-val2.json` | 9.5 KB | `6feeb4bb48cbb4361f099e9daf143e72` | 2026-10-22 03:53 |
| `pose_study/inner/d128-L3-lr5e-4-out3-val4.json` | 9.5 KB | `6cafe9b720bca077b67524e93b976841` | 2026-10-22 03:54 |
| `pose_study/inner/d128-L3-lr5e-4-out4-val0.json` | 9.5 KB | `1cabd4d3dff8d42a95d18f4d12b42c17` | 2026-10-22 03:55 |
| `pose_study/inner/d128-L3-lr5e-4-out4-val1.json` | 9.6 KB | `d2df2c680fa91745ace371758a1a4f1a` | 2026-10-22 03:55 |
| `pose_study/inner/d128-L3-lr5e-4-out4-val2.json` | 9.5 KB | `5f446e7ca136ad1ac9055477b41bc245` | 2026-10-22 03:56 |
| `pose_study/inner/d128-L3-lr5e-4-out4-val3.json` | 9.5 KB | `ff8db972abfca9b192291e8593018880` | 2026-10-22 03:57 |
| `pose_study/inner/d128-L4-lr1e-3-out0-val1.json` | 9.5 KB | `e6561b242f4b711111650ff882f78382` | 2026-10-22 04:29 |
| `pose_study/inner/d128-L4-lr1e-3-out0-val2.json` | 9.5 KB | `f03d0e9d3275a96b49533da2c8ecda67` | 2026-10-22 04:30 |
| `pose_study/inner/d128-L4-lr1e-3-out0-val3.json` | 9.5 KB | `9f81a9ea86bffb0d6001e6e731d568af` | 2026-10-22 04:31 |
| `pose_study/inner/d128-L4-lr1e-3-out0-val4.json` | 9.5 KB | `0d9b43c0032597fb8edecca0ec148381` | 2026-10-22 04:31 |
| `pose_study/inner/d128-L4-lr1e-3-out1-val0.json` | 9.5 KB | `dd360b899ab01b18d4ccb61afcc60a9d` | 2026-10-22 04:33 |
| `pose_study/inner/d128-L4-lr1e-3-out1-val2.json` | 9.5 KB | `6f6740465010b22e25af901aa376eaaf` | 2026-10-22 04:33 |
| `pose_study/inner/d128-L4-lr1e-3-out1-val3.json` | 9.5 KB | `dbbdea9a6f42642aa33482010b6e791b` | 2026-10-22 04:34 |
| `pose_study/inner/d128-L4-lr1e-3-out1-val4.json` | 9.5 KB | `d3010e709756b27870d9d702a3182d79` | 2026-10-22 04:35 |
| `pose_study/inner/d128-L4-lr1e-3-out2-val0.json` | 9.5 KB | `b67ad411356db54b55d9d84f01eac9e2` | 2026-10-22 04:36 |
| `pose_study/inner/d128-L4-lr1e-3-out2-val1.json` | 9.5 KB | `930492dd53fbf30a6b4f4a66a1f01169` | 2026-10-22 04:36 |
| `pose_study/inner/d128-L4-lr1e-3-out2-val3.json` | 9.5 KB | `5b32e9692dce910395837bd2a3c5ab30` | 2026-10-22 04:38 |
| `pose_study/inner/d128-L4-lr1e-3-out2-val4.json` | 9.5 KB | `1ee1fb1dbd82bb57e6af03b31cb7324f` | 2026-10-22 04:38 |
| `pose_study/inner/d128-L4-lr1e-3-out3-val0.json` | 9.5 KB | `dca6a214de84be8e974d45e9ce2efff5` | 2026-10-22 04:40 |
| `pose_study/inner/d128-L4-lr1e-3-out3-val1.json` | 9.5 KB | `f0b982d505235306083fa9868ad6f081` | 2026-10-22 04:40 |
| `pose_study/inner/d128-L4-lr1e-3-out3-val2.json` | 9.5 KB | `e6767de4da4951cd27e803a4d6905930` | 2026-10-22 04:41 |
| `pose_study/inner/d128-L4-lr1e-3-out3-val4.json` | 9.5 KB | `8de6ebef5a01cf10f80dcd5476ab8893` | 2026-10-22 04:42 |
| `pose_study/inner/d128-L4-lr1e-3-out4-val0.json` | 9.5 KB | `e504644ed851fa5e4079e8c9c439f610` | 2026-10-22 04:43 |
| `pose_study/inner/d128-L4-lr1e-3-out4-val1.json` | 9.6 KB | `d71eac1ce8d32aa84f557a7ba49019ab` | 2026-10-22 04:43 |
| `pose_study/inner/d128-L4-lr1e-3-out4-val2.json` | 9.5 KB | `91046532f12da84ffa8c6b964f5f9c5c` | 2026-10-22 04:45 |
| `pose_study/inner/d128-L4-lr1e-3-out4-val3.json` | 9.5 KB | `a7040d5b256acdef5c5ac4e2e32d9ddc` | 2026-10-22 04:45 |
| `pose_study/inner/d128-L4-lr5e-4-out0-val1.json` | 9.5 KB | `cf6fd3c904be522ddd658a2dd38806be` | 2026-10-22 04:12 |
| `pose_study/inner/d128-L4-lr5e-4-out0-val2.json` | 9.5 KB | `04db7959f11d96c92c228198a3bbf2fa` | 2026-10-22 04:13 |
| `pose_study/inner/d128-L4-lr5e-4-out0-val3.json` | 9.5 KB | `3ee03c0efd0a7ea650883930f855604c` | 2026-10-22 04:13 |
| `pose_study/inner/d128-L4-lr5e-4-out0-val4.json` | 9.5 KB | `1be2d0bce05882375738c09bb1e17e31` | 2026-10-22 04:14 |
| `pose_study/inner/d128-L4-lr5e-4-out1-val0.json` | 9.5 KB | `1c836d8aeb38874d06f505301bb51854` | 2026-10-22 04:15 |
| `pose_study/inner/d128-L4-lr5e-4-out1-val2.json` | 9.5 KB | `2c0ed9043c3f137eaf2c3627313dbeb1` | 2026-10-22 04:15 |
| `pose_study/inner/d128-L4-lr5e-4-out1-val3.json` | 9.5 KB | `b69e7f0e5089337dcbb734becbad0fff` | 2026-10-22 04:17 |
| `pose_study/inner/d128-L4-lr5e-4-out1-val4.json` | 9.5 KB | `c3d70249e7872c22f0e3f541e318842a` | 2026-10-22 04:17 |
| `pose_study/inner/d128-L4-lr5e-4-out2-val0.json` | 9.5 KB | `646336342fabfcdcf1278a60c39a1d05` | 2026-10-22 04:19 |
| `pose_study/inner/d128-L4-lr5e-4-out2-val1.json` | 9.5 KB | `f2ced00993867bf80c5299347f98b2c1` | 2026-10-22 04:19 |
| `pose_study/inner/d128-L4-lr5e-4-out2-val3.json` | 9.5 KB | `57e5f29772b4445c571d4be6cabcbccc` | 2026-10-22 04:20 |
| `pose_study/inner/d128-L4-lr5e-4-out2-val4.json` | 9.5 KB | `2bf5a724821037afc445fa93c05081f6` | 2026-10-22 04:21 |
| `pose_study/inner/d128-L4-lr5e-4-out3-val0.json` | 9.5 KB | `81336691b49610efcf9a17ac86836b00` | 2026-10-22 04:22 |
| `pose_study/inner/d128-L4-lr5e-4-out3-val1.json` | 9.5 KB | `43b81ace4928e359c45b5d5087e5f027` | 2026-10-22 04:22 |
| `pose_study/inner/d128-L4-lr5e-4-out3-val2.json` | 9.5 KB | `1361b9f528806649f5c86b23e28a06fd` | 2026-10-22 04:24 |
| `pose_study/inner/d128-L4-lr5e-4-out3-val4.json` | 9.5 KB | `198f65bbec2df8311cd64a1cd02208c1` | 2026-10-22 04:25 |
| `pose_study/inner/d128-L4-lr5e-4-out4-val0.json` | 9.5 KB | `0cd0a12534ac6d1efe8243f050730954` | 2026-10-22 04:25 |
| `pose_study/inner/d128-L4-lr5e-4-out4-val1.json` | 9.6 KB | `8102dc93f852147498e9dd5e7c6fbd7f` | 2026-10-22 04:26 |
| `pose_study/inner/d128-L4-lr5e-4-out4-val2.json` | 9.5 KB | `2c6d9a68da126e9bf14cb754b2045983` | 2026-10-22 04:28 |
| `pose_study/inner/d128-L4-lr5e-4-out4-val3.json` | 9.5 KB | `89634a113d8cce0c45f6a6bb99884fee` | 2026-10-22 04:28 |
| `pose_study/inner/d256-L2-lr1e-3-out0-val1.json` | 9.5 KB | `534b48951564481d7aa63131cd2eb222` | 2026-10-22 05:11 |
| `pose_study/inner/d256-L2-lr1e-3-out0-val2.json` | 9.5 KB | `912d8c4906eed222f0920af9b7ab52fa` | 2026-10-22 05:11 |
| `pose_study/inner/d256-L2-lr1e-3-out0-val3.json` | 9.5 KB | `653749da7df74109f3fd787367735c55` | 2026-10-22 05:13 |
| `pose_study/inner/d256-L2-lr1e-3-out0-val4.json` | 9.5 KB | `69626a88de40b6ccf04595a591428dbc` | 2026-10-22 05:13 |
| `pose_study/inner/d256-L2-lr1e-3-out1-val0.json` | 9.5 KB | `02413ec8fa1dee849106f74029ad3d40` | 2026-10-22 05:15 |
| `pose_study/inner/d256-L2-lr1e-3-out1-val2.json` | 9.5 KB | `0ab980e1bf22e4d2215ba213ae4d4fd1` | 2026-10-22 05:16 |
| `pose_study/inner/d256-L2-lr1e-3-out1-val3.json` | 9.5 KB | `43474f2f079a86e76ca99b69f45c5bac` | 2026-10-22 05:18 |
| `pose_study/inner/d256-L2-lr1e-3-out1-val4.json` | 9.5 KB | `15c768a2aa91e23254866d41f6f27237` | 2026-10-22 05:18 |
| `pose_study/inner/d256-L2-lr1e-3-out2-val0.json` | 9.5 KB | `c255cc3ab78ef3f35e585ad52bda90d2` | 2026-10-22 05:20 |
| `pose_study/inner/d256-L2-lr1e-3-out2-val1.json` | 9.6 KB | `f23f5a478e94e3544f383c505375f5b1` | 2026-10-22 05:20 |
| `pose_study/inner/d256-L2-lr1e-3-out2-val3.json` | 9.5 KB | `3740e5d4d4abeab9e651eb86ee9d8992` | 2026-10-22 05:22 |
| `pose_study/inner/d256-L2-lr1e-3-out2-val4.json` | 9.5 KB | `f0e17af3dd432d628e8919c409f9cac4` | 2026-10-22 05:23 |
| `pose_study/inner/d256-L2-lr1e-3-out3-val0.json` | 9.5 KB | `981d219f690ad4631a077c974e872d14` | 2026-10-22 05:25 |
| `pose_study/inner/d256-L2-lr1e-3-out3-val1.json` | 9.5 KB | `5501c0d27e81d5b26eec9e4f8459743d` | 2026-10-22 05:25 |
| `pose_study/inner/d256-L2-lr1e-3-out3-val2.json` | 9.5 KB | `b07d89fc36ecb9f4203c25b9d8475b8e` | 2026-10-22 05:27 |
| `pose_study/inner/d256-L2-lr1e-3-out3-val4.json` | 9.5 KB | `5177df06fdcab0cdd84677e172f8260f` | 2026-10-22 05:27 |
| `pose_study/inner/d256-L2-lr1e-3-out4-val0.json` | 9.5 KB | `c7c124413ce71a17771cb143825827f3` | 2026-10-22 05:29 |
| `pose_study/inner/d256-L2-lr1e-3-out4-val1.json` | 9.5 KB | `2aabda0ae1837481eca4a381b1cee8b5` | 2026-10-22 05:30 |
| `pose_study/inner/d256-L2-lr1e-3-out4-val2.json` | 9.5 KB | `8fcd38d3d5b2177f5f00b1f9efb37bc6` | 2026-10-22 05:32 |
| `pose_study/inner/d256-L2-lr1e-3-out4-val3.json` | 9.5 KB | `057000235c842776315131d3238e2715` | 2026-10-22 05:32 |
| `pose_study/inner/d256-L2-lr5e-4-out0-val1.json` | 9.5 KB | `3ab6df56b1223eb57512f278c28adb3d` | 2026-10-22 04:48 |
| `pose_study/inner/d256-L2-lr5e-4-out0-val2.json` | 9.5 KB | `ee3286629740929af71c27c09e84be10` | 2026-10-22 04:48 |
| `pose_study/inner/d256-L2-lr5e-4-out0-val3.json` | 9.5 KB | `472b104ca2a3a6d64ce230fd095669ce` | 2026-10-22 04:50 |
| `pose_study/inner/d256-L2-lr5e-4-out0-val4.json` | 9.5 KB | `107ad55e10a300690d603955c9acac9f` | 2026-10-22 04:50 |
| `pose_study/inner/d256-L2-lr5e-4-out1-val0.json` | 9.5 KB | `a1ca2f95dccfc729ce46a7e8d62cd64c` | 2026-10-22 04:52 |
| `pose_study/inner/d256-L2-lr5e-4-out1-val2.json` | 9.5 KB | `f38b376b66f573bb35e11139c4e79f8b` | 2026-10-22 04:52 |
| `pose_study/inner/d256-L2-lr5e-4-out1-val3.json` | 9.5 KB | `f1620052e475ef53c6c4ee0a21059cfe` | 2026-10-22 04:54 |
| `pose_study/inner/d256-L2-lr5e-4-out1-val4.json` | 9.5 KB | `6d6d80eabc174ed1dbd9f3d9fef6350e` | 2026-10-22 04:55 |
| `pose_study/inner/d256-L2-lr5e-4-out2-val0.json` | 9.5 KB | `30845fff0b3ac8bd34dd88672254663d` | 2026-10-22 04:57 |
| `pose_study/inner/d256-L2-lr5e-4-out2-val1.json` | 9.5 KB | `ab09f5e6d9d6117c248d834b7d27053f` | 2026-10-22 04:57 |
| `pose_study/inner/d256-L2-lr5e-4-out2-val3.json` | 9.5 KB | `a5df735da062c36a9a7452d367552242` | 2026-10-22 04:59 |
| `pose_study/inner/d256-L2-lr5e-4-out2-val4.json` | 9.5 KB | `b669358bb3f6f5f295f74c5b95285192` | 2026-10-22 04:59 |
| `pose_study/inner/d256-L2-lr5e-4-out3-val0.json` | 9.5 KB | `c9e47c869ef8b1e9f29772dd5e445163` | 2026-10-22 05:01 |
| `pose_study/inner/d256-L2-lr5e-4-out3-val1.json` | 9.5 KB | `0c53a4a61ca999ab0f7cec5146bfcc55` | 2026-10-22 05:02 |
| `pose_study/inner/d256-L2-lr5e-4-out3-val2.json` | 9.5 KB | `4a91e9d0723555ca20b181dbf6696b4e` | 2026-10-22 05:04 |
| `pose_study/inner/d256-L2-lr5e-4-out3-val4.json` | 9.5 KB | `73c179c7706897ba2bc79d4522695934` | 2026-10-22 05:04 |
| `pose_study/inner/d256-L2-lr5e-4-out4-val0.json` | 9.5 KB | `d5d79cbc8f92450d8b1c738b32752f09` | 2026-10-22 05:06 |
| `pose_study/inner/d256-L2-lr5e-4-out4-val1.json` | 9.5 KB | `d50b3c95d14d5e59caf8333ad7f701d3` | 2026-10-22 05:06 |
| `pose_study/inner/d256-L2-lr5e-4-out4-val2.json` | 9.5 KB | `57506b32bc1271aa01fa1cd3e390c507` | 2026-10-22 05:08 |
| `pose_study/inner/d256-L2-lr5e-4-out4-val3.json` | 9.5 KB | `896af8513e2f7c942cd97aab79f92e62` | 2026-10-22 05:09 |
| `pose_study/inner/d256-L3-lr1e-3-out0-val1.json` | 9.5 KB | `16cb1ec4bc73f41a19c93e78fe7b3fa6` | 2026-10-22 06:10 |
| `pose_study/inner/d256-L3-lr1e-3-out0-val2.json` | 9.5 KB | `0f9960154b673b24c32da50d94c8e9eb` | 2026-10-22 06:10 |
| `pose_study/inner/d256-L3-lr1e-3-out0-val3.json` | 9.5 KB | `bbeac647ef5b4a2ba64a5a2e40479d45` | 2026-10-22 06:12 |
| `pose_study/inner/d256-L3-lr1e-3-out0-val4.json` | 9.5 KB | `a3157558daee7c3fad13e6242616df61` | 2026-10-22 06:13 |
| `pose_study/inner/d256-L3-lr1e-3-out1-val0.json` | 9.5 KB | `167c075c36c177a3be8d202515b8df55` | 2026-10-22 06:15 |
| `pose_study/inner/d256-L3-lr1e-3-out1-val2.json` | 9.5 KB | `bc6a609b7b6c4396bdbe33fd2244fa23` | 2026-10-22 06:17 |
| `pose_study/inner/d256-L3-lr1e-3-out1-val3.json` | 9.5 KB | `daf3adede801e136aa6101ded4af1094` | 2026-10-22 06:20 |
| `pose_study/inner/d256-L3-lr1e-3-out1-val4.json` | 9.5 KB | `7f39b127e9d9ad72221374f69042b7f7` | 2026-10-22 06:21 |
| `pose_study/inner/d256-L3-lr1e-3-out2-val0.json` | 9.5 KB | `09e41b1a0026ddc60f26e16a3aca7e5f` | 2026-10-22 06:23 |
| `pose_study/inner/d256-L3-lr1e-3-out2-val1.json` | 9.5 KB | `f406b7fd6984e46d226cee1beb49d67f` | 2026-10-22 06:23 |
| `pose_study/inner/d256-L3-lr1e-3-out2-val3.json` | 9.5 KB | `cb1eb6bead2bd6a32cb51d1ea836365d` | 2026-10-22 06:25 |
| `pose_study/inner/d256-L3-lr1e-3-out2-val4.json` | 9.5 KB | `1d6daa798b291391755c55e00baa1c94` | 2026-10-22 06:27 |
| `pose_study/inner/d256-L3-lr1e-3-out3-val0.json` | 9.5 KB | `8f18b49fff69b18ac4a2a185e91184e5` | 2026-10-22 06:30 |
| `pose_study/inner/d256-L3-lr1e-3-out3-val1.json` | 9.6 KB | `d06281e47806ff2ce81450fa7ac613c5` | 2026-10-22 06:31 |
| `pose_study/inner/d256-L3-lr1e-3-out3-val2.json` | 9.5 KB | `bcbed7cfed586004204a48c0b5b5d8ee` | 2026-10-22 06:33 |
| `pose_study/inner/d256-L3-lr1e-3-out3-val4.json` | 9.5 KB | `720f15cba2a878cb871969bd6ccf1eee` | 2026-10-22 06:33 |
| `pose_study/inner/d256-L3-lr1e-3-out4-val0.json` | 9.5 KB | `8079a476ca7eccf2cac6eff2fbc240dd` | 2026-10-22 06:35 |
| `pose_study/inner/d256-L3-lr1e-3-out4-val1.json` | 9.5 KB | `6c6a79237d945cba6d287590a1b9f58c` | 2026-10-22 06:37 |
| `pose_study/inner/d256-L3-lr1e-3-out4-val2.json` | 9.5 KB | `4bd56da7f365dc452ed4bdf9bc105994` | 2026-10-22 06:40 |
| `pose_study/inner/d256-L3-lr1e-3-out4-val3.json` | 9.5 KB | `5db6e6c5a1e8de59ef71c945aa96ea73` | 2026-10-22 06:41 |
| `pose_study/inner/d256-L3-lr5e-4-out0-val1.json` | 9.5 KB | `2c246a02d266e2dcc963df28eab0f4f0` | 2026-10-22 05:37 |
| `pose_study/inner/d256-L3-lr5e-4-out0-val2.json` | 9.5 KB | `f4ce0d1c7e1569c66a1fdc9691ffac5b` | 2026-10-22 05:37 |
| `pose_study/inner/d256-L3-lr5e-4-out0-val3.json` | 9.5 KB | `04457502d348c0d66553a22c1bc5a3a6` | 2026-10-22 05:39 |
| `pose_study/inner/d256-L3-lr5e-4-out0-val4.json` | 9.5 KB | `024b24bd22e042a56286a111093d7465` | 2026-10-22 05:40 |
| `pose_study/inner/d256-L3-lr5e-4-out1-val0.json` | 9.5 KB | `9598c28ae7166260fbb554f5e6169dc3` | 2026-10-22 05:42 |
| `pose_study/inner/d256-L3-lr5e-4-out1-val2.json` | 9.5 KB | `b2529c2796a24a2e907947e2ba1d499c` | 2026-10-22 05:42 |
| `pose_study/inner/d256-L3-lr5e-4-out1-val3.json` | 9.5 KB | `70d42eff318fdb6cda17a7fcaf286567` | 2026-10-22 05:44 |
| `pose_study/inner/d256-L3-lr5e-4-out1-val4.json` | 9.5 KB | `f17fe63300cf1d66e2dad56be4b1af35` | 2026-10-22 05:47 |
| `pose_study/inner/d256-L3-lr5e-4-out2-val0.json` | 9.5 KB | `d5a67615aa7c590a3c0c9ad31cf6f4a1` | 2026-10-22 05:50 |
| `pose_study/inner/d256-L3-lr5e-4-out2-val1.json` | 9.5 KB | `cd6aa0c772f1bf3451f6f5ba94296459` | 2026-10-22 05:50 |
| `pose_study/inner/d256-L3-lr5e-4-out2-val3.json` | 9.5 KB | `f767a9674d26a0f43175dcd2b1ae3c19` | 2026-10-22 05:52 |
| `pose_study/inner/d256-L3-lr5e-4-out2-val4.json` | 9.5 KB | `e0475f1a4b94c50b6b93fd57a60cb9e0` | 2026-10-22 05:52 |
| `pose_study/inner/d256-L3-lr5e-4-out3-val0.json` | 9.5 KB | `6890942cec52e983d34426625eec321f` | 2026-10-22 05:55 |
| `pose_study/inner/d256-L3-lr5e-4-out3-val1.json` | 9.6 KB | `11926286eedf65e88f9783336020fa13` | 2026-10-22 05:57 |
| `pose_study/inner/d256-L3-lr5e-4-out3-val2.json` | 9.5 KB | `1638410b7c7552d263a897adb333f321` | 2026-10-22 06:00 |
| `pose_study/inner/d256-L3-lr5e-4-out3-val4.json` | 9.5 KB | `d3a66c42d4031f27e72e2939a2437749` | 2026-10-22 06:00 |
| `pose_study/inner/d256-L3-lr5e-4-out4-val0.json` | 9.5 KB | `0e31933f4e666f10330119fde5897d86` | 2026-10-22 06:02 |
| `pose_study/inner/d256-L3-lr5e-4-out4-val1.json` | 9.5 KB | `1a4d09a0abd4e34e1eed6032d0da8bb9` | 2026-10-22 06:02 |
| `pose_study/inner/d256-L3-lr5e-4-out4-val2.json` | 9.5 KB | `4ff6445144b94a84133dddf55d27d2b5` | 2026-10-22 06:05 |
| `pose_study/inner/d256-L3-lr5e-4-out4-val3.json` | 9.5 KB | `938bc9179dbd7ca61e543b941098bff3` | 2026-10-22 06:07 |
| `pose_study/inner/d256-L4-lr1e-3-out0-val1.json` | 9.5 KB | `6838f3575d6a565ae4baac68a4b23d3e` | 2026-10-22 07:29 |
| `pose_study/inner/d256-L4-lr1e-3-out0-val2.json` | 9.5 KB | `9f89c495b0360738c9073db1e33d157a` | 2026-10-22 07:30 |
| `pose_study/inner/d256-L4-lr1e-3-out0-val3.json` | 9.5 KB | `1159bed833e2e6ae5e4c251c5f4271d3` | 2026-10-22 07:34 |
| `pose_study/inner/d256-L4-lr1e-3-out0-val4.json` | 9.5 KB | `f357f4b8c3d0390b869a77e1c7165bed` | 2026-10-22 07:34 |
| `pose_study/inner/d256-L4-lr1e-3-out1-val0.json` | 9.5 KB | `119397eb0f8bf286eafc4ba1dd15219f` | 2026-10-22 07:38 |
| `pose_study/inner/d256-L4-lr1e-3-out1-val2.json` | 9.5 KB | `1e1d8f17c4955819fd65370b6c8c8312` | 2026-10-22 07:39 |
| `pose_study/inner/d256-L4-lr1e-3-out1-val3.json` | 9.5 KB | `3ba0d3d475df671cc29b776a6d2116e6` | 2026-10-22 07:42 |
| `pose_study/inner/d256-L4-lr1e-3-out1-val4.json` | 9.5 KB | `2e0d7382c313bc0ec804659ff889ea1a` | 2026-10-22 07:44 |
| `pose_study/inner/d256-L4-lr1e-3-out2-val0.json` | 9.5 KB | `b1e1c2923dc6134881d788ba460b3088` | 2026-10-22 07:47 |
| `pose_study/inner/d256-L4-lr1e-3-out2-val1.json` | 9.5 KB | `e8cf35b745731cb9f246bc95f4b1afb2` | 2026-10-22 07:47 |
| `pose_study/inner/d256-L4-lr1e-3-out2-val3.json` | 9.5 KB | `87cb314c78d54ffb9eacc1ab79eca5e5` | 2026-10-22 07:51 |
| `pose_study/inner/d256-L4-lr1e-3-out2-val4.json` | 9.5 KB | `81c08e612a9a6bbf04d68deb54a18ff4` | 2026-10-22 07:52 |
| `pose_study/inner/d256-L4-lr1e-3-out3-val0.json` | 9.5 KB | `cd488cd113320d52bd6fdb70bb0c904b` | 2026-10-22 07:56 |
| `pose_study/inner/d256-L4-lr1e-3-out3-val1.json` | 9.5 KB | `05a7db91ce7a043a28584dd7c62b80a0` | 2026-10-22 07:57 |
| `pose_study/inner/d256-L4-lr1e-3-out3-val2.json` | 9.5 KB | `405bf728b258178cc5a032044e9f64aa` | 2026-10-22 08:00 |
| `pose_study/inner/d256-L4-lr1e-3-out3-val4.json` | 9.5 KB | `ff5c574feb56b00657cf8c31797cc851` | 2026-10-22 08:00 |
| `pose_study/inner/d256-L4-lr1e-3-out4-val0.json` | 9.5 KB | `2775964c9ee339591dde3e377aecc874` | 2026-10-22 08:04 |
| `pose_study/inner/d256-L4-lr1e-3-out4-val1.json` | 9.5 KB | `2de214a76fda112898b5f731dd8c1fb8` | 2026-10-22 08:05 |
| `pose_study/inner/d256-L4-lr1e-3-out4-val2.json` | 9.5 KB | `3dbc2888e682434714b47af5351e4ae2` | 2026-10-22 08:09 |
| `pose_study/inner/d256-L4-lr1e-3-out4-val3.json` | 9.5 KB | `5309890fb8e6f823a5d4d1e2333c04cb` | 2026-10-22 08:10 |
| `pose_study/inner/d256-L4-lr5e-4-out0-val1.json` | 9.5 KB | `bcf3ec2acee35cc4d59a1476db504ea2` | 2026-10-22 06:46 |
| `pose_study/inner/d256-L4-lr5e-4-out0-val2.json` | 9.5 KB | `1bb1122ea1f67af3f10427f7f2f769bd` | 2026-10-22 06:46 |
| `pose_study/inner/d256-L4-lr5e-4-out0-val3.json` | 9.5 KB | `cb93a490a4a04a40162524c57b0ebcb4` | 2026-10-22 06:49 |
| `pose_study/inner/d256-L4-lr5e-4-out0-val4.json` | 9.5 KB | `7b306605fd7a948ae50a4618e031100d` | 2026-10-22 06:51 |
| `pose_study/inner/d256-L4-lr5e-4-out1-val0.json` | 9.5 KB | `211d0233995aa89ec1914fccb8452154` | 2026-10-22 06:54 |
| `pose_study/inner/d256-L4-lr5e-4-out1-val2.json` | 9.5 KB | `4ac341ac3c31cb9793a3fd39a721b442` | 2026-10-22 06:54 |
| `pose_study/inner/d256-L4-lr5e-4-out1-val3.json` | 9.5 KB | `ae2532432f4e40c7cd2443d6e7532cd5` | 2026-10-22 06:58 |
| `pose_study/inner/d256-L4-lr5e-4-out1-val4.json` | 9.5 KB | `2e54be0a6efc0a12061b50862b7bad13` | 2026-10-22 07:00 |
| `pose_study/inner/d256-L4-lr5e-4-out2-val0.json` | 9.5 KB | `b70fc892576ea1e2d53ec60a589e2ff6` | 2026-10-22 07:02 |
| `pose_study/inner/d256-L4-lr5e-4-out2-val1.json` | 9.5 KB | `1564b5b280e2616729e6dec93c8e1474` | 2026-10-22 07:04 |
| `pose_study/inner/d256-L4-lr5e-4-out2-val3.json` | 9.5 KB | `f0bed23cacfa476c2fd9496d77f79343` | 2026-10-22 07:07 |
| `pose_study/inner/d256-L4-lr5e-4-out2-val4.json` | 9.5 KB | `69c2532582a36349e0c7227eb64b19e1` | 2026-10-22 07:08 |
| `pose_study/inner/d256-L4-lr5e-4-out3-val0.json` | 9.5 KB | `6f633c555aec42d6b925c4a4d91e98de` | 2026-10-22 07:11 |
| `pose_study/inner/d256-L4-lr5e-4-out3-val1.json` | 9.6 KB | `3e5e6e090f58d3cc481ba61ce47143ee` | 2026-10-22 07:13 |
| `pose_study/inner/d256-L4-lr5e-4-out3-val2.json` | 9.5 KB | `5674ee10363830b18cf61186407833fe` | 2026-10-22 07:16 |
| `pose_study/inner/d256-L4-lr5e-4-out3-val4.json` | 9.5 KB | `b546600ec88408194bba974b58b5ef3d` | 2026-10-22 07:17 |
| `pose_study/inner/d256-L4-lr5e-4-out4-val0.json` | 9.5 KB | `e00b3028edc0528df51e2562867791dd` | 2026-10-22 07:21 |
| `pose_study/inner/d256-L4-lr5e-4-out4-val1.json` | 9.5 KB | `a4e1550501ca55539dede4b35968d5e8` | 2026-10-22 07:21 |
| `pose_study/inner/d256-L4-lr5e-4-out4-val2.json` | 9.5 KB | `32c7923bb4aab121ec4922f704c73f03` | 2026-10-22 07:24 |
| `pose_study/inner/d256-L4-lr5e-4-out4-val3.json` | 9.5 KB | `e45e5df0187b4f73c820f643400cb85d` | 2026-10-22 07:26 |
| `pose_study/inner/d64-L2-lr1e-3-out0-val1.json` | 9.5 KB | `9468bdaeb1f65bc76475e2ac77232244` | 2026-10-22 02:44 |
| `pose_study/inner/d64-L2-lr1e-3-out0-val2.json` | 9.5 KB | `d4416bea276d09a122aa5da74c577090` | 2026-10-22 02:44 |
| `pose_study/inner/d64-L2-lr1e-3-out0-val3.json` | 9.5 KB | `a7a6b05b6ee436378e8bf47f2c2ff848` | 2026-10-22 02:44 |
| `pose_study/inner/d64-L2-lr1e-3-out0-val4.json` | 9.5 KB | `2c5d7c7afd550da5904a92aefdf18fca` | 2026-10-22 02:45 |
| `pose_study/inner/d64-L2-lr1e-3-out1-val0.json` | 9.5 KB | `305ea19e5d1fc7420e8808bbc1e5528d` | 2026-10-22 02:45 |
| `pose_study/inner/d64-L2-lr1e-3-out1-val2.json` | 9.5 KB | `a80f5b866c6c87219bab13ea1f4a9c66` | 2026-10-22 02:45 |
| `pose_study/inner/d64-L2-lr1e-3-out1-val3.json` | 9.5 KB | `7ecd0e89d205dc2a5a0b0d1e9dc7df8f` | 2026-10-22 02:46 |
| `pose_study/inner/d64-L2-lr1e-3-out1-val4.json` | 9.5 KB | `e0b0fae5158a20014cf9789d5be15638` | 2026-10-22 02:46 |
| `pose_study/inner/d64-L2-lr1e-3-out2-val0.json` | 9.5 KB | `80fa4b8a82a3d860e57b84a8fc5e6c20` | 2026-10-22 02:46 |
| `pose_study/inner/d64-L2-lr1e-3-out2-val1.json` | 9.5 KB | `9c37f4b988932c93282c684337ab901e` | 2026-10-22 02:46 |
| `pose_study/inner/d64-L2-lr1e-3-out2-val3.json` | 9.5 KB | `41d931bed3ae2b3b46e427aabd6847e7` | 2026-10-22 02:47 |
| `pose_study/inner/d64-L2-lr1e-3-out2-val4.json` | 9.5 KB | `42fa814e8bc1f2fd5c4b294e3fbf853e` | 2026-10-22 02:47 |
| `pose_study/inner/d64-L2-lr1e-3-out3-val0.json` | 9.5 KB | `5525e10b5ba82400a980139999a207a0` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out3-val1.json` | 9.5 KB | `6844701da0c39c424924a002c544500d` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out3-val2.json` | 9.5 KB | `9b0f36f4e082f32484cca2f585f024f1` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out3-val4.json` | 9.5 KB | `5cd19fdbf4fce6204c58b6f925cb0ab9` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out4-val0.json` | 9.5 KB | `864343d343301d29d5a374b9c825ef55` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out4-val1.json` | 9.5 KB | `697188347ac1ca220f71fb7f8e199a5e` | 2026-10-22 02:48 |
| `pose_study/inner/d64-L2-lr1e-3-out4-val2.json` | 9.5 KB | `7ee81d0da50863e7b5c2cf9c3c7aae8c` | 2026-10-22 02:49 |
| `pose_study/inner/d64-L2-lr1e-3-out4-val3.json` | 9.5 KB | `ce695759400be73f10da474f9a7b65ee` | 2026-10-22 02:49 |
| `pose_study/inner/d64-L2-lr5e-4-out0-val1.json` | 9.5 KB | `0bb2c52c83e32c2d7ac1b19de20dfc4b` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out0-val2.json` | 9.5 KB | `6baabeae93bf879bb4442cf1f788e8c4` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out0-val3.json` | 9.5 KB | `8fdf04003ff35c80181b6a12ece654e0` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out0-val4.json` | 9.5 KB | `00190daf280c409d320703d6359304b9` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out1-val0.json` | 9.5 KB | `1d0b3ee0960e8008d845b39664079ae0` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out1-val2.json` | 9.5 KB | `86a3a80fd8a15273930571eb6c137812` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out1-val3.json` | 9.5 KB | `b06cfaf1e154f242ab0a8056f56a0586` | 2026-10-22 02:39 |
| `pose_study/inner/d64-L2-lr5e-4-out1-val4.json` | 9.5 KB | `e1eb490ba33bbf23a7d73032a96e84cc` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out2-val0.json` | 9.5 KB | `f09fe1ca699f23a53a9fd218d9fb15d8` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out2-val1.json` | 9.5 KB | `669ba44416dc5954000dfcfac8ca8bb6` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out2-val3.json` | 9.5 KB | `ed8c5628d5d26ea48598b3270fe15f62` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out2-val4.json` | 9.5 KB | `1508d8996580ae7f9e5c249c03209098` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out3-val0.json` | 9.5 KB | `3f5b8d85ef590d33c224d9de09dc70a6` | 2026-10-22 02:41 |
| `pose_study/inner/d64-L2-lr5e-4-out3-val1.json` | 9.5 KB | `71cd2eefe4352953bddf5c4fd1fd2de3` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out3-val2.json` | 9.5 KB | `0d1f5a9518c59a67aafb2d679417c2c6` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out3-val4.json` | 9.5 KB | `f77975e0190bfa72310f1f31d88fb509` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out4-val0.json` | 9.5 KB | `682bea9d25829bb19850148e24fd6cf8` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out4-val1.json` | 9.5 KB | `00f8c9f7dd48a4e4fffe6258e4823427` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out4-val2.json` | 9.5 KB | `20553d85e0bce9fd92dee4a7a2d81ca4` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L2-lr5e-4-out4-val3.json` | 9.5 KB | `671bd2e4311649eb5a83f857dadce28f` | 2026-10-22 02:43 |
| `pose_study/inner/d64-L3-lr1e-3-out0-val1.json` | 9.5 KB | `1e04b32500276f365f755635a90a3722` | 2026-10-22 02:57 |
| `pose_study/inner/d64-L3-lr1e-3-out0-val2.json` | 9.5 KB | `94a7af0bacb9fdfa9f016c8dcd4f1add` | 2026-10-22 02:57 |
| `pose_study/inner/d64-L3-lr1e-3-out0-val3.json` | 9.5 KB | `a5240f0ca46ffa7cdbe16e995dad9116` | 2026-10-22 02:58 |
| `pose_study/inner/d64-L3-lr1e-3-out0-val4.json` | 9.5 KB | `83684cca1cb090069e7ae71ba4ca4e5a` | 2026-10-22 02:58 |
| `pose_study/inner/d64-L3-lr1e-3-out1-val0.json` | 9.5 KB | `aa6fbe061198c0065ca91b4f43e1e089` | 2026-10-22 02:59 |
| `pose_study/inner/d64-L3-lr1e-3-out1-val2.json` | 9.5 KB | `8f943d6b419f436cbbbdcb97b504076c` | 2026-10-22 02:59 |
| `pose_study/inner/d64-L3-lr1e-3-out1-val3.json` | 9.5 KB | `d3d92aec52be8844354415457515c976` | 2026-10-22 02:59 |
| `pose_study/inner/d64-L3-lr1e-3-out1-val4.json` | 9.5 KB | `f021da3e8a8b885b5b60fa27ff72aedb` | 2026-10-22 03:00 |
| `pose_study/inner/d64-L3-lr1e-3-out2-val0.json` | 9.6 KB | `537e4b4816968bfdad81767a6b20c428` | 2026-10-22 03:01 |
| `pose_study/inner/d64-L3-lr1e-3-out2-val1.json` | 9.5 KB | `79bf801bdb7aa301fb7924043e2197a4` | 2026-10-22 03:01 |
| `pose_study/inner/d64-L3-lr1e-3-out2-val3.json` | 9.5 KB | `d5fb2db5a8340b9668f19e22857277ea` | 2026-10-22 03:01 |
| `pose_study/inner/d64-L3-lr1e-3-out2-val4.json` | 9.5 KB | `a8b4fd904fe0920a579545d184ea6083` | 2026-10-22 03:02 |
| `pose_study/inner/d64-L3-lr1e-3-out3-val0.json` | 9.5 KB | `82dcf6b6f579664508a757e17c297476` | 2026-10-22 03:02 |
| `pose_study/inner/d64-L3-lr1e-3-out3-val1.json` | 9.5 KB | `7bcb75653d9d6b8222078ed9e6cc53c6` | 2026-10-22 03:02 |
| `pose_study/inner/d64-L3-lr1e-3-out3-val2.json` | 9.5 KB | `57548d93514d0ce0eff33f381dbe542e` | 2026-10-22 03:03 |
| `pose_study/inner/d64-L3-lr1e-3-out3-val4.json` | 9.5 KB | `965b1884923d4074e2bc04b5dc7f7b39` | 2026-10-22 03:03 |
| `pose_study/inner/d64-L3-lr1e-3-out4-val0.json` | 9.5 KB | `bb008d0911124bd14ef93cdd6c0949bb` | 2026-10-22 03:04 |
| `pose_study/inner/d64-L3-lr1e-3-out4-val1.json` | 9.5 KB | `971bff8dcb6162ea80ae57a0a57d3501` | 2026-10-22 03:04 |
| `pose_study/inner/d64-L3-lr1e-3-out4-val2.json` | 9.5 KB | `6f3217e019fade0f28ef7fc79623b1f4` | 2026-10-22 03:04 |
| `pose_study/inner/d64-L3-lr1e-3-out4-val3.json` | 9.5 KB | `36b6e13bde46bc991d485f2e842aece1` | 2026-10-22 03:04 |
| `pose_study/inner/d64-L3-lr5e-4-out0-val1.json` | 9.5 KB | `632d556291e70673c3ce9007aaa9452c` | 2026-10-22 02:50 |
| `pose_study/inner/d64-L3-lr5e-4-out0-val2.json` | 9.5 KB | `11d9a4660afafe8a657876be9d49f0c6` | 2026-10-22 02:51 |
| `pose_study/inner/d64-L3-lr5e-4-out0-val3.json` | 9.5 KB | `18ffdcf83a024c0ee8d847bad5783f1e` | 2026-10-22 02:50 |
| `pose_study/inner/d64-L3-lr5e-4-out0-val4.json` | 9.5 KB | `85b61dc0b1036cd98ceab8736bd302a2` | 2026-10-22 02:51 |
| `pose_study/inner/d64-L3-lr5e-4-out1-val0.json` | 9.5 KB | `e9a733ef7ed479874390337b86a390de` | 2026-10-22 02:51 |
| `pose_study/inner/d64-L3-lr5e-4-out1-val2.json` | 9.5 KB | `3b517b5a1c211db93ef34db02c06f591` | 2026-10-22 02:51 |
| `pose_study/inner/d64-L3-lr5e-4-out1-val3.json` | 9.5 KB | `e20d60d1fe15596b9b7b47d899461d22` | 2026-10-22 02:52 |
| `pose_study/inner/d64-L3-lr5e-4-out1-val4.json` | 9.5 KB | `b65471feeb4b57f5e7efbd2249cc6884` | 2026-10-22 02:53 |
| `pose_study/inner/d64-L3-lr5e-4-out2-val0.json` | 9.5 KB | `756e84cf59294e049734e6d449dcc0f9` | 2026-10-22 02:53 |
| `pose_study/inner/d64-L3-lr5e-4-out2-val1.json` | 9.5 KB | `0aa3efa21e9cf8f2e8d566a17af133c4` | 2026-10-22 02:53 |
| `pose_study/inner/d64-L3-lr5e-4-out2-val3.json` | 9.5 KB | `278889d058d349c2420e04681b108c3d` | 2026-10-22 02:54 |
| `pose_study/inner/d64-L3-lr5e-4-out2-val4.json` | 9.5 KB | `500a9fcfa2a499feefc412c1854ebbab` | 2026-10-22 02:54 |
| `pose_study/inner/d64-L3-lr5e-4-out3-val0.json` | 9.5 KB | `811a1975c0885791645881afc1aceae8` | 2026-10-22 02:54 |
| `pose_study/inner/d64-L3-lr5e-4-out3-val1.json` | 9.5 KB | `4b3a0527075809c390b345ad13cd2bc8` | 2026-10-22 02:55 |
| `pose_study/inner/d64-L3-lr5e-4-out3-val2.json` | 9.5 KB | `3535d8be04581205a8fe3f756fd0cf34` | 2026-10-22 02:55 |
| `pose_study/inner/d64-L3-lr5e-4-out3-val4.json` | 9.5 KB | `dc24710ae9fe0b2039bae26a6604d608` | 2026-10-22 02:55 |
| `pose_study/inner/d64-L3-lr5e-4-out4-val0.json` | 9.5 KB | `1f4ad0758e994026fcab86cedef20156` | 2026-10-22 02:56 |
| `pose_study/inner/d64-L3-lr5e-4-out4-val1.json` | 9.5 KB | `d12dd6719323040c19e1e82dc2b0b280` | 2026-10-22 02:56 |
| `pose_study/inner/d64-L3-lr5e-4-out4-val2.json` | 9.5 KB | `b24d3ea0aa5d5e5494684cddce6c1118` | 2026-10-22 02:57 |
| `pose_study/inner/d64-L3-lr5e-4-out4-val3.json` | 9.5 KB | `d44b6541ba0f156fa2d4cd1174784fd5` | 2026-10-22 02:57 |
| `pose_study/inner/d64-L4-lr1e-3-out0-val1.json` | 9.5 KB | `bdcd9a838a94cc74410fbcdfbca5f944` | 2026-10-22 03:15 |
| `pose_study/inner/d64-L4-lr1e-3-out0-val2.json` | 9.5 KB | `669713726ebfce5e0802c87b7880fb2c` | 2026-10-22 03:15 |
| `pose_study/inner/d64-L4-lr1e-3-out0-val3.json` | 9.5 KB | `cc64a8a8b1394cbdd7193282c0f32023` | 2026-10-22 03:15 |
| `pose_study/inner/d64-L4-lr1e-3-out0-val4.json` | 9.5 KB | `9eead0e7110335680d454b64850d864e` | 2026-10-22 03:16 |
| `pose_study/inner/d64-L4-lr1e-3-out1-val0.json` | 9.5 KB | `58e5bf16b81d3609743f7a0819defd7c` | 2026-10-22 03:16 |
| `pose_study/inner/d64-L4-lr1e-3-out1-val2.json` | 9.5 KB | `5588f586e713adb6cf03edf927f7fc14` | 2026-10-22 03:17 |
| `pose_study/inner/d64-L4-lr1e-3-out1-val3.json` | 9.5 KB | `7cec15978881e59902272dbe4ac9bc7b` | 2026-10-22 03:18 |
| `pose_study/inner/d64-L4-lr1e-3-out1-val4.json` | 9.5 KB | `4fc787bca46eff8af67a50fb0ae4103d` | 2026-10-22 03:18 |
| `pose_study/inner/d64-L4-lr1e-3-out2-val0.json` | 9.5 KB | `ef8b45f2a833780d1995b0c97f82efee` | 2026-10-22 03:18 |
| `pose_study/inner/d64-L4-lr1e-3-out2-val1.json` | 9.6 KB | `773de9ff3debef02bbde806678f27c4c` | 2026-10-22 03:19 |
| `pose_study/inner/d64-L4-lr1e-3-out2-val3.json` | 9.5 KB | `a909ff50f924fdbbc3f5631e0e38e84f` | 2026-10-22 03:19 |
| `pose_study/inner/d64-L4-lr1e-3-out2-val4.json` | 9.5 KB | `e5639b8a64a1ce1ff379c9f7d5a69f3c` | 2026-10-22 03:20 |
| `pose_study/inner/d64-L4-lr1e-3-out3-val0.json` | 9.5 KB | `d9d3025eb91e45792dcf67c8428a553a` | 2026-10-22 03:21 |
| `pose_study/inner/d64-L4-lr1e-3-out3-val1.json` | 9.5 KB | `fbad6704e0eda09d17a3ddaae6ae8817` | 2026-10-22 03:21 |
| `pose_study/inner/d64-L4-lr1e-3-out3-val2.json` | 9.5 KB | `973f0896a71bc940b7c4b8a23dfc4bbc` | 2026-10-22 03:21 |
| `pose_study/inner/d64-L4-lr1e-3-out3-val4.json` | 9.5 KB | `eec1e4b7f79e5999bc744b7e1fe1a1c3` | 2026-10-22 03:22 |
| `pose_study/inner/d64-L4-lr1e-3-out4-val0.json` | 9.6 KB | `8d1a20c10876a7f30816d8c75f6ca87c` | 2026-10-22 03:22 |
| `pose_study/inner/d64-L4-lr1e-3-out4-val1.json` | 9.5 KB | `ebd8ccbf586c3fea311ad785484142e2` | 2026-10-22 03:23 |
| `pose_study/inner/d64-L4-lr1e-3-out4-val2.json` | 9.5 KB | `9c0c7fbdfb5ba8af18df0061d4dc8000` | 2026-10-22 03:24 |
| `pose_study/inner/d64-L4-lr1e-3-out4-val3.json` | 9.5 KB | `2c72636d96bf015ef53e75b2576457c2` | 2026-10-22 03:24 |
| `pose_study/inner/d64-L4-lr5e-4-out0-val1.json` | 9.5 KB | `8ed12898ad64fb3ba8cba220b9704a70` | 2026-10-22 03:06 |
| `pose_study/inner/d64-L4-lr5e-4-out0-val2.json` | 9.5 KB | `5eb41dcaaceb736a9d938a1a87749fd7` | 2026-10-22 03:06 |
| `pose_study/inner/d64-L4-lr5e-4-out0-val3.json` | 9.5 KB | `e0782f7bb666e8cad68dac1b0999300a` | 2026-10-22 03:06 |
| `pose_study/inner/d64-L4-lr5e-4-out0-val4.json` | 9.5 KB | `28a9efab37951e42076bfebeac216a2b` | 2026-10-22 03:07 |
| `pose_study/inner/d64-L4-lr5e-4-out1-val0.json` | 9.5 KB | `e549c52fd7f2527e0c6362d1b036bc6c` | 2026-10-22 03:07 |
| `pose_study/inner/d64-L4-lr5e-4-out1-val2.json` | 9.5 KB | `b882205a56fc65f0f5744f375936610c` | 2026-10-22 03:07 |
| `pose_study/inner/d64-L4-lr5e-4-out1-val3.json` | 9.5 KB | `d4f17883e4098245807c719f8eef757e` | 2026-10-22 03:08 |
| `pose_study/inner/d64-L4-lr5e-4-out1-val4.json` | 9.5 KB | `3b17c0d3049932d435d25c5a65148d41` | 2026-10-22 03:09 |
| `pose_study/inner/d64-L4-lr5e-4-out2-val0.json` | 9.5 KB | `edb81fc2b00a69b8adb5765e4a9e6a32` | 2026-10-22 03:09 |
| `pose_study/inner/d64-L4-lr5e-4-out2-val1.json` | 9.5 KB | `72c71f8adc557cd516ebfa7fb4c12764` | 2026-10-22 03:09 |
| `pose_study/inner/d64-L4-lr5e-4-out2-val3.json` | 9.5 KB | `1273f1e6467821adef22aa5a6f2f14a8` | 2026-10-22 03:10 |
| `pose_study/inner/d64-L4-lr5e-4-out2-val4.json` | 9.5 KB | `19b39c119e46544d5420504bd0d5b993` | 2026-10-22 03:10 |
| `pose_study/inner/d64-L4-lr5e-4-out3-val0.json` | 9.5 KB | `076ba08bbbe5c54b38956b820b776c5c` | 2026-10-22 03:11 |
| `pose_study/inner/d64-L4-lr5e-4-out3-val1.json` | 9.5 KB | `fb35cbff86c293240ce76dc1bcda8834` | 2026-10-22 03:11 |
| `pose_study/inner/d64-L4-lr5e-4-out3-val2.json` | 9.5 KB | `ad3a9cbbff61d26d79ffef74280bb038` | 2026-10-22 03:12 |
| `pose_study/inner/d64-L4-lr5e-4-out3-val4.json` | 9.5 KB | `93abbb903352f1e147da56f04411c9ed` | 2026-10-22 03:12 |
| `pose_study/inner/d64-L4-lr5e-4-out4-val0.json` | 9.5 KB | `41ea004948af6c770230b8ca8770dadb` | 2026-10-22 03:12 |
| `pose_study/inner/d64-L4-lr5e-4-out4-val1.json` | 9.5 KB | `1ce19bb2733e8b6979339404bcaa30ab` | 2026-10-22 03:13 |
| `pose_study/inner/d64-L4-lr5e-4-out4-val2.json` | 9.5 KB | `961d5e4ea2bb3ebcf174c87af40113b1` | 2026-10-22 03:14 |
| `pose_study/inner/d64-L4-lr5e-4-out4-val3.json` | 9.5 KB | `3eb5dd3cf5c46c3417a0389b54f3f4e9` | 2026-10-22 03:14 |
| `pose_study/nested/pose-loso-s0-seed0.json` | 9.5 KB | `e665c468fa4676b01e381315c8606511` | 2026-10-22 11:45 |
| `pose_study/nested/pose-loso-s0-seed1.json` | 9.5 KB | `97251aca540bec7b2fa222b5071e7492` | 2026-10-22 11:45 |
| `pose_study/nested/pose-loso-s0-seed2.json` | 9.5 KB | `f788af3802f1c3ceb4a57cd89e9fc8ba` | 2026-10-22 11:45 |
| `pose_study/nested/pose-loso-s0-seed3.json` | 9.5 KB | `51d0ffc2723fcff3e00d023d00ff547e` | 2026-10-22 11:45 |
| `pose_study/nested/pose-loso-s0-seed4.json` | 9.5 KB | `3f9aec4fa2551d3d0983af87154d5e40` | 2026-10-22 11:45 |
| `pose_study/nested/pose-loso-s1-seed0.json` | 9.5 KB | `018353eafa5ce0dd61d11053a175a451` | 2026-10-22 11:41 |
| `pose_study/nested/pose-loso-s1-seed1.json` | 9.5 KB | `bafd310360a2e6d2d3729182458fdba5` | 2026-10-22 11:41 |
| `pose_study/nested/pose-loso-s1-seed2.json` | 9.5 KB | `b1b8f2e3dca01053a0d7e088ab66492f` | 2026-10-22 11:41 |
| `pose_study/nested/pose-loso-s1-seed3.json` | 9.5 KB | `ee7a63877822e8e82e64b3d4f3247c7b` | 2026-10-22 11:50 |
| `pose_study/nested/pose-loso-s1-seed4.json` | 9.5 KB | `f492503e49b5e228f200eab47fe8aec2` | 2026-10-22 11:50 |
| `pose_study/nested/pose-loso-s2-seed0.json` | 9.5 KB | `df5ed0d088346386d101d16cb56b7885` | 2026-10-22 11:54 |
| `pose_study/nested/pose-loso-s2-seed1.json` | 9.5 KB | `4f98398eacce000cfa941ebe4f1dbbdd` | 2026-10-22 11:58 |
| `pose_study/nested/pose-loso-s2-seed2.json` | 9.5 KB | `3f8ef07708e5271caa369bed80f04aa3` | 2026-10-22 11:58 |
| `pose_study/nested/pose-loso-s2-seed3.json` | 9.5 KB | `4a38c175839196d03d947d6c6bcff903` | 2026-10-22 11:58 |
| `pose_study/nested/pose-loso-s2-seed4.json` | 9.5 KB | `9a49f6e1c2e154b4bc73ed38a99a1b89` | 2026-10-22 11:59 |
| `pose_study/nested/pose-loso-s3-seed0.json` | 9.5 KB | `beb3eef41fa7ff0ed876d1f15fb52027` | 2026-10-22 11:49 |
| `pose_study/nested/pose-loso-s3-seed1.json` | 9.5 KB | `520316e6743d9b4b3b9f6a319ee73e8d` | 2026-10-22 11:53 |
| `pose_study/nested/pose-loso-s3-seed2.json` | 9.5 KB | `d79b5fb23d5f253e00096db69d383033` | 2026-10-22 11:54 |
| `pose_study/nested/pose-loso-s3-seed3.json` | 9.5 KB | `ac15dec56aaa036a1c89bda32824caaa` | 2026-10-22 11:54 |
| `pose_study/nested/pose-loso-s3-seed4.json` | 9.5 KB | `0c4608810177c71182a54e35d9767654` | 2026-10-22 11:57 |
| `pose_study/nested/pose-loso-s4-seed0.json` | 9.5 KB | `24119995ae3fd84fadcc7e81e895bc57` | 2026-10-22 12:05 |
| `pose_study/nested/pose-loso-s4-seed1.json` | 9.5 KB | `3109e31ed3dce72282bf0a4943c63671` | 2026-10-22 12:05 |
| `pose_study/nested/pose-loso-s4-seed2.json` | 9.5 KB | `7a848f33143c651798bf4f27bf42fd85` | 2026-10-22 12:05 |
| `pose_study/nested/pose-loso-s4-seed3.json` | 9.5 KB | `1f20bb8bfa2fd3cd6dc631e585469d41` | 2026-10-22 12:07 |
| `pose_study/nested/pose-loso-s4-seed4.json` | 9.5 KB | `0b9870552c04d7ce72ad00d55185c26a` | 2026-10-22 12:08 |
| `pose_study/sensitivity/d128-L2-lr1e-3-s0.json` | 9.5 KB | `b5286b33766a2aecb62a45dd437c138e` | 2026-10-22 03:36 |
| `pose_study/sensitivity/d128-L2-lr1e-3-s1.json` | 9.5 KB | `03b54bf97152e5554911c869c6d4733f` | 2026-10-22 03:38 |
| `pose_study/sensitivity/d128-L2-lr1e-3-s2.json` | 9.5 KB | `76b1b2727fc0d1c930294f429ccb26c7` | 2026-10-22 03:40 |
| `pose_study/sensitivity/d128-L2-lr1e-3-s3.json` | 9.5 KB | `275c8663fdff721eb716c081ddf361f4` | 2026-10-22 03:42 |
| `pose_study/sensitivity/d128-L2-lr1e-3-s4.json` | 9.5 KB | `2502885581b9bfd2fc67b63baafaa280` | 2026-10-22 03:44 |
| `pose_study/sensitivity/d128-L2-lr5e-4-s0.json` | 9.5 KB | `b24ec0ab465281d3ab99fb4d13d7f468` | 2026-10-22 03:26 |
| `pose_study/sensitivity/d128-L2-lr5e-4-s1.json` | 9.5 KB | `3ee833d0afab4d4113d49b931dda599b` | 2026-10-22 03:29 |
| `pose_study/sensitivity/d128-L2-lr5e-4-s2.json` | 9.5 KB | `c60abafded68dab0ff6170b02288c65e` | 2026-10-22 03:31 |
| `pose_study/sensitivity/d128-L2-lr5e-4-s3.json` | 9.5 KB | `7d921528fe5a978aab073684254a2fbc` | 2026-10-22 03:33 |
| `pose_study/sensitivity/d128-L2-lr5e-4-s4.json` | 9.5 KB | `d7d69becbdab9d14cd6ce9ccb4980e85` | 2026-10-22 03:34 |
| `pose_study/sensitivity/d128-L3-lr1e-3-s0.json` | 9.5 KB | `fe1803ae9c8509f2c206faa74b994acb` | 2026-10-22 04:01 |
| `pose_study/sensitivity/d128-L3-lr1e-3-s1.json` | 9.5 KB | `f9e999d32131b7eaafee98898928ceb8` | 2026-10-22 04:04 |
| `pose_study/sensitivity/d128-L3-lr1e-3-s2.json` | 9.5 KB | `e69477539a67956bc01f678536bbaed9` | 2026-10-22 04:06 |
| `pose_study/sensitivity/d128-L3-lr1e-3-s3.json` | 9.5 KB | `9cbbbb66f1c4b594894e152aac51b0e4` | 2026-10-22 04:09 |
| `pose_study/sensitivity/d128-L3-lr1e-3-s4.json` | 9.5 KB | `c35841084792e61373d8ad229f310f4f` | 2026-10-22 04:12 |
| `pose_study/sensitivity/d128-L3-lr5e-4-s0.json` | 9.5 KB | `abe31d7746816b91afe9511f9389b40f` | 2026-10-22 03:47 |
| `pose_study/sensitivity/d128-L3-lr5e-4-s1.json` | 9.5 KB | `e4f4a291d9cfeeccbd5d1fdf4eb62652` | 2026-10-22 03:50 |
| `pose_study/sensitivity/d128-L3-lr5e-4-s2.json` | 9.5 KB | `ce9176b571050a3f7516baf93b1a1216` | 2026-10-22 03:53 |
| `pose_study/sensitivity/d128-L3-lr5e-4-s3.json` | 9.5 KB | `d097d16302cc1f619a6f73ebcaa6e2ba` | 2026-10-22 03:56 |
| `pose_study/sensitivity/d128-L3-lr5e-4-s4.json` | 9.5 KB | `484b207015e23f0193ee2ac9e79aa0df` | 2026-10-22 03:58 |
| `pose_study/sensitivity/d128-L4-lr1e-3-s0.json` | 9.5 KB | `2be376ce0c3211353e1d9f0184057977` | 2026-10-22 04:34 |
| `pose_study/sensitivity/d128-L4-lr1e-3-s1.json` | 9.5 KB | `5992c56df7d578e0a4b76f28effd84c4` | 2026-10-22 04:37 |
| `pose_study/sensitivity/d128-L4-lr1e-3-s2.json` | 9.5 KB | `9d2e8fb8e5978d5abdb77e3ac90e1175` | 2026-10-22 04:40 |
| `pose_study/sensitivity/d128-L4-lr1e-3-s3.json` | 9.5 KB | `5bf6db881fddb8d105307015a9515349` | 2026-10-22 04:44 |
| `pose_study/sensitivity/d128-L4-lr1e-3-s4.json` | 9.5 KB | `28c94a1bf48c1fcf1f4a0063063084b5` | 2026-10-22 04:48 |
| `pose_study/sensitivity/d128-L4-lr5e-4-s0.json` | 9.5 KB | `a6157c58c2be838195d3af27fd03a28c` | 2026-10-22 04:16 |
| `pose_study/sensitivity/d128-L4-lr5e-4-s1.json` | 9.5 KB | `e03ab88be8f561c3d5737a63b9beab66` | 2026-10-22 04:20 |
| `pose_study/sensitivity/d128-L4-lr5e-4-s2.json` | 9.5 KB | `711bed2af111b138ec4656e7d44eab8d` | 2026-10-22 04:23 |
| `pose_study/sensitivity/d128-L4-lr5e-4-s3.json` | 9.5 KB | `a8ab2948f9d0f72c43640b1afc7d9df4` | 2026-10-22 04:27 |
| `pose_study/sensitivity/d128-L4-lr5e-4-s4.json` | 9.5 KB | `d906a7470227a6096d6f3748305b1b33` | 2026-10-22 04:29 |
| `pose_study/sensitivity/d256-L2-lr1e-3-s0.json` | 9.5 KB | `77854718b1047b97dc721022a173588c` | 2026-10-22 05:16 |
| `pose_study/sensitivity/d256-L2-lr1e-3-s1.json` | 9.5 KB | `377b6797a219ccd4bf5225621ae03627` | 2026-10-22 05:20 |
| `pose_study/sensitivity/d256-L2-lr1e-3-s2.json` | 9.5 KB | `1672cdb8e728bb7ecf533624319db648` | 2026-10-22 05:25 |
| `pose_study/sensitivity/d256-L2-lr1e-3-s3.json` | 9.5 KB | `66a9fc58b71d68080b1355f573495795` | 2026-10-22 05:30 |
| `pose_study/sensitivity/d256-L2-lr1e-3-s4.json` | 9.5 KB | `ee77c91cd35fde308a84f851f6a0a6bc` | 2026-10-22 05:34 |
| `pose_study/sensitivity/d256-L2-lr5e-4-s0.json` | 9.5 KB | `2e47d5600ff065c2bb0a9e5c2f491d1e` | 2026-10-22 04:53 |
| `pose_study/sensitivity/d256-L2-lr5e-4-s1.json` | 9.5 KB | `0e66f84607ffce26dc3deb2c4dcea2be` | 2026-10-22 04:58 |
| `pose_study/sensitivity/d256-L2-lr5e-4-s2.json` | 9.5 KB | `178e51c0cdde1bef2761dd313a4968f7` | 2026-10-22 05:02 |
| `pose_study/sensitivity/d256-L2-lr5e-4-s3.json` | 9.5 KB | `7b3f42d75282472a3822538f301b8ad4` | 2026-10-22 05:07 |
| `pose_study/sensitivity/d256-L2-lr5e-4-s4.json` | 9.5 KB | `b3bc7d1eb4364f8b69f6490d0382f3dc` | 2026-10-22 05:11 |
| `pose_study/sensitivity/d256-L3-lr1e-3-s0.json` | 9.5 KB | `542687b6f157435c5b961c13d4cf305f` | 2026-10-22 06:17 |
| `pose_study/sensitivity/d256-L3-lr1e-3-s1.json` | 9.5 KB | `e447b85cf335db324e36af6c751bff27` | 2026-10-22 06:24 |
| `pose_study/sensitivity/d256-L3-lr1e-3-s2.json` | 9.5 KB | `7f7ee036bf3062a8d0f8a3f51908f93f` | 2026-10-22 06:30 |
| `pose_study/sensitivity/d256-L3-lr1e-3-s3.json` | 9.5 KB | `7522cf97881b8f858b3371e76071a1c8` | 2026-10-22 06:37 |
| `pose_study/sensitivity/d256-L3-lr1e-3-s4.json` | 9.5 KB | `a9373ab8870021bf3e049857d7cb0738` | 2026-10-22 06:44 |
| `pose_study/sensitivity/d256-L3-lr5e-4-s0.json` | 9.5 KB | `a20471efb14b053257fd7c5600e5ca16` | 2026-10-22 05:43 |
| `pose_study/sensitivity/d256-L3-lr5e-4-s1.json` | 9.5 KB | `7d129eb0288a30911636254800962ff9` | 2026-10-22 05:50 |
| `pose_study/sensitivity/d256-L3-lr5e-4-s2.json` | 9.5 KB | `cbcf2c2b6d414bc29f604c380ca8255f` | 2026-10-22 05:57 |
| `pose_study/sensitivity/d256-L3-lr5e-4-s3.json` | 9.5 KB | `e310bbfa191a635fef2d9ae88c46e4c1` | 2026-10-22 06:04 |
| `pose_study/sensitivity/d256-L3-lr5e-4-s4.json` | 9.5 KB | `b4effc54074d2b65360513a45e3ebe3b` | 2026-10-22 06:11 |
| `pose_study/sensitivity/d256-L4-lr1e-3-s0.json` | 9.5 KB | `c8bfe3cf2a1176a3fbcc70e531183960` | 2026-10-22 07:40 |
| `pose_study/sensitivity/d256-L4-lr1e-3-s1.json` | 9.5 KB | `22012598eb8ef43adbaf462bfd7b6702` | 2026-10-22 07:48 |
| `pose_study/sensitivity/d256-L4-lr1e-3-s2.json` | 9.5 KB | `e9a309d9b45f7bc9d506ed0b6a50cd5f` | 2026-10-22 07:57 |
| `pose_study/sensitivity/d256-L4-lr1e-3-s3.json` | 9.5 KB | `2ae965a60733621b3b22050df979674b` | 2026-10-22 08:06 |
| `pose_study/sensitivity/d256-L4-lr1e-3-s4.json` | 9.5 KB | `62dc775f7564ccfbb2996335309b419c` | 2026-10-22 08:15 |
| `pose_study/sensitivity/d256-L4-lr5e-4-s0.json` | 9.5 KB | `d3b20fc0a5a9f17caf1780772970aff4` | 2026-10-22 06:55 |
| `pose_study/sensitivity/d256-L4-lr5e-4-s1.json` | 9.5 KB | `eeb3a4671e52f7aa9daad04b4698c70f` | 2026-10-22 07:04 |
| `pose_study/sensitivity/d256-L4-lr5e-4-s2.json` | 9.5 KB | `5abd70fc60065eb80a320bde3ee66a82` | 2026-10-22 07:12 |
| `pose_study/sensitivity/d256-L4-lr5e-4-s3.json` | 9.5 KB | `18e07bd851b818a23b19f8bc94008c84` | 2026-10-22 07:22 |
| `pose_study/sensitivity/d256-L4-lr5e-4-s4.json` | 9.5 KB | `77a7c1170e5d2b3fe5580a512a1eb194` | 2026-10-22 07:31 |
| `pose_study/sensitivity/d64-L2-lr1e-3-s0.json` | 9.5 KB | `504ca771d223e071ba28441d87be2939` | 2026-10-22 02:45 |
| `pose_study/sensitivity/d64-L2-lr1e-3-s1.json` | 9.5 KB | `37ba1632026473128384b6ea5ce9b376` | 2026-10-22 02:47 |
| `pose_study/sensitivity/d64-L2-lr1e-3-s2.json` | 9.5 KB | `cd7ad71eb9398ce303aef44265c31e76` | 2026-10-22 02:48 |
| `pose_study/sensitivity/d64-L2-lr1e-3-s3.json` | 9.5 KB | `2ec4eb6e7f193e6387490bbfbc7a48aa` | 2026-10-22 02:49 |
| `pose_study/sensitivity/d64-L2-lr1e-3-s4.json` | 9.5 KB | `c59ba8ed938a358f0dde4daf882a2ee4` | 2026-10-22 02:50 |
| `pose_study/sensitivity/d64-L2-lr5e-4-s0.json` | 9.5 KB | `4b3273d0c24181746e71d21af1b08846` | 2026-10-22 02:40 |
| `pose_study/sensitivity/d64-L2-lr5e-4-s1.json` | 9.5 KB | `92597f6e9f4f52206326716192e14df6` | 2026-10-22 02:41 |
| `pose_study/sensitivity/d64-L2-lr5e-4-s2.json` | 9.5 KB | `5cbb9802b49c781a5e77703461a1bf6d` | 2026-10-22 02:41 |
| `pose_study/sensitivity/d64-L2-lr5e-4-s3.json` | 9.5 KB | `ab22eab3c7866c3020a9a835147f176b` | 2026-10-22 02:43 |
| `pose_study/sensitivity/d64-L2-lr5e-4-s4.json` | 9.5 KB | `489eb2acad486ee7191f50ced522e689` | 2026-10-22 02:45 |
| `pose_study/sensitivity/d64-L3-lr1e-3-s0.json` | 9.5 KB | `059dd046e938edfdfecba7ee0b92e809` | 2026-10-22 02:59 |
| `pose_study/sensitivity/d64-L3-lr1e-3-s1.json` | 9.5 KB | `c0226b4077a6591ca555064d1146df90` | 2026-10-22 03:01 |
| `pose_study/sensitivity/d64-L3-lr1e-3-s2.json` | 9.5 KB | `c9eba34847450573a0dedb551c9dbb34` | 2026-10-22 03:02 |
| `pose_study/sensitivity/d64-L3-lr1e-3-s3.json` | 9.5 KB | `1ea4dc7ce2f49c9875ece61fa089a026` | 2026-10-22 03:04 |
| `pose_study/sensitivity/d64-L3-lr1e-3-s4.json` | 9.5 KB | `8fd0a76f478b90d48cec9f2920f1729d` | 2026-10-22 03:05 |
| `pose_study/sensitivity/d64-L3-lr5e-4-s0.json` | 9.5 KB | `3abe7ce1fd1ac886cab580bdd70c90c8` | 2026-10-22 02:52 |
| `pose_study/sensitivity/d64-L3-lr5e-4-s1.json` | 9.5 KB | `df1bd1e4b5e2bfd1cbccd2401b5d2f6a` | 2026-10-22 02:53 |
| `pose_study/sensitivity/d64-L3-lr5e-4-s2.json` | 9.5 KB | `23594d35e2880511eb42cde1dd57d2d9` | 2026-10-22 02:55 |
| `pose_study/sensitivity/d64-L3-lr5e-4-s3.json` | 9.5 KB | `1d4194f10e962e826bd195748e7ccb8a` | 2026-10-22 02:56 |
| `pose_study/sensitivity/d64-L3-lr5e-4-s4.json` | 9.5 KB | `874caf6bf5816935df2b2d8841ad0065` | 2026-10-22 02:58 |
| `pose_study/sensitivity/d64-L4-lr1e-3-s0.json` | 9.5 KB | `938cf3b501306ce10785e1936577e103` | 2026-10-22 03:17 |
| `pose_study/sensitivity/d64-L4-lr1e-3-s1.json` | 9.5 KB | `6a98a6a78dedae75addf5f083c6a7809` | 2026-10-22 03:19 |
| `pose_study/sensitivity/d64-L4-lr1e-3-s2.json` | 9.5 KB | `5d781d5d7f354f90b417efe998e9f19c` | 2026-10-22 03:21 |
| `pose_study/sensitivity/d64-L4-lr1e-3-s3.json` | 9.5 KB | `0fa880f2a9589e9a11bcdc3870c6f886` | 2026-10-22 03:23 |
| `pose_study/sensitivity/d64-L4-lr1e-3-s4.json` | 9.5 KB | `8c4117685bd7b549c5f394a271fa7861` | 2026-10-22 03:25 |
| `pose_study/sensitivity/d64-L4-lr5e-4-s0.json` | 9.5 KB | `6a039e7afc4e27e59d10b549a913e3c7` | 2026-10-22 03:08 |
| `pose_study/sensitivity/d64-L4-lr5e-4-s1.json` | 9.5 KB | `296d5ef51118f02e6ea4b38b946e1614` | 2026-10-22 03:10 |
| `pose_study/sensitivity/d64-L4-lr5e-4-s2.json` | 9.5 KB | `7dffb7dd1808788a90183db7443a972a` | 2026-10-22 03:11 |
| `pose_study/sensitivity/d64-L4-lr5e-4-s3.json` | 9.5 KB | `16476cdb662803f306a06449b10c5ab6` | 2026-10-22 03:13 |
| `pose_study/sensitivity/d64-L4-lr5e-4-s4.json` | 9.5 KB | `f8577ff1edb25a6adadc4a018548a1d1` | 2026-10-22 03:15 |
| `pose_study_stats/ci_ablations.csv` | 2.2 KB | `9018692b129f7d71357fed32bd3adab9` | 2026-10-23 14:07 |
| `pose_study_stats/ci_ablations.log` | 3.0 KB | `d74d7989eef48dcb9ad0f38210c0030b` | 2026-10-23 14:07 |
| `pose_study_stats/ci_frames.csv` | 1023 B | `fbc1a9998acf4825e96051f13f7a0f5b` | 2026-10-23 14:13 |
| `pose_study_stats/ci_frames.log` | 1.3 KB | `adfab8985c3579fd68a9f2403d403a53` | 2026-10-23 14:13 |
| `pose_study_stats/ci_nested.csv` | 576 B | `b0d14b8846cea9731aa4a4dc04363398` | 2026-10-23 13:56 |
| `pose_study_stats/ci_nested.log` | 690 B | `0df994f28043632cbfec44896854264c` | 2026-10-23 13:56 |
| `pose_study_stats/commit.txt` | 66 B | `faa751df186ea7c783b2f7e0456d1659` | 2026-10-23 13:53 |
| `pose_study_stats/pairs_ablations.csv` | 2.0 KB | `5594711438b322073636e8b822c11c42` | 2026-10-23 14:07 |
| `pose_study_stats/pairs_frames.csv` | 935 B | `b63527b61dc9e5a5425422bfbee2003e` | 2026-10-23 14:13 |
| `pose_study_stats/pairs_nested.csv` | 418 B | `a7c8fd3433560bd3e7a0bacc3536c027` | 2026-10-23 13:56 |
| `pose_study_stats/s1_nested.csv` | 499 B | `1b33d2b06d02224622b1f8ca26b9e00b` | 2026-10-23 13:53 |
| `pose_study_stats/s1_selected_configs.csv` | 371 B | `d4290680e456a7e86693d9ab85a10311` | 2026-10-23 13:53 |
| `pose_study_stats/s2_sensitivity.csv` | 2.4 KB | `4996298e53b87e892e921eadb97de17d` | 2026-10-23 13:53 |
| `pose_study_stats/s3_s4_variants.csv` | 2.5 KB | `13386698a4958231ad7efb462d643136` | 2026-10-23 13:53 |
| `pose_study_stats/s5_learning_curve.csv` | 604 B | `fdf917dcab2da49d0cf3535ae7fa2229` | 2026-10-23 13:53 |
| `pose_study_stats/summary.log` | 3.1 KB | `51df27fb0ae1857ff3815ebd9acc8cfd` | 2026-10-23 13:53 |
| `prediction_metrics/command.txt` | 2.8 KB | `722cb3418c4dc0bced57249b8265c89d` | 2026-10-28 23:45 |
| `prediction_metrics/commit.txt` | 223 B | `f58576222c63e9704d167fff986c39b6` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_landmarks_tsfel_body_relative_rf_8020.csv` | 6.1 KB | `cacc9d88c63612c05fc21717ad6b03e0` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_landmarks_tsfel_body_relative_rf_loso.csv` | 6.7 KB | `975492e95dfb55a55de2f89924ea2d88` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_late_fusion_slowfast_spoter_8020.csv` | 5.9 KB | `f1aa2c498f57063e5e79763e4f9e5cbb` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_late_fusion_slowfast_spoter_loso.csv` | 7.7 KB | `2ef0f2bd2626710dc0578bf303795e19` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_official_spoter_8020.csv` | 5.8 KB | `7a63c6540a27b1250f76aecff434b1d0` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_official_spoter_loso.csv` | 6.6 KB | `ef4d34fffb484fb0b5cbe6f6ffe353c1` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_slowfast_r50_8020.csv` | 6.1 KB | `18ffd0caa9af9bbb1387869631332953` | 2026-10-28 23:45 |
| `prediction_metrics/confusion_slowfast_r50_loso.csv` | 7.7 KB | `b08cf818d9fe5e177b6668f58b9535df` | 2026-10-28 23:45 |
| `prediction_metrics/metrics_runs.csv` | 115.4 KB | `2d2314a6d3031085391ad97f5b0fc3a9` | 2026-10-28 23:45 |
| `prediction_metrics/metrics_summary.csv` | 38.6 KB | `3d81f071b1868c8f4e903fac18eb1e16` | 2026-10-28 23:45 |
| `prediction_metrics/per_sign_f1.csv` | 32.3 KB | `28af2a316c5778b2414e5961aba3babf` | 2026-10-28 23:45 |
| `prediction_metrics/prediction_metrics.log` | 7.6 KB | `96be7c01d5107a28173e187695ad35cb` | 2026-10-28 23:45 |
| `prediction_metrics/sign_names.json` | 835 B | `0a550b1d45a0ed0b239a2ae5c078af72` | 2026-10-28 23:45 |
| `prediction_metrics/top_confusions_loso.csv` | 3.7 KB | `4e534d9bc5b06d40792e9a7e1ad22d10` | 2026-10-28 23:45 |
| `prediction_metrics_first/command.txt` | 2.8 KB | `a25b27a143bc9143b8450a511bff9e48` | 2026-10-28 23:43 |
| `prediction_metrics_first/commit.txt` | 221 B | `cf45ac4e4beb7bfac3af2c38474d090a` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_landmarks_tsfel_body_relative_rf_8020.csv` | 6.1 KB | `cacc9d88c63612c05fc21717ad6b03e0` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_landmarks_tsfel_body_relative_rf_loso.csv` | 6.7 KB | `975492e95dfb55a55de2f89924ea2d88` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_late_fusion_slowfast_spoter_8020.csv` | 5.8 KB | `f0c9f863596977a92c98cb71e773cd8a` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_late_fusion_slowfast_spoter_loso.csv` | 7.1 KB | `6d714c6c658feb0087cb15e0ae3c5c61` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_official_spoter_8020.csv` | 5.8 KB | `7a63c6540a27b1250f76aecff434b1d0` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_official_spoter_loso.csv` | 6.6 KB | `ef4d34fffb484fb0b5cbe6f6ffe353c1` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_slowfast_r50_8020.csv` | 6.0 KB | `67bac53431c0f1bd186267d2f2efe8a3` | 2026-10-28 23:43 |
| `prediction_metrics_first/confusion_slowfast_r50_loso.csv` | 7.1 KB | `9adb51a85fc9df4085ef2c132c139726` | 2026-10-28 23:43 |
| `prediction_metrics_first/metrics_runs.csv` | 142.4 KB | `c217d04b2a5d2e5b42931ac1e90d5b3d` | 2026-10-28 23:43 |
| `prediction_metrics_first/metrics_summary.csv` | 40.3 KB | `27fb8a32a589c9bdf9b256ebee107c2c` | 2026-10-28 23:43 |
| `prediction_metrics_first/per_sign_f1.csv` | 32.3 KB | `28af2a316c5778b2414e5961aba3babf` | 2026-10-28 23:43 |
| `prediction_metrics_first/prediction_metrics.log` | 7.6 KB | `daa9ac0ab4570fe4a550d106d1eb3141` | 2026-10-28 23:43 |
| `prediction_metrics_first/sign_names.json` | 835 B | `0a550b1d45a0ed0b239a2ae5c078af72` | 2026-10-28 23:43 |
| `prediction_metrics_first/top_confusions_loso.csv` | 3.7 KB | `4e534d9bc5b06d40792e9a7e1ad22d10` | 2026-10-28 23:43 |
| `results/errors.log` | 34.7 KB | `0aa1d79356566e52354d22a24e536bab` | 2026-10-15 21:02 |
| `results/errors_frames.log` | 388.2 KB | `6ff53dcfc2c7c7655bf81e6e71bb3698` | 2026-10-16 18:10 |
| `results/errors_groupcv.log` | 15.4 KB | `c3fbc1e4c1971b75a1418b9bd3697e00` | 2026-10-16 18:51 |
| `results/errors_groupcv_seeds.log` | 50.6 KB | `727f4febb3937aacbdb35943b6c9b1eb` | 2026-10-16 22:26 |
| `results/errors_signant.log` | 24.0 KB | `b79689c54056b19fd7aa5f4504c18027` | 2026-10-16 22:51 |
| `results/run_frames.sh` | 1.7 KB | `2a3d00a62f455ed384d49b6136b019d7` | 2026-10-15 19:25 |
| `results/run_groupcv.sh` | 850 B | `6c4fcdde066988ba0ed55f58e89cafd6` | 2026-10-15 20:24 |
| `results/run_groupcv_seeds.sh` | 727 B | `af151a152bb5e3afff796c53ba1be899` | 2026-10-16 19:29 |
| `results/run_signant.sh` | 1.0 KB | `700e37b818b3bdf66afee1c7cca7a3c9` | 2026-10-16 19:43 |
| `results/run_slr.sh` | 1.1 KB | `91eeefee22445e57a56b4250ec6555d4` | 2026-10-15 17:00 |
| `results/signant_labeling_permutation_bodynorm_knn.csv` | 944 B | `75538eea27d723c4b8b5a2eb758d4e8c` | 2026-10-20 21:18 |
| `results/signant_labeling_permutation_bodynorm_rf.csv` | 945 B | `631df8e4db34c211848333dfaef31942` | 2026-10-20 21:18 |
| `results/signant_labeling_permutation_bodynorm_svm.csv` | 905 B | `553998499cc474864c649f59c327e93b` | 2026-10-20 21:18 |
| `results/signant_summary.csv` | 3.7 KB | `d37bbfc756835146393cbf7e43dce551` | 2026-10-20 21:18 |
| `results/signant_summary_runs.csv` | 8.8 KB | `d1c126b0b016dfb47cc764cf3b35bc00` | 2026-10-20 21:18 |
| `results/signant_v2.commit` | 155 B | `27b68c1335a5d4a0c4b27c83b766f3e0` | 2026-10-20 15:57 |
| `results/signant_v2.log` | 125.3 KB | `7b9d5a898d3e96954fd6e7c0fa81b017` | 2026-10-20 21:18 |
| `results/summary_stage1.csv` | 1.9 KB | `4935c703c5589092ecd21651d0632b3f` | 2026-10-15 19:08 |
| `results/dup_test/cm_rf_temporal_dupv1_balanced_seed0.pkl` | 19.7 KB | `ab35bcd026151dfea4d33a535d0c4f9c` | 2026-10-15 19:57 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_0_seed0.pkl` | 19.7 KB | `f9b5563e3934e94bcf724a4bf26a3805` | 2026-10-15 19:59 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_1_seed0.pkl` | 19.7 KB | `ca3ac1de85b9f53f111a290dca98bd79` | 2026-10-15 20:00 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_2_seed0.pkl` | 19.7 KB | `6bcf91865b9197419191bcac5f829eeb` | 2026-10-15 20:01 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_3_seed0.pkl` | 19.7 KB | `65f5ccd8e59116daf20b3db865a5d7fe` | 2026-10-15 20:02 |
| `results/dup_test/cm_rf_temporal_dupv1_loso_4_seed0.pkl` | 19.7 KB | `d3a3cadc595d9414c530098c84cab388` | 2026-10-15 20:02 |
| `results/dup_test/err.log` | 3.7 KB | `5d34b2eea9b58a3253aeb76e7c966f70` | 2026-10-15 20:02 |
| `results/dup_test/grid_search_results_temporal_dupv1_seed0.pkl` | 576.4 KB | `9c986792591df11d5b1f39e5f0af33d3` | 2026-10-15 20:02 |
| `results/dup_test/names.txt` | 5.4 KB | `a43e645830e5dd0a79e82342734a3307` | 2026-10-15 19:56 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_balanced_seed0.pkl` | 19.7 KB | `dcfb4d2d08dd4754584e51588ef70867` | 2026-10-16 17:48 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_0_seed0.pkl` | 19.7 KB | `c915397bbbf3cbd995d48c74c1827c5d` | 2026-10-16 17:54 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_1_seed0.pkl` | 19.7 KB | `f53f3b6a8a11617b557e7372bebd4456` | 2026-10-16 18:01 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_2_seed0.pkl` | 19.7 KB | `15ae9f4d93035ff1e1700de3ba477347` | 2026-10-16 18:04 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_3_seed0.pkl` | 19.7 KB | `136a27b9acb89fa6d529520d07370089` | 2026-10-16 18:07 |
| `results/frames/cm_rf_general_db_lm_chronos_f0_loso_4_seed0.pkl` | 19.7 KB | `301459fc58270cd5e319d22ac97af266` | 2026-10-16 18:10 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_balanced_seed0.pkl` | 19.7 KB | `b799124d7c87e44895958c6a3694631f` | 2026-10-16 15:17 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_0_seed0.pkl` | 19.7 KB | `0abd840badb772c6cb9cb186b44092ec` | 2026-10-16 15:21 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_1_seed0.pkl` | 19.7 KB | `6c7d2365224e6a771acaf09790704b7c` | 2026-10-16 15:24 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_2_seed0.pkl` | 19.7 KB | `180836ef68cb17751fd6cb8e3067930b` | 2026-10-16 15:27 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_3_seed0.pkl` | 19.7 KB | `62a9a30b95f16da1b804abe1c50b691a` | 2026-10-16 15:31 |
| `results/frames/cm_rf_general_db_lm_chronos_f16_loso_4_seed0.pkl` | 19.7 KB | `0048e42f5c47f30fe41f3d7d30578bce` | 2026-10-16 15:34 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_balanced_seed0.pkl` | 19.7 KB | `57a1126e3f57ce2794071cd48001cbfc` | 2026-10-16 16:05 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_0_seed0.pkl` | 19.7 KB | `40931453ef78b6918db8b3c86c2ef048` | 2026-10-16 16:08 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_1_seed0.pkl` | 19.7 KB | `a129c4ee272951cdc4fcf2bfe2fdc1cc` | 2026-10-16 16:12 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_2_seed0.pkl` | 19.7 KB | `3366c0ab73118ebea6429a7bd299461f` | 2026-10-16 16:16 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_3_seed0.pkl` | 19.7 KB | `ae9a246dbab3f00903c878c7bd634567` | 2026-10-16 16:19 |
| `results/frames/cm_rf_general_db_lm_chronos_f32_loso_4_seed0.pkl` | 19.7 KB | `10057a59ec76c475b5974f3c9265fd81` | 2026-10-16 16:23 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_balanced_seed0.pkl` | 19.7 KB | `84fe1f1d38c9b73ec2d1b3360cab0b08` | 2026-10-16 16:55 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_0_seed0.pkl` | 19.7 KB | `5f2c0768a5724065348d22e32e8960ed` | 2026-10-16 16:59 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_1_seed0.pkl` | 19.7 KB | `c9756d0aca0613c18ded72078eb3d6f1` | 2026-10-16 17:02 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_2_seed0.pkl` | 19.7 KB | `8a4048f1ce3306ffca77f7e655cf037c` | 2026-10-16 17:06 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_3_seed0.pkl` | 19.7 KB | `3ca5d17cb9746c2afb5b69a47436e092` | 2026-10-16 17:10 |
| `results/frames/cm_rf_general_db_lm_chronos_f48_loso_4_seed0.pkl` | 19.7 KB | `4b5d121682912dcf4189416524093615` | 2026-10-16 17:13 |
| `results/frames/cm_rf_temporal_features_f0_balanced_seed0.pkl` | 19.7 KB | `96df6d305c4fdbd6f9bc1bfc9b85ea3d` | 2026-10-16 17:19 |
| `results/frames/cm_rf_temporal_features_f0_loso_0_seed0.pkl` | 19.7 KB | `19539eadec5e2220ff53632a521d5269` | 2026-10-16 17:24 |
| `results/frames/cm_rf_temporal_features_f0_loso_1_seed0.pkl` | 19.7 KB | `8c038694a5ee54e875cc52496790b3f8` | 2026-10-16 17:29 |
| `results/frames/cm_rf_temporal_features_f0_loso_2_seed0.pkl` | 19.7 KB | `de17c55280d92599f3918a83afe92c33` | 2026-10-16 17:35 |
| `results/frames/cm_rf_temporal_features_f0_loso_3_seed0.pkl` | 19.7 KB | `49dca09be587b58137ee9b6a190f8dde` | 2026-10-16 17:40 |
| `results/frames/cm_rf_temporal_features_f0_loso_4_seed0.pkl` | 19.7 KB | `28256b947f2c6ca579e8fed2d08f59a5` | 2026-10-16 17:45 |
| `results/frames/cm_rf_temporal_features_f16_balanced_seed0.pkl` | 19.7 KB | `c5dee017bf4d9bdd0ba5b0797816e8ba` | 2026-10-16 08:40 |
| `results/frames/cm_rf_temporal_features_f16_loso_0_seed0.pkl` | 19.7 KB | `aaf39157c6c72a653c897c4e755cb04e` | 2026-10-16 14:57 |
| `results/frames/cm_rf_temporal_features_f16_loso_1_seed0.pkl` | 19.7 KB | `6febd188e37a6a2c4b63e2f6821013ef` | 2026-10-16 15:01 |
| `results/frames/cm_rf_temporal_features_f16_loso_2_seed0.pkl` | 19.7 KB | `bd1414596275bbb69c82b8b485a76f53` | 2026-10-16 15:05 |
| `results/frames/cm_rf_temporal_features_f16_loso_3_seed0.pkl` | 19.7 KB | `f46713fb488fa4eff0942fc5ae60c63e` | 2026-10-16 15:09 |
| `results/frames/cm_rf_temporal_features_f16_loso_4_seed0.pkl` | 19.7 KB | `6d5342c019ee38ed3e935f6796ae7108` | 2026-10-16 15:14 |
| `results/frames/cm_rf_temporal_features_f32_balanced_seed0.pkl` | 19.7 KB | `2d8b9fad8ae4bf9a8fe6c63d85ec71d3` | 2026-10-16 15:39 |
| `results/frames/cm_rf_temporal_features_f32_loso_0_seed0.pkl` | 19.7 KB | `41a4cb0cff40e607abb8fd8ec58fcf25` | 2026-10-16 15:43 |
| `results/frames/cm_rf_temporal_features_f32_loso_1_seed0.pkl` | 19.7 KB | `91023999bc89e44a3377316fd035aaf3` | 2026-10-16 15:47 |
| `results/frames/cm_rf_temporal_features_f32_loso_2_seed0.pkl` | 19.7 KB | `a408e34087a6a7f61691aa32ca36fc3a` | 2026-10-16 15:52 |
| `results/frames/cm_rf_temporal_features_f32_loso_3_seed0.pkl` | 19.7 KB | `e511f0a60ec75f78ba13cec2fdfc6320` | 2026-10-16 15:56 |
| `results/frames/cm_rf_temporal_features_f32_loso_4_seed0.pkl` | 19.7 KB | `9c7531e7ae51b1110b53417c23655c10` | 2026-10-16 16:01 |
| `results/frames/cm_rf_temporal_features_f48_balanced_seed0.pkl` | 19.7 KB | `f33915c5ee284228d53d3a689f799434` | 2026-10-16 16:28 |
| `results/frames/cm_rf_temporal_features_f48_loso_0_seed0.pkl` | 19.7 KB | `bacc3469de9964cc03b1b0ea61250e42` | 2026-10-16 16:32 |
| `results/frames/cm_rf_temporal_features_f48_loso_1_seed0.pkl` | 19.7 KB | `f358005cb69522916b5b8aa28ae545c6` | 2026-10-16 16:37 |
| `results/frames/cm_rf_temporal_features_f48_loso_2_seed0.pkl` | 19.7 KB | `7ff2a809d90c24d5b945df2826c9d77b` | 2026-10-16 16:41 |
| `results/frames/cm_rf_temporal_features_f48_loso_3_seed0.pkl` | 19.7 KB | `be4f6d1e0aa26884088813f5af47a714` | 2026-10-16 16:46 |
| `results/frames/cm_rf_temporal_features_f48_loso_4_seed0.pkl` | 19.7 KB | `f0ed4e005366d20510aae135621b8734` | 2026-10-16 16:51 |
| `results/frames/grid_search_results_general_db_lm_chronos_f0_chronos_seed0.pkl` | 649.6 KB | `1235f9e6889b521c9b4bf50a1833e82f` | 2026-10-16 18:10 |
| `results/frames/grid_search_results_general_db_lm_chronos_f16_chronos_seed0.pkl` | 649.6 KB | `374c91614b3f54a06f2b2ee3bd36851b` | 2026-10-16 15:34 |
| `results/frames/grid_search_results_general_db_lm_chronos_f32_chronos_seed0.pkl` | 649.6 KB | `4ee7ab79dd794d2232a4f41a19c46d1d` | 2026-10-16 16:23 |
| `results/frames/grid_search_results_general_db_lm_chronos_f48_chronos_seed0.pkl` | 649.6 KB | `459ad7ef3333192679123389e6d1600d` | 2026-10-16 17:13 |
| `results/frames/grid_search_results_temporal_features_f0_chronos_seed0.pkl` | 710.9 KB | `0e53ae4b6fa0dcd5b88277e9b59e7018` | 2026-10-16 17:45 |
| `results/frames/grid_search_results_temporal_features_f16_chronos_seed0.pkl` | 710.9 KB | `23bc878ee607ba64f172883d4bc2879e` | 2026-10-16 15:14 |
| `results/frames/grid_search_results_temporal_features_f32_chronos_seed0.pkl` | 710.9 KB | `bbfe782b2499af878557adabc9ff5709` | 2026-10-16 16:01 |
| `results/frames/grid_search_results_temporal_features_f48_chronos_seed0.pkl` | 710.9 KB | `05ba832978f84547917052a4c6c6925d` | 2026-10-16 16:51 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed0.pkl` | 19.7 KB | `eda66360710feee8a2f87e6c23e7eafc` | 2026-10-15 18:05 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed1.pkl` | 19.7 KB | `273cc2d2b2307bb810a5065b8f901112` | 2026-10-15 21:05 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed2.pkl` | 19.7 KB | `ee888b2a80f85d202e2cfb1269a8a9d0` | 2026-10-15 21:10 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed3.pkl` | 19.7 KB | `c5928370f85bfdf9303f063f1e4d03c9` | 2026-10-15 21:15 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_seed4.pkl` | 19.7 KB | `b0679787a3da4e40fdace33c01f43d6c` | 2026-10-15 21:35 |
| `results/imu/cm_rf_general_db_imu_chronos_balanced_shuffled_seed0.pkl` | 19.7 KB | `5d438d4bdd62b3c2961c85558cd5b534` | 2026-10-15 20:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed0.pkl` | 19.7 KB | `75a788923bf67f2451679ef8c149033a` | 2026-10-16 18:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed1.pkl` | 19.7 KB | `0612bdd7b2936f6987cdae4aff677ce4` | 2026-10-16 19:32 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed2.pkl` | 19.7 KB | `ecbe5f9a5193fb4cc95b8232d92e64dc` | 2026-10-16 19:37 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed3.pkl` | 19.7 KB | `3698633cffddcec06abbfc611721bacf` | 2026-10-16 19:43 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_groupcv_seed4.pkl` | 19.7 KB | `e9f6db27e1a5d845128b7097835e71ce` | 2026-10-16 19:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed0.pkl` | 19.7 KB | `705d735d2180347ef73f35593914c5b1` | 2026-10-15 18:05 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed1.pkl` | 19.7 KB | `f3bf10e34407595b52b3272b99177afc` | 2026-10-15 21:05 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed2.pkl` | 19.7 KB | `a241225dfb26535262c51d3904069f14` | 2026-10-15 21:10 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed3.pkl` | 19.7 KB | `67113b3af56de49a9f7003a8cb120d9a` | 2026-10-15 21:15 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_seed4.pkl` | 19.7 KB | `a35f98df34aa5004a69d6d940d1cc23d` | 2026-10-15 21:35 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_0_shuffled_seed0.pkl` | 19.7 KB | `5402c748ad2d18211b179165efd0cd77` | 2026-10-15 20:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed0.pkl` | 19.7 KB | `ece8d31d6875af45082931854eb9cb33` | 2026-10-16 18:49 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed1.pkl` | 19.7 KB | `aa407c04e2fa8d1fe386deb7c298ab1f` | 2026-10-16 19:33 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed2.pkl` | 19.7 KB | `ba1786ccc009f9c36a973bab43d1ae87` | 2026-10-16 19:38 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed3.pkl` | 19.7 KB | `5aa3093770608a1e74a135863eefdbbd` | 2026-10-16 19:44 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_groupcv_seed4.pkl` | 19.7 KB | `d274dcf73cc8f105c206aca9594b60a1` | 2026-10-16 19:50 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed0.pkl` | 19.7 KB | `49a9634dfcbab78d71a168005a5f1a8a` | 2026-10-15 18:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed1.pkl` | 19.7 KB | `6536d8397c09e00395070588f0f14872` | 2026-10-15 21:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed2.pkl` | 19.7 KB | `523e4fd755a46e297ed44e44dd78c3c7` | 2026-10-15 21:11 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed3.pkl` | 19.7 KB | `d8a690aa1fe132fd03a3e6916462de55` | 2026-10-15 21:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_seed4.pkl` | 19.7 KB | `38edd144374cda930a5dde411ee9facc` | 2026-10-15 21:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_1_shuffled_seed0.pkl` | 19.7 KB | `07d83fc5aea171675f251085e05064e6` | 2026-10-15 20:18 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed0.pkl` | 19.7 KB | `7a2dcce783ceba81aefef4b351d1f66b` | 2026-10-16 18:50 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed1.pkl` | 19.7 KB | `e114c446c06ff9d6102ea571445ae17d` | 2026-10-16 19:33 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed2.pkl` | 19.7 KB | `2fb07cf23056542b9033788d6704000d` | 2026-10-16 19:39 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed3.pkl` | 19.7 KB | `c64f1a0d47659eed11e153eec04e21fd` | 2026-10-16 19:45 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_groupcv_seed4.pkl` | 19.7 KB | `932c9f272d944ad3e0de7ca47dfff1ad` | 2026-10-16 19:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed0.pkl` | 19.7 KB | `c10a032190e111d00ccd0e911f6d4ebd` | 2026-10-15 18:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed1.pkl` | 19.7 KB | `4dbb24736a85107496d044062915697f` | 2026-10-15 21:06 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed2.pkl` | 19.7 KB | `0925bf0d40b05fc4045ecf96b52b14bb` | 2026-10-15 21:11 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed3.pkl` | 19.7 KB | `3a6692439ec8186caaa521f3baebba12` | 2026-10-15 21:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_seed4.pkl` | 19.7 KB | `20bf2c780df57551787742e3cdaa10ec` | 2026-10-15 21:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_2_shuffled_seed0.pkl` | 19.7 KB | `9a66f41b368cf5df355da266052ce497` | 2026-10-15 20:19 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed0.pkl` | 19.7 KB | `319be95cf9076a10ae38c9fb3e388461` | 2026-10-16 18:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed1.pkl` | 19.7 KB | `752be20b2c6d3f50174cd970d376da73` | 2026-10-16 19:34 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed2.pkl` | 19.7 KB | `f7a1b1715faf2c5f3fe956214837acde` | 2026-10-16 19:39 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed3.pkl` | 19.7 KB | `2dcc7bcec2f52562972a78d2336b37ce` | 2026-10-16 19:45 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_groupcv_seed4.pkl` | 19.7 KB | `d72dbb805ae9320e648836485fb77aad` | 2026-10-16 19:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed0.pkl` | 19.7 KB | `e034a799b56ade60c1b847e7098e9be1` | 2026-10-15 18:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed1.pkl` | 19.7 KB | `45f2154eee2cb01820a6ccc679dba74b` | 2026-10-15 21:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed2.pkl` | 19.7 KB | `d4327274bffc0ea7f2582dcc45b83cda` | 2026-10-15 21:12 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed3.pkl` | 19.7 KB | `17c44f31a3a6c268212e72d2f01ac087` | 2026-10-15 21:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_seed4.pkl` | 19.7 KB | `d602cdb54d060cde962535ded8fa95a3` | 2026-10-15 22:16 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_3_shuffled_seed0.pkl` | 19.7 KB | `6221eee535dbe42e496148cd854143c4` | 2026-10-15 20:20 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed0.pkl` | 18.9 KB | `fceec78dcdc406f6f3cf0c7aed57a5ae` | 2026-10-16 18:51 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed1.pkl` | 18.9 KB | `5f273e2534a7a60fcec03907eae01d56` | 2026-10-16 19:35 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed2.pkl` | 18.9 KB | `1ec890a72497d1b27d0ffc3166fa1c91` | 2026-10-16 19:40 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed3.pkl` | 18.9 KB | `bd15985069f04924f3703a2528f89b5f` | 2026-10-16 19:46 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_groupcv_seed4.pkl` | 18.9 KB | `8604bdd319ed5d70d295c50da413cfcd` | 2026-10-16 19:52 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed0.pkl` | 18.9 KB | `b3356aeedff1a8f9ffffaa771f2967c5` | 2026-10-15 18:08 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed1.pkl` | 18.9 KB | `80be15af6056a745902d0de5f5673a03` | 2026-10-15 21:07 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed2.pkl` | 18.9 KB | `04e9633c72bf11c0bf07d1d832d47e67` | 2026-10-15 21:12 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed3.pkl` | 19.7 KB | `0f62d510f4be7da58dae23ad706855f2` | 2026-10-15 21:17 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_seed4.pkl` | 19.7 KB | `118cee778030f4e9e760cd73ec81c7f1` | 2026-10-15 23:56 |
| `results/imu/cm_rf_general_db_imu_chronos_loso_4_shuffled_seed0.pkl` | 19.7 KB | `c63aa90076757f622a0f1b8edce1b93c` | 2026-10-15 20:22 |
| `results/imu/cm_rf_temporal_balanced_seed0.pkl` | 19.7 KB | `a3e15d0124fd342ea14ddf8556ccb8ee` | 2026-10-15 18:02 |
| `results/imu/cm_rf_temporal_balanced_seed1.pkl` | 19.7 KB | `a75c315680e7197ccf1057f4b781bf2a` | 2026-10-15 21:02 |
| `results/imu/cm_rf_temporal_balanced_seed2.pkl` | 19.7 KB | `5b7b8b39d4cc2e7997843455f5216a9e` | 2026-10-15 21:08 |
| `results/imu/cm_rf_temporal_balanced_seed3.pkl` | 19.7 KB | `22c76aa13d14372e685a6f80a3860d51` | 2026-10-15 21:13 |
| `results/imu/cm_rf_temporal_balanced_seed4.pkl` | 19.7 KB | `6ad7f32e5b8ec1ea2bbbd319bd26a62d` | 2026-10-15 21:17 |
| `results/imu/cm_rf_temporal_balanced_shuffled_seed0.pkl` | 19.7 KB | `75e330b6b618847cd9acc8ad4dd4bb28` | 2026-10-15 20:14 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed0.pkl` | 19.7 KB | `01f63586bc14ee749a7f1636cc9dccfb` | 2026-10-16 18:46 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed1.pkl` | 19.7 KB | `967f29b43a7bb86153b26a29ce8f783d` | 2026-10-16 19:30 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed2.pkl` | 19.7 KB | `fbeca6c1466ed62b70a5981845998c82` | 2026-10-16 19:35 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed3.pkl` | 19.7 KB | `126b47f83e35bd445ff9bb9792d939af` | 2026-10-16 19:41 |
| `results/imu/cm_rf_temporal_loso_0_groupcv_seed4.pkl` | 19.7 KB | `2575b93ee55d8466f125477a3d83e43c` | 2026-10-16 19:47 |
| `results/imu/cm_rf_temporal_loso_0_seed0.pkl` | 19.7 KB | `6538c2671309f3e5440d96795658697d` | 2026-10-15 18:02 |
| `results/imu/cm_rf_temporal_loso_0_seed1.pkl` | 19.7 KB | `23b5dba511ff673af7e2c81168fe0c0a` | 2026-10-15 21:03 |
| `results/imu/cm_rf_temporal_loso_0_seed2.pkl` | 19.7 KB | `77882a90e959648cb29b1d8a2dc4425b` | 2026-10-15 21:08 |
| `results/imu/cm_rf_temporal_loso_0_seed3.pkl` | 19.7 KB | `55a1400d3c1af4ce195ace00ce9f6c04` | 2026-10-15 21:13 |
| `results/imu/cm_rf_temporal_loso_0_seed4.pkl` | 19.7 KB | `eb530387a305b6d3d044861446d129a4` | 2026-10-15 21:18 |
| `results/imu/cm_rf_temporal_loso_0_shuffled_seed0.pkl` | 19.7 KB | `21e58ed257083baff89210fbf9c72103` | 2026-10-15 20:15 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed0.pkl` | 19.7 KB | `fd67f2956cc3e2729e6aee3f499f461a` | 2026-10-16 18:47 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed1.pkl` | 19.7 KB | `3718fd83cd162b12feb14e3a9c037525` | 2026-10-16 19:30 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed2.pkl` | 19.7 KB | `f48185386a64b045f798bc8c3e8dff43` | 2026-10-16 19:35 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed3.pkl` | 19.7 KB | `fc6aee7fd172e7b24e48487ed63cf6d2` | 2026-10-16 19:41 |
| `results/imu/cm_rf_temporal_loso_1_groupcv_seed4.pkl` | 19.7 KB | `5b7dc0a6d324649e2a7d453a88dc87b3` | 2026-10-16 19:47 |
| `results/imu/cm_rf_temporal_loso_1_seed0.pkl` | 19.7 KB | `6aea8e7e3cb492323b7e0aeae1c7e3db` | 2026-10-15 18:03 |
| `results/imu/cm_rf_temporal_loso_1_seed1.pkl` | 19.7 KB | `0d4b3628c9c2fcf78e27c58bdfe546ba` | 2026-10-15 21:03 |
| `results/imu/cm_rf_temporal_loso_1_seed2.pkl` | 19.7 KB | `bfd8135529231231abdd26eee266c27d` | 2026-10-15 21:08 |
| `results/imu/cm_rf_temporal_loso_1_seed3.pkl` | 19.7 KB | `daacccd946262fabdd28090415535204` | 2026-10-15 21:13 |
| `results/imu/cm_rf_temporal_loso_1_seed4.pkl` | 19.7 KB | `3ef9bf3d58174e61757d4faba032f79b` | 2026-10-15 21:18 |
| `results/imu/cm_rf_temporal_loso_1_shuffled_seed0.pkl` | 19.7 KB | `23dc25a6ca622171a252521408757440` | 2026-10-15 20:15 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed0.pkl` | 19.7 KB | `8f6b033acb0bca6e3322c3e8c14f41ca` | 2026-10-16 18:47 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed1.pkl` | 19.7 KB | `12fbf8687581fe1bafe7ffbb83b13bc6` | 2026-10-16 19:31 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed2.pkl` | 19.7 KB | `97133ea3c9bfbeaff1553eaae5efffbb` | 2026-10-16 19:36 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed3.pkl` | 19.7 KB | `26a50c8df4a1221b29985ff18b71c112` | 2026-10-16 19:42 |
| `results/imu/cm_rf_temporal_loso_2_groupcv_seed4.pkl` | 19.7 KB | `6621003f29d8199b94e1871d3c975d2d` | 2026-10-16 19:48 |
| `results/imu/cm_rf_temporal_loso_2_seed0.pkl` | 19.7 KB | `2c2302e65148f611cbaf0bf84ded75fd` | 2026-10-15 18:03 |
| `results/imu/cm_rf_temporal_loso_2_seed1.pkl` | 19.7 KB | `12fbf8687581fe1bafe7ffbb83b13bc6` | 2026-10-15 21:03 |
| `results/imu/cm_rf_temporal_loso_2_seed2.pkl` | 19.7 KB | `0f8aad5c26a0a3d02b0766ad5c55c39b` | 2026-10-15 21:09 |
| `results/imu/cm_rf_temporal_loso_2_seed3.pkl` | 19.7 KB | `7509f9212b006c71d07d0be0ca1eadbf` | 2026-10-15 21:14 |
| `results/imu/cm_rf_temporal_loso_2_seed4.pkl` | 19.7 KB | `3903e8fc5d6367519a612f46a4807536` | 2026-10-15 21:18 |
| `results/imu/cm_rf_temporal_loso_2_shuffled_seed0.pkl` | 19.7 KB | `3792c8233384f46e62a3d566f19ef7f8` | 2026-10-15 20:15 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed0.pkl` | 19.7 KB | `738c367c82e53a83a12dc2ceb14dcc6a` | 2026-10-16 18:47 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed1.pkl` | 19.7 KB | `0be87c4601a7c9210d18682255c5a8c7` | 2026-10-16 19:31 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed2.pkl` | 19.7 KB | `159db6dbdcce4840e3fc161701a1c837` | 2026-10-16 19:36 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed3.pkl` | 19.7 KB | `d8e9698860105b1b4e696938b01cfe98` | 2026-10-16 19:42 |
| `results/imu/cm_rf_temporal_loso_3_groupcv_seed4.pkl` | 19.7 KB | `b4460afb89548d60d55530b16fb79ace` | 2026-10-16 19:48 |
| `results/imu/cm_rf_temporal_loso_3_seed0.pkl` | 19.7 KB | `b58b2ac3732602ea161068295cdf549f` | 2026-10-15 18:04 |
| `results/imu/cm_rf_temporal_loso_3_seed1.pkl` | 19.7 KB | `76d93b2656d7cee5413744c322ec4dcc` | 2026-10-15 21:04 |
| `results/imu/cm_rf_temporal_loso_3_seed2.pkl` | 19.7 KB | `1f21637df598d2d4ea344e37eb4143ee` | 2026-10-15 21:09 |
| `results/imu/cm_rf_temporal_loso_3_seed3.pkl` | 19.7 KB | `86b2545b07a46cb51e557fcd022d5f1f` | 2026-10-15 21:14 |
| `results/imu/cm_rf_temporal_loso_3_seed4.pkl` | 19.7 KB | `775986a0f6b1467e85bcf2e47ab28dad` | 2026-10-15 21:19 |
| `results/imu/cm_rf_temporal_loso_3_shuffled_seed0.pkl` | 19.7 KB | `af5a1c94c30ed64d413cf09e306877e0` | 2026-10-15 20:16 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed0.pkl` | 19.7 KB | `287ab4543f103dbd25381b8ec1e17ca6` | 2026-10-16 18:48 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed1.pkl` | 18.9 KB | `5a6f9850cce4a23daf3615dc20e1a055` | 2026-10-16 19:31 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed2.pkl` | 18.9 KB | `3da3806d73aa84acbe8c00a3c9e2d542` | 2026-10-16 19:37 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed3.pkl` | 19.7 KB | `fe71ad0312adef6a88aa11cf988d47b4` | 2026-10-16 19:42 |
| `results/imu/cm_rf_temporal_loso_4_groupcv_seed4.pkl` | 18.9 KB | `b6bf29c802436b2d8dcb7d20a7a0aa47` | 2026-10-16 19:48 |
| `results/imu/cm_rf_temporal_loso_4_seed0.pkl` | 19.7 KB | `638c4fd4e9d4e71ede5ce2c967c127ac` | 2026-10-15 18:04 |
| `results/imu/cm_rf_temporal_loso_4_seed1.pkl` | 18.9 KB | `f5776271172c991d1c10b11477c8e03c` | 2026-10-15 21:04 |
| `results/imu/cm_rf_temporal_loso_4_seed2.pkl` | 18.9 KB | `6dd162aa4890cf40e4ef8e16b6b95344` | 2026-10-15 21:09 |
| `results/imu/cm_rf_temporal_loso_4_seed3.pkl` | 18.9 KB | `4e2fb39038a1ecddfbba86695c5eaa18` | 2026-10-15 21:14 |
| `results/imu/cm_rf_temporal_loso_4_seed4.pkl` | 19.7 KB | `53d3774c8fa295add131647de5ff261e` | 2026-10-15 21:19 |
| `results/imu/cm_rf_temporal_loso_4_shuffled_seed0.pkl` | 18.9 KB | `776f211a9af37ec5ac3bc09bdffc885c` | 2026-10-15 20:16 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed0.pkl` | 517.9 KB | `3fde5b9a4824e04759f4bc29681228ec` | 2026-10-16 18:51 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed1.pkl` | 517.9 KB | `67e903515702d428ddff26b852cf4185` | 2026-10-16 19:35 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed2.pkl` | 517.9 KB | `e3de0f1db68dab7f4937d1a657f9b1c6` | 2026-10-16 19:40 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed3.pkl` | 517.9 KB | `3f11a2ae27dff06365e3696351e41584` | 2026-10-16 19:46 |
| `results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed4.pkl` | 517.9 KB | `088d2f212bbe316c9f3e4e456c29a81e` | 2026-10-16 19:52 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed0.pkl` | 590.9 KB | `a3026e7bc60c3c3f2da60fb6040919bc` | 2026-10-15 18:08 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed1.pkl` | 590.9 KB | `b18434cff3f19f8a36c2c7e7553e5dc5` | 2026-10-15 21:07 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed2.pkl` | 590.9 KB | `e3a1342891b6a5ce5a68d07abb5c6fa3` | 2026-10-15 21:12 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed3.pkl` | 590.9 KB | `78aac20fb663bb57aa826361e52cedab` | 2026-10-15 21:17 |
| `results/imu/grid_search_results_general_db_imu_chronos_seed4.pkl` | 590.9 KB | `bc056e386fc0d4ef31ddd626fab68286` | 2026-10-15 23:56 |
| `results/imu/grid_search_results_general_db_imu_chronos_shuffled_seed0.pkl` | 590.9 KB | `66dccb120d50d3397781fc928ef7471a` | 2026-10-15 20:22 |
| `results/imu/grid_search_results_temporal_groupcv_seed0.pkl` | 505.6 KB | `e7443aae932f18473aeec310b05678cc` | 2026-10-16 18:48 |
| `results/imu/grid_search_results_temporal_groupcv_seed1.pkl` | 505.6 KB | `db64b698d57559a4777befdb1c17a689` | 2026-10-16 19:31 |
| `results/imu/grid_search_results_temporal_groupcv_seed2.pkl` | 505.6 KB | `36c04d870e143ca9dcfbda8f291d0a90` | 2026-10-16 19:37 |
| `results/imu/grid_search_results_temporal_groupcv_seed3.pkl` | 505.6 KB | `a0a2307c1466c777d786fc052d689a6c` | 2026-10-16 19:42 |
| `results/imu/grid_search_results_temporal_groupcv_seed4.pkl` | 505.6 KB | `44b164d0d55211b46748573ea4181e62` | 2026-10-16 19:48 |
| `results/imu/grid_search_results_temporal_seed0.pkl` | 576.1 KB | `599bec5364bf88c8edc35dd42999bdc1` | 2026-10-15 18:04 |
| `results/imu/grid_search_results_temporal_seed1.pkl` | 576.1 KB | `a3d61ce0c99e612989faaa2e4bb292a4` | 2026-10-15 21:04 |
| `results/imu/grid_search_results_temporal_seed2.pkl` | 576.1 KB | `a16f8da27638d2aae9776b6c14b6ba57` | 2026-10-15 21:09 |
| `results/imu/grid_search_results_temporal_seed3.pkl` | 576.1 KB | `b6b0f0bc9baaa77f797eb8dcddca0c90` | 2026-10-15 21:14 |
| `results/imu/grid_search_results_temporal_seed4.pkl` | 576.1 KB | `d10a83b46c824964a84a589b14f2bdae` | 2026-10-15 21:19 |
| `results/imu/grid_search_results_temporal_shuffled_seed0.pkl` | 576.1 KB | `f6cf6e9eb646b52d202a9724977b9783` | 2026-10-15 20:16 |
| `results/imu/names.txt` | 6.4 KB | `32986c9e41e77beb22be4b089e243b00` | 2026-10-15 21:19 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed0.pkl` | 19.7 KB | `97aa078022fc612e96811841256b161f` | 2026-10-15 17:38 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed1.pkl` | 19.7 KB | `266252a8fcf816655653162469afb0a0` | 2026-10-15 20:33 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed2.pkl` | 19.7 KB | `3eb3191ba42d76687f0d1151a672a7e0` | 2026-10-15 20:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed3.pkl` | 19.7 KB | `3bf7f29b0d144cc607d6549e702a1737` | 2026-10-15 20:52 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_seed4.pkl` | 19.7 KB | `452a6d2b51687796159d95551baac961` | 2026-10-15 21:02 |
| `results/landmarks/cm_rf_general_db_lm_chronos_balanced_shuffled_seed0.pkl` | 19.7 KB | `f5642c91417a599f6295ab1fb040ddfa` | 2026-10-15 19:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed0.pkl` | 19.7 KB | `1f0835c2b5eb536b387ab2b78f4254ba` | 2026-10-16 18:33 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed1.pkl` | 19.7 KB | `8b210e89eb2be0972224ce5789dd2112` | 2026-10-16 20:18 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed2.pkl` | 19.7 KB | `78ab98bbdb8be785ebbf66594446726c` | 2026-10-16 20:58 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed3.pkl` | 19.7 KB | `33d0df6cc86f0f21b61f5fd62b4c21b0` | 2026-10-16 21:37 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_groupcv_seed4.pkl` | 19.7 KB | `8574b83a9c23bd408c753276cb25d060` | 2026-10-16 22:14 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_seed0.pkl` | 19.7 KB | `92d57eedbc12dcc1546b014b66f6724b` | 2026-10-15 17:42 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_0_shuffled_seed0.pkl` | 19.7 KB | `e3c87cb92c54d286af3677320b9a8ef5` | 2026-10-15 19:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed0.pkl` | 19.7 KB | `9fd80a5c6559a8df41c3050eb7bad97d` | 2026-10-16 18:36 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed1.pkl` | 19.7 KB | `1401270ef141c21dc9e4a87a91db2adb` | 2026-10-16 20:21 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed2.pkl` | 19.7 KB | `565502c2b1df55e5deedc872038b39ee` | 2026-10-16 21:01 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed3.pkl` | 19.7 KB | `8d6d18f0c9298e7603d6fbf1f30ce059` | 2026-10-16 21:40 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_groupcv_seed4.pkl` | 19.7 KB | `ea1b3ada68e29b06190f723bd42f2124` | 2026-10-16 22:17 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_seed0.pkl` | 19.7 KB | `828d74648d72496151b933ff10321c5d` | 2026-10-15 17:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_1_shuffled_seed0.pkl` | 19.7 KB | `0308445de78e229ff834653f2bf8a03f` | 2026-10-15 19:53 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed0.pkl` | 19.7 KB | `38345285798c1a25f3b597b0d9fd5e12` | 2026-10-16 18:40 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed1.pkl` | 19.7 KB | `daa959e38cb70aec6ee9dd3c3be5e776` | 2026-10-16 20:25 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed2.pkl` | 19.7 KB | `47e665af43c7b295fddaa11666bfcee3` | 2026-10-16 21:05 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed3.pkl` | 19.7 KB | `47e069b6b71b3101ccb26cf32d145ef7` | 2026-10-16 21:44 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_groupcv_seed4.pkl` | 19.7 KB | `e7a6ebba2ac6410db8e85e79a21ec955` | 2026-10-16 22:20 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_seed0.pkl` | 19.7 KB | `3a956da9989f51ae68fe8d002a074834` | 2026-10-15 17:51 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_2_shuffled_seed0.pkl` | 19.7 KB | `878c75441cad02aff385048a6b0b99d7` | 2026-10-15 20:03 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed0.pkl` | 19.7 KB | `adc1e1b5271ab5121e83a795eca40f71` | 2026-10-16 18:43 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed1.pkl` | 19.7 KB | `eb316144042a2b5bfb560755c7635c4f` | 2026-10-16 20:28 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed2.pkl` | 19.7 KB | `85b2d32c4d21b1c39691614a435d9802` | 2026-10-16 21:08 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed3.pkl` | 19.7 KB | `d3f0a9a9598c79e73e499d93d2a9dfa1` | 2026-10-16 21:47 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_groupcv_seed4.pkl` | 19.7 KB | `f44d7e571d0191b90316dc8bb3a16740` | 2026-10-16 22:23 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_seed0.pkl` | 19.7 KB | `f3961212c4eceb06e09d9b3565e57194` | 2026-10-15 17:56 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_3_shuffled_seed0.pkl` | 19.7 KB | `c7554c1f9cdcf2944c50354618d1628f` | 2026-10-15 20:08 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed0.pkl` | 19.7 KB | `f04d5bcd581df25b85d2ec46c210efb0` | 2026-10-16 18:46 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed1.pkl` | 19.7 KB | `dfc5083325f2d5dc3c3062008a2a3030` | 2026-10-16 20:32 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed2.pkl` | 19.7 KB | `a1ba34854b3abfe4face62f95ae5d2d5` | 2026-10-16 21:12 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed3.pkl` | 19.7 KB | `1fecc94b15847639ce5bdfb62ec8faab` | 2026-10-16 21:50 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_groupcv_seed4.pkl` | 19.7 KB | `831f3fbe2e3406e5f06be1d177d5858e` | 2026-10-16 22:26 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_seed0.pkl` | 19.7 KB | `5f51b139f106360af0376763c6ee08f4` | 2026-10-15 18:01 |
| `results/landmarks/cm_rf_general_db_lm_chronos_loso_4_shuffled_seed0.pkl` | 19.7 KB | `7543ce7a764d6a98d043f00e9420b5a8` | 2026-10-15 20:14 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed0.pkl` | 19.7 KB | `729a75bd541412b52acc00f87c45349b` | 2026-10-15 17:07 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed1.pkl` | 19.7 KB | `0c34d489c8bb3591ff1a4fd0c29d916d` | 2026-10-15 20:28 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed2.pkl` | 19.7 KB | `8a6c8aa44850db879d0f9e58bb5f81ef` | 2026-10-15 20:38 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed3.pkl` | 19.7 KB | `b992da4fb98ee98a3e281ab3dcf8f99f` | 2026-10-15 20:48 |
| `results/landmarks/cm_rf_temporal_features_balanced_seed4.pkl` | 19.7 KB | `3bdb0d5881f71c0852812494f52f6dea` | 2026-10-15 20:58 |
| `results/landmarks/cm_rf_temporal_features_balanced_shuffled_seed0.pkl` | 19.7 KB | `66452328d9698d00c072f4928b2f50b1` | 2026-10-15 18:16 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed0.pkl` | 19.7 KB | `bf732032d9ecdaa8fd5dad416b4c344a` | 2026-10-16 18:14 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed1.pkl` | 19.7 KB | `e8d37b4787bf4f46fc3d5008b9a28347` | 2026-10-16 19:57 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed2.pkl` | 19.7 KB | `294761e5b393bea51f2bb89b4486f29f` | 2026-10-16 20:36 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed3.pkl` | 19.7 KB | `6a431bf6743756f92e4e3faf2f891625` | 2026-10-16 21:16 |
| `results/landmarks/cm_rf_temporal_features_loso_0_groupcv_seed4.pkl` | 19.7 KB | `649f3874d6de0c127e48ec8a48153f80` | 2026-10-16 21:55 |
| `results/landmarks/cm_rf_temporal_features_loso_0_seed0.pkl` | 19.7 KB | `d2a88fa926072324a5034e0dff9c676f` | 2026-10-15 17:12 |
| `results/landmarks/cm_rf_temporal_features_loso_0_shuffled_seed0.pkl` | 19.7 KB | `392f36fa87178c4d27464bdaddeef4dd` | 2026-10-15 19:02 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed0.pkl` | 19.7 KB | `42644aebbe621c99d0aa7fc234d4bb9d` | 2026-10-16 18:18 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed1.pkl` | 19.7 KB | `132726b6958a907cff5ee69c46731ed2` | 2026-10-16 20:01 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed2.pkl` | 19.7 KB | `0b493f5df7fda4ec06c58cd7596bb687` | 2026-10-16 20:40 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed3.pkl` | 19.7 KB | `1878cd54e9727f5465e97e72fb47ffa4` | 2026-10-16 21:20 |
| `results/landmarks/cm_rf_temporal_features_loso_1_groupcv_seed4.pkl` | 19.7 KB | `703e4dad4df5bb886e3bf8c879ebd753` | 2026-10-16 21:59 |
| `results/landmarks/cm_rf_temporal_features_loso_1_seed0.pkl` | 19.7 KB | `1b555f3035f65d4e7aef3dce5a6afd2c` | 2026-10-15 17:17 |
| `results/landmarks/cm_rf_temporal_features_loso_1_shuffled_seed0.pkl` | 19.7 KB | `af26a00687c4c632a37cdb36eab1271a` | 2026-10-15 19:08 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed0.pkl` | 19.7 KB | `c7f9b40af049f289c24565383d34ac87` | 2026-10-16 18:22 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed1.pkl` | 19.7 KB | `2655e27e5d03cd0d8d3f47056322ce44` | 2026-10-16 20:05 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed2.pkl` | 19.7 KB | `faa8ec7b5f354718660e7907444fd8e7` | 2026-10-16 20:45 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed3.pkl` | 19.7 KB | `46c81dd8a5472cd9379fef14e65126fb` | 2026-10-16 21:25 |
| `results/landmarks/cm_rf_temporal_features_loso_2_groupcv_seed4.pkl` | 19.7 KB | `411f32e99d7a6c04ea9fff94811e08ac` | 2026-10-16 22:03 |
| `results/landmarks/cm_rf_temporal_features_loso_2_seed0.pkl` | 19.7 KB | `18a9e7d2367204110861cb6dcb3bb227` | 2026-10-15 17:23 |
| `results/landmarks/cm_rf_temporal_features_loso_2_shuffled_seed0.pkl` | 19.7 KB | `6d49befa917305431308c7865d48c74e` | 2026-10-15 19:15 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed0.pkl` | 19.7 KB | `99576579638013435ec7e245b5af737f` | 2026-10-16 18:26 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed1.pkl` | 19.7 KB | `1e634c4ef7b918cb25e8ec2f104c5f16` | 2026-10-16 20:10 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed2.pkl` | 19.7 KB | `92012a8fe5648001c470b3520b59747e` | 2026-10-16 20:50 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed3.pkl` | 19.7 KB | `68b959eb3ce351c6eb40ad53fc2bbda0` | 2026-10-16 21:29 |
| `results/landmarks/cm_rf_temporal_features_loso_3_groupcv_seed4.pkl` | 19.7 KB | `616b1a5545d1beea7acc065213ca4831` | 2026-10-16 22:07 |
| `results/landmarks/cm_rf_temporal_features_loso_3_seed0.pkl` | 19.7 KB | `6fd62dfcd2b2d4021f38d82af30c0454` | 2026-10-15 17:28 |
| `results/landmarks/cm_rf_temporal_features_loso_3_shuffled_seed0.pkl` | 19.7 KB | `72d12253d926f62a675430355e71a72a` | 2026-10-15 19:22 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed0.pkl` | 19.7 KB | `f411e9cdd04f1182c4a1cc3955598f26` | 2026-10-16 18:30 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed1.pkl` | 19.7 KB | `48e2fff2c4501d10fd5ea4df22b2e901` | 2026-10-16 20:15 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed2.pkl` | 19.7 KB | `11b0645d47d5b242a2dc5be76d25605c` | 2026-10-16 20:55 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed3.pkl` | 19.7 KB | `dd364efd11a023e159899b489964a62b` | 2026-10-16 21:34 |
| `results/landmarks/cm_rf_temporal_features_loso_4_groupcv_seed4.pkl` | 19.7 KB | `c861afa2b47765be9f54870c3504cc54` | 2026-10-16 22:11 |
| `results/landmarks/cm_rf_temporal_features_loso_4_seed0.pkl` | 19.7 KB | `5d55e763a7374d2f5b0bd78c7efbd011` | 2026-10-15 17:34 |
| `results/landmarks/cm_rf_temporal_features_loso_4_shuffled_seed0.pkl` | 19.7 KB | `5f3b82addf735f6098bef1505552ad8a` | 2026-10-15 19:32 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed0.pkl` | 541.3 KB | `51c297d71ace0caab1971815a4d93fe3` | 2026-10-16 18:46 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed1.pkl` | 541.3 KB | `cda69a0a6a11b282c0d71802e402da9e` | 2026-10-16 20:32 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed2.pkl` | 541.3 KB | `0468eb2195051b098dcad4a18819a575` | 2026-10-16 21:12 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed3.pkl` | 541.3 KB | `4e7402b20f72d915dc371d38aa74a47c` | 2026-10-16 21:50 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed4.pkl` | 541.3 KB | `404a0bda84d11c06fae4b62ef243d2f4` | 2026-10-16 22:26 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed0.pkl` | 649.6 KB | `a98bd7632d1f3439ccaad534648dca6a` | 2026-10-15 18:01 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed1.pkl` | 108.8 KB | `27c220c1523a2f75caab065c647d7821` | 2026-10-15 20:33 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed2.pkl` | 108.8 KB | `2939065cfda48692963cb3edaa4dc0bb` | 2026-10-15 20:42 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed3.pkl` | 108.8 KB | `7dead5a7e7d236a84f9f4e684ac67180` | 2026-10-15 20:52 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed4.pkl` | 108.8 KB | `e6a73490abc40746d39c65a250b72f8b` | 2026-10-15 21:02 |
| `results/landmarks/grid_search_results_general_db_lm_chronos_chronos_shuffled_seed0.pkl` | 649.6 KB | `3247f938e049ec8ed45ae17846d41978` | 2026-10-15 20:14 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed0.pkl` | 592.4 KB | `814e2748e6c36250bc2f253382574748` | 2026-10-16 18:30 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed1.pkl` | 592.4 KB | `89f5d203e7442cc3bb982f25e5665919` | 2026-10-16 20:15 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed2.pkl` | 592.4 KB | `c507a6f58f2568a29141bc82bc2eb520` | 2026-10-16 20:55 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed3.pkl` | 592.4 KB | `378fcaeae27e166e0ac34583db9cd7c5` | 2026-10-16 21:34 |
| `results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed4.pkl` | 592.4 KB | `d0ede19468e218bb048543925c66c2bb` | 2026-10-16 22:11 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed0.pkl` | 710.9 KB | `93993bb47b46b7c9a4be823bbcee9135` | 2026-10-15 17:34 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed1.pkl` | 119.0 KB | `0df827b22732912f3bf4140721b826a3` | 2026-10-15 20:28 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed2.pkl` | 119.0 KB | `d3b8d5ff36d96246d3649ed0c763654f` | 2026-10-15 20:38 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed3.pkl` | 119.0 KB | `7fc864df2af82d7206f571cd4818191c` | 2026-10-15 20:48 |
| `results/landmarks/grid_search_results_temporal_features_chronos_seed4.pkl` | 119.0 KB | `f8db3ace788690bce9b4cfc5b9c74325` | 2026-10-15 20:58 |
| `results/landmarks/grid_search_results_temporal_features_chronos_shuffled_seed0.pkl` | 710.9 KB | `c89924b40748f30e3fbc09a90b761452` | 2026-10-15 19:32 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_0_seed0.pkl` | 181 B | `9fd829bfcbd7b9d446516cc1d2ebb50b` | 2026-10-20 16:05 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_0_seed1.pkl` | 181 B | `8a6f7d52b5984b09bbf2ed1c2631513d` | 2026-10-20 16:33 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_0_seed2.pkl` | 181 B | `d58ac9990f0709beb2505082df60697c` | 2026-10-20 16:59 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_0_seed3.pkl` | 181 B | `b7340b18d42e01277d12a2b097e92a62` | 2026-10-20 17:27 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_0_seed4.pkl` | 181 B | `5967b76be9665dbda40154157e826ce0` | 2026-10-20 17:54 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_1_seed0.pkl` | 181 B | `e0d7474bbf0f09a787332bd5efb4909c` | 2026-10-20 16:08 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_1_seed1.pkl` | 181 B | `353437e7222ab227f1c2bbaadd3bc87a` | 2026-10-20 16:36 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_1_seed2.pkl` | 181 B | `b894a92f9c0ad8210fa3b05dda4fda84` | 2026-10-20 17:02 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_1_seed3.pkl` | 181 B | `07e88cf782fc13fc45526a0d9e52d2d8` | 2026-10-20 17:30 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_1_seed4.pkl` | 181 B | `e7bd399e385dcda04af2d165fb979765` | 2026-10-20 17:57 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_2_seed0.pkl` | 181 B | `bfd9b34f0bf4b1f2ad2eacfffe1d36dc` | 2026-10-20 16:13 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_2_seed1.pkl` | 181 B | `b2b2fdd54cdd494cb4317a03427f5139` | 2026-10-20 16:40 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_2_seed2.pkl` | 181 B | `5a6b8862f685324fd19598707d6eb4a7` | 2026-10-20 17:06 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_2_seed3.pkl` | 181 B | `b0bbf2c5ef509c881b87c8317231230d` | 2026-10-20 17:34 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_2_seed4.pkl` | 181 B | `5a6b8862f685324fd19598707d6eb4a7` | 2026-10-20 18:01 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_3_seed0.pkl` | 181 B | `c456fc5af25474e2db0fde27c6725ee4` | 2026-10-20 16:17 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_3_seed1.pkl` | 181 B | `33ef1112744d7a9e546938a9d734246c` | 2026-10-20 16:43 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_3_seed2.pkl` | 181 B | `687f31dc0d5d92dcfb8746a3de8e7c06` | 2026-10-20 17:11 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_3_seed3.pkl` | 181 B | `687f31dc0d5d92dcfb8746a3de8e7c06` | 2026-10-20 17:38 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_3_seed4.pkl` | 181 B | `687f31dc0d5d92dcfb8746a3de8e7c06` | 2026-10-20 18:05 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_4_seed0.pkl` | 181 B | `ac482a1e6ff58e3e50d6aaac8974447e` | 2026-10-20 16:21 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_4_seed1.pkl` | 181 B | `c7ee338155900acc73981033ce49bdbb` | 2026-10-20 16:47 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_4_seed2.pkl` | 181 B | `3143dbffadd95421ff4cb9d5f98cb94d` | 2026-10-20 17:15 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_4_seed3.pkl` | 181 B | `4c1bf40a93a41dbc1fff0d87dc8895e4` | 2026-10-20 17:42 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_loso_4_seed4.pkl` | 181 B | `c7ee338155900acc73981033ce49bdbb` | 2026-10-20 18:09 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_seed0.pkl` | 181 B | `8e3c3d015dd42d1b9cffe5c0ac13756b` | 2026-10-20 16:01 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_seed1.pkl` | 181 B | `9a033c73c921e4c3cc64a9b7e8535e84` | 2026-10-20 16:29 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_seed2.pkl` | 181 B | `07281c071ad89de79058dfa2e5b37bc7` | 2026-10-20 16:55 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_seed3.pkl` | 181 B | `cdd4f52ea00067c9ba00d29796e9fb3b` | 2026-10-20 17:23 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_deaf_seed4.pkl` | 181 B | `99f40650e1550996b8555548e5810627` | 2026-10-20 17:50 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_schema_new_seed0.pkl` | 181 B | `f8c3584524ef946fd4eeaf09c5d679bf` | 2026-10-20 16:25 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_schema_new_seed1.pkl` | 181 B | `9963dd2e6ea330fcc8c2e3455610197b` | 2026-10-20 16:51 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_schema_new_seed2.pkl` | 181 B | `2bb67ecaac4c0e5972f7326d27c670ee` | 2026-10-20 17:19 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_schema_new_seed3.pkl` | 181 B | `0733079501937cf0341b98acbddb0c17` | 2026-10-20 17:46 |
| `results/signant_bodynorm/cm_rf_temporal_features_bodynorm_schema_new_seed4.pkl` | 181 B | `086c39108bbfed748e37409d116985e3` | 2026-10-20 18:13 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_new_schema_seed0.pkl` | 124.0 KB | `9b7d392bd49f210a482e05373f8900d5` | 2026-10-20 16:25 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_new_schema_seed1.pkl` | 124.1 KB | `b65d4be6d6c1c36a6e6c11c3da2d27d5` | 2026-10-20 16:51 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_new_schema_seed2.pkl` | 124.0 KB | `f4f1e976913f9339b09e836f8b48b9a4` | 2026-10-20 17:19 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_new_schema_seed3.pkl` | 124.0 KB | `84682f3d674eb6edc99e6f4f2113126b` | 2026-10-20 17:46 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_new_schema_seed4.pkl` | 124.1 KB | `e59b52eb0ce3e8d0f60cbf3f562325fb` | 2026-10-20 18:13 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed0.pkl` | 741.4 KB | `2a672ebd6f6fa61059bca6f56719a6a4` | 2026-10-20 16:21 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed1.pkl` | 741.4 KB | `29f01990b58bfb5e9dc61ab9f5eadbd3` | 2026-10-20 16:47 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed2.pkl` | 741.4 KB | `1244943b38fc43002f93922784b0cd24` | 2026-10-20 17:15 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed3.pkl` | 741.4 KB | `6617dcc6eaa498889f852cff8b6c05d5` | 2026-10-20 17:42 |
| `results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed4.pkl` | 741.4 KB | `c28bb9912512dd428f9d72c312b187e4` | 2026-10-20 18:09 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed0.pkl` | 181 B | `533f6c91afef98724eed87404879fa18` | 2026-10-16 22:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed1.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:34 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed2.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:48 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed3.pkl` | 181 B | `31539431b28471d79ba5b287aaa906e2` | 2026-10-20 21:01 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_0_seed4.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 21:15 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 22:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed1.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:35 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed2.pkl` | 181 B | `ca86ccc43af591e77fc923bd005b46a4` | 2026-10-20 20:48 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed3.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 21:02 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_1_seed4.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 21:15 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed0.pkl` | 181 B | `9fd41059324d3455b2e4f96854f42d13` | 2026-10-16 22:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed1.pkl` | 181 B | `81b5eba105e9d9b37bb454ffdf6203d3` | 2026-10-20 20:36 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed2.pkl` | 181 B | `34b8615048c9865ed304dce0327a64b1` | 2026-10-20 20:49 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed3.pkl` | 181 B | `e7b0dbb289afb2e2567e1095c7bf8520` | 2026-10-20 21:02 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_2_seed4.pkl` | 181 B | `e7b0dbb289afb2e2567e1095c7bf8520` | 2026-10-20 21:16 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed0.pkl` | 181 B | `84aefbb7540243c594d022f96e97afba` | 2026-10-16 22:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed1.pkl` | 181 B | `34b8615048c9865ed304dce0327a64b1` | 2026-10-20 20:36 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed2.pkl` | 181 B | `34b8615048c9865ed304dce0327a64b1` | 2026-10-20 20:50 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed3.pkl` | 181 B | `34b8615048c9865ed304dce0327a64b1` | 2026-10-20 21:03 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_3_seed4.pkl` | 181 B | `84aefbb7540243c594d022f96e97afba` | 2026-10-20 21:17 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed0.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-16 22:34 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed1.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-20 20:37 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed2.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-20 20:50 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed3.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-20 21:04 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_loso_4_seed4.pkl` | 181 B | `95dce421a53e62271a0994af0977c3f5` | 2026-10-20 21:17 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed0.pkl` | 181 B | `216083e92903b0f87bfa3affc5a1e2fe` | 2026-10-16 22:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed1.pkl` | 181 B | `3f3d3766ba2e572276bec9f5f52b451f` | 2026-10-20 20:34 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed2.pkl` | 181 B | `17481daffe4e486cc66a25c66747ec79` | 2026-10-20 20:47 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed3.pkl` | 181 B | `983cd5acf248c14cbf6d35fed5d7acfe` | 2026-10-20 21:01 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_deaf_seed4.pkl` | 181 B | `04e74423450b161b22ed0568b9aebcd7` | 2026-10-20 21:14 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed0.pkl` | 19.7 KB | `705d735d2180347ef73f35593914c5b1` | 2026-10-16 22:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed1.pkl` | 19.7 KB | `850a0758ff2a0d97c6fc6c5fb43cff68` | 2026-10-20 20:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed2.pkl` | 19.7 KB | `54275bc18949e5d398580514b722b072` | 2026-10-20 20:43 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed3.pkl` | 19.7 KB | `e72dee07d915f6193d9ccc36dedb23ec` | 2026-10-20 20:57 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_0_seed4.pkl` | 19.7 KB | `5d7df81658a16c28d85273537d61ae4c` | 2026-10-20 21:10 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed0.pkl` | 19.7 KB | `49a9634dfcbab78d71a168005a5f1a8a` | 2026-10-16 22:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed1.pkl` | 19.7 KB | `6536d8397c09e00395070588f0f14872` | 2026-10-20 20:30 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed2.pkl` | 19.7 KB | `5a938224468a0683a05c2bc1d2733f21` | 2026-10-20 20:44 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed3.pkl` | 19.7 KB | `d8a690aa1fe132fd03a3e6916462de55` | 2026-10-20 20:57 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_1_seed4.pkl` | 19.7 KB | `442da0858267353bd35a6e05d5776a1d` | 2026-10-20 21:11 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed0.pkl` | 19.7 KB | `c10a032190e111d00ccd0e911f6d4ebd` | 2026-10-16 22:31 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed1.pkl` | 19.7 KB | `e4411e3ede2253a3b6b2619ebd1d4fb9` | 2026-10-20 20:31 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed2.pkl` | 19.7 KB | `d0e702fea4ce91d70f9ecae0adcdd4de` | 2026-10-20 20:45 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed3.pkl` | 19.7 KB | `8db590627e9983213c9db653655f6cfa` | 2026-10-20 20:58 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_2_seed4.pkl` | 19.7 KB | `53a3dca50ebfe470bbbfba76d48332b4` | 2026-10-20 21:12 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed0.pkl` | 19.7 KB | `e034a799b56ade60c1b847e7098e9be1` | 2026-10-16 22:31 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed1.pkl` | 19.7 KB | `cfa54f0854518d4498f07b889baa7eb3` | 2026-10-20 20:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed2.pkl` | 19.7 KB | `5fe89c19dd3adba0c4b91dc319340504` | 2026-10-20 20:46 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed3.pkl` | 19.7 KB | `c0b936ac6ac7e507380cb9bd2887cf4d` | 2026-10-20 20:59 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_3_seed4.pkl` | 19.7 KB | `eb23b47f0d3970c0572eee42d1bb9548` | 2026-10-20 21:13 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed0.pkl` | 18.9 KB | `b3356aeedff1a8f9ffffaa771f2967c5` | 2026-10-16 22:32 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed1.pkl` | 18.9 KB | `042c176ffe81f2690f03be2aa9fbd783` | 2026-10-20 20:33 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed2.pkl` | 18.9 KB | `04e9633c72bf11c0bf07d1d832d47e67` | 2026-10-20 20:46 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed3.pkl` | 18.9 KB | `2d1855f3967055f1c892dd6501d6b44f` | 2026-10-20 21:00 |
| `results/signant_imu/cm_rf_general_db_imu_chronos_loso_4_seed4.pkl` | 18.9 KB | `d9c90dd6681525c9fd70aac5bd564519` | 2026-10-20 21:13 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 22:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed1.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:27 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed2.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:40 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed3.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:54 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_0_seed4.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 21:07 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed0.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-16 22:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed1.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:27 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed2.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:41 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed3.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 20:54 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_1_seed4.pkl` | 181 B | `607ce34b1bc439ceae62fb0c91948e04` | 2026-10-20 21:08 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed0.pkl` | 181 B | `1be56a5254bd6f759ec365f659caced0` | 2026-10-16 22:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed1.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-20 20:28 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed2.pkl` | 181 B | `1be56a5254bd6f759ec365f659caced0` | 2026-10-20 20:41 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed3.pkl` | 181 B | `1be56a5254bd6f759ec365f659caced0` | 2026-10-20 20:55 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_2_seed4.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-20 21:08 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed0.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-16 22:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed1.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-20 20:28 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed2.pkl` | 181 B | `c0e34bc5add6fff8fd5e7f39cd7c5cd1` | 2026-10-20 20:42 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed3.pkl` | 181 B | `7488e6775761905c4a13879b31cd42f1` | 2026-10-20 20:55 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_3_seed4.pkl` | 181 B | `e027b50e506ca23c7039f1c911ab33ee` | 2026-10-20 21:09 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed0.pkl` | 181 B | `ae9a4c2e68166bf8b19979616c24cf32` | 2026-10-16 22:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed1.pkl` | 181 B | `e76596349b60eaf4ff500b0c4a2f05f8` | 2026-10-20 20:29 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed2.pkl` | 181 B | `056e06e193f776f50f7aaeab33b1b2ad` | 2026-10-20 20:42 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed3.pkl` | 181 B | `fc288dae3ccbc29c3e011824959a3996` | 2026-10-20 20:56 |
| `results/signant_imu/cm_rf_temporal_deaf_loso_4_seed4.pkl` | 181 B | `56d71be8e85c7540a34ddaa0d9c7a5d0` | 2026-10-20 21:09 |
| `results/signant_imu/cm_rf_temporal_deaf_seed0.pkl` | 181 B | `38f79d5ba058dd77837f39a28191069d` | 2026-10-16 22:28 |
| `results/signant_imu/cm_rf_temporal_deaf_seed1.pkl` | 181 B | `b0f714279f8ae6054acf5bce24a8553f` | 2026-10-20 20:27 |
| `results/signant_imu/cm_rf_temporal_deaf_seed2.pkl` | 181 B | `b0f714279f8ae6054acf5bce24a8553f` | 2026-10-20 20:40 |
| `results/signant_imu/cm_rf_temporal_deaf_seed3.pkl` | 181 B | `dd76a693228d50fdd36f08bf7e759d13` | 2026-10-20 20:53 |
| `results/signant_imu/cm_rf_temporal_deaf_seed4.pkl` | 181 B | `39afb3d28d7bcc6e5680291f7d2f22df` | 2026-10-20 21:07 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed0.pkl` | 19.7 KB | `6538c2671309f3e5440d96795658697d` | 2026-10-16 22:27 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed1.pkl` | 19.7 KB | `9a74aba01f153377904da91b3febb663` | 2026-10-20 20:24 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed2.pkl` | 19.7 KB | `0dea3bc95b0c797bf8d218531c241bed` | 2026-10-20 20:37 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed3.pkl` | 19.7 KB | `c0c2255a0eb1c2609b49d8264a58ddc9` | 2026-10-20 20:51 |
| `results/signant_imu/cm_rf_temporal_loso_0_seed4.pkl` | 19.7 KB | `328f0c2d2ba7ddfac55d52aa237b203b` | 2026-10-20 21:04 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed0.pkl` | 19.7 KB | `6aea8e7e3cb492323b7e0aeae1c7e3db` | 2026-10-16 22:27 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed1.pkl` | 19.7 KB | `2c1360ccee4d76337a5b0060341d8c8f` | 2026-10-20 20:24 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed2.pkl` | 19.7 KB | `d69031f427c6566b01d655bde037f5f6` | 2026-10-20 20:38 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed3.pkl` | 19.7 KB | `b8d25b808df815c8914899133c7884b4` | 2026-10-20 20:51 |
| `results/signant_imu/cm_rf_temporal_loso_1_seed4.pkl` | 19.7 KB | `19c66ce33d50eeff4fb76e26f48d5e65` | 2026-10-20 21:05 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed0.pkl` | 19.7 KB | `2c2302e65148f611cbaf0bf84ded75fd` | 2026-10-16 22:28 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed1.pkl` | 19.7 KB | `ccd15085727f216198c02ee1b22d9c30` | 2026-10-20 20:25 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed2.pkl` | 19.7 KB | `7d8cf9af299576a4bf0c1383cd3a7fef` | 2026-10-20 20:38 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed3.pkl` | 19.7 KB | `7cabe3390724a996b5bcece905d6e1f0` | 2026-10-20 20:52 |
| `results/signant_imu/cm_rf_temporal_loso_2_seed4.pkl` | 19.7 KB | `4cd5c7b97015e6374859b56dedefa99c` | 2026-10-20 21:05 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed0.pkl` | 19.7 KB | `b58b2ac3732602ea161068295cdf549f` | 2026-10-16 22:28 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed1.pkl` | 19.7 KB | `dd4570f26d4b1b845320680dd5c7498d` | 2026-10-20 20:26 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed2.pkl` | 19.7 KB | `1f7c1f966e29d09ab2c7e0df23a04059` | 2026-10-20 20:39 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed3.pkl` | 19.7 KB | `b14b3bc1b7a2537050576a112b9b5aff` | 2026-10-20 20:52 |
| `results/signant_imu/cm_rf_temporal_loso_3_seed4.pkl` | 19.7 KB | `8e142701f257778d14072883d279820f` | 2026-10-20 21:06 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed0.pkl` | 19.7 KB | `638c4fd4e9d4e71ede5ce2c967c127ac` | 2026-10-16 22:28 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed1.pkl` | 18.9 KB | `12cdb8915126d1d4b4fed563489d89fd` | 2026-10-20 20:26 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed2.pkl` | 18.9 KB | `6a1d79954629ff1468409615602562ef` | 2026-10-20 20:39 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed3.pkl` | 18.9 KB | `ca7bf8ffcca37ce862982c038f345340` | 2026-10-20 20:53 |
| `results/signant_imu/cm_rf_temporal_loso_4_seed4.pkl` | 19.7 KB | `10429f870c100022cc16846c42fbf7c0` | 2026-10-20 21:06 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed0.pkl` | 1.1 MB | `27f87e2a6f55ba094f84389ca531370a` | 2026-10-16 22:34 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed1.pkl` | 1.1 MB | `50668a58f4a0dcee247593abc2533774` | 2026-10-20 20:37 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed2.pkl` | 1.1 MB | `6ef5dafa764ecbda5eabe5b23f5f69e7` | 2026-10-20 20:50 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed3.pkl` | 1.1 MB | `c1b9f15182d534b6dabe347aebf39961` | 2026-10-20 21:04 |
| `results/signant_imu/grid_search_results_general_db_imu_chronos_seed4.pkl` | 1.1 MB | `e1f5fc4c81c1c230b3e94d45fb7d5ec1` | 2026-10-20 21:17 |
| `results/signant_imu/grid_search_results_temporal_seed0.pkl` | 1.1 MB | `6aa33e684d82e243449bec6ffe4746ae` | 2026-10-16 22:29 |
| `results/signant_imu/grid_search_results_temporal_seed1.pkl` | 1.1 MB | `092ec92491cc97fef61818d2e13e693e` | 2026-10-20 20:29 |
| `results/signant_imu/grid_search_results_temporal_seed2.pkl` | 1.1 MB | `78ec3c9c7558fe0d8d6e4b8f1a291bdc` | 2026-10-20 20:42 |
| `results/signant_imu/grid_search_results_temporal_seed3.pkl` | 1.1 MB | `5b472c56fc7a8023b8c1fee6636a0ea4` | 2026-10-20 20:56 |
| `results/signant_imu/grid_search_results_temporal_seed4.pkl` | 1.1 MB | `45dc0ba75ee84402da8b00b2d3205699` | 2026-10-20 21:09 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed0.pkl` | 181 B | `6793b535246503f4d1d35c0348180183` | 2026-10-16 22:44 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed1.pkl` | 181 B | `e4c27f15f65cb8b58b9b33af52983dbd` | 2026-10-20 18:44 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed2.pkl` | 181 B | `4ec7e0f210a9734a1a04c88e54e20b9d` | 2026-10-20 19:18 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed3.pkl` | 181 B | `59cedbd838e57f322e225dab8db92178` | 2026-10-20 19:45 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_0_seed4.pkl` | 181 B | `97edcfafa574d96fe2c073eb04255f86` | 2026-10-20 20:13 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed0.pkl` | 181 B | `22d34d30dd17424302a8a3d162e42427` | 2026-10-16 22:45 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed1.pkl` | 181 B | `1c18d44643a3d256a36f01daf3794a9e` | 2026-10-20 18:48 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed2.pkl` | 181 B | `1c18d44643a3d256a36f01daf3794a9e` | 2026-10-20 19:20 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed3.pkl` | 181 B | `d66de21085fe15b99ed084057520d0d8` | 2026-10-20 19:47 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_1_seed4.pkl` | 181 B | `22d34d30dd17424302a8a3d162e42427` | 2026-10-20 20:15 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed0.pkl` | 181 B | `6f5002acb17fe5ba6421fe8232c7cc00` | 2026-10-16 22:47 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed1.pkl` | 181 B | `6d2dd502230c0353812408407f34c96c` | 2026-10-20 18:51 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed2.pkl` | 181 B | `d0aab7ff7a06094227068d3b1b892403` | 2026-10-20 19:22 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed3.pkl` | 181 B | `6d2dd502230c0353812408407f34c96c` | 2026-10-20 19:49 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_2_seed4.pkl` | 181 B | `a6805affb906724b83069f655ec593c3` | 2026-10-20 20:17 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed0.pkl` | 181 B | `b6f22e292ef66dae268ebbdab26991f6` | 2026-10-16 22:48 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed1.pkl` | 181 B | `13b54c3625306134d7599b0e4a7ad665` | 2026-10-20 18:55 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed2.pkl` | 181 B | `923dedb8a570060a1998bc954a1c9442` | 2026-10-20 19:24 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed3.pkl` | 181 B | `2ee0dfce6957cbb7ff0dd9c973ac6053` | 2026-10-20 19:51 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_3_seed4.pkl` | 181 B | `7a59eb1da18f83c8011a4fec389771a9` | 2026-10-20 20:19 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed0.pkl` | 181 B | `2ee0dfce6957cbb7ff0dd9c973ac6053` | 2026-10-16 22:49 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed1.pkl` | 181 B | `2588daf55b85e799aee021e67fe916f2` | 2026-10-20 18:58 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed2.pkl` | 181 B | `c9996dfd4cd77c8b4adc1b633ebcd550` | 2026-10-20 19:26 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed3.pkl` | 181 B | `3353e5bf2a1233480a832e36d7773889` | 2026-10-20 19:53 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_loso_4_seed4.pkl` | 181 B | `7dd660fe22b0adf92258b3cd7bde430e` | 2026-10-20 20:21 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed0.pkl` | 181 B | `7dbac3765dfe5dd9df61ef7d598f952a` | 2026-10-16 22:43 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed1.pkl` | 181 B | `4fe54d25a3794253be623da29b46493c` | 2026-10-20 18:40 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed2.pkl` | 181 B | `f250f4c40089c3fe4b89e066dcabc20b` | 2026-10-20 19:16 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed3.pkl` | 181 B | `1a5fdf18f8fc3d02ca5824963182a604` | 2026-10-20 19:43 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_deaf_seed4.pkl` | 181 B | `e46821f79eb83773a32d858af22f6b0c` | 2026-10-20 20:11 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed0.pkl` | 181 B | `146eaa99e871945ab17ce699db3942d3` | 2026-10-16 22:51 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed1.pkl` | 181 B | `2877922c293bbeecfd1916acb2224adc` | 2026-10-20 19:01 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed2.pkl` | 181 B | `67d7f55dff4151c3e7228a563c6f3e65` | 2026-10-20 19:28 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed3.pkl` | 181 B | `8afd53d821f583e2b6250193c565796e` | 2026-10-20 19:56 |
| `results/signant_landmarks/cm_rf_general_db_lm_chronos_schema_new_seed4.pkl` | 181 B | `925218512aeb75caaf7db742388609b5` | 2026-10-20 20:23 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed0.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-16 22:36 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed1.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 18:20 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed2.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 19:05 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed3.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 19:32 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_0_seed4.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 19:59 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed0.pkl` | 181 B | `12b59d2030363b89520a21ec67b0589c` | 2026-10-16 22:37 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed1.pkl` | 181 B | `8976950a3fb6d5c9b03f674f88bc08bc` | 2026-10-20 18:23 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed2.pkl` | 181 B | `4639657a8dea81dc4d3e2e1603aae757` | 2026-10-20 19:06 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed3.pkl` | 181 B | `eef8833833645467944a391583ae51ad` | 2026-10-20 19:33 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_1_seed4.pkl` | 181 B | `8976950a3fb6d5c9b03f674f88bc08bc` | 2026-10-20 20:01 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed0.pkl` | 181 B | `d3d7eaa6625738b34b1a9173c7135bcc` | 2026-10-16 22:38 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed1.pkl` | 181 B | `3c559774f80460664266f3b8657ada6a` | 2026-10-20 18:26 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed2.pkl` | 181 B | `d3d7eaa6625738b34b1a9173c7135bcc` | 2026-10-20 19:08 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed3.pkl` | 181 B | `3c559774f80460664266f3b8657ada6a` | 2026-10-20 19:35 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_2_seed4.pkl` | 181 B | `d3d7eaa6625738b34b1a9173c7135bcc` | 2026-10-20 20:03 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed0.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-16 22:39 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed1.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 18:29 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed2.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 19:10 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed3.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 19:37 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_3_seed4.pkl` | 157 B | `1fe5d0432fa8f079287e418cdc5b2fa6` | 2026-10-20 20:05 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed0.pkl` | 181 B | `3143dbffadd95421ff4cb9d5f98cb94d` | 2026-10-16 22:40 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed1.pkl` | 181 B | `4c1bf40a93a41dbc1fff0d87dc8895e4` | 2026-10-20 18:32 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed2.pkl` | 181 B | `d6b86422f87df675f82a04f43575f308` | 2026-10-20 19:12 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed3.pkl` | 181 B | `ac482a1e6ff58e3e50d6aaac8974447e` | 2026-10-20 19:39 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_loso_4_seed4.pkl` | 181 B | `c7ee338155900acc73981033ce49bdbb` | 2026-10-20 20:06 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed0.pkl` | 181 B | `9a033c73c921e4c3cc64a9b7e8535e84` | 2026-10-16 22:35 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed1.pkl` | 181 B | `9a033c73c921e4c3cc64a9b7e8535e84` | 2026-10-20 18:16 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed2.pkl` | 181 B | `086c39108bbfed748e37409d116985e3` | 2026-10-20 19:03 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed3.pkl` | 181 B | `086c39108bbfed748e37409d116985e3` | 2026-10-20 19:30 |
| `results/signant_landmarks/cm_rf_temporal_features_deaf_seed4.pkl` | 181 B | `fbc1212eb9d0c6adcb06974176594490` | 2026-10-20 19:58 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed0.pkl` | 181 B | `d9bfe1b48f7662f4851d792b15a69e85` | 2026-10-16 22:41 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed1.pkl` | 181 B | `7bd1cbac791e4088f38c53f0cc5e6952` | 2026-10-20 18:35 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed2.pkl` | 181 B | `d082eb99c685d950f17356dacc31705b` | 2026-10-20 19:13 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed3.pkl` | 181 B | `46909ff640951af4d7bf2d5632bd6975` | 2026-10-20 19:41 |
| `results/signant_landmarks/cm_rf_temporal_features_schema_new_seed4.pkl` | 181 B | `1adea347b7547b7beed6899460230034` | 2026-10-20 20:08 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed0.pkl` | 113.8 KB | `367ecd4b4b4b76da9d87c64196dd7921` | 2026-10-16 22:51 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed1.pkl` | 113.9 KB | `b74a146944f4eae78c38dc798496e236` | 2026-10-20 19:01 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed2.pkl` | 113.8 KB | `3f359648f4465b0ccf4478d20b7f4bf5` | 2026-10-20 19:28 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed3.pkl` | 113.8 KB | `de4159ac5cd3fcb09c6b8cfdd2bd07a2` | 2026-10-20 19:56 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_new_schema_seed4.pkl` | 113.9 KB | `4bfed848ab99c26619419823fb9c88d4` | 2026-10-20 20:23 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed0.pkl` | 680.1 KB | `61f04b2b95f8a783526f6b311c6af80b` | 2026-10-16 22:49 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed1.pkl` | 680.1 KB | `c1956c0115c55df96a1230067ada0b40` | 2026-10-20 18:58 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed2.pkl` | 680.1 KB | `3ace63bb6941115c6793b0e1014d0c0d` | 2026-10-20 19:26 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed3.pkl` | 680.1 KB | `84dc268f388e6382ffdb8e5d19b7eb62` | 2026-10-20 19:53 |
| `results/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed4.pkl` | 680.1 KB | `5b7140329cbd84a23a63bcb9c72d290e` | 2026-10-20 20:21 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed0.pkl` | 124.0 KB | `cfc9fe76fe85ef1dd087bfc9dd3f4cb1` | 2026-10-16 22:41 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed1.pkl` | 124.1 KB | `7949e6fb774011e997e1f20f294b01d6` | 2026-10-20 18:35 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed2.pkl` | 124.0 KB | `0c0ee898f84acced908224bd5a047175` | 2026-10-20 19:13 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed3.pkl` | 124.0 KB | `3cb786f2db835e867d9a15772daee48b` | 2026-10-20 19:41 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_new_schema_seed4.pkl` | 124.1 KB | `90f164cfe4bb2d9479d4c6f109bd04d4` | 2026-10-20 20:08 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed0.pkl` | 741.4 KB | `e125db6f577a47f5cfe94642dfe4f487` | 2026-10-16 22:40 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed1.pkl` | 741.4 KB | `58f859ddca59a4fdca8826bbd22ddedb` | 2026-10-20 18:32 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed2.pkl` | 741.4 KB | `06babbe4bab9925aed10a56a8cbf9671` | 2026-10-20 19:12 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed3.pkl` | 741.4 KB | `7690ba7f180426c89972212f1df0e5de` | 2026-10-20 19:39 |
| `results/signant_landmarks/grid_search_results_temporal_features_chronos_seed4.pkl` | 741.4 KB | `4448ffd056d52738f6b19b98bb4161ef` | 2026-10-20 20:06 |
| `sign_mapping_check/commit.txt` | 131 B | `94355ac041c20c9dc37ba211fa166dde` | 2026-10-28 23:49 |
| `sign_mapping_check/sign_mapping_check.csv` | 1.1 KB | `1df1dcecc12af7e15dfc5e1b80d717c3` | 2026-10-28 23:50 |
| `sign_mapping_check/sign_mapping_check.log` | 1.3 KB | `13f15d68263501216a5b6b80cb30efbe` | 2026-10-28 23:50 |
| `sign_mapping_check/sign_mapping_check_video_seconds.csv` | 3.5 KB | `b76113666a785b6593623ab42d074a2a` | 2026-10-28 23:50 |
| `signer_ci/command.txt` | 2.5 KB | `071028cd09eff9d4b9fdc7d9ded465b3` | 2026-10-20 15:45 |
| `signer_ci/commit.txt` | 170 B | `a04153971be01f3be86f33862609f637` | 2026-10-20 15:45 |
| `signer_ci/signer_ci.csv` | 5.4 KB | `e0f2d5fad4756cae57212209c8ef3aba` | 2026-10-20 17:12 |
| `signer_ci/signer_ci.log` | 5.5 KB | `798e33e8c86c940fd6d3094978c1d33a` | 2026-10-20 17:12 |
| `signer_ci/signer_pairs.csv` | 2.2 KB | `5e08356c0d7aa8a71aa53decd34a5a94` | 2026-10-20 17:12 |
| `signer_ci_final/command.txt` | 3.0 KB | `e043d31eaeb5a36d2101096aeb3fbaf2` | 2026-10-27 18:35 |
| `signer_ci_final/commit.txt` | 222 B | `94019ddb51d2044bbc69aa9f4f17b916` | 2026-10-27 18:35 |
| `signer_ci_final/signer_ci.csv` | 6.8 KB | `cb97f91cbd41e0c0935ad08df10133d0` | 2026-10-27 19:06 |
| `signer_ci_final/signer_ci.log` | 7.4 KB | `1b98f3f19df6b87dc9644af62a6b945c` | 2026-10-27 19:06 |
| `signer_ci_final/signer_pairs.csv` | 3.7 KB | `74a2bd21f68768dbda8fd921dc9df782` | 2026-10-27 19:06 |
| `signer_ci_v2/command.txt` | 2.5 KB | `aae077da8b1d25968c4cf6bf86598d34` | 2026-10-21 15:09 |
| `signer_ci_v2/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-21 15:09 |
| `signer_ci_v2/signer_ci.csv` | 5.9 KB | `27970ac949edfc01af37775d48f02136` | 2026-10-21 15:37 |
| `signer_ci_v2/signer_ci.log` | 6.0 KB | `258630af024221775652638f77cd6548` | 2026-10-21 15:37 |
| `signer_ci_v2/signer_pairs.csv` | 2.6 KB | `56c0446e33e2d8784d6fd0e4740d57e5` | 2026-10-21 15:37 |
| `signer_ci_v3/command.txt` | 2.5 KB | `31e00257491a198b92c1184c8e9535da` | 2026-10-22 02:03 |
| `signer_ci_v3/commit.txt` | 184 B | `dc762a89f7e465c5ff6cfa06bf97d8c3` | 2026-10-22 02:03 |
| `signer_ci_v3/signer_ci.csv` | 5.9 KB | `111e8067ef9f2837de927b8d36932c88` | 2026-10-22 02:31 |
| `signer_ci_v3/signer_ci.log` | 6.0 KB | `d5841d4aca54cbfd22d90fef45d3af2f` | 2026-10-22 02:31 |
| `signer_ci_v3/signer_pairs.csv` | 2.6 KB | `462c363512b7a15a066732a2150ecf0e` | 2026-10-22 02:31 |
| `slowfast_v2_smoke/slowfast-loso-s0-seed0-val1-smoke.json` | 2.4 KB | `1f417e2857819a28cc2f55ebc46f4455` | 2026-10-23 14:23 |
| `spoter/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-24 01:58 |
| `spoter/commit.txt` | 238 B | `af80507922454a0c2ce2e2e36371c861` | 2026-10-23 14:11 |
| `spoter/jobs.txt` | 1.2 KB | `320e9a74720df5a206ea27f9c3fbe334` | 2026-10-23 14:11 |
| `spoter/run.log` | 3.7 KB | `79f4febc0a80616c1c6cb4716c8d5daa` | 2026-10-24 01:58 |
| `spoter/spoter-8020-seed0-shuffled.json` | 11.1 KB | `a569b0b899097311dac184b5a43a9914` | 2026-10-24 01:57 |
| `spoter/spoter-8020-seed0.json` | 11.1 KB | `760a6453145e9696b46d691fb8f3bb18` | 2026-10-23 16:37 |
| `spoter/spoter-8020-seed1.json` | 11.0 KB | `1ad798b58cd90eb68f162a2b2e8711db` | 2026-10-23 19:28 |
| `spoter/spoter-8020-seed2.json` | 10.7 KB | `5afdcb92e19d1b270d8cc792da83e48f` | 2026-10-23 21:50 |
| `spoter/spoter-8020-seed3.json` | 11.0 KB | `81a42ca51c1c9c3fd48f11b835bfbd3c` | 2026-10-23 21:59 |
| `spoter/spoter-8020-seed4.json` | 11.0 KB | `66c53348577e65b6ea2121b99b34d952` | 2026-10-24 00:05 |
| `spoter/spoter-loso-s0-seed0-shuffled.json` | 11.1 KB | `b3a97bda0638a372be0e1230fef2ab98` | 2026-10-24 00:15 |
| `spoter/spoter-loso-s0-seed0.json` | 11.1 KB | `a1e83830c3f2d3d634f4991adeff3e02` | 2026-10-23 16:40 |
| `spoter/spoter-loso-s0-seed1.json` | 11.1 KB | `8f861cdedc270ce5a788c8f7db13f2ab` | 2026-10-23 16:35 |
| `spoter/spoter-loso-s0-seed2.json` | 11.1 KB | `2d6e3c84fd8be4652d194737837d7fb3` | 2026-10-23 19:31 |
| `spoter/spoter-loso-s0-seed3.json` | 11.0 KB | `8901c6cf6334cb47bfa22aa51f2a0da3` | 2026-10-23 21:52 |
| `spoter/spoter-loso-s0-seed4.json` | 11.1 KB | `6fe9ad57b064ccd2f4f3bb9387c63be6` | 2026-10-23 23:55 |
| `spoter/spoter-loso-s1-seed0-shuffled.json` | 11.1 KB | `dda62cd447a9733a4530ce87890ffdf7` | 2026-10-24 00:16 |
| `spoter/spoter-loso-s1-seed0.json` | 11.1 KB | `bb2436533d75858862ebba3ef5e103e2` | 2026-10-23 16:41 |
| `spoter/spoter-loso-s1-seed1.json` | 11.1 KB | `1561b581eaa821c48c54b5b4d06d209c` | 2026-10-23 16:38 |
| `spoter/spoter-loso-s1-seed2.json` | 11.1 KB | `1f0aa5e31af9570910b3b885738855aa` | 2026-10-23 19:33 |
| `spoter/spoter-loso-s1-seed3.json` | 11.1 KB | `ab60274d55b3d526d2e85e23dd046b61` | 2026-10-23 21:49 |
| `spoter/spoter-loso-s1-seed4.json` | 11.1 KB | `fc6a4eb4b8be3b38ac414d75bfc969da` | 2026-10-24 00:07 |
| `spoter/spoter-loso-s2-seed0-shuffled.json` | 11.0 KB | `79c52dffe28981b14aa5cc66869dfe38` | 2026-10-24 01:46 |
| `spoter/spoter-loso-s2-seed0.json` | 11.1 KB | `ff9356d028c49e743003fdc071551d7b` | 2026-10-23 16:40 |
| `spoter/spoter-loso-s2-seed1.json` | 11.1 KB | `3a58c38f3eff0f8808a41820c33c16f4` | 2026-10-23 19:33 |
| `spoter/spoter-loso-s2-seed2.json` | 11.1 KB | `346b1a29c3aad60c4afeac0d6beba1ff` | 2026-10-23 19:39 |
| `spoter/spoter-loso-s2-seed3.json` | 11.1 KB | `376f2615a921f4a9c290afe3ea4a7287` | 2026-10-23 21:56 |
| `spoter/spoter-loso-s2-seed4.json` | 10.9 KB | `c0b366cd91c82da6823dd3ed974ecab5` | 2026-10-24 00:11 |
| `spoter/spoter-loso-s3-seed0-shuffled.json` | 11.1 KB | `e5c7db6008638b61c7e1b299447b5b23` | 2026-10-24 01:57 |
| `spoter/spoter-loso-s3-seed0.json` | 10.8 KB | `7369f72ca08b97766906c6d1486385a8` | 2026-10-23 16:43 |
| `spoter/spoter-loso-s3-seed1.json` | 10.7 KB | `a18c5d3b0b07ab3609a03dddd393710e` | 2026-10-23 19:31 |
| `spoter/spoter-loso-s3-seed2.json` | 10.6 KB | `0e77dab779fd11ec77ad64732e4f60ad` | 2026-10-23 19:38 |
| `spoter/spoter-loso-s3-seed3.json` | 10.6 KB | `6a93ffbe0eb23cd7e42f3326c36045c4` | 2026-10-23 21:56 |
| `spoter/spoter-loso-s3-seed4.json` | 10.7 KB | `2f51eac446ada986488aae457a9e7657` | 2026-10-24 00:11 |
| `spoter/spoter-loso-s4-seed0-shuffled.json` | 11.1 KB | `4661488c21567313dc8263071cc87e4c` | 2026-10-24 01:53 |
| `spoter/spoter-loso-s4-seed0.json` | 11.1 KB | `5e563da6d46523fd69581bb16cfa78ce` | 2026-10-23 16:37 |
| `spoter/spoter-loso-s4-seed1.json` | 11.1 KB | `87cde4577d963524b44a4f2c9ca6d361` | 2026-10-23 19:30 |
| `spoter/spoter-loso-s4-seed2.json` | 11.1 KB | `ae9c8afbdaf7c762d7f75ce71ff7718d` | 2026-10-23 21:48 |
| `spoter/spoter-loso-s4-seed3.json` | 11.1 KB | `0127d08cc63519ec21c3b425ae5bb76a` | 2026-10-23 21:59 |
| `spoter/spoter-loso-s4-seed4.json` | 11.1 KB | `39230e97995a761d849ed38cdc063d6f` | 2026-10-24 00:12 |
| `spoter_smoke/spoter-loso-s0-seed0.json` | 2.2 KB | `6e97ba75e0a29a7055223db411dee1af` | 2026-10-23 14:11 |
| `stgcn/STOPPED` | 95 B | `36330fd3ae0c87651175e79dc5404dfe` | 2026-10-20 15:24 |
| `stgcn/commit.txt` | 154 B | `bf8c4ccbb5e0d0c30e0b77536d2c017f` | 2026-10-20 00:43 |
| `stgcn/run.log` | 4.3 KB | `013fb173d6f502e337a93df2c8735cc6` | 2026-10-20 15:00 |
| `stgcn/bodynorm/stgcn-loso-s0-seed0.json` | 7.9 KB | `2660cd5c6aa98a2203aeadbafc2eeeb2` | 2026-10-20 14:56 |
| `stgcn/bodynorm/stgcn-loso-s1-seed0.json` | 7.9 KB | `df88b77a497c373b9666a12abf44c57a` | 2026-10-20 14:54 |
| `stgcn/bodynorm/stgcn-loso-s2-seed0.json` | 7.9 KB | `6a0073e3c50725601d9461b8c7ff4790` | 2026-10-20 14:35 |
| `stgcn/bodynorm/stgcn-loso-s3-seed0.json` | 7.9 KB | `959e1be5319ac2716417def08cdb8aa6` | 2026-10-20 15:00 |
| `stgcn/image/stgcn-8020-seed0.json` | 7.9 KB | `624e40c67e54ccbfabfe7026b92cd535` | 2026-10-20 04:22 |
| `stgcn/image/stgcn-8020-seed1.json` | 7.9 KB | `db367947332cc15e9389772e7eb9aa8e` | 2026-10-20 07:49 |
| `stgcn/image/stgcn-8020-seed2.json` | 7.9 KB | `31a1ae969396dd21a9133ae1ce4cf50c` | 2026-10-20 07:46 |
| `stgcn/image/stgcn-8020-seed3.json` | 7.9 KB | `bc4dcaa10d362aaaa7aafdfa4736ac99` | 2026-10-20 11:11 |
| `stgcn/image/stgcn-8020-seed4.json` | 7.8 KB | `b91645fc8fdef5902c6423f96506a612` | 2026-10-20 11:19 |
| `stgcn/image/stgcn-loso-s0-seed0.json` | 7.8 KB | `f1f73fda17dc1a95298e9d76d845dfe1` | 2026-10-20 04:19 |
| `stgcn/image/stgcn-loso-s0-seed1.json` | 7.9 KB | `b94fea45c63a8bb6ebc8a9f36d4022aa` | 2026-10-20 04:16 |
| `stgcn/image/stgcn-loso-s0-seed2.json` | 7.9 KB | `cda4cbff6156eeae130a3eaef37002c6` | 2026-10-20 07:42 |
| `stgcn/image/stgcn-loso-s0-seed3.json` | 7.9 KB | `325fc9226885c6bcf13a856dd05c3152` | 2026-10-20 07:50 |
| `stgcn/image/stgcn-loso-s0-seed4.json` | 7.9 KB | `4778dace18221a5d1de79026e97a4b71` | 2026-10-20 11:19 |
| `stgcn/image/stgcn-loso-s1-seed0.json` | 7.9 KB | `3f03efa84d5fcd2eba3bdb6f767c66d6` | 2026-10-20 04:20 |
| `stgcn/image/stgcn-loso-s1-seed1.json` | 7.9 KB | `556a2f518eda7b0f9bb94a337668697f` | 2026-10-20 04:20 |
| `stgcn/image/stgcn-loso-s1-seed2.json` | 7.9 KB | `f670f3a5dc56ca9971a5de3eb740a253` | 2026-10-20 07:49 |
| `stgcn/image/stgcn-loso-s1-seed3.json` | 7.9 KB | `e4e1b7bf6ae58f710fac4e3eca2a16bc` | 2026-10-20 07:53 |
| `stgcn/image/stgcn-loso-s1-seed4.json` | 7.9 KB | `4eff754c54d831c6f980e820efb09cab` | 2026-10-20 11:19 |
| `stgcn/image/stgcn-loso-s2-seed0.json` | 7.9 KB | `f3a1b8a531071fa65037fb38a20cfc45` | 2026-10-20 04:16 |
| `stgcn/image/stgcn-loso-s2-seed1.json` | 7.9 KB | `05fad21525cc179ee24cb7015872afc7` | 2026-10-20 04:16 |
| `stgcn/image/stgcn-loso-s2-seed2.json` | 7.8 KB | `f75a8073bb25ce90394712cfbfea2bac` | 2026-10-20 07:46 |
| `stgcn/image/stgcn-loso-s2-seed3.json` | 7.9 KB | `b5260f6a750c4e9116db32bbf8037dd2` | 2026-10-20 11:09 |
| `stgcn/image/stgcn-loso-s2-seed4.json` | 7.9 KB | `3ce945a5f4744396914f91abecc1a724` | 2026-10-20 11:16 |
| `stgcn/image/stgcn-loso-s3-seed0.json` | 7.9 KB | `e5b9885a4dc5bb6c995ea4d55e4c8656` | 2026-10-20 04:18 |
| `stgcn/image/stgcn-loso-s3-seed1.json` | 7.8 KB | `dc29ec76d94b0b354734dff5e354a298` | 2026-10-20 04:20 |
| `stgcn/image/stgcn-loso-s3-seed2.json` | 7.9 KB | `36a36a4c090da3f99e8005595aac2fe5` | 2026-10-20 07:46 |
| `stgcn/image/stgcn-loso-s3-seed3.json` | 7.9 KB | `d4a2b0fa1d9943e20804d70e321c17ee` | 2026-10-20 11:17 |
| `stgcn/image/stgcn-loso-s3-seed4.json` | 7.9 KB | `f783db3b750f8e47dd2b3eb048beaf84` | 2026-10-20 11:19 |
| `stgcn/image/stgcn-loso-s4-seed0.json` | 7.9 KB | `0d416540b637f7d97a117078da7b4e13` | 2026-10-20 04:18 |
| `stgcn/image/stgcn-loso-s4-seed1.json` | 7.9 KB | `290e612fc83fb5ad9ec94863c2a62c0d` | 2026-10-20 07:47 |
| `stgcn/image/stgcn-loso-s4-seed2.json` | 7.9 KB | `955d038364fb2d927c41fa6d02e46324` | 2026-10-20 07:47 |
| `stgcn/image/stgcn-loso-s4-seed3.json` | 7.9 KB | `617b0ba54c983f38493c75e879ad567a` | 2026-10-20 11:17 |
| `stgcn/image/stgcn-loso-s4-seed4.json` | 7.9 KB | `e1a88c664c5075148d73fe013a47f5a0` | 2026-10-20 11:17 |
| `stgcn/image_control/stgcn-8020-seed0-shuffled.json` | 7.9 KB | `1b8b89eba770933808bcc7c82d49830c` | 2026-10-20 14:57 |
| `stgcn/image_control/stgcn-loso-s0-seed0-shuffled.json` | 7.8 KB | `86517ef7774a40fba4d18c823ba48f49` | 2026-10-20 14:27 |
| `stgcn/image_control/stgcn-loso-s1-seed0-shuffled.json` | 7.9 KB | `b3a936b7235e3db70671f54b52728cba` | 2026-10-20 14:31 |
| `stgcn/image_control/stgcn-loso-s2-seed0-shuffled.json` | 7.9 KB | `d41e1cf41b93f0f47504adf1fb5b295e` | 2026-10-20 14:54 |
| `stgcn/image_control/stgcn-loso-s3-seed0-shuffled.json` | 7.9 KB | `c506e166de2415d59c2559c9e2de9dbd` | 2026-10-20 14:37 |
| `stgcn/image_control/stgcn-loso-s4-seed0-shuffled.json` | 7.9 KB | `141a052b096aff5a127728b766d50e2b` | 2026-10-20 14:59 |
| `stgcn_v2/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-21 00:44 |
| `stgcn_v2/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-20 16:54 |
| `stgcn_v2/final_jobs.txt` | 13.4 KB | `2ada271a7bc9899b1b9b69ab15b940ea` | 2026-10-20 18:01 |
| `stgcn_v2/run.log` | 11.5 KB | `8b7f87c40da4f2dd8a8ef313a96b0e82` | 2026-10-21 00:44 |
| `stgcn_v2/selected_lr_bodynorm.txt` | 5 B | `14673621d9ed27dfa4fd8c2f42a43cd4` | 2026-10-20 18:01 |
| `stgcn_v2/selected_lr_image.txt` | 6 B | `976c55a570010b297cf125d68ac00451` | 2026-10-20 18:01 |
| `stgcn_v2/selection_jobs.txt` | 7.0 KB | `c3289bde99d621a69f735fffe9a69a04` | 2026-10-20 16:54 |
| `stgcn_v2/bodynorm/stgcn-8020-seed0.json` | 17.2 KB | `30d725a2cbe4e9bf0e2c3f20a85a0c74` | 2026-10-20 22:03 |
| `stgcn_v2/bodynorm/stgcn-8020-seed1.json` | 17.2 KB | `489a9451088a34905d2bb9840ab1a6a9` | 2026-10-20 22:30 |
| `stgcn_v2/bodynorm/stgcn-8020-seed2.json` | 17.2 KB | `9213c3a5cb528859971d77b53fa44488` | 2026-10-20 23:08 |
| `stgcn_v2/bodynorm/stgcn-8020-seed3.json` | 17.2 KB | `d5d5f4cdfc441917d56aec8f147e57aa` | 2026-10-20 23:37 |
| `stgcn_v2/bodynorm/stgcn-8020-seed4.json` | 17.2 KB | `a90a486018c9204496b19ee69d59935a` | 2026-10-21 00:13 |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed0.json` | 17.2 KB | `2b222b666d7d8973c11c2160f51e9e27` | 2026-10-20 21:38 |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed1.json` | 17.1 KB | `05bb18736b61372243e1ddf6e84741c1` | 2026-10-20 22:06 |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed2.json` | 17.2 KB | `47e2f11f56192e503605d2980bf4063b` | 2026-10-20 22:42 |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed3.json` | 17.2 KB | `77bb6de2644dbcfd675f46f8c0778e25` | 2026-10-20 23:13 |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed4.json` | 17.1 KB | `5afa36abfb2fced4389fd0930d823db4` | 2026-10-20 23:47 |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed0.json` | 17.2 KB | `748bb78b2e7ac4873d592e00bb474fb1` | 2026-10-20 21:41 |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed1.json` | 17.2 KB | `2c0d810dc4ebabc121d4df26778a359d` | 2026-10-20 22:08 |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed2.json` | 17.2 KB | `ebdc45ea4a3605c0539b70c70a08012f` | 2026-10-20 22:46 |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed3.json` | 17.2 KB | `83f4151627460747ec1c55685a9500c2` | 2026-10-20 23:15 |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed4.json` | 17.2 KB | `ece9f4981ba1dc6fc6e1d0151633b938` | 2026-10-20 23:51 |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed0.json` | 17.2 KB | `09b5669df8dd23f6f37fbfb4d466fb67` | 2026-10-20 21:44 |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed1.json` | 17.2 KB | `50adf2802a7fffe999a87fddfeb63c8f` | 2026-10-20 22:21 |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed2.json` | 17.2 KB | `54ae2fb27bb9761eefd535678e8cc338` | 2026-10-20 22:50 |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed3.json` | 17.2 KB | `f191cdd55af09b303909672ebfe5716b` | 2026-10-20 23:25 |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed4.json` | 17.2 KB | `d42f0ac93056e4dd7ab27639a8fca4eb` | 2026-10-20 23:57 |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed0.json` | 17.2 KB | `91c8436686112358780afc555c463280` | 2026-10-20 21:46 |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed1.json` | 17.2 KB | `eacfa93a57799add6da7df1711d4a7d0` | 2026-10-20 22:25 |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed2.json` | 17.1 KB | `3d6e147f8174df81b9f0d1b5781fdc81` | 2026-10-20 22:53 |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed3.json` | 17.2 KB | `acc7c7d1e8deb141c32b8452fef4b308` | 2026-10-20 23:30 |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed4.json` | 17.1 KB | `220d9127e124ba1191fe6063ab8bd043` | 2026-10-20 23:59 |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed0.json` | 17.2 KB | `6f268f7fcf6eaa357968423f2aa5dac5` | 2026-10-20 21:59 |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed1.json` | 17.2 KB | `56547da2a00c5b4da104b1d178a6fc11` | 2026-10-20 22:28 |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed2.json` | 17.2 KB | `527ef8ec4cff83147996b096ee676f57` | 2026-10-20 23:04 |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed3.json` | 17.2 KB | `debdea09e45c7d8553f1dde5bcfd0999` | 2026-10-20 23:35 |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed4.json` | 17.2 KB | `f3f3cbd00cc62e3adf41523812594d16` | 2026-10-21 00:08 |
| `stgcn_v2/bodynorm_control/stgcn-8020-seed0-shuffled.json` | 17.0 KB | `3d85f7bf6a3dc7eb7c34b722d6ff0418` | 2026-10-21 00:44 |
| `stgcn_v2/bodynorm_control/stgcn-loso-s0-seed0-shuffled.json` | 17.1 KB | `21539226b80bef17038271857010219d` | 2026-10-21 00:19 |
| `stgcn_v2/bodynorm_control/stgcn-loso-s1-seed0-shuffled.json` | 17.0 KB | `91c5884391086afef15d3dac38ffb877` | 2026-10-21 00:22 |
| `stgcn_v2/bodynorm_control/stgcn-loso-s2-seed0-shuffled.json` | 17.1 KB | `e459a6768acdbb40b0c74fe6d2b7fcc7` | 2026-10-21 00:29 |
| `stgcn_v2/bodynorm_control/stgcn-loso-s3-seed0-shuffled.json` | 17.0 KB | `c30678a6752961dbdbc0f0794aca598b` | 2026-10-21 00:35 |
| `stgcn_v2/bodynorm_control/stgcn-loso-s4-seed0-shuffled.json` | 17.0 KB | `1a1f85351aa28a64d225a7f640afa2e8` | 2026-10-21 00:41 |
| `stgcn_v2/image/stgcn-8020-seed0.json` | 17.3 KB | `f79169fa3b82b98b9dcf9f9bb0f51087` | 2026-10-20 18:46 |
| `stgcn_v2/image/stgcn-8020-seed1.json` | 17.3 KB | `40d9ea60114f7350549c52586d2e64e9` | 2026-10-20 19:09 |
| `stgcn_v2/image/stgcn-8020-seed2.json` | 17.3 KB | `f63d706b293109ed003fe4f82bb2da38` | 2026-10-20 19:52 |
| `stgcn_v2/image/stgcn-8020-seed3.json` | 17.3 KB | `a637c59608859e6e7352f5bddc2ecd0a` | 2026-10-20 20:16 |
| `stgcn_v2/image/stgcn-8020-seed4.json` | 17.3 KB | `ddb17ff628430ee26d1d985d3946cacc` | 2026-10-20 20:57 |
| `stgcn_v2/image/stgcn-loso-s0-seed0.json` | 17.3 KB | `509fd0250853b6ffd541d0c73a02c8b5` | 2026-10-20 18:23 |
| `stgcn_v2/image/stgcn-loso-s0-seed1.json` | 17.3 KB | `98a7e5745270e3624a16e121caed736b` | 2026-10-20 18:47 |
| `stgcn_v2/image/stgcn-loso-s0-seed2.json` | 17.3 KB | `402dda5fc142789c7c612eaf7ebe0220` | 2026-10-20 19:28 |
| `stgcn_v2/image/stgcn-loso-s0-seed3.json` | 17.3 KB | `96b22e6d22175fc4122f0edc2e235057` | 2026-10-20 19:53 |
| `stgcn_v2/image/stgcn-loso-s0-seed4.json` | 17.3 KB | `83886b9ccd5a2cee7dfa62fc68c692a7` | 2026-10-20 20:33 |
| `stgcn_v2/image/stgcn-loso-s1-seed0.json` | 17.4 KB | `bd20fe0ab280ad2ec8d320de25273b77` | 2026-10-20 18:24 |
| `stgcn_v2/image/stgcn-loso-s1-seed1.json` | 17.4 KB | `29ddd14a986cc65e4624caf04e0f6473` | 2026-10-20 18:47 |
| `stgcn_v2/image/stgcn-loso-s1-seed2.json` | 17.4 KB | `0cc295e045f7d48877a94df351ef3785` | 2026-10-20 19:30 |
| `stgcn_v2/image/stgcn-loso-s1-seed3.json` | 17.3 KB | `029d6ee0151e962cb472d64ab06581de` | 2026-10-20 19:54 |
| `stgcn_v2/image/stgcn-loso-s1-seed4.json` | 17.3 KB | `a0a7d34fdc7a89649f3993b4d064480a` | 2026-10-20 20:36 |
| `stgcn_v2/image/stgcn-loso-s2-seed0.json` | 17.3 KB | `acd018e1579b61e519af04da4cfd8881` | 2026-10-20 18:24 |
| `stgcn_v2/image/stgcn-loso-s2-seed1.json` | 17.3 KB | `ede31eafb7efad5709927dc209225acd` | 2026-10-20 19:07 |
| `stgcn_v2/image/stgcn-loso-s2-seed2.json` | 17.3 KB | `702e1c19ba1cf049af36f5c51fab369e` | 2026-10-20 19:31 |
| `stgcn_v2/image/stgcn-loso-s2-seed3.json` | 17.4 KB | `29315feb0f566cff5afe8489a3afa967` | 2026-10-20 20:12 |
| `stgcn_v2/image/stgcn-loso-s2-seed4.json` | 17.3 KB | `4c901e7edc8d8be7bd1b083e1c488fdc` | 2026-10-20 20:38 |
| `stgcn_v2/image/stgcn-loso-s3-seed0.json` | 17.3 KB | `2ff9415a858cc89aa7ee53ed6ba3e980` | 2026-10-20 18:24 |
| `stgcn_v2/image/stgcn-loso-s3-seed1.json` | 17.3 KB | `ff3fcd5d6ec3ee2c4dda3cb555e1fec5` | 2026-10-20 19:08 |
| `stgcn_v2/image/stgcn-loso-s3-seed2.json` | 17.3 KB | `5acccd380207e0196e9d27fedf65c65b` | 2026-10-20 19:32 |
| `stgcn_v2/image/stgcn-loso-s3-seed3.json` | 17.3 KB | `8cbad5d88d47ba70e3f71de9a15fc4c2` | 2026-10-20 20:14 |
| `stgcn_v2/image/stgcn-loso-s3-seed4.json` | 17.3 KB | `23e7702bc7b558b6f0578955a0dc5c65` | 2026-10-20 20:39 |
| `stgcn_v2/image/stgcn-loso-s4-seed0.json` | 17.3 KB | `7de708dfa8ac97cb5720dda136364d14` | 2026-10-20 18:45 |
| `stgcn_v2/image/stgcn-loso-s4-seed1.json` | 17.3 KB | `5a832fd64daa74bc9c9134be883a3a8c` | 2026-10-20 19:09 |
| `stgcn_v2/image/stgcn-loso-s4-seed2.json` | 17.3 KB | `7eec47355c28898773d346080881d517` | 2026-10-20 19:50 |
| `stgcn_v2/image/stgcn-loso-s4-seed3.json` | 17.3 KB | `84506627cb003063a60548927012f7d3` | 2026-10-20 20:15 |
| `stgcn_v2/image/stgcn-loso-s4-seed4.json` | 17.3 KB | `552658cea39717a42ca1cf2817971b8b` | 2026-10-20 20:55 |
| `stgcn_v2/image_control/stgcn-8020-seed0-shuffled.json` | 17.2 KB | `f3f64c576dd2c70b5b624a70a9e3aa0c` | 2026-10-20 21:23 |
| `stgcn_v2/image_control/stgcn-loso-s0-seed0-shuffled.json` | 17.3 KB | `df245734c80706d4508e4568fc79cb40` | 2026-10-20 21:00 |
| `stgcn_v2/image_control/stgcn-loso-s1-seed0-shuffled.json` | 17.2 KB | `c2c478bc87f251a251537b089ea8b2b4` | 2026-10-20 21:01 |
| `stgcn_v2/image_control/stgcn-loso-s2-seed0-shuffled.json` | 17.2 KB | `e64bc6b93b753dd8b9d57a55f1671ede` | 2026-10-20 21:16 |
| `stgcn_v2/image_control/stgcn-loso-s3-seed0-shuffled.json` | 17.2 KB | `eaaafbddbc4875c6b718154b716d5ae7` | 2026-10-20 21:19 |
| `stgcn_v2/image_control/stgcn-loso-s4-seed0-shuffled.json` | 17.2 KB | `9a5896e23f2c82fe940f8327c6a5026d` | 2026-10-20 21:22 |
| `stgcn_v2/logs/stgcn-8020-seed0-shuffled.log` | 128 B | `58ecb2b39fedd7ed3e01b4be98587050` | 2026-10-21 00:44 |
| `stgcn_v2/logs/stgcn-8020-seed0.log` | 119 B | `884eeb5bc1f26c748782a94c14f4cb75` | 2026-10-20 22:03 |
| `stgcn_v2/logs/stgcn-8020-seed1.log` | 119 B | `720dacf3a560b6a8a5716e6da3e318df` | 2026-10-20 22:30 |
| `stgcn_v2/logs/stgcn-8020-seed2.log` | 119 B | `5f2f85ffb0292cb437a2e696c789bc91` | 2026-10-20 23:08 |
| `stgcn_v2/logs/stgcn-8020-seed3.log` | 119 B | `76747e934f1b2bc0cddef5222ed02302` | 2026-10-20 23:37 |
| `stgcn_v2/logs/stgcn-8020-seed4.log` | 119 B | `ff4b64e263251f0ac3ed175d34c15b90` | 2026-10-21 00:13 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-shuffled.log` | 131 B | `915f834b689caeaca5bd1d42cadb562f` | 2026-10-21 00:19 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.01.log` | 134 B | `5f296951bafd93aa9750225e09978ea5` | 2026-10-20 17:45 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.025.log` | 135 B | `154451b51ca9023952868a5bf476e15e` | 2026-10-20 17:27 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.05.log` | 134 B | `97f6c0165a54e4d078853d65d94e6695` | 2026-10-20 17:10 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0.log` | 122 B | `c6f415bd09fd3251e2cd5ba7e19456ab` | 2026-10-20 21:38 |
| `stgcn_v2/logs/stgcn-loso-s0-seed1.log` | 122 B | `4b8eddc302c97133c86014ae79f3aca2` | 2026-10-20 22:06 |
| `stgcn_v2/logs/stgcn-loso-s0-seed2.log` | 122 B | `917b2a80efea60ecb6ea2f37b88069b1` | 2026-10-20 22:42 |
| `stgcn_v2/logs/stgcn-loso-s0-seed3.log` | 122 B | `b71c59afa56bef401de3ab59efa90cb8` | 2026-10-20 23:13 |
| `stgcn_v2/logs/stgcn-loso-s0-seed4.log` | 122 B | `9b039fb4db09f5ad805b361cb6690a33` | 2026-10-20 23:47 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-shuffled.log` | 131 B | `e195e25b88d0ba060759c4197367281f` | 2026-10-21 00:22 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.01.log` | 134 B | `8c769b531017f25d16009ef0867037ca` | 2026-10-20 17:45 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.025.log` | 135 B | `34c168a1e05774c229326c469bff11ce` | 2026-10-20 17:28 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.05.log` | 134 B | `c9977bb45d700949368e6974bbd56aec` | 2026-10-20 17:11 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0.log` | 122 B | `3a491f90bbd7a9446d7cc627ce1f4848` | 2026-10-20 21:41 |
| `stgcn_v2/logs/stgcn-loso-s1-seed1.log` | 122 B | `0e8484d8aa13bec09d6bee2e4ea71fef` | 2026-10-20 22:08 |
| `stgcn_v2/logs/stgcn-loso-s1-seed2.log` | 122 B | `5439ea59ee81af19f0f27bfcae2b48d2` | 2026-10-20 22:46 |
| `stgcn_v2/logs/stgcn-loso-s1-seed3.log` | 122 B | `f978b6c04b5de884712d31bca2025b29` | 2026-10-20 23:15 |
| `stgcn_v2/logs/stgcn-loso-s1-seed4.log` | 122 B | `5c67d2bccd620d47b3070aed88df5ff2` | 2026-10-20 23:51 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-shuffled.log` | 131 B | `af39e15f9c2ff4442ffcfe922cb5e052` | 2026-10-21 00:29 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.01.log` | 134 B | `f220580d4421106e19404698cdd4634d` | 2026-10-20 17:59 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.025.log` | 135 B | `70b79cb1a5e0490b04ee02cee62f0730` | 2026-10-20 17:28 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.05.log` | 134 B | `81d2fcd16c2382d7f1c527030671b5ee` | 2026-10-20 17:11 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0.log` | 122 B | `94a71690363473cc7f98f911624df770` | 2026-10-20 21:44 |
| `stgcn_v2/logs/stgcn-loso-s2-seed1.log` | 122 B | `e1ff6aaab826c95f9fe449f9ecb7176d` | 2026-10-20 22:21 |
| `stgcn_v2/logs/stgcn-loso-s2-seed2.log` | 122 B | `f8fdd1865a152e3da18b9bcdcc07433c` | 2026-10-20 22:50 |
| `stgcn_v2/logs/stgcn-loso-s2-seed3.log` | 122 B | `5489f602931ca0b4e43c9b61b8eaa57e` | 2026-10-20 23:25 |
| `stgcn_v2/logs/stgcn-loso-s2-seed4.log` | 122 B | `98e0eecd85b52aaddb3f7ec32fa13b27` | 2026-10-20 23:57 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-shuffled.log` | 131 B | `7329d96d88afc15f1c22f845e9509422` | 2026-10-21 00:35 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.01.log` | 134 B | `ba3815a7d0bdd3bf08b636011b97a18a` | 2026-10-20 18:01 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.025.log` | 135 B | `ab1f9b14c43243649ac934b89a5a10e5` | 2026-10-20 17:42 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.05.log` | 134 B | `5a1599e713a3e752980b89615c7e3b66` | 2026-10-20 17:11 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0.log` | 122 B | `0d677ed34894af830f73cb2adc753598` | 2026-10-20 21:46 |
| `stgcn_v2/logs/stgcn-loso-s3-seed1.log` | 122 B | `8195caabc80c12b0764b6c1d36ae1e2c` | 2026-10-20 22:25 |
| `stgcn_v2/logs/stgcn-loso-s3-seed2.log` | 122 B | `ee3d84ab4e5ca4c37eecbd897784537f` | 2026-10-20 22:53 |
| `stgcn_v2/logs/stgcn-loso-s3-seed3.log` | 122 B | `56547a191a755800d19bca6b57db934d` | 2026-10-20 23:30 |
| `stgcn_v2/logs/stgcn-loso-s3-seed4.log` | 122 B | `b57f83f09f5e762ba3e271b491bc7485` | 2026-10-20 23:59 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-shuffled.log` | 131 B | `968d0be49fe16c5d1919d083b923f853` | 2026-10-21 00:41 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.01.log` | 134 B | `91849c406efabeeb97b1b1bf70782c55` | 2026-10-20 18:01 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.025.log` | 135 B | `544750cc4d0d8e0da7c30cdc9262e946` | 2026-10-20 17:44 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.05.log` | 134 B | `6b1d3d447b8623cb1f6369650250ec5c` | 2026-10-20 17:26 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0.log` | 122 B | `9b599eb18a5a6fb0c1a4fbba2e303962` | 2026-10-20 21:59 |
| `stgcn_v2/logs/stgcn-loso-s4-seed1.log` | 122 B | `04d11ba5562dcf0b25017cc5c31b434c` | 2026-10-20 22:28 |
| `stgcn_v2/logs/stgcn-loso-s4-seed2.log` | 122 B | `76e3b813018c5387a9a1198c772840f5` | 2026-10-20 23:04 |
| `stgcn_v2/logs/stgcn-loso-s4-seed3.log` | 122 B | `c6f60604a4dbb5e65c075bacdd645cae` | 2026-10-20 23:35 |
| `stgcn_v2/logs/stgcn-loso-s4-seed4.log` | 122 B | `cb296672f6835dbe522d2f8a38c6cbd1` | 2026-10-21 00:08 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.01.json` | 15.7 KB | `cfb55d6658b20f76bb4b27c08971aeb3` | 2026-10-20 17:45 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.025.json` | 17.3 KB | `411d43ff6047be9bab0f48f5b4480c6a` | 2026-10-20 17:27 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.05.json` | 17.2 KB | `234d655a0b3b1f61521a9e00977e450c` | 2026-10-20 17:10 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.01.json` | 15.7 KB | `4af775dd93fa1d13268846a5128ad5a2` | 2026-10-20 17:45 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.025.json` | 17.4 KB | `8adb5676ddd1025117e08de9a093ffe7` | 2026-10-20 17:28 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.05.json` | 17.1 KB | `84f2fad96d5b41c2af74987c17c01de0` | 2026-10-20 17:11 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.01.json` | 15.7 KB | `19e63765215c254bc83912d38cfe1590` | 2026-10-20 17:59 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.025.json` | 17.3 KB | `1c8b740f5785eb7b31280cd222ffea2b` | 2026-10-20 17:28 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.05.json` | 17.1 KB | `3ce388271806a5fe2f2f717e3e1b2df4` | 2026-10-20 17:11 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.01.json` | 15.7 KB | `2b0631f8e46071fc4a638033b36e4e5b` | 2026-10-20 18:01 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.025.json` | 17.3 KB | `9ee9f0a9f78feff79c9e4380115d42bf` | 2026-10-20 17:42 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.05.json` | 17.2 KB | `cb54d3efdd5c02347d23f46c0f680e3a` | 2026-10-20 17:11 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.01.json` | 15.6 KB | `02415079aa368a110cdaff3e13e9d2cc` | 2026-10-20 18:01 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.025.json` | 17.3 KB | `90e9d7c9f0e22ae694477faab413b071` | 2026-10-20 17:44 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.05.json` | 17.1 KB | `0e140211cbed0abbb7e4a3289449334e` | 2026-10-20 17:26 |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.01.json` | 15.7 KB | `ab23e3b681ec2211c6cbd40bac6c01f0` | 2026-10-20 16:17 |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.025.json` | 17.3 KB | `3ce82ad773f5af0a4d0d35a97ab0b5ac` | 2026-10-20 16:00 |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.05.json` | 17.2 KB | `ed44e36afafa1d85a07b9530bf22d5f5` | 2026-10-20 15:43 |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.01.json` | 15.7 KB | `7930846d138f23c05848d124274e7c96` | 2026-10-20 16:18 |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.025.json` | 17.3 KB | `4b0f0da596314172301cda530070f2c5` | 2026-10-20 16:00 |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.05.json` | 17.1 KB | `1bf54add56884425c973f10a15d375c0` | 2026-10-20 15:44 |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.01.json` | 15.6 KB | `a7945c5774efc3f29cbf7c0cd1fe68ba` | 2026-10-20 16:32 |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.025.json` | 17.3 KB | `1bf022c90e8775ac8e07b64518462a2b` | 2026-10-20 16:01 |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.05.json` | 17.1 KB | `e0433257d28be69d8bad3cb7196985d6` | 2026-10-20 15:44 |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.01.json` | 15.7 KB | `b1aa81f7aa26ccfe6517901dcfc3e49f` | 2026-10-20 16:34 |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.025.json` | 17.3 KB | `710e95397a440bbf595d7ed8e24411f6` | 2026-10-20 16:16 |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.05.json` | 17.1 KB | `879a25fc48bd7c549c12ac3d30dad426` | 2026-10-20 15:44 |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.01.json` | 15.6 KB | `7e4142808448ed2533f8f7b394114eaf` | 2026-10-20 16:34 |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.025.json` | 17.3 KB | `84430b97b49df4eb20b2cbd6c78caad9` | 2026-10-20 16:17 |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.05.json` | 17.1 KB | `e353d9bcc89fb56821e1607afa68383f` | 2026-10-20 15:59 |
| `summaries/pose_transformer_runs.commit.txt` | 100 B | `2b395677b84c03713d21edba7edbfe9a` | 2026-10-20 16:18 |
| `summaries/pose_transformer_runs.csv` | 12.2 KB | `adafc7f2ed8362081072fa5c98f605d2` | 2026-10-20 16:18 |
| `summaries/pose_transformer_runs_summary.csv` | 1.7 KB | `aecdf3f553372169f4b806d0b6e0c623` | 2026-10-20 16:18 |
| `summaries/slowfast_runs.commit.txt` | 238 B | `af80507922454a0c2ce2e2e36371c861` | 2026-10-23 14:12 |
| `summaries/slowfast_runs.csv` | 3.1 KB | `3ca42ca612b1e63ad831751764672355` | 2026-10-23 14:12 |
| `summaries/slowfast_runs_summary.csv` | 790 B | `3c9267c4ea261fc22a6d2887973fdf4a` | 2026-10-23 14:12 |
| `summaries/stgcn_ntu_epochs_runs.commit.txt` | 100 B | `2b395677b84c03713d21edba7edbfe9a` | 2026-10-20 16:18 |
| `summaries/stgcn_ntu_epochs_runs.csv` | 7.5 KB | `d311d5d04ccb488eacf67aa35d075e4e` | 2026-10-20 16:18 |
| `summaries/stgcn_ntu_epochs_runs_summary.csv` | 1.3 KB | `aaf88410fbf4ec0ae2c7eda0d1a4a98b` | 2026-10-20 16:18 |
| `summaries/stgcn_v2_runs.commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-21 15:09 |
| `summaries/stgcn_v2_runs.csv` | 13.2 KB | `f2248b6a3cf0d518fa11c0b26a235c37` | 2026-10-21 15:09 |
| `summaries/stgcn_v2_runs_summary.csv` | 1.9 KB | `bf2dfeae0e3370559c14ceb5ac49b271` | 2026-10-21 15:09 |
| `vivit_frozen/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-17 23:31 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_seed0.pkl` | 19.7 KB | `e97c0f1c91c160b984e41e13ca80b232` | 2026-10-17 22:58 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_seed1.pkl` | 19.7 KB | `450e05336a53e7c2e1bcd617ba9963df` | 2026-10-17 23:06 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_seed2.pkl` | 19.7 KB | `a856fed2bb36b847254a625773f9546e` | 2026-10-17 23:14 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_seed3.pkl` | 19.7 KB | `d6f314a829740471ca9d5f0597ac1898` | 2026-10-17 23:23 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_seed4.pkl` | 19.7 KB | `0824e0a8831bbea768792e392d847b17` | 2026-10-17 23:31 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_balanced_shuffled_seed0.pkl` | 19.7 KB | `bcd93ba8922b106082f742cfd4dd723b` | 2026-10-20 18:50 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_0_groupcv_seed0.pkl` | 19.7 KB | `5ea03fb3154fca44805e6bdc8b544a17` | 2026-10-17 22:17 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_0_groupcv_shuffled_seed0.pkl` | 19.7 KB | `dda94d48ff8daea3b7f1862dea66dec4` | 2026-10-20 17:19 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_1_groupcv_seed0.pkl` | 19.7 KB | `1f164606ebbe7a55be152a9692e6fcf6` | 2026-10-17 22:26 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_1_groupcv_shuffled_seed0.pkl` | 19.7 KB | `1b2d8287e2882437609e8df51971d83f` | 2026-10-20 17:38 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_2_groupcv_seed0.pkl` | 19.7 KB | `38637cb51a541e2e89d6d839c49b6144` | 2026-10-17 22:34 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_2_groupcv_shuffled_seed0.pkl` | 19.7 KB | `ae1c9e8b48fb897879e9000d6b7f8ce6` | 2026-10-20 17:56 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_3_groupcv_seed0.pkl` | 19.7 KB | `c719e7d76beae50b31bd9d969f89189d` | 2026-10-17 22:42 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_3_groupcv_shuffled_seed0.pkl` | 19.7 KB | `915e160e80377866edf33df6a395d661` | 2026-10-20 18:13 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_4_groupcv_seed0.pkl` | 19.7 KB | `b92e6a45a3ce3c16335c318135676d2d` | 2026-10-17 22:50 |
| `vivit_frozen/cm_rf_vivit_frozen_cls_loso_4_groupcv_shuffled_seed0.pkl` | 19.7 KB | `f351de2738b341700cb77c8078ca08f8` | 2026-10-20 18:32 |
| `vivit_frozen/commit.txt` | 84 B | `a8081282eb904bcbe3594d291324c42c` | 2026-10-17 21:52 |
| `vivit_frozen/extract.log` | 74.2 KB | `e40be28cafe1828871c85cbf1b9684a8` | 2026-10-17 22:00 |
| `vivit_frozen/grid_8020.log` | 2.6 KB | `1a743ead0dafa4c1bc226f80cf035cde` | 2026-10-17 23:31 |
| `vivit_frozen/grid_loso.log` | 3.3 KB | `74503a135c96082c340c224e25984678` | 2026-10-17 22:50 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_groupcv_seed0.pkl` | 551.4 KB | `7145665cadd6521d465f9e0267ff4362` | 2026-10-17 22:50 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_groupcv_shuffled_seed0.pkl` | 551.4 KB | `c8f7e2c94c7845bee8c3d89bd7664435` | 2026-10-20 18:32 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed0.pkl` | 110.8 KB | `bc226d3a17ddcd0fb6e61a7b5a4bbc59` | 2026-10-17 22:58 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed1.pkl` | 110.8 KB | `7bbfec38ad7931f0d8a96757226aeac2` | 2026-10-17 23:06 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed2.pkl` | 110.8 KB | `de1ddeee5a909e4460444cb47908c7aa` | 2026-10-17 23:14 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed3.pkl` | 110.8 KB | `f440a29ee0d943dc602ebffed61b1780` | 2026-10-17 23:23 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed4.pkl` | 110.8 KB | `f96fe7cb5bf1c055231666d81f4710f3` | 2026-10-17 23:31 |
| `vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_shuffled_seed0.pkl` | 110.8 KB | `9dd88006aa8a3af23ffd44037818a7dd` | 2026-10-20 18:50 |
| `vivit_frozen/probe_cls.csv` | 682 B | `30065358339374c9366015d96ee1955d` | 2026-10-17 22:05 |
| `vivit_frozen/probe_cls.log` | 1.6 KB | `89458d8e44d9501abf63d3aaf617be16` | 2026-10-17 22:05 |
| `vivit_frozen/probe_cls_shuffled.csv` | 425 B | `07a9a022736518eec325cd7176e28705` | 2026-10-20 18:58 |
| `vivit_frozen/probe_mean.csv` | 689 B | `7d0e645076eda78d56fefd27d55d61f2` | 2026-10-17 22:09 |
| `vivit_frozen/probe_mean.log` | 1.6 KB | `1f2b3ca506215ae795fb1a663c559d5c` | 2026-10-17 22:09 |
| `vivit_frozen/vivit_frozen_cls.csv` | 8.1 MB | `f650474aa6403fb88eaf65f9ff4655f9` | 2026-10-17 22:00 |
| `vivit_frozen/vivit_frozen_mean.csv` | 8.1 MB | `3e1057ff7f2a85384c862037f14e9d4c` | 2026-10-17 22:00 |

| Bulk group (weights, checkpoints, Arrow shards) | Files | Total size |
|-----------------------------------------------|-------|------------|
| `fusion/weights/*.pt` | 40 | 3.0 GB |
| `fusion_smoke/weights/*.pt` | 2 | 151.9 MB |

### Server ViViT runs (~/lsc-revision/vivit): `vivit`

Generated 2026-10-28 23:31. 193 files listed; 113 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `run_vivit.log` | 18.1 KB | `9605ed13a08c1402b8842f5bededaa0c` | 2026-10-24 01:36 |
| `vivit_summary.csv` | 3.0 KB | `55d2d9446697bccefd6bebc243b5a1a2` | 2026-10-24 01:36 |
| `logs/vivit-8020-seed0.log` | 104.7 KB | `ed495494877c2e6a33b8a6ff1a7d039b` | 2026-10-18 11:27 |
| `logs/vivit-8020-seed1.log` | 104.6 KB | `dab7847ef35c7b0a582f44024765e472` | 2026-10-19 13:02 |
| `logs/vivit-8020-seed2.log` | 104.8 KB | `94baf980b448de3b4fdb5962d732026a` | 2026-10-20 17:20 |
| `logs/vivit-B-s0-seed0-shuffled.log` | 51.5 KB | `c444c22e11aa044f13ad8ba162017ecd` | 2026-10-22 08:03 |
| `logs/vivit-B-s0-seed0.log` | 51.6 KB | `4da3985fc4e7608925cc65b5a8be0f7b` | 2026-10-19 04:38 |
| `logs/vivit-B-s0-seed1.log` | 51.6 KB | `9b99c9967335d5b5f79ff06e4f407edb` | 2026-10-20 00:00 |
| `logs/vivit-B-s0-seed2.log` | 52.3 KB | `74f78931b69da4e7cd3d2ca1c9101c80` | 2026-10-21 08:53 |
| `logs/vivit-B-s1-seed0-shuffled.log` | 52.3 KB | `a885aa5f2f9bfb69abc3fbf65f34b91c` | 2026-10-22 12:45 |
| `logs/vivit-B-s1-seed0.log` | 51.6 KB | `7de91c51b3e7487c74758ae2c9190041` | 2026-10-19 08:23 |
| `logs/vivit-B-s1-seed1.log` | 51.6 KB | `10d155c783f5ed6bdaee60380f560b8a` | 2026-10-20 00:47 |
| `logs/vivit-B-s1-seed2.log` | 52.1 KB | `f49774f610709489960674cc31685894` | 2026-10-21 08:33 |
| `logs/vivit-B-s2-seed0-shuffled.log` | 52.4 KB | `da75615af6fa3f870ffb2c83276d2f9f` | 2026-10-22 12:46 |
| `logs/vivit-B-s2-seed0.log` | 51.6 KB | `9135e84dd13f5faa0c8b3ab1d648d091` | 2026-10-19 12:18 |
| `logs/vivit-B-s2-seed1.log` | 51.6 KB | `f227aa1dafc911def4b3694941cf9f4f` | 2026-10-20 01:38 |
| `logs/vivit-B-s2-seed2.log` | 52.1 KB | `18fc91a9fb5921900a3c38a633af1ca8` | 2026-10-21 14:21 |
| `logs/vivit-B-s3-seed0-shuffled.log` | 51.8 KB | `ff98d78cc512dbb35fa485fd6655e9c7` | 2026-10-22 09:52 |
| `logs/vivit-B-s3-seed0.log` | 51.6 KB | `d42b74d8bf5d066a1e6df9e0f52a153f` | 2026-10-19 13:30 |
| `logs/vivit-B-s3-seed1.log` | 51.6 KB | `b17ec967a7781033bcea01c3cd1d39e3` | 2026-10-20 05:08 |
| `logs/vivit-B-s3-seed2.log` | 52.2 KB | `dc5a06dc7adead3fd984ab6efc06b32e` | 2026-10-21 16:25 |
| `logs/vivit-B-s4-seed0-shuffled.log` | 51.5 KB | `e039280230bc3f72902008dc3714f019` | 2026-10-24 01:36 |
| `logs/vivit-B-s4-seed0-shuffled.oom-2026-10-22.log` | 20.3 KB | `1150335946a089bf66ea4957c5cf09b5` | 2026-10-22 08:13 |
| `logs/vivit-B-s4-seed0.log` | 51.6 KB | `ff782856c92d709ce2bec24a871f4c39` | 2026-10-19 16:50 |
| `logs/vivit-B-s4-seed1.log` | 51.6 KB | `65950e0b450ef153ee56900c5c2ebcc9` | 2026-10-20 11:55 |
| `logs/vivit-B-s4-seed2.log` | 51.5 KB | `7423053fc0b811954ccc76573637a10b` | 2026-10-21 20:11 |
| `logs/vivit-s0-seed0.log` | 436.0 KB | `b881b114e08c63356f3fa8832f200354` | 2026-10-18 06:37 |
| `logs/vivit-s0-seed1.log` | 436.0 KB | `be2caaa128217dfb3142027910ff717f` | 2026-10-18 16:08 |
| `logs/vivit-s0-seed2.log` | 436.0 KB | `3117f0501522c7b9baa4dee09afd826d` | 2026-10-20 10:03 |
| `logs/vivit-s1-seed0.log` | 436.0 KB | `194d868d35e8ef3dd0ad9f62c2e17bab` | 2026-10-18 07:02 |
| `logs/vivit-s1-seed1.log` | 436.0 KB | `f3077a1f5da9b268162da60e12048284` | 2026-10-18 16:25 |
| `logs/vivit-s1-seed2.log` | 436.0 KB | `c59687964309ee130f66c5937ec128a8` | 2026-10-20 11:10 |
| `logs/vivit-s2-seed0.log` | 436.0 KB | `cade4f1b88b75f86510377318e2252fa` | 2026-10-18 06:54 |
| `logs/vivit-s2-seed1.log` | 436.0 KB | `63961779eaa12d5481b686a8081afd43` | 2026-10-18 20:33 |
| `logs/vivit-s2-seed2.log` | 436.0 KB | `3e9ceef6a2e2f1e2a411c42d80a6af51` | 2026-10-20 14:49 |
| `logs/vivit-s3-seed0.log` | 436.0 KB | `d7d75f58fca78c9a607bd4b8977a70d9` | 2026-10-18 06:48 |
| `logs/vivit-s3-seed1.log` | 436.0 KB | `135130423b25c1b1af116b737c9cf87a` | 2026-10-19 00:38 |
| `logs/vivit-s3-seed2.log` | 436.4 KB | `91b60e6b342c3c61ba591d69cf58a443` | 2026-10-20 22:53 |
| `logs/vivit-s4-seed0.log` | 436.0 KB | `62324f3a7cd9be1386a4d6a36aba4248` | 2026-10-18 15:37 |
| `logs/vivit-s4-seed1.log` | 436.0 KB | `e7e4984ade9ee614edf21be99cc57bf8` | 2026-10-19 01:23 |
| `logs/vivit-s4-seed2.log` | 436.4 KB | `da2fefa7aef0fac4d0b81683063b5662` | 2026-10-21 01:09 |
| `vivit-8020-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 11:26 |
| `vivit-8020-seed0/log_history.csv` | 2.5 KB | `58a57193da1d98d5350a4ec21a136a3b` | 2026-10-18 11:26 |
| `vivit-8020-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 11:26 |
| `vivit-8020-seed0/results.json` | 2.7 KB | `97a6976490364c935138c3b565348c57` | 2026-10-18 11:27 |
| `vivit-8020-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 13:01 |
| `vivit-8020-seed1/log_history.csv` | 2.5 KB | `b1ad1bb2d1cd212f0538a1371c5240b3` | 2026-10-19 13:01 |
| `vivit-8020-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 13:01 |
| `vivit-8020-seed1/results.json` | 2.7 KB | `38a96517cfc0ca6a637a2c1ccc817cc6` | 2026-10-19 13:02 |
| `vivit-8020-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 17:18 |
| `vivit-8020-seed2/log_history.csv` | 2.5 KB | `cda8d4523bf3585f902d6527bd400491` | 2026-10-20 17:18 |
| `vivit-8020-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 17:18 |
| `vivit-8020-seed2/results.json` | 2.7 KB | `db712f27342ecd4fac6c0d74448c9751` | 2026-10-20 17:20 |
| `vivit-B-s0-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 04:38 |
| `vivit-B-s0-seed0/log_history.csv` | 2.1 KB | `12ff9aecb90bf733ae0cd4586fdf3b3b` | 2026-10-19 04:38 |
| `vivit-B-s0-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 04:38 |
| `vivit-B-s0-seed0/results.json` | 2.7 KB | `101e982f6523e32494174939e71052dd` | 2026-10-19 04:38 |
| `vivit-B-s0-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 08:02 |
| `vivit-B-s0-seed0-shuffled/log_history.csv` | 2.1 KB | `1bdbcb3acede453327abd69af5e327a6` | 2026-10-22 08:02 |
| `vivit-B-s0-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 08:02 |
| `vivit-B-s0-seed0-shuffled/results.json` | 2.8 KB | `a14a73ca6be259e250f9173af3611aaf` | 2026-10-22 08:03 |
| `vivit-B-s0-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 00:00 |
| `vivit-B-s0-seed1/log_history.csv` | 2.1 KB | `a1f99579cbe207fe71130cfc1a67419a` | 2026-10-20 00:00 |
| `vivit-B-s0-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 00:00 |
| `vivit-B-s0-seed1/results.json` | 2.7 KB | `a4147aed4a11a77427b8f31ae2fd15d4` | 2026-10-20 00:00 |
| `vivit-B-s0-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 08:52 |
| `vivit-B-s0-seed2/log_history.csv` | 2.1 KB | `c31662d1c2d4da440901731c08de844b` | 2026-10-21 08:52 |
| `vivit-B-s0-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 08:52 |
| `vivit-B-s0-seed2/results.json` | 2.8 KB | `3cfe65e43cf95f27d6f4aad338485ace` | 2026-10-21 08:53 |
| `vivit-B-s1-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 08:23 |
| `vivit-B-s1-seed0/log_history.csv` | 2.1 KB | `0c1563c6c31131ad7526a5a2e81f705f` | 2026-10-19 08:23 |
| `vivit-B-s1-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 08:23 |
| `vivit-B-s1-seed0/results.json` | 2.7 KB | `01a93470acb2e42a697fc0d15fd33ec5` | 2026-10-19 08:23 |
| `vivit-B-s1-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 12:44 |
| `vivit-B-s1-seed0-shuffled/log_history.csv` | 2.1 KB | `cf77bfeba615ad17a67371d7709e81e6` | 2026-10-22 12:44 |
| `vivit-B-s1-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 12:44 |
| `vivit-B-s1-seed0-shuffled/results.json` | 2.7 KB | `5b066f4ccd6962ff4cd1cb6d5359b7bb` | 2026-10-22 12:45 |
| `vivit-B-s1-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 00:47 |
| `vivit-B-s1-seed1/log_history.csv` | 2.1 KB | `dff05332689ecf145483fee82d209a6e` | 2026-10-20 00:47 |
| `vivit-B-s1-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 00:47 |
| `vivit-B-s1-seed1/results.json` | 2.7 KB | `e25bd4ef293077f92f3c8c0388064411` | 2026-10-20 00:47 |
| `vivit-B-s1-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 08:32 |
| `vivit-B-s1-seed2/log_history.csv` | 2.1 KB | `4269f5dc1ed45da72608653c53006151` | 2026-10-21 08:32 |
| `vivit-B-s1-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 08:32 |
| `vivit-B-s1-seed2/results.json` | 2.7 KB | `7a579a1c404a24fe5721053410636fe2` | 2026-10-21 08:33 |
| `vivit-B-s2-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 12:17 |
| `vivit-B-s2-seed0/log_history.csv` | 2.1 KB | `cb03fd49df1276665b2758c8d26b04a7` | 2026-10-19 12:17 |
| `vivit-B-s2-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 12:17 |
| `vivit-B-s2-seed0/results.json` | 2.8 KB | `c7ec08f80003e02ad1e4051259de6397` | 2026-10-19 12:18 |
| `vivit-B-s2-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 12:44 |
| `vivit-B-s2-seed0-shuffled/log_history.csv` | 2.1 KB | `f350d02ea20fbcc2077d018bd5e5b3d4` | 2026-10-22 12:44 |
| `vivit-B-s2-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 12:44 |
| `vivit-B-s2-seed0-shuffled/results.json` | 2.8 KB | `6049307dbd6ab288c79794d9cb0bc399` | 2026-10-22 12:46 |
| `vivit-B-s2-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 01:37 |
| `vivit-B-s2-seed1/log_history.csv` | 2.1 KB | `391a533a95de75a3c1000a47c2729acc` | 2026-10-20 01:37 |
| `vivit-B-s2-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 01:37 |
| `vivit-B-s2-seed1/results.json` | 2.7 KB | `b71455817992cee4714f865ffc886155` | 2026-10-20 01:38 |
| `vivit-B-s2-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 14:20 |
| `vivit-B-s2-seed2/log_history.csv` | 2.1 KB | `8e74f8f6f3c0508f1a4fa4fdb8344d31` | 2026-10-21 14:20 |
| `vivit-B-s2-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 14:20 |
| `vivit-B-s2-seed2/results.json` | 2.8 KB | `f5502ce96d320f35447e9788e2da7ca4` | 2026-10-21 14:21 |
| `vivit-B-s3-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 13:29 |
| `vivit-B-s3-seed0/log_history.csv` | 2.1 KB | `b709ff956e09524746d4b9d0f5f3d918` | 2026-10-19 13:29 |
| `vivit-B-s3-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 13:29 |
| `vivit-B-s3-seed0/results.json` | 2.7 KB | `bce0f7d829d7eba3ea21b8f243d491aa` | 2026-10-19 13:30 |
| `vivit-B-s3-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 09:51 |
| `vivit-B-s3-seed0-shuffled/log_history.csv` | 2.1 KB | `ce51e3eafe7123e196e2bc2bd6a9f33b` | 2026-10-22 09:51 |
| `vivit-B-s3-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 09:51 |
| `vivit-B-s3-seed0-shuffled/results.json` | 2.8 KB | `58ec7738bf2a681a14104007516021aa` | 2026-10-22 09:52 |
| `vivit-B-s3-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 05:07 |
| `vivit-B-s3-seed1/log_history.csv` | 2.1 KB | `84a7ca42b8f30b5831ecf98e9a79fc5c` | 2026-10-20 05:07 |
| `vivit-B-s3-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 05:07 |
| `vivit-B-s3-seed1/results.json` | 2.7 KB | `c8dc7e3b8e02b3b4ec527f4d07e7ab86` | 2026-10-20 05:08 |
| `vivit-B-s3-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 16:23 |
| `vivit-B-s3-seed2/log_history.csv` | 2.1 KB | `b2335eecda9d80fff03d8fa850b7a33d` | 2026-10-21 16:23 |
| `vivit-B-s3-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 16:23 |
| `vivit-B-s3-seed2/results.json` | 2.7 KB | `b955329718257522ecd7877968f31e8c` | 2026-10-21 16:25 |
| `vivit-B-s4-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 16:49 |
| `vivit-B-s4-seed0/log_history.csv` | 2.1 KB | `2778beba94debb9519c54e2ea63d291b` | 2026-10-19 16:49 |
| `vivit-B-s4-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 16:49 |
| `vivit-B-s4-seed0/results.json` | 2.7 KB | `1ddc187ec8a6be0d42101fdfe59844ce` | 2026-10-19 16:50 |
| `vivit-B-s4-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-24 01:35 |
| `vivit-B-s4-seed0-shuffled/log_history.csv` | 2.1 KB | `b76a0fa693cc9d9a45d1383fe7b937d0` | 2026-10-24 01:35 |
| `vivit-B-s4-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-24 01:35 |
| `vivit-B-s4-seed0-shuffled/results.json` | 2.8 KB | `5b766eb23d4edd09712c04c8adc060f6` | 2026-10-24 01:36 |
| `vivit-B-s4-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 11:54 |
| `vivit-B-s4-seed1/log_history.csv` | 2.1 KB | `a71dbb5396518431b2c2b8f512f72327` | 2026-10-20 11:54 |
| `vivit-B-s4-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 11:54 |
| `vivit-B-s4-seed1/results.json` | 2.7 KB | `a6124c5e4fc97a1ca397eb0b0a794b89` | 2026-10-20 11:55 |
| `vivit-B-s4-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 20:10 |
| `vivit-B-s4-seed2/log_history.csv` | 2.1 KB | `3f3d55c7d372ec5f9ba1081bc681573a` | 2026-10-21 20:10 |
| `vivit-B-s4-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 20:10 |
| `vivit-B-s4-seed2/results.json` | 2.7 KB | `d5b62b5ca65f094e8b6afde53de04b82` | 2026-10-21 20:11 |
| `vivit-s0-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 06:36 |
| `vivit-s0-seed0/log_history.csv` | 5.4 KB | `78cd3c022a1665bdf151f4f29870c750` | 2026-10-18 06:36 |
| `vivit-s0-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 06:36 |
| `vivit-s0-seed0/results.json` | 2.8 KB | `a0a48781e0a22a6df1e31d59d430c942` | 2026-10-18 06:37 |
| `vivit-s0-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 16:08 |
| `vivit-s0-seed1/log_history.csv` | 5.5 KB | `b1e43b6230ca163d35bb41be63989604` | 2026-10-18 16:08 |
| `vivit-s0-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 16:08 |
| `vivit-s0-seed1/results.json` | 2.8 KB | `7112e07bbf03665b427c9fbfeee7a832` | 2026-10-18 16:08 |
| `vivit-s0-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 10:02 |
| `vivit-s0-seed2/log_history.csv` | 5.4 KB | `d7b24b79e805d22d0cb99fda7c14f846` | 2026-10-20 10:02 |
| `vivit-s0-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 10:02 |
| `vivit-s0-seed2/results.json` | 2.8 KB | `4e2a65e2f9271003cbf79ae29c7b3117` | 2026-10-20 10:03 |
| `vivit-s1-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 07:01 |
| `vivit-s1-seed0/log_history.csv` | 5.4 KB | `a2e5734ddd9e3b2b8fa03158e223da56` | 2026-10-18 07:01 |
| `vivit-s1-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 07:01 |
| `vivit-s1-seed0/results.json` | 2.8 KB | `5e59b6cf85080123e4e4ab7ac1af9910` | 2026-10-18 07:02 |
| `vivit-s1-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 16:24 |
| `vivit-s1-seed1/log_history.csv` | 5.4 KB | `5e61a7b6140f4a1b7c23225804881845` | 2026-10-18 16:24 |
| `vivit-s1-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 16:24 |
| `vivit-s1-seed1/results.json` | 2.8 KB | `5d718aa89a90949e3042b73631531201` | 2026-10-18 16:25 |
| `vivit-s1-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 11:09 |
| `vivit-s1-seed2/log_history.csv` | 5.4 KB | `a088b741f3cd4d9cd6f028fedb978729` | 2026-10-20 11:09 |
| `vivit-s1-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 11:09 |
| `vivit-s1-seed2/results.json` | 2.8 KB | `fbf6444e3137b524cdb6393d8edc46fa` | 2026-10-20 11:10 |
| `vivit-s2-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 06:53 |
| `vivit-s2-seed0/log_history.csv` | 5.4 KB | `c2f7a5c32a3bd514811fbf1691b2f458` | 2026-10-18 06:53 |
| `vivit-s2-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 06:53 |
| `vivit-s2-seed0/results.json` | 2.8 KB | `b850f99899a725866c6d2c580bdb908b` | 2026-10-18 06:54 |
| `vivit-s2-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 20:32 |
| `vivit-s2-seed1/log_history.csv` | 5.4 KB | `260a715309e05bc5bd6eaf1073080014` | 2026-10-18 20:32 |
| `vivit-s2-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 20:32 |
| `vivit-s2-seed1/results.json` | 2.7 KB | `3913a4dba9c34558e69eb53976957d1a` | 2026-10-18 20:33 |
| `vivit-s2-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 14:48 |
| `vivit-s2-seed2/log_history.csv` | 5.4 KB | `38286330982bc1d84148584c1bdab32e` | 2026-10-20 14:49 |
| `vivit-s2-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 14:49 |
| `vivit-s2-seed2/results.json` | 2.8 KB | `f1f16e7604950a295cefd352d3fd60e6` | 2026-10-20 14:49 |
| `vivit-s3-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 06:48 |
| `vivit-s3-seed0/log_history.csv` | 5.4 KB | `b4c7966a1362403f8aea42bfbdc3a1ee` | 2026-10-18 06:48 |
| `vivit-s3-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 06:48 |
| `vivit-s3-seed0/results.json` | 2.8 KB | `695107916ca15ff8143de8f1ca7bff8f` | 2026-10-18 06:48 |
| `vivit-s3-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 00:37 |
| `vivit-s3-seed1/log_history.csv` | 5.4 KB | `a0dc3801ea5c1416b9ea6a3d57d08381` | 2026-10-19 00:37 |
| `vivit-s3-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 00:37 |
| `vivit-s3-seed1/results.json` | 2.8 KB | `28d9914f70525469a5f36e05378a7103` | 2026-10-19 00:38 |
| `vivit-s3-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-20 22:52 |
| `vivit-s3-seed2/log_history.csv` | 5.5 KB | `d6a5548aa8ec4dc72f4164e5cf29cd3f` | 2026-10-20 22:52 |
| `vivit-s3-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-20 22:52 |
| `vivit-s3-seed2/results.json` | 2.8 KB | `3455065ae08c00a302aef0f51d2091c3` | 2026-10-20 22:53 |
| `vivit-s4-seed0/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-18 15:36 |
| `vivit-s4-seed0/log_history.csv` | 5.5 KB | `8749c84aff5c4b2f8f668077f17b8431` | 2026-10-18 15:36 |
| `vivit-s4-seed0/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-18 15:36 |
| `vivit-s4-seed0/results.json` | 2.8 KB | `57ce9fd9aaf81eb23c12778267dba9aa` | 2026-10-18 15:37 |
| `vivit-s4-seed1/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-19 01:23 |
| `vivit-s4-seed1/log_history.csv` | 5.4 KB | `d4db56232a10766310b839da9933b5fc` | 2026-10-19 01:23 |
| `vivit-s4-seed1/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-19 01:23 |
| `vivit-s4-seed1/results.json` | 2.8 KB | `5150fbe0721d2c572dc5a5be21f6cb8a` | 2026-10-19 01:23 |
| `vivit-s4-seed2/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-21 01:08 |
| `vivit-s4-seed2/log_history.csv` | 5.4 KB | `1611bdeabb675ae57270c2f0f862beb1` | 2026-10-21 01:08 |
| `vivit-s4-seed2/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-21 01:08 |
| `vivit-s4-seed2/results.json` | 2.8 KB | `c4b8fcc985fb70bc09fa675aa6e2f530` | 2026-10-21 01:09 |

| Bulk group (weights, checkpoints, Arrow shards) | Files | Total size |
|-----------------------------------------------|-------|------------|
| `clips_all` | 12 | 9.1 GB |
| `vivit-8020-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-8020-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-8020-seed0/checkpoint-276` | 8 | 1015.1 MB |
| `vivit-8020-seed0/checkpoint-299` | 8 | 1015.1 MB |
| `vivit-8020-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-8020-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-8020-seed1/checkpoint-276` | 8 | 1015.1 MB |
| `vivit-8020-seed1/checkpoint-299` | 8 | 1015.1 MB |
| `vivit-8020-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-8020-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-8020-seed2/checkpoint-230` | 8 | 1015.1 MB |
| `vivit-8020-seed2/checkpoint-299` | 8 | 1015.1 MB |
| `vivit-B-s0-seed0-shuffled/*.bin` | 1 | 5.2 KB |
| `vivit-B-s0-seed0-shuffled/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s0-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-B-s0-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s0-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-B-s0-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s0-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-B-s0-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s1-seed0-shuffled/*.bin` | 1 | 5.2 KB |
| `vivit-B-s1-seed0-shuffled/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s1-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-B-s1-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s1-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-B-s1-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s1-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-B-s1-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s2-seed0-shuffled/*.bin` | 1 | 5.2 KB |
| `vivit-B-s2-seed0-shuffled/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s2-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-B-s2-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s2-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-B-s2-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s2-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-B-s2-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s3-seed0-shuffled/*.bin` | 1 | 5.2 KB |
| `vivit-B-s3-seed0-shuffled/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s3-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-B-s3-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s3-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-B-s3-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s3-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-B-s3-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s4-seed0-shuffled/*.bin` | 1 | 5.2 KB |
| `vivit-B-s4-seed0-shuffled/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s4-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-B-s4-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s4-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-B-s4-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-B-s4-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-B-s4-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s0-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-s0-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-s0-seed0/checkpoint-182` | 8 | 1015.1 MB |
| `vivit-s0-seed0/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s0-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-s0-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-s0-seed1/checkpoint-117` | 8 | 1015.1 MB |
| `vivit-s0-seed1/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s0-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-s0-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s0-seed2/checkpoint-143` | 8 | 1015.1 MB |
| `vivit-s0-seed2/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s1-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-s1-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-s1-seed0/checkpoint-221` | 8 | 1015.1 MB |
| `vivit-s1-seed0/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s1-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-s1-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-s1-seed1/checkpoint-156` | 8 | 1015.1 MB |
| `vivit-s1-seed1/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s1-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-s1-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s1-seed2/checkpoint-299` | 8 | 1015.1 MB |
| `vivit-s1-seed2/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s2-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-s2-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-s2-seed0/checkpoint-169` | 8 | 1015.1 MB |
| `vivit-s2-seed0/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s2-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-s2-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-s2-seed1/checkpoint-117` | 8 | 1015.1 MB |
| `vivit-s2-seed1/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s2-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-s2-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s2-seed2/checkpoint-234` | 8 | 1015.1 MB |
| `vivit-s2-seed2/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s3-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-s3-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-s3-seed0/checkpoint-234` | 8 | 1015.1 MB |
| `vivit-s3-seed0/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s3-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-s3-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-s3-seed1/checkpoint-156` | 8 | 1015.1 MB |
| `vivit-s3-seed1/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s3-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-s3-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s3-seed2/checkpoint-169` | 8 | 1015.1 MB |
| `vivit-s3-seed2/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s4-seed0/*.bin` | 1 | 5.2 KB |
| `vivit-s4-seed0/*.safetensors` | 1 | 338.3 MB |
| `vivit-s4-seed0/checkpoint-143` | 8 | 1015.1 MB |
| `vivit-s4-seed0/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s4-seed1/*.bin` | 1 | 5.2 KB |
| `vivit-s4-seed1/*.safetensors` | 1 | 338.3 MB |
| `vivit-s4-seed1/checkpoint-182` | 8 | 1015.1 MB |
| `vivit-s4-seed1/checkpoint-390` | 8 | 1015.1 MB |
| `vivit-s4-seed2/*.bin` | 1 | 5.2 KB |
| `vivit-s4-seed2/*.safetensors` | 1 | 338.3 MB |
| `vivit-s4-seed2/checkpoint-221` | 8 | 1015.1 MB |
| `vivit-s4-seed2/checkpoint-390` | 8 | 1015.1 MB |

### Server SlowFast, first recipe (~/lsc-revision/slowfast): `slowfast`

Generated 2026-10-28 23:31. 41 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `run_slowfast.log` | 3.0 KB | `c0febe8302d9017ec0e3194d2f24455a` | 2026-10-22 23:12 |
| `logs/slowfast-8020-seed0-shuffled.log` | 1.2 KB | `f9d3d0701f8f91996b9e6a72505f780f` | 2026-10-22 23:12 |
| `logs/slowfast-8020-seed0.log` | 1.2 KB | `21447ce5155803f6676a19efb5ad205b` | 2026-10-22 14:57 |
| `logs/slowfast-8020-seed1.log` | 1.1 KB | `d69281700bc6e0743001c56a956ee0b8` | 2026-10-22 18:48 |
| `logs/slowfast-8020-seed2.log` | 1.2 KB | `adaacd5285c368c4e0c9f5e951792707` | 2026-10-22 21:08 |
| `logs/slowfast-loso-s0-seed0-shuffled.log` | 1.2 KB | `15b2040db3981bbbf09c0c587c856ad2` | 2026-10-22 22:26 |
| `logs/slowfast-loso-s0-seed0.log` | 1.2 KB | `bb1c07af1a98359bdfe8c011894d8527` | 2026-10-22 09:56 |
| `logs/slowfast-loso-s0-seed1.log` | 1.2 KB | `085884e33175e35eccebc4ee924e41a8` | 2026-10-22 15:48 |
| `logs/slowfast-loso-s0-seed2.log` | 1.1 KB | `00732aff4e313ca44ffe1b4ebd322f76` | 2026-10-22 18:41 |
| `logs/slowfast-loso-s1-seed0.log` | 1.2 KB | `b3f53d85e9115e00dacf1047bd0a2896` | 2026-10-22 11:59 |
| `logs/slowfast-loso-s1-seed1.log` | 1.2 KB | `05fbec01f3b2af355a288711ed527fec` | 2026-10-22 15:32 |
| `logs/slowfast-loso-s1-seed2.log` | 1.2 KB | `1650f7b9cf3cfedf1ed8d5e7ceeac432` | 2026-10-22 19:16 |
| `logs/slowfast-loso-s2-seed0.log` | 1.2 KB | `ff911db8b2afe6f3e263b774325a00d3` | 2026-10-22 11:48 |
| `logs/slowfast-loso-s2-seed1.log` | 1.2 KB | `dfcf6f929f048ed8e16ce167f66774ba` | 2026-10-22 16:21 |
| `logs/slowfast-loso-s2-seed2.log` | 1.1 KB | `340f82ad046a8079bc1f42667bed8495` | 2026-10-22 20:13 |
| `logs/slowfast-loso-s3-seed0.log` | 1.1 KB | `b130ab15e2e99b06eabc37490fcd2ecc` | 2026-10-22 13:40 |
| `logs/slowfast-loso-s3-seed1.log` | 1.2 KB | `d85db8e9cc64bdcf24b72649836d3699` | 2026-10-22 17:29 |
| `logs/slowfast-loso-s3-seed2.log` | 1.2 KB | `497d1bd2f2b5a409504a7a83dd3862fa` | 2026-10-22 20:58 |
| `logs/slowfast-loso-s4-seed0.log` | 1.1 KB | `88c09e3e2901ad83b7413abc3ba499ac` | 2026-10-22 14:09 |
| `logs/slowfast-loso-s4-seed1.log` | 1.2 KB | `6e51aee9653c15d9a7c51cc887c761c0` | 2026-10-22 17:24 |
| `logs/slowfast-loso-s4-seed2.log` | 1.2 KB | `d0d372584e0686ba3a639a5b7b921aba` | 2026-10-22 21:36 |
| `results/slowfast-8020-seed0-shuffled.json` | 4.3 KB | `46f39ff1445e36bc17554bc2b9177ea7` | 2026-10-22 23:12 |
| `results/slowfast-8020-seed0.json` | 4.3 KB | `d27a523e8441362fef1627888c0c2b48` | 2026-10-22 14:57 |
| `results/slowfast-8020-seed1.json` | 3.7 KB | `e052803584045da8ca3809c9116e017b` | 2026-10-22 18:48 |
| `results/slowfast-8020-seed2.json` | 4.3 KB | `c28d5ed75b4b29ef21cf3f927b326318` | 2026-10-22 21:08 |
| `results/slowfast-loso-s0-seed0-shuffled.json` | 4.3 KB | `f97da629cff3f2196427a4692cf436e6` | 2026-10-22 22:26 |
| `results/slowfast-loso-s0-seed0.json` | 4.3 KB | `6bbbb6d8a4fe46bf194ebad8efc784bc` | 2026-10-22 09:56 |
| `results/slowfast-loso-s0-seed1.json` | 4.3 KB | `de79ba332141c2c37ab1a18c085e9e48` | 2026-10-22 15:48 |
| `results/slowfast-loso-s0-seed2.json` | 3.8 KB | `c90587d2dac5af7fdb617cfea9ac189e` | 2026-10-22 18:41 |
| `results/slowfast-loso-s1-seed0.json` | 4.3 KB | `928810182f39c1fb53b17d24afac931d` | 2026-10-22 11:59 |
| `results/slowfast-loso-s1-seed1.json` | 4.3 KB | `02303aebdfc59fa1e225ad84c50c9370` | 2026-10-22 15:32 |
| `results/slowfast-loso-s1-seed2.json` | 4.3 KB | `cf274044eb9f663275825581140774c0` | 2026-10-22 19:16 |
| `results/slowfast-loso-s2-seed0.json` | 4.3 KB | `3b1441cbca2f577ffaac6d31d70851da` | 2026-10-22 11:48 |
| `results/slowfast-loso-s2-seed1.json` | 4.3 KB | `9411c03212a5e907aa897533f202952b` | 2026-10-22 16:21 |
| `results/slowfast-loso-s2-seed2.json` | 3.7 KB | `36fe7102c09efdaa9dde246038f5b0b6` | 2026-10-22 20:13 |
| `results/slowfast-loso-s3-seed0.json` | 3.7 KB | `5f48bbb5e3e202f37f6bfcf59e9345ee` | 2026-10-22 13:40 |
| `results/slowfast-loso-s3-seed1.json` | 4.3 KB | `4458e47076c584bb0b99c726d02b11ae` | 2026-10-22 17:29 |
| `results/slowfast-loso-s3-seed2.json` | 4.3 KB | `172baec29617cedead002c6484912c69` | 2026-10-22 20:58 |
| `results/slowfast-loso-s4-seed0.json` | 3.7 KB | `4b38fba129af6996b130dc135647d957` | 2026-10-22 14:09 |
| `results/slowfast-loso-s4-seed1.json` | 4.2 KB | `f2ed67126675bfd2335a73b94c41d01b` | 2026-10-22 17:24 |
| `results/slowfast-loso-s4-seed2.json` | 4.3 KB | `5c2833f1649ac82b903237c9ba2ebca3` | 2026-10-22 21:36 |

### Server SlowFast, revised recipe (~/lsc-revision/slowfast_v2): `slowfast_v2`

Generated 2026-10-28 23:31. 75 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `commit.txt` | 361 B | `a1a0026d35257b9a8aaa2cf4094700c9` | 2026-10-23 14:23 |
| `final_jobs.txt` | 2.3 KB | `d30c7fa5192839b42fcd46c81ffd67af` | 2026-10-24 01:36 |
| `run.log` | 4.7 KB | `99a77c8c11ca687101009e1d83fd8efa` | 2026-10-24 11:09 |
| `selected_lr.txt` | 6 B | `5f9b5d6e0cded1fa997ce119dfea1b70` | 2026-10-24 01:36 |
| `selection_jobs.txt` | 2.3 KB | `9843ebf72781098314c31633f677fe08` | 2026-10-23 14:23 |
| `logs/slowfast-8020-seed0-shuffled.log` | 1.2 KB | `8e9d2b6d4f6db28ccad85b3c4f975fa0` | 2026-10-24 11:09 |
| `logs/slowfast-8020-seed0.log` | 1.2 KB | `e74e1acc5c719e7aff387147e217b2e0` | 2026-10-24 05:25 |
| `logs/slowfast-8020-seed1.log` | 1.2 KB | `93426371c0facb4bab92679757ec9b05` | 2026-10-24 07:20 |
| `logs/slowfast-8020-seed2.log` | 1.2 KB | `844344dcdaea93a86ee226194eb159a4` | 2026-10-24 11:06 |
| `logs/slowfast-loso-s0-seed0-shuffled.log` | 1.2 KB | `2daca1307cc6c473387d3ab4d6a51b3f` | 2026-10-24 11:08 |
| `logs/slowfast-loso-s0-seed0-val1-lr0.001.log` | 1.2 KB | `7e383e3cc0fe916764e9a732ec96c417` | 2026-10-23 19:05 |
| `logs/slowfast-loso-s0-seed0-val1-lr0.003.log` | 1.2 KB | `400eefef82ab9f016906d723c1117bf4` | 2026-10-23 17:18 |
| `logs/slowfast-loso-s0-seed0-val1-lr0.01.log` | 399 B | `397c58f04e57ef0090598125be80d8b1` | 2026-10-23 14:44 |
| `logs/slowfast-loso-s0-seed0.log` | 1.2 KB | `e19458d8d19cdddbf158210c950357ad` | 2026-10-24 03:28 |
| `logs/slowfast-loso-s0-seed1.log` | 1.2 KB | `807eca10a5d3fe9053e0808c6473f5af` | 2026-10-24 05:25 |
| `logs/slowfast-loso-s0-seed2.log` | 1.2 KB | `27005f35016565115fbe06a475126853` | 2026-10-24 09:06 |
| `logs/slowfast-loso-s1-seed0-val2-lr0.001.log` | 1.2 KB | `c8dddf6eef21b7c4cf7b857dc6f10dcf` | 2026-10-23 20:10 |
| `logs/slowfast-loso-s1-seed0-val2-lr0.003.log` | 1.2 KB | `0700f1257044a67355b6e94ee9bd204d` | 2026-10-23 17:31 |
| `logs/slowfast-loso-s1-seed0-val2-lr0.01.log` | 285 B | `bfe7963de837310e67447d2cbf004fe5` | 2026-10-23 14:36 |
| `logs/slowfast-loso-s1-seed0.log` | 1.2 KB | `0f6cf788f5cf26223da764149768a50a` | 2026-10-24 03:31 |
| `logs/slowfast-loso-s1-seed1.log` | 1.2 KB | `a595589e1e7f39e0feb8720163124516` | 2026-10-24 05:26 |
| `logs/slowfast-loso-s1-seed2.log` | 1.2 KB | `3924772cce8ee07385c54aba9b788e87` | 2026-10-24 09:12 |
| `logs/slowfast-loso-s2-seed0-val3-lr0.001.log` | 1.2 KB | `0f3f477276c088a7554e8b3107c03103` | 2026-10-23 20:23 |
| `logs/slowfast-loso-s2-seed0-val3-lr0.003.log` | 1.2 KB | `9f1a669c6eb799bfc2b3e55d3f8b4aa0` | 2026-10-23 17:39 |
| `logs/slowfast-loso-s2-seed0-val3-lr0.01.log` | 1.2 KB | `7f204ba8e702c19a41dfaa2fc391902b` | 2026-10-23 15:50 |
| `logs/slowfast-loso-s2-seed0.log` | 1.2 KB | `5c1d3af9cfa9f84c260a812304bd8b6c` | 2026-10-24 03:31 |
| `logs/slowfast-loso-s2-seed1.log` | 1.2 KB | `6a6143c251d3052e1e3fb8954592d35b` | 2026-10-24 07:14 |
| `logs/slowfast-loso-s2-seed2.log` | 1.2 KB | `7378c3e6e103a1c6d531054202bc7c8e` | 2026-10-24 09:14 |
| `logs/slowfast-loso-s3-seed0-val4-lr0.001.log` | 1.2 KB | `b8fc4a515c29dcfbe827315aae7415cb` | 2026-10-23 20:31 |
| `logs/slowfast-loso-s3-seed0-val4-lr0.003.log` | 1.2 KB | `1ff39d8cfabc67d251544432cf2249ef` | 2026-10-23 18:44 |
| `logs/slowfast-loso-s3-seed0-val4-lr0.01.log` | 1.2 KB | `de1b44cc223e1850d8667bbe24f845c5` | 2026-10-23 16:02 |
| `logs/slowfast-loso-s3-seed0.log` | 1.2 KB | `79c16d252cb9b601107b3a204c00152d` | 2026-10-24 03:31 |
| `logs/slowfast-loso-s3-seed1.log` | 1.2 KB | `6483f0db70cbddbc93a00c5ed1427694` | 2026-10-24 07:18 |
| `logs/slowfast-loso-s3-seed2.log` | 1.2 KB | `4c457bd9f25ca2b48d0045dd84b8c337` | 2026-10-24 09:14 |
| `logs/slowfast-loso-s4-seed0-val0-lr0.001.log` | 1.2 KB | `83b5b5dbf1f4cd87e75a70010b53a85c` | 2026-10-23 21:35 |
| `logs/slowfast-loso-s4-seed0-val0-lr0.003.log` | 1.2 KB | `3e6ff4cae265004e00cdc86fb49e7e54` | 2026-10-23 18:57 |
| `logs/slowfast-loso-s4-seed0-val0-lr0.01.log` | 1.2 KB | `60a251a3e16e9555ce1a9d35d75b8e80` | 2026-10-23 16:10 |
| `logs/slowfast-loso-s4-seed0.log` | 1.2 KB | `593df7d3c8821f3595edd8699c702e0d` | 2026-10-24 05:21 |
| `logs/slowfast-loso-s4-seed1.log` | 1.2 KB | `8867845ebbfd0dfa0d56ed4fbe3e18c9` | 2026-10-24 07:19 |
| `logs/slowfast-loso-s4-seed2.log` | 1.2 KB | `90fcd0e56ca214bdf13e6bf516ec8a47` | 2026-10-24 10:59 |
| `results/slowfast-8020-seed0-shuffled.json` | 4.5 KB | `4e7f2cc1d514d78ec9184f46bb0a3d4c` | 2026-10-24 11:09 |
| `results/slowfast-8020-seed0.json` | 4.5 KB | `d6a4efd97e563a715f6b6fc858cb0c35` | 2026-10-24 05:25 |
| `results/slowfast-8020-seed1.json` | 4.5 KB | `8a22a2544989bff9b75c676fe015e49a` | 2026-10-24 07:20 |
| `results/slowfast-8020-seed2.json` | 4.5 KB | `284f83f971b524c164a48e4766739930` | 2026-10-24 11:06 |
| `results/slowfast-loso-s0-seed0-shuffled.json` | 4.5 KB | `7982983ee2f6a5af9749b29dffe53287` | 2026-10-24 11:08 |
| `results/slowfast-loso-s0-seed0.json` | 4.5 KB | `dbb2ed299956216328fe42c8a75827f0` | 2026-10-24 03:28 |
| `results/slowfast-loso-s0-seed1.json` | 4.5 KB | `70c1bb17c8efd97c0697e163b56711ff` | 2026-10-24 05:25 |
| `results/slowfast-loso-s0-seed2.json` | 4.5 KB | `58be9607a9633da87750dd1ab6a26c23` | 2026-10-24 09:06 |
| `results/slowfast-loso-s1-seed0.json` | 4.5 KB | `240531a95c182b7dcd9d6657cc8e6f6e` | 2026-10-24 03:31 |
| `results/slowfast-loso-s1-seed1.json` | 4.5 KB | `fd518f74c05e5a5317d27f13701689df` | 2026-10-24 05:26 |
| `results/slowfast-loso-s1-seed2.json` | 4.5 KB | `473e1c769fe54b242bd88036691d9cb9` | 2026-10-24 09:12 |
| `results/slowfast-loso-s2-seed0.json` | 4.5 KB | `6fd1755472858740a546a647cb9fc5bd` | 2026-10-24 03:31 |
| `results/slowfast-loso-s2-seed1.json` | 4.5 KB | `e15ecd5f66f03a0a99a8f0de36e71b7e` | 2026-10-24 07:14 |
| `results/slowfast-loso-s2-seed2.json` | 4.5 KB | `ecae5be1a73d3a3bb5229c3c2747b212` | 2026-10-24 09:14 |
| `results/slowfast-loso-s3-seed0.json` | 4.5 KB | `5c53ce6f417f98f1dad72b46644be907` | 2026-10-24 03:31 |
| `results/slowfast-loso-s3-seed1.json` | 4.5 KB | `82c65ec03201c1171a21b26088c3358c` | 2026-10-24 07:18 |
| `results/slowfast-loso-s3-seed2.json` | 4.5 KB | `780987eec955fcabea96033feb8fef3c` | 2026-10-24 09:14 |
| `results/slowfast-loso-s4-seed0.json` | 4.5 KB | `d92e17f613882be506575a2a236091dc` | 2026-10-24 05:21 |
| `results/slowfast-loso-s4-seed1.json` | 4.5 KB | `62108f34ed11ff9f02055bf777f87008` | 2026-10-24 07:19 |
| `results/slowfast-loso-s4-seed2.json` | 4.5 KB | `6c0c06e2d44a4770dac7d1608391d45b` | 2026-10-24 10:59 |
| `selection/slowfast-loso-s0-seed0-val1-lr0.001.json` | 4.5 KB | `4811b8375904a7a0d701321871f71f14` | 2026-10-23 19:05 |
| `selection/slowfast-loso-s0-seed0-val1-lr0.003.json` | 4.5 KB | `8a60ebbd9ec164e5e085292155b9619f` | 2026-10-23 17:18 |
| `selection/slowfast-loso-s0-seed0-val1-lr0.01.json` | 2.6 KB | `ddd90891edda71fd05d324a581a30795` | 2026-10-23 14:44 |
| `selection/slowfast-loso-s1-seed0-val2-lr0.001.json` | 4.5 KB | `ac0afeeb15305aaee4e82b2bbaa539f0` | 2026-10-23 20:10 |
| `selection/slowfast-loso-s1-seed0-val2-lr0.003.json` | 4.5 KB | `d18ab0e24feb1789f1ac05c130dc3271` | 2026-10-23 17:31 |
| `selection/slowfast-loso-s1-seed0-val2-lr0.01.json` | 2.4 KB | `2788ff9d7e00e8876ee8095097ebc811` | 2026-10-23 14:36 |
| `selection/slowfast-loso-s2-seed0-val3-lr0.001.json` | 4.5 KB | `ea5bb69e1d086d59439815c7e655e757` | 2026-10-23 20:23 |
| `selection/slowfast-loso-s2-seed0-val3-lr0.003.json` | 4.5 KB | `0ac815d0a31ee2bc7eab1aba1df606af` | 2026-10-23 17:39 |
| `selection/slowfast-loso-s2-seed0-val3-lr0.01.json` | 4.4 KB | `32a96a0ca75329db18264ce42a02de36` | 2026-10-23 15:50 |
| `selection/slowfast-loso-s3-seed0-val4-lr0.001.json` | 4.5 KB | `4c02cf37c3b653309186397a412251f3` | 2026-10-23 20:31 |
| `selection/slowfast-loso-s3-seed0-val4-lr0.003.json` | 4.5 KB | `bf6e3ce6afee6945330b0a7af43c72cb` | 2026-10-23 18:44 |
| `selection/slowfast-loso-s3-seed0-val4-lr0.01.json` | 4.5 KB | `72fca80184314eca3e7f46de93e87928` | 2026-10-23 16:02 |
| `selection/slowfast-loso-s4-seed0-val0-lr0.001.json` | 4.5 KB | `717e7d78cff3bc5cc9cad12551c4e2b6` | 2026-10-23 21:35 |
| `selection/slowfast-loso-s4-seed0-val0-lr0.003.json` | 4.5 KB | `e041399d5ea9e3ccda44eb758ac3a9e2` | 2026-10-23 18:57 |
| `selection/slowfast-loso-s4-seed0-val0-lr0.01.json` | 4.4 KB | `be030a7fca64f6c8158eebd95e2256de` | 2026-10-23 16:10 |

SlowFast clips (`slowfast/clips/`, not hashed): `frames.npy` 5.9 GB (uint8 1000 × 32 × 256 × 256 × 3); `meta.csv` MD5 `ab648abc3d7275ba7ba4a1b02fabd373` (unchanged since 2026-10-20).


## 4. Copies kept in the repository (`docs/results/`)

Small result files are copied into the repository so the register is self-contained: all summary CSVs, the DTW pair tables, signer matrices, per-sign tables and the normalization check (`dtw/`, `dtw/pathnorm/`), the permutation-importance tables, the linear-probe tables, the audit re-run logs (`audit/`), the pose-transformer runs and controls (`pose/`, `pose_control/`), and every finished ViViT job's `results.json` (test predictions and metrics) and `log_history.csv` (per-epoch learning curves) plus the launcher log (`vivit/`). Draft figures (PNG) are in `docs/figures/`; the TIFF versions stay on the server (`WORK/figures/`). ST-GCN runs (`stgcn/`) and the SlowFast clip metadata and launcher log (`slowfast/`) are copied as they complete.

MD5 rows for every repository copy (audit N12; regenerated 2026-10-28 on the Mac):

### Repository copies: `docs/results/`

Generated 2026-10-28 18:52. 1784 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `importance_imu.csv` | 11.6 KB | `a21c55d143049e08e507c266566b8357` | 2026-10-18 11:56 |
| `importance_landmarks_bodynorm.csv` | 32.2 KB | `b0f81693d360d38271b1d2a7472dba75` | 2026-10-18 11:56 |
| `importance_stability_imu.csv` | 380 B | `f50b260e8d0b3be6b8d67ba6776e1dcd` | 2026-10-20 11:16 |
| `importance_stability_landmarks_bodynorm.csv` | 482 B | `7f7d24e6e092cfc9a2e37a97db1a6ab4` | 2026-10-20 11:16 |
| `pose_transformer_runs.csv` | 6.1 KB | `a1b45f110844041a4f8cc71d9a4acd19` | 2026-10-19 10:07 |
| `signant_labeling_permutation_bodynorm_knn.csv` | 944 B | `75538eea27d723c4b8b5a2eb758d4e8c` | 2026-10-20 16:18 |
| `signant_labeling_permutation_bodynorm_rf.csv` | 945 B | `631df8e4db34c211848333dfaef31942` | 2026-10-20 16:18 |
| `signant_labeling_permutation_bodynorm_svm.csv` | 905 B | `553998499cc474864c649f59c327e93b` | 2026-10-20 16:18 |
| `signant_labeling_permutation_temporal.csv` | 676 B | `a3014323b4f2a5a080faedf740409631` | 2026-10-16 17:52 |
| `signant_labeling_permutation_temporal_features.csv` | 854 B | `044a347333f2dfd5e9dbe3af16194687` | 2026-10-16 17:52 |
| `signant_summary.csv` | 3.7 KB | `d37bbfc756835146393cbf7e43dce551` | 2026-10-20 16:18 |
| `signant_summary_runs.csv` | 8.8 KB | `d1c126b0b016dfb47cc764cf3b35bc00` | 2026-10-20 16:18 |
| `signant_v2.commit` | 155 B | `27b68c1335a5d4a0c4b27c83b766f3e0` | 2026-10-20 10:57 |
| `signant_v2.log` | 123.9 KB | `32984b3f170371dbccd58238431ae30d` | 2026-11-18 (server paths anonymized) |
| `signer_ci.csv` | 6.8 KB | `cb97f91cbd41e0c0935ad08df10133d0` | 2026-10-27 14:06 |
| `slr_bodynorm_seeds0-4.csv` | 726 B | `bac2ff2e7b9d5e585983cd6ca7eefdd0` | 2026-10-18 11:23 |
| `slr_frames_seed0.csv` | 4.1 KB | `f5dca848e68e1af4553b1676bb0f23f7` | 2026-10-16 13:11 |
| `slr_imu_seeds0-4.csv` | 1.1 KB | `ffb76da466cb2ca9cf3772fe785df4e1` | 2026-10-16 09:59 |
| `slr_landmarks_seeds0-4.csv` | 1.1 KB | `43cab6f12d48b95e6823d364c43c3fd3` | 2026-10-15 16:02 |
| `slr_loso_groupcv_seed0.csv` | 1.1 KB | `81c293e83447d49b31204045e3e09e81` | 2026-10-16 14:06 |
| `slr_loso_groupcv_seeds0-4.csv` | 1.2 KB | `3bb8f6b1d2d15338926b2c4877f40fd3` | 2026-10-16 17:27 |
| `slr_seed0.csv` | 1.9 KB | `4935c703c5589092ecd21651d0632b3f` | 2026-10-15 14:21 |
| `slr_shuffled_seed0.csv` | 1.9 KB | `969346aa26010253046b888b1e72b57c` | 2026-10-15 15:26 |
| `slr_vivit_frozen_cls.csv` | 633 B | `3a1a6e1eb13eb1554f9f53d9931acdab` | 2026-10-18 11:23 |
| `vivit_frozen_probe_cls.csv` | 682 B | `30065358339374c9366015d96ee1955d` | 2026-10-17 17:10 |
| `vivit_frozen_probe_mean.csv` | 689 B | `7d0e645076eda78d56fefd27d55d61f2` | 2026-10-17 17:10 |
| `vivit_runs.csv` | 2.7 KB | `c29e8537ebb5a63de3049f693fe939f7` | 2026-10-21 21:02 |
| `audit/imu_reproduce.log` | 1.3 KB | `92413229ea498e2509923af507a3e543` | 2026-11-18 (server paths anonymized) |
| `audit/imu_segmentation_check.csv` | 48.6 KB | `44354fdf9c3881629d7f4ddd4af6e226` | 2026-10-19 12:25 |
| `audit/vivit_duplicates.log` | 172 B | `aa6d900a82ee227ad7b474b6c9ab8f91` | 2026-10-18 14:42 |
| `audit/sign_mapping_check/commit.txt` | 131 B | `94355ac041c20c9dc37ba211fa166dde` | 2026-10-28 18:51 |
| `audit/sign_mapping_check/sign_mapping_check.csv` | 1.1 KB | `1df1dcecc12af7e15dfc5e1b80d717c3` | 2026-10-28 18:51 |
| `audit/sign_mapping_check/sign_mapping_check.log` | 1.3 KB | `13f15d68263501216a5b6b80cb30efbe` | 2026-10-28 18:51 |
| `audit/sign_mapping_check/sign_mapping_check_video_seconds.csv` | 3.5 KB | `b76113666a785b6593623ab42d074a2a` | 2026-10-28 18:51 |
| `controls/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-20 14:51 |
| `controls/controls.commit` | 109 B | `7c0c3c974949f1e1c3017b04403f48f1` | 2026-10-20 14:51 |
| `controls/controls.log` | 9.7 KB | `d87f21940548ce029193916c4fa952f7` | 2026-11-18 (server paths anonymized) |
| `controls/controls_shuffled.csv` | 1.2 KB | `d1e6be384e69dffedbd8979269ac86d5` | 2026-10-20 14:51 |
| `controls/probe_cls_shuffled.csv` | 425 B | `07a9a022736518eec325cd7176e28705` | 2026-10-20 14:51 |
| `dtw/dtw_all_pairs.csv` | 486.9 KB | `dc6cab5e6cd718c3db54843141b41544` | 2026-10-18 12:01 |
| `dtw/dtw_all_per_sign_matrix.csv` | 36.9 KB | `21cca9cf99000e1e82100922d3a8f513` | 2026-10-20 10:05 |
| `dtw/dtw_all_per_sign_summary.csv` | 15.5 KB | `ba39e28c2e12826010568cdf90948f24` | 2026-10-20 10:05 |
| `dtw/dtw_all_signer_matrix.csv` | 493 B | `eac3572a7efae2ce7001a53663429e7c` | 2026-10-18 11:56 |
| `dtw/dtw_hands_pairs.csv` | 487.4 KB | `f90fa515482df3471959641469f0cc82` | 2026-10-18 12:01 |
| `dtw/dtw_hands_per_sign_matrix.csv` | 36.9 KB | `5ae4dec099f23b9c515f4fbf5ba5f05d` | 2026-10-20 10:05 |
| `dtw/dtw_hands_per_sign_summary.csv` | 15.5 KB | `64323769340b23f2f8541cb18ce9d527` | 2026-10-20 10:05 |
| `dtw/dtw_hands_signer_matrix.csv` | 499 B | `7d8380a6ca0c10e0c610d010bc4843e7` | 2026-10-18 11:56 |
| `dtw/pathnorm/dtw_all_pathnorm.log` | 1.4 KB | `31cf1c29ac4c7cda29bda487baad9ca1` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_all_pathnorm_pairs.csv` | 909.4 KB | `c31e4f9af2e28bcd90f466a6efbcc526` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_all_pathnorm_per_sign_matrix.csv` | 36.7 KB | `bddc2fb41bccd47e178b2e81f0a3e884` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_all_pathnorm_per_sign_summary.csv` | 15.4 KB | `18853fa64f3fe0c9dabc334e7fddac6d` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_hands_pathnorm.log` | 1.4 KB | `09da44c06c188dc956c6a904d54f76df` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_hands_pathnorm_pairs.csv` | 910.3 KB | `6259498c2d21b158af8f1e863f742b36` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_hands_pathnorm_per_sign_matrix.csv` | 36.8 KB | `f6ff3aacc9364880a5865310f06582c5` | 2026-10-20 10:13 |
| `dtw/pathnorm/dtw_hands_pathnorm_per_sign_summary.csv` | 15.4 KB | `562ab37bb78e9d994febc43f18bd6dd5` | 2026-10-20 10:14 |
| `dtw/signer_level/dtw_all_pathnorm_signer_level_all_signers.csv` | 395 B | `521c30eaa1b98b149305589fb0885955` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_all_pathnorm_signer_level_summary.csv` | 589 B | `dd2e03b86a3f95cacd7912f402891f6a` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_all_pathnorm_signer_level_without_V1.csv` | 318 B | `66052f038e617ac938665f29cb3070bd` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_all_signer_level_all_signers.csv` | 392 B | `129889053d37e6a30e70a5b161bf6c4d` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_all_signer_level_summary.csv` | 586 B | `015720633dff81160424aade401b7040` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_all_signer_level_without_V1.csv` | 316 B | `5330572c06a1ed5fafddfd5f1a938712` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_hands_signer_level_all_signers.csv` | 392 B | `efd58307402d06377384ef35f3881097` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_hands_signer_level_summary.csv` | 587 B | `72d4d3fef1d0cedfdfdc3c2323a51d89` | 2026-10-20 10:58 |
| `dtw/signer_level/dtw_hands_signer_level_without_V1.csv` | 318 B | `5a23a902365c6e796b65fcfb0f8e5e92` | 2026-10-20 10:58 |
| `fusion/DONE_fuse` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 13:28 |
| `fusion/DONE_slowfast` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-27 09:51 |
| `fusion/DONE_spoter` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-26 21:55 |
| `fusion/commit_fuse.txt` | 101 B | `44c36749adc12bd95b8a1f50387a896f` | 2026-10-27 13:28 |
| `fusion/commit_slowfast.txt` | 96 B | `654d2c8ee23a6b94c657faa47c734eeb` | 2026-10-27 06:05 |
| `fusion/commit_spoter.txt` | 540 B | `c53abc0e3f4a4c6281e63953d4f3b582` | 2026-10-26 12:37 |
| `fusion/fuse.log` | 7.5 KB | `dbf87d9308e676e3958c8e7afd5b4459` | 2026-10-27 13:28 |
| `fusion/fusion_runs.commit.txt` | 101 B | `44c36749adc12bd95b8a1f50387a896f` | 2026-10-27 13:28 |
| `fusion/fusion_runs.csv` | 9.2 KB | `1a6a6be8aba62ca2d339d3b2e5830ab8` | 2026-10-27 13:28 |
| `fusion/fusion_runs_summary.csv` | 1.9 KB | `2d30f50880cb5f750f3321bd151741d1` | 2026-10-27 13:28 |
| `fusion/importance_spoter_per_signer.csv` | 897 B | `500efa0f56af3e5be3758b86d2bcb758` | 2026-10-27 13:28 |
| `fusion/importance_spoter_runs.csv` | 4.6 KB | `590ad975e32ce405d129bf4abcf53d69` | 2026-10-27 13:28 |
| `fusion/importance_spoter_stability.csv` | 110 B | `7394ef101bfd2a8cec26db091a2e7e0a` | 2026-10-27 13:28 |
| `fusion/importance_spoter_summary.csv` | 572 B | `5aa589a2ad38b6afc62bc3e0cb002707` | 2026-10-27 13:28 |
| `fusion/retry_then_fuse.sh` | 914 B | `79dc498ddd6ee3fc14f170a006119643` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast.log` | 5.1 KB | `7ae86715cafa66f2576b4251a62de854` | 2026-10-27 09:51 |
| `fusion/slowfast_jobs.txt` | 952 B | `239579966ffc9b9c05a418d72dbedcc3` | 2026-10-27 06:05 |
| `fusion/spoter.log` | 2.6 KB | `d8d9912ef4df442e4b2d3cc8e82e39c9` | 2026-10-26 21:55 |
| `fusion/spoter_jobs.txt` | 2.5 KB | `463278ec5c539fbb4f1f93618de2db38` | 2026-11-18 (server paths anonymized) |
| `fusion/fused/fusion-8020-seed0-shuffled.json` | 4.1 KB | `d7ade5a52f8bbef2543437a3533a32f8` | 2026-10-27 13:28 |
| `fusion/fused/fusion-8020-seed0.json` | 4.2 KB | `1a82a2ad557497c1f7427bb5ac67b9d0` | 2026-10-27 13:28 |
| `fusion/fused/fusion-8020-seed1.json` | 4.2 KB | `c8234c1139afca1331551441fffbb9d6` | 2026-10-27 13:28 |
| `fusion/fused/fusion-8020-seed2.json` | 4.2 KB | `f6ec0182b5eac0d33d7325e95d40159e` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s0-seed0-shuffled.json` | 4.2 KB | `fbe7ccf9c42c73fd02c362f674b30fe9` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s0-seed0.json` | 4.2 KB | `6fbe93b86b4f682b915773a19d19531d` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s0-seed1.json` | 4.2 KB | `66eb14587bd3398d1126eb9eebab80fe` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s0-seed2.json` | 4.2 KB | `307dd0913d1a0a281217b9608633a80c` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s1-seed0.json` | 4.2 KB | `123c2c9780f913eac882e9cf9fc235ae` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s1-seed1.json` | 4.2 KB | `2ab7fe12edf1709f594b5f0e14f47eaf` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s1-seed2.json` | 4.2 KB | `56ea166e99dc846c2f6b84a746365579` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s2-seed0.json` | 4.1 KB | `b6fd75ec6465a096ecdd2aa903a7868c` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s2-seed1.json` | 4.1 KB | `7f932cb4ce960f8ac7e0df82e3a2b62a` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s2-seed2.json` | 4.1 KB | `b7487d8d78df6690fa80ae5c994871df` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s3-seed0.json` | 4.2 KB | `2144bf389b31648c0d6d6068c05cb9aa` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s3-seed1.json` | 4.2 KB | `c35314e4a0c657a7348ed9be593bb8ca` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s3-seed2.json` | 4.2 KB | `fb3bb03ccbae177e6f1218cdd3258863` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s4-seed0.json` | 4.2 KB | `0c91b1c07310e6621712e795577057ab` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s4-seed1.json` | 4.2 KB | `6f828daf5b95ec0739603e75e709cba1` | 2026-10-27 13:28 |
| `fusion/fused/fusion-loso-s4-seed2.json` | 4.2 KB | `4c1a541a7e3614e3a4b54de85a7076a2` | 2026-10-27 13:28 |
| `fusion/logs/slowfast-8020-seed0-shuffled.log` | 1.2 KB | `bd3398918214545f4c5cb11f2473a415` | 2026-10-27 06:04 |
| `fusion/logs/slowfast-8020-seed0.log` | 1.2 KB | `1a7036aaedafe17e54066e9036a93d01` | 2026-10-26 16:49 |
| `fusion/logs/slowfast-8020-seed1.log` | 1.2 KB | `39cfc887e35637fc3e938308053ffad0` | 2026-10-26 22:32 |
| `fusion/logs/slowfast-8020-seed2.log` | 1.2 KB | `a60e826dc8f32b8312842e85b5d44686` | 2026-10-27 04:12 |
| `fusion/logs/slowfast-loso-s0-seed0-shuffled.log` | 1.2 KB | `f964271f7aaaa99cdfccb4bfd84b216a` | 2026-10-27 04:15 |
| `fusion/logs/slowfast-loso-s0-seed0.log` | 1.2 KB | `aaf9325989c927bafd08245d92604948` | 2026-10-27 07:59 |
| `fusion/logs/slowfast-loso-s0-seed1.log` | 1.2 KB | `89b1d154c5fa138a0c5dc31d33ee1a60` | 2026-10-26 16:53 |
| `fusion/logs/slowfast-loso-s0-seed2.log` | 1.2 KB | `64bd73ac294341df943754ded7bc71c8` | 2026-10-26 22:33 |
| `fusion/logs/slowfast-loso-s1-seed0.log` | 1.2 KB | `8e7ecc9a8f90c2fbe507446f3ef55657` | 2026-10-27 07:59 |
| `fusion/logs/slowfast-loso-s1-seed1.log` | 1.2 KB | `7eba22c5d8563543e1e945cf452942eb` | 2026-10-26 18:43 |
| `fusion/logs/slowfast-loso-s1-seed2.log` | 1.2 KB | `47b2f6ba43492690e32e3d65a986bc5c` | 2026-10-27 00:27 |
| `fusion/logs/slowfast-loso-s2-seed0.log` | 1.2 KB | `551fe8ce80f1f557d2363eed13ccf20c` | 2026-10-27 09:51 |
| `fusion/logs/slowfast-loso-s2-seed1.log` | 1.2 KB | `5c9fc1e83a220cef8b7f6cf500472a50` | 2026-10-26 18:47 |
| `fusion/logs/slowfast-loso-s2-seed2.log` | 1.2 KB | `e59138289c5df10464e510b29d64a5c8` | 2026-10-27 00:26 |
| `fusion/logs/slowfast-loso-s3-seed0.log` | 1.2 KB | `1eedf76491993ac811bf17afa8c4e8bd` | 2026-10-26 14:54 |
| `fusion/logs/slowfast-loso-s3-seed1.log` | 1.2 KB | `154613f05c88350061d9e0345e8a882c` | 2026-10-26 20:38 |
| `fusion/logs/slowfast-loso-s3-seed2.log` | 1.2 KB | `937622b4ff9803c97a459b92f70e592b` | 2026-10-27 02:19 |
| `fusion/logs/slowfast-loso-s4-seed0.log` | 1.2 KB | `83f08393ac1c0ba219d8d8723fe9e180` | 2026-10-26 15:00 |
| `fusion/logs/slowfast-loso-s4-seed1.log` | 1.2 KB | `e3c641db9164255484a49f533f935d63` | 2026-10-26 20:40 |
| `fusion/logs/slowfast-loso-s4-seed2.log` | 1.2 KB | `bb969673213584c1745ff6579c6d7b7a` | 2026-10-27 02:21 |
| `fusion/logs/spoter-8020-seed0-shuffled.log` | 108 B | `b0d1f9f943ae6ed95c2308d496ef8bce` | 2026-10-26 21:55 |
| `fusion/logs/spoter-8020-seed0.log` | 99 B | `c9c832e07a32c5ff24e43dbe45204063` | 2026-10-26 15:03 |
| `fusion/logs/spoter-8020-seed1.log` | 99 B | `e64f87b2399e9723922d73efd64df359` | 2026-10-26 17:30 |
| `fusion/logs/spoter-8020-seed2.log` | 99 B | `a0819f7ef76be5a06dce7cb2248050a4` | 2026-10-26 20:02 |
| `fusion/logs/spoter-loso-s0-seed0-shuffled.log` | 111 B | `6d2b39e50ee7ef6cd0a6318669b196f6` | 2026-10-26 21:51 |
| `fusion/logs/spoter-loso-s0-seed0.log` | 102 B | `1a966f2c9d669244d32a7066c984dc77` | 2026-10-26 15:13 |
| `fusion/logs/spoter-loso-s0-seed1.log` | 102 B | `603c27d7f5231e820e859b8ff7d8e7f0` | 2026-10-26 17:28 |
| `fusion/logs/spoter-loso-s0-seed2.log` | 102 B | `082d307d6f5d7259825f1924ef8b6beb` | 2026-10-26 19:57 |
| `fusion/logs/spoter-loso-s1-seed0.log` | 102 B | `e985e5ebb006032e64717dc8a035d6b1` | 2026-10-26 15:16 |
| `fusion/logs/spoter-loso-s1-seed1.log` | 102 B | `aeb0385c47b00fb38f991d6b68fc51f8` | 2026-10-26 17:36 |
| `fusion/logs/spoter-loso-s1-seed2.log` | 102 B | `7ee9a2b0d48d44d3f0227df5bf061d1a` | 2026-10-26 19:59 |
| `fusion/logs/spoter-loso-s2-seed0.log` | 102 B | `efa2146f5106b0567d80ebf091f5bd7f` | 2026-10-26 15:13 |
| `fusion/logs/spoter-loso-s2-seed1.log` | 102 B | `5619ae4e002fa23fe9fd01d9e222dfac` | 2026-10-26 17:40 |
| `fusion/logs/spoter-loso-s2-seed2.log` | 102 B | `a50ed590ed3b919c190f52b1372a7248` | 2026-10-26 20:08 |
| `fusion/logs/spoter-loso-s3-seed0.log` | 102 B | `c16bd101fc240a4704618a1b7109165b` | 2026-10-26 15:14 |
| `fusion/logs/spoter-loso-s3-seed1.log` | 102 B | `1c87e97878cc3e21d09af22a45d3af08` | 2026-10-26 17:42 |
| `fusion/logs/spoter-loso-s3-seed2.log` | 102 B | `fb1ec61fbd8add4188ac0fa5ce37d60c` | 2026-10-26 20:07 |
| `fusion/logs/spoter-loso-s4-seed0.log` | 102 B | `982f5fbf01ed074b1d66da6257f44eff` | 2026-10-26 15:11 |
| `fusion/logs/spoter-loso-s4-seed1.log` | 102 B | `77508785f08b65a6118a989eaae2b9cd` | 2026-10-26 17:38 |
| `fusion/logs/spoter-loso-s4-seed2.log` | 102 B | `4ca0215a2a69d1cab33bc60d3151015f` | 2026-10-26 20:03 |
| `fusion/slowfast/slowfast-8020-seed0-shuffled.json` | 201.3 KB | `eefa99b342a47076a33dc72200e502fa` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-8020-seed0.json` | 97.4 KB | `17ccaed2bcc3440f0e3e0b33a965dcf7` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-8020-seed1.json` | 94.2 KB | `468b97c74c62cf71bb4d72bed33c12d3` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-8020-seed2.json` | 98.8 KB | `a557391f8f0f1ad68f888c2d8547f9d4` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s0-seed0-shuffled.json` | 201.7 KB | `078e32b3055202516965494a81f9025a` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s0-seed0.json` | 140.9 KB | `16bfb136c9f10c05e904a77f03351122` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s0-seed1.json` | 146.6 KB | `bc115c594165009dafff9ec2ff4b176a` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s0-seed2.json` | 141.9 KB | `f4e304db9ae38404af086cfcb6f56b6d` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s1-seed0.json` | 123.9 KB | `d2926ea84253bbe51073ab204da54f55` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s1-seed1.json` | 128.5 KB | `912b6fd87881f90c23210e531b88d47a` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s1-seed2.json` | 133.5 KB | `0e9d83bd66da116155ecb7a698510b40` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s2-seed0.json` | 118.6 KB | `fd51fb61d7420ef5fdf65f5f7a12e5b4` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s2-seed1.json` | 118.3 KB | `96ae7714b73148076cc0776c961e2954` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s2-seed2.json` | 126.9 KB | `16797093e228311162338b3da675238f` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s3-seed0.json` | 105.8 KB | `575e3b5146c93be72e45a997dd34686b` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s3-seed1.json` | 110.4 KB | `d47a1630e8876681c96c13171aacd85b` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s3-seed2.json` | 109.4 KB | `1a2ed0993c8f7a38acab1ee94c547320` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s4-seed0.json` | 106.4 KB | `4f0b89eeabdcdeca615d84ea3fbe3d0d` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s4-seed1.json` | 110.3 KB | `cac980f664b921c3ee42ec07555a3110` | 2026-11-18 (server paths anonymized) |
| `fusion/slowfast/slowfast-loso-s4-seed2.json` | 121.5 KB | `bbadc993dfe667482273cd476f283da3` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-8020-seed0-shuffled.json` | 233.3 KB | `388cac9acee1f89b3ffbed08b6246cae` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-8020-seed0.json` | 240.0 KB | `bf17a973fb4afadd01b27f98523930f6` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-8020-seed1.json` | 240.3 KB | `74d2751847c7dd58d7dd8ec4a2541509` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-8020-seed2.json` | 240.2 KB | `c92ef523b1a28f861ea221c411262858` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s0-seed0-shuffled.json` | 231.1 KB | `580fe46ed104bd7a99a64838ec3b2f06` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s0-seed0.json` | 239.1 KB | `fd2af7bf64fdcfa308b658a80bde31cf` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s0-seed1.json` | 239.5 KB | `ff01eb22ca618159bec5eda14208eded` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s0-seed2.json` | 238.9 KB | `e1a62aa5f97ca939404ed27b900c83f2` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s1-seed0.json` | 238.6 KB | `2be48490140a061cc7a1706acbe09b4c` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s1-seed1.json` | 238.5 KB | `97dd931bf0dc5d389ea44274814bb2bb` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s1-seed2.json` | 238.8 KB | `3e606a1dca8adc42f7840701ca3eb075` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s2-seed0.json` | 237.7 KB | `c98bea1f1b98fae47313d4078308352f` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s2-seed1.json` | 238.1 KB | `0ec45a6fae834df88cac2201a983aa85` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s2-seed2.json` | 238.0 KB | `bd8c2b8ac005a3d864a68aa3b2bc6cd1` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s3-seed0.json` | 240.0 KB | `d3f58b823abc06d2a4f7d9436ba4c440` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s3-seed1.json` | 240.4 KB | `05db30c4f86cc688cdea17ce1208a74d` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s3-seed2.json` | 240.3 KB | `0817bb463583c9ffb5fe0759c7e3a818` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s4-seed0.json` | 240.7 KB | `cbad3a50822ce2952b2343832cddfb76` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s4-seed1.json` | 240.7 KB | `12479f55f84e5748648f0ddbc8008900` | 2026-11-18 (server paths anonymized) |
| `fusion/spoter/spoter-loso-s4-seed2.json` | 240.5 KB | `f65895288eaab5ea9c214608e788d9ed` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/frame_count_gap.csv` | 11.7 KB | `864fef135c95e1f116385c50d8a8c19c` | 2026-10-23 16:09 |
| `importance_sequence/hand_motion.csv` | 195 B | `f1afa846ee01f9b369c7f84000e91d91` | 2026-10-23 14:32 |
| `importance_sequence/pose/DONE_pose` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-23 14:27 |
| `importance_sequence/pose/commit.txt` | 386 B | `dd68075a51485e14ebe415fb4e965068` | 2026-10-23 12:16 |
| `importance_sequence/pose/importance_pose_per_signer.csv` | 17.6 KB | `2023b0edb49fbdb2b7be4f7f6aabb84c` | 2026-10-23 14:27 |
| `importance_sequence/pose/importance_pose_runs.csv` | 161.5 KB | `caa5f170f7f55ebb297148fe831b6215` | 2026-10-23 14:27 |
| `importance_sequence/pose/importance_pose_stability.csv` | 262 B | `6b5ee589329d94208decfa572374a687` | 2026-10-23 14:27 |
| `importance_sequence/pose/importance_pose_summary.csv` | 11.8 KB | `d2173c6553d3a91a6a0597335b9b8d42` | 2026-10-23 14:27 |
| `importance_sequence/pose/run.log` | 4.8 KB | `077d4e6c5995f48c76463b219f1ac113` | 2026-10-23 14:27 |
| `importance_sequence/pose/logs/pose-loso-s0-seed0.log` | 326 B | `0514d440873b0c6a2731ab3952dc815a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s0-seed1.log` | 326 B | `05cb4dc587417042d4dfaa3abdaea580` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s0-seed2.log` | 326 B | `58ed8b231802b6cb23b3cbbc76e3d5f0` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s0-seed3.log` | 326 B | `7475bd618ea496b182fcd18506f0cd30` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s0-seed4.log` | 326 B | `9f1af57ec0c5b72da84f09ccfe2d7e80` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s1-seed0.log` | 326 B | `564e6af9a17d77271f8ec36d800b1d99` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s1-seed1.log` | 326 B | `eda15a879bee2db7cc10b6ba6acf705b` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s1-seed2.log` | 326 B | `59fa24780c86608bd8082f5d7454b5b4` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s1-seed3.log` | 326 B | `c014bbfca61238743ee93a2983e604d7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s1-seed4.log` | 326 B | `c9a0d221d3b1a1dd23208a556e9b18cc` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s2-seed0.log` | 326 B | `42ffc77500650684caf7b4cd3409ca93` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s2-seed1.log` | 326 B | `dc358788821793a33581e0e14b12d96c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s2-seed2.log` | 326 B | `908944236acd4bfe4cc1a777162ccf14` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s2-seed3.log` | 326 B | `86e3435cc23fc6a374f1a6dfeb1b09b7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s2-seed4.log` | 326 B | `2ca7cf612892995a9beecbcf2c4de773` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s3-seed0.log` | 326 B | `3482e1763b7d682bbff06fece33d74c0` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s3-seed1.log` | 326 B | `513f5a929a781d76a2417d11c7395594` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s3-seed2.log` | 326 B | `093093b23054f4923339d688bdeb0680` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s3-seed3.log` | 326 B | `23860686b6a28e3f2562f562ca6f7742` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s3-seed4.log` | 326 B | `09717f8fa3b98da4c74bd55e9ed4e47a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s4-seed0.log` | 326 B | `86953f590829379b062383af9b48bf9e` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s4-seed1.log` | 326 B | `cc13aa8765a7f22af0d8c108907f10ae` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s4-seed2.log` | 326 B | `8aa85bc662f9c34b61acc3a5ad59d123` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s4-seed3.log` | 326 B | `bf72263b72af7424c17beba60b1de45a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/logs/pose-loso-s4-seed4.log` | 326 B | `a5df2183a2463b4bb28ded358da08a09` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s0-seed0.json` | 20.6 KB | `b50914bcd9327e4ba417180ddb668558` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s0-seed1.json` | 20.6 KB | `aa01f2b9ad57cc27d7911bc98d48296a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s0-seed2.json` | 20.6 KB | `f7fee5aea667ac967ce6f2fb28519628` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s0-seed3.json` | 20.6 KB | `297a9b010c326379b353d7f746a91934` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s0-seed4.json` | 20.6 KB | `c8cab59490c2056f179aa2ef00d818db` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s1-seed0.json` | 20.6 KB | `cec3a2c1d9bf1dccf5efdf37df165f2c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s1-seed1.json` | 20.6 KB | `be0f7d29b55ba0e0a84251a7ee5767e9` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s1-seed2.json` | 20.7 KB | `4b55d517b467104c78aea83619941009` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s1-seed3.json` | 20.6 KB | `bf7969606dddc47f189a166c95ba5fd6` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s1-seed4.json` | 20.6 KB | `de0a9e62d6507dba36b3e815451b447a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s2-seed0.json` | 20.6 KB | `41deb04feec9e6679a0f1b2d376deae0` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s2-seed1.json` | 20.6 KB | `6da4993a835eaa92998acd898b2588c2` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s2-seed2.json` | 20.5 KB | `13ee908a915cf9b4035a0bc6b5cc5327` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s2-seed3.json` | 20.6 KB | `34ae6bdac9ab3f42a8860cece21c8b0c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s2-seed4.json` | 20.6 KB | `6c8e863d09b942b0609f297c40c359a0` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s3-seed0.json` | 20.5 KB | `e0b4746d4562664ecb39a00f5a143d93` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s3-seed1.json` | 20.6 KB | `25a0dd0f14a808c0b01cb8da36f0e496` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s3-seed2.json` | 20.6 KB | `d3e1b3bcb1dfe8a7159a62ecf81c33ff` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s3-seed3.json` | 20.5 KB | `3c6ba8459c59f52450cf75dfc88e0958` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s3-seed4.json` | 20.6 KB | `e0987ee08483337d16e95a865a1f5654` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s4-seed0.json` | 20.5 KB | `0b948391a4770ef875d52e241b15dbb7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s4-seed1.json` | 20.6 KB | `2eba675a642baf1f9dea632c174c636b` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s4-seed2.json` | 20.6 KB | `ddefe6f80824c8a2e0111284a6fb8511` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s4-seed3.json` | 20.5 KB | `9111cc6a47ed504d46667422aa000075` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose/runs/pose-loso-s4-seed4.json` | 20.5 KB | `f0ff60ffcbb157446cb10bb5409491f7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/DONE_pose` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/commit.txt` | 369 B | `27b133b0c4ee17584ee57d8b484c14e8` | 2026-10-26 08:51 |
| `importance_sequence/pose_subregion/importance_pose_per_signer.csv` | 5.9 KB | `d102869e285b1e4fd86486b1ca6a2fd9` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/importance_pose_runs.csv` | 51.0 KB | `5a7abcdf000c18e31404832fd6d10036` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/importance_pose_stability.csv` | 268 B | `638bb8d1ebafd11f0e94b74bb5c6732d` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/importance_pose_summary.csv` | 3.6 KB | `2d701acee371b5e6e00ada1ea39b9781` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/run.log` | 4.8 KB | `5046b484f88b4365ffe91a67a641edeb` | 2026-10-26 10:08 |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed0.log` | 326 B | `9cafe7da059bd3608135d0911c354ff3` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed1.log` | 326 B | `29a4ebc0f1ac837afef9622456304285` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed2.log` | 326 B | `23a178fb1118c5bbb769277824c0cec8` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed3.log` | 326 B | `e1ac7e70e2f95ad4c7eff6b865a1db29` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s0-seed4.log` | 326 B | `7a2fc6905b2daa9c21a9f27618f644cb` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed0.log` | 326 B | `cc3190e9b51d6e2f7bb3d5c5d197ffc3` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed1.log` | 326 B | `583ab2bd6086658e28c98ed31b334541` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed2.log` | 326 B | `92ccf4ee6d347d233a2f8c8043be516e` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed3.log` | 326 B | `91e462cdefe707d6af8cafe6b5a7dc7c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s1-seed4.log` | 326 B | `dc374f02c4aebbbf717a0990349968c4` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed0.log` | 326 B | `42d02387abc3a1a8464a124dcb1cc1d7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed1.log` | 326 B | `468da9053b9087086b6a6ed46e0629f7` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed2.log` | 326 B | `358463bd428932ad69ce617bbc6b045e` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed3.log` | 326 B | `41d0fc9a076d136151c01cb4b147c1d4` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s2-seed4.log` | 326 B | `cb57a2cd6a2362d51b3b7b59cc916509` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed0.log` | 326 B | `98931c2d13151eff8d98be38153f0a46` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed1.log` | 326 B | `c714fea266e93e2885f7048b5020fc47` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed2.log` | 326 B | `4535b8bd811175dedb8c655658cc7cee` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed3.log` | 326 B | `35b9218744c7532f18dbd9c534dd1dba` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s3-seed4.log` | 326 B | `3256d3f9994c4aef8165b8e7ff2ca9af` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed0.log` | 326 B | `874e94432ceca6134decd54a37aef51b` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed1.log` | 326 B | `c491fc80f12ce874bc16f39c4ebab806` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed2.log` | 326 B | `0013b1f6612024e0a28a4731e568cd24` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed3.log` | 326 B | `36f4bb9b5d22e36def4376c3273a9bf3` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/logs/pose-loso-s4-seed4.log` | 326 B | `c33882e14c0d2d43585284c7bc6ccf5f` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed0.json` | 13.0 KB | `0f6fe86b50f8a0829eed9d8aecc581e1` | 2026-10-26 08:55 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed1.json` | 13.0 KB | `0d1bdb48e1aac0192ea15ffff48c596f` | 2026-10-26 09:10 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed2.json` | 13.0 KB | `0f071371f806a227835697c2100e54f4` | 2026-10-26 09:26 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed3.json` | 13.0 KB | `05195001980d5b43360f8f9cd5ed6ae7` | 2026-10-26 09:41 |
| `importance_sequence/pose_subregion/runs/pose-loso-s0-seed4.json` | 12.9 KB | `5093d1afc87be6a37eb47661612e635f` | 2026-10-26 09:57 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed0.json` | 13.0 KB | `b04eb3106bff3a1c470833a00526f186` | 2026-10-26 08:58 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed1.json` | 13.0 KB | `1643c3672a004e6ddf4e81280059e28e` | 2026-10-26 09:14 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed2.json` | 13.0 KB | `c32be6e952c1182eb9a06f2a8599dfe5` | 2026-10-26 09:29 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed3.json` | 13.0 KB | `78c55bd689c211b8228fdd65b36c529a` | 2026-10-26 09:44 |
| `importance_sequence/pose_subregion/runs/pose-loso-s1-seed4.json` | 13.0 KB | `d563ba13afc29ba0b9663c5a7dae776d` | 2026-10-26 09:59 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed0.json` | 12.9 KB | `5efb02024c578c89b57c8783b5c154a3` | 2026-10-26 09:01 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed1.json` | 12.9 KB | `30a998bc960acacd6aae29d1539ea556` | 2026-10-26 09:17 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed2.json` | 12.9 KB | `bdcf9ad7a6b97abf0d278c7b87529161` | 2026-10-26 09:32 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed3.json` | 13.0 KB | `6b0bbb853fee7909829b74f95643ec90` | 2026-10-26 09:47 |
| `importance_sequence/pose_subregion/runs/pose-loso-s2-seed4.json` | 12.9 KB | `1b7e93b23bac4c7c92a0e1b97b5f33f8` | 2026-10-26 10:02 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed0.json` | 12.9 KB | `884220d76fc0342eb8de77746b69f323` | 2026-10-26 09:04 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed1.json` | 12.9 KB | `b9c184f326dc5497bb46500e687c2a91` | 2026-10-26 09:20 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed2.json` | 12.9 KB | `aa578b6c73eedf7ff5194234ed9e66bf` | 2026-10-26 09:35 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed3.json` | 12.9 KB | `a231c15a70c6d93579b10bd78ba64ccc` | 2026-10-26 09:50 |
| `importance_sequence/pose_subregion/runs/pose-loso-s3-seed4.json` | 13.0 KB | `63ccf2c2a506fbbc4cc4ebd748f88b6e` | 2026-10-26 10:05 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed0.json` | 12.9 KB | `909cd5c5c9f1e3cde8bf9d6defac19a0` | 2026-10-26 09:07 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed1.json` | 13.0 KB | `6aaf8b07bcfba8321254d6b7d9961af8` | 2026-10-26 09:23 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed2.json` | 13.0 KB | `bc9097a895914725e8dd11081386d380` | 2026-10-26 09:38 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed3.json` | 13.0 KB | `9663012a7d6bd016f9af871b54d11432` | 2026-10-26 09:53 |
| `importance_sequence/pose_subregion/runs/pose-loso-s4-seed4.json` | 12.9 KB | `ca832f73e3c8f52b3524fe8eec0899ac` | 2026-10-26 10:08 |
| `importance_sequence/stgcn/DONE_stgcn` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/commit.txt` | 386 B | `dd68075a51485e14ebe415fb4e965068` | 2026-10-23 12:24 |
| `importance_sequence/stgcn/importance_stgcn_per_signer.csv` | 18.1 KB | `06870542d3f78de5826578e38511edd8` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/importance_stgcn_runs.csv` | 165.0 KB | `1b2badddc4c5d5e119b37c8599e03996` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/importance_stgcn_stability.csv` | 263 B | `aa678c31a034c65938b862c5dd33f5db` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/importance_stgcn_summary.csv` | 12.2 KB | `848f9080a4064624e85288dd2ed8b7b9` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/run.log` | 6.2 KB | `0ba5543d718321de7c742cdf9beecc60` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed0.log` | 122 B | `7bd2babf7c6d2eacee80b2856ad0a6a0` | 2026-10-24 06:21 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed1.log` | 122 B | `e765055c8741931114aa044e9a52676a` | 2026-10-24 06:35 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed2.log` | 122 B | `889bf6f24914c87836ac643dd5499819` | 2026-10-24 06:49 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed3.log` | 122 B | `2d687f55fe4b251a3f71f4c8a220df90` | 2026-10-24 07:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s0-seed4.log` | 122 B | `c259413060ff14f033863b0b23575799` | 2026-10-24 07:25 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed0.log` | 122 B | `e08e3063a4f5f691afa484ccb45eb7ab` | 2026-10-24 06:22 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed1.log` | 122 B | `cdaf71d8971201b53e8cd0e944f83ae4` | 2026-10-24 06:36 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed2.log` | 122 B | `26d5d43c43996a5af7bdfa618cebaed8` | 2026-10-24 06:49 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed3.log` | 122 B | `e0aa8ef0dfc2726a58a77b15025c0297` | 2026-10-24 07:12 |
| `importance_sequence/stgcn/logs/stgcn-loso-s1-seed4.log` | 122 B | `cb85d7fa9cd3635c08e1ea6746e555f0` | 2026-10-24 07:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed0.log` | 122 B | `79e532e14c32440ae5edf61938fa837c` | 2026-10-24 06:23 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed1.log` | 122 B | `eaccee72336b374e07aedf11d2817631` | 2026-10-24 06:36 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed2.log` | 122 B | `63e3a58178fce5cabd1d19a1641c524d` | 2026-10-24 07:00 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed3.log` | 122 B | `29cf21d311f72411084271b5592e6b9d` | 2026-10-24 07:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s2-seed4.log` | 122 B | `6e8871338b2d3e0d6850d4da073952c6` | 2026-10-24 07:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed0.log` | 122 B | `782d1ffed356e9173d207bab3b094251` | 2026-10-24 06:23 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed1.log` | 122 B | `033faf86409b1a6d25dac41e9459fe14` | 2026-10-24 06:47 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed2.log` | 122 B | `3ecef520ecc85fab63e0d867b3a17876` | 2026-10-24 07:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed3.log` | 122 B | `18a99dc58a489c7d9dca1684e65f9832` | 2026-10-24 07:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s3-seed4.log` | 122 B | `41027470848397945fc25e84c2c5ff82` | 2026-10-24 07:27 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed0.log` | 122 B | `fcf42fd5c9e5cd7b4c3dc1765c41f0e7` | 2026-10-24 06:34 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed1.log` | 122 B | `1c68bf9274655675a015bb91c54fd933` | 2026-10-24 06:48 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed2.log` | 122 B | `bca02271cb7a9fc4a1e2168362f81319` | 2026-10-24 07:01 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed3.log` | 122 B | `8b2408950a00e01e6b1b4c270d1f39b6` | 2026-10-24 07:14 |
| `importance_sequence/stgcn/logs/stgcn-loso-s4-seed4.log` | 122 B | `f68765da3f8603d3d97a89ae4aa3c010` | 2026-10-24 07:38 |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed0.json` | 28.3 KB | `aa63a6c787609966fc2e06dc6a96859c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed1.json` | 28.3 KB | `9d17da210f3abfcffa64ffab8b02a50f` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed2.json` | 28.3 KB | `362a8555e4cfe92529c5df1ef783ebd3` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed3.json` | 28.4 KB | `5421a61df17f2426ef7638a5856bf142` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s0-seed4.json` | 28.3 KB | `79b03acee3cc7b847e38a5ec783aaa71` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed0.json` | 28.4 KB | `b93259c31338673f404539da39ab9e3a` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed1.json` | 28.4 KB | `1df633dc3f264fae88b78dd332d11ef9` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed2.json` | 28.3 KB | `fc5073bd20af549ef4c3ae78dd0893ba` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed3.json` | 28.4 KB | `3c808fe2586ed7464f8c1a7f0b1f33f4` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s1-seed4.json` | 28.4 KB | `480efdf5449356f04c49955979a473a5` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed0.json` | 28.3 KB | `8a24bd6ef55f2bab5e82da6d5fbb97c4` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed1.json` | 28.3 KB | `870eb0dd16d6e65045972c47d6f27e81` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed2.json` | 28.2 KB | `03fbecf9dfbce99618bf9521aaff07bb` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed3.json` | 28.2 KB | `ad083edc62fd05c9b70d200d05e80591` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s2-seed4.json` | 28.2 KB | `ff533711e9fea1537c4cd848b269a80c` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed0.json` | 28.4 KB | `cf64ed220cb49ced3f8b1e89386a0d6b` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed1.json` | 28.2 KB | `51617f97db1596b433bc7c54fc49c2c9` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed2.json` | 28.2 KB | `a7b01720c2aa1df79ec9aafc7fdac1d1` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed3.json` | 28.2 KB | `39b81d2347c7041b3a033e3248c1bad3` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s3-seed4.json` | 28.3 KB | `c0812672129eccf2482ce2a92eb4ef4e` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed0.json` | 28.4 KB | `b268b58d44351652dec6a53425201542` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed1.json` | 28.3 KB | `e3fd4efd240931ada4928640d32d38e9` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed2.json` | 28.4 KB | `2100ea6ee0a63b2eb0258ff805c30afc` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed3.json` | 28.2 KB | `3840be99aacd7bf4b07a087323e5486e` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn/runs/stgcn-loso-s4-seed4.json` | 28.3 KB | `fb626f18e15e720544a295872c31fc10` | 2026-11-18 (server paths anonymized) |
| `importance_sequence/stgcn_subregion/DONE_stgcn` | 0 B | `d41d8cd98f00b204e9800998ecf8427e` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/commit.txt` | 369 B | `27b133b0c4ee17584ee57d8b484c14e8` | 2026-10-26 08:51 |
| `importance_sequence/stgcn_subregion/importance_stgcn_per_signer.csv` | 6.0 KB | `f7091f35651383dcd94a546cd690a983` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_runs.csv` | 52.2 KB | `130662c5ddbcddc231041b115642004c` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_stability.csv` | 269 B | `ebc714ec947a3b9663dfe9b1d54b4652` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/importance_stgcn_summary.csv` | 3.7 KB | `6eb600272b9932eb29fae817d5e8337c` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/run.log` | 6.2 KB | `2c0a8b43aa59c14140002e14da246a5e` | 2026-10-26 10:09 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed0.log` | 122 B | `44a4b7ca8b25807423f648ff96c10c55` | 2026-10-26 09:02 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed1.log` | 122 B | `31dc2b79cdd06ec148930d84d6acd092` | 2026-10-26 09:14 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed2.log` | 122 B | `463b6a578345ed99c1f503581d270eee` | 2026-10-26 09:26 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed3.log` | 122 B | `d60b49313b4b216c7c4e22a59852a61e` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s0-seed4.log` | 122 B | `b58cc01753d6fd4af7aa5431efa6bfb5` | 2026-10-26 09:57 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed0.log` | 122 B | `bb367d2febf9d8168bd4162c19b285d3` | 2026-10-26 09:03 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed1.log` | 122 B | `83cdd2d628a5c12a1ece6a9166d9966b` | 2026-10-26 09:14 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed2.log` | 122 B | `9e33b282b766a7647ccb4bccff4496b8` | 2026-10-26 09:26 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed3.log` | 122 B | `1ea0fb969167c24ad76757b2955f5143` | 2026-10-26 09:46 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s1-seed4.log` | 122 B | `938bfa47a3d0a31457ce2a6815d12b7f` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed0.log` | 122 B | `598bf4ecc52c38985e1622ca8f898e9a` | 2026-10-26 09:03 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed1.log` | 122 B | `8b8d2adb7207dbb34a36476f0153abb7` | 2026-10-26 09:15 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed2.log` | 122 B | `e2211a85e23f2f820e5c4c1d3f41b476` | 2026-10-26 09:35 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed3.log` | 122 B | `46036827082ece363f4b4c77f7fbe6d2` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s2-seed4.log` | 122 B | `1da954cf26fc2e4da8483afe064606fc` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed0.log` | 122 B | `c33e813e34c37e66dcd14d71d0127707` | 2026-10-26 09:04 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed1.log` | 122 B | `41f8816ff83628243a055173204b272d` | 2026-10-26 09:24 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed2.log` | 122 B | `4818faa2aaa073e05cfd249c2c49bff9` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed3.log` | 122 B | `b4f9ae92cc905834ebf7b9d20f0d8787` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s3-seed4.log` | 122 B | `30e700c08fc5854c7930323aae7235bf` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed0.log` | 122 B | `536b774f687c51f30adc4a8b4cbeb6ca` | 2026-10-26 09:13 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed1.log` | 122 B | `d571819dd93d9e080ca2f93b6bb1db4b` | 2026-10-26 09:25 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed2.log` | 122 B | `6e08437c1f82059ab15dbf71e1e256fc` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed3.log` | 122 B | `7b99d3cc10db92c394d5421e2f2baf0b` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/logs/stgcn-loso-s4-seed4.log` | 122 B | `709dc5f398bb0b16dcafa78383238b1e` | 2026-10-26 10:08 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed0.json` | 20.6 KB | `00ddbbeea65205df753067f090906cef` | 2026-10-26 09:02 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed1.json` | 20.7 KB | `d3ac0cb1a38437636586e3421c32e563` | 2026-10-26 09:14 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed2.json` | 20.6 KB | `cd33b4ec01878217b56b963f82c4a55c` | 2026-10-26 09:26 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed3.json` | 20.7 KB | `40a9b639a8d2904e01a5aeacd557fdaf` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s0-seed4.json` | 20.6 KB | `9f65181ce920638880c83616df1fe5a1` | 2026-10-26 09:57 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed0.json` | 20.7 KB | `6b046a80f54dc991125bd0146d41cc51` | 2026-10-26 09:03 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed1.json` | 20.7 KB | `558981ad585af8f4c56e6c0cc38c7391` | 2026-10-26 09:14 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed2.json` | 20.7 KB | `cc9c36d74932a6edf721edce0846b2d2` | 2026-10-26 09:26 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed3.json` | 20.7 KB | `eab5fe6a07cfde20717f39077cccf875` | 2026-10-26 09:46 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s1-seed4.json` | 20.7 KB | `dce801e1fe01af136527a62f291c2df7` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed0.json` | 20.6 KB | `777077f4ceb2612c7d80b86ea2674990` | 2026-10-26 09:03 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed1.json` | 20.6 KB | `30f9c3aad3583818d12d71eb35daee18` | 2026-10-26 09:15 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed2.json` | 20.6 KB | `30251ac0b5685ba41241e92a37d9e004` | 2026-10-26 09:35 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed3.json` | 20.6 KB | `e3a2a74926c16c92d04407970d900cf1` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s2-seed4.json` | 20.6 KB | `3808a271d0723a1d7cc13e5d14d2b214` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed0.json` | 20.6 KB | `035586c310b7054e6e46bcd6ce910efa` | 2026-10-26 09:04 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed1.json` | 20.6 KB | `e8fe01532303b4cf048de937b16416d1` | 2026-10-26 09:24 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed2.json` | 20.6 KB | `8a366e906b002933e1cd5a0115218487` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed3.json` | 20.6 KB | `d1d307528b15c36c62bfdca73fdca28b` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s3-seed4.json` | 20.6 KB | `bc9774d4b51d72877842161032f65c0a` | 2026-10-26 09:59 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed0.json` | 20.6 KB | `6c2fe10acff06f797f0d011f91a44986` | 2026-10-26 09:13 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed1.json` | 20.6 KB | `2c3ddb4c589ff71c0ef8b7d258b0614d` | 2026-10-26 09:25 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed2.json` | 20.7 KB | `934f85e84f4c462057d9c3570ba63de5` | 2026-10-26 09:37 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed3.json` | 20.7 KB | `e43f7eefafe7085069fbf080058be751` | 2026-10-26 09:48 |
| `importance_sequence/stgcn_subregion/runs/stgcn-loso-s4-seed4.json` | 20.6 KB | `53cbba50b809cc2b85e422239b6f8a5d` | 2026-10-26 10:08 |
| `pose/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-19 10:07 |
| `pose/commit.txt` | 117 B | `c039de8b8e0dd71a3ea15947051c1929` | 2026-10-19 09:25 |
| `pose/run.log` | 6.1 KB | `f166f090a4995067598d9d4b43beef83` | 2026-10-19 10:07 |
| `pose/bodynorm/pose-8020-seed0.json` | 9.2 KB | `46ed9785192dd47f79d3b48792f6b9eb` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-8020-seed1.json` | 9.2 KB | `3d10b811f512e8e48889a0a14d8033d3` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-8020-seed2.json` | 9.2 KB | `72d365bc309ec740ea5efca57a0da0c6` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-8020-seed3.json` | 9.2 KB | `bc22d253dec6257117b9c745046c19f0` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-8020-seed4.json` | 9.2 KB | `a543857b719ae16e214f2279a903cdc2` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s0-seed0.json` | 9.2 KB | `7cd21644b3e7a16ce8661c380e2a0bfb` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s0-seed1.json` | 9.2 KB | `9548f00cd694bb145afdf4f51c8fba5b` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s0-seed2.json` | 9.2 KB | `588cd31e8a48f04c62d3d6edaa4995b6` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s0-seed3.json` | 9.2 KB | `f10528c9861098b2805a74e925fd6839` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s0-seed4.json` | 9.2 KB | `796731f2ec7da8bcd566aa2043e9b7fa` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s1-seed0.json` | 9.2 KB | `c4ebea08a0b9cebe2087f10aa2424e15` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s1-seed1.json` | 9.2 KB | `d271ffd7510f886921e067908bded8b2` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s1-seed2.json` | 9.2 KB | `18b8deca59f5190a7db5e400497910e1` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s1-seed3.json` | 9.2 KB | `53c99b7a91b9081e7c8e78df3df34005` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s1-seed4.json` | 9.2 KB | `d0c57d98372624e8dc42ba2443de2897` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s2-seed0.json` | 9.2 KB | `50de4f98d936111e8c4f47c18bdf754a` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s2-seed1.json` | 9.2 KB | `1a81b26042d20cf4f8a1ae10cd2edbbc` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s2-seed2.json` | 9.2 KB | `5c5fadffca06557f56ef50d8ddef3b67` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s2-seed3.json` | 9.2 KB | `4e3dbf0a7ef118ddef1f0366fb4bd165` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s2-seed4.json` | 9.2 KB | `7c161358217ea77832cbbb4822e0b9e7` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s3-seed0.json` | 9.2 KB | `f96c80c0dae2902487b3be0163af2843` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s3-seed1.json` | 9.2 KB | `8d1b235e62c28909b9c833c65725d278` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s3-seed2.json` | 9.2 KB | `87a4f17771c10d437b83cbb71650f130` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s3-seed3.json` | 9.2 KB | `4a65f9b1cf1f46246634fc361ca4bba2` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s3-seed4.json` | 9.2 KB | `23880ee28e28874d3710b903fbeaf882` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s4-seed0.json` | 9.2 KB | `1450d11815237a6a06d4bdad5213c2f8` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s4-seed1.json` | 9.2 KB | `421a18667af915f98ed0501cbb8cb624` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s4-seed2.json` | 9.2 KB | `eb6c39c67b677cb1d62fd66a7b47c1d3` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s4-seed3.json` | 9.2 KB | `db6ec424f4e10b1ff1afaf9c13c34240` | 2026-11-18 (server paths anonymized) |
| `pose/bodynorm/pose-loso-s4-seed4.json` | 9.2 KB | `9dad8a60af4e7e1a7d694f33a9ac1c8f` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-8020-seed0.json` | 9.2 KB | `6da4d79ccf9bf4aca20fc48f4814aace` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-8020-seed1.json` | 9.2 KB | `c5eaab15176e0806b215e21deab7545b` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-8020-seed2.json` | 9.2 KB | `52c50a5a5683aeeec4443c98ca6dffdb` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-8020-seed3.json` | 9.2 KB | `d1f899458a37e2fdd91759b9798edf51` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-8020-seed4.json` | 9.2 KB | `d89f1ec6ef2f8062853d4965770c7edc` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s0-seed0.json` | 9.2 KB | `ff81b0509cd59f77086110bb163974ff` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s0-seed1.json` | 9.2 KB | `44d0d545b751d63632082a5bf0e28425` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s0-seed2.json` | 9.2 KB | `7df85c2c5baf40dbdbf56b2e2d04a9ce` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s0-seed3.json` | 9.2 KB | `27210b0241cfb637cdc1450b7b5737c0` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s0-seed4.json` | 9.2 KB | `e325bd85d682510bbf61052a81dca961` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s1-seed0.json` | 9.2 KB | `fab828621bbe81510c922232c489ed84` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s1-seed1.json` | 9.2 KB | `28d5b7b0e4f68476c27e71781637e5d9` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s1-seed2.json` | 9.1 KB | `0e749bfbb2855191d48a7bdf168c40c1` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s1-seed3.json` | 9.2 KB | `953c4bda3f76b83c5e81f17dc485b8ff` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s1-seed4.json` | 9.2 KB | `2e8b91d647f6a905f6db9f57242e913b` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s2-seed0.json` | 9.2 KB | `45fd7db5da259b75ac96bafa096b6623` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s2-seed1.json` | 9.2 KB | `4e66ea074e224c8e6f80723ade27e6bc` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s2-seed2.json` | 9.2 KB | `a6627ee610f82156f6fbfe93cd282fae` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s2-seed3.json` | 9.1 KB | `9270b07fae0dbebe666ade3db783647d` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s2-seed4.json` | 9.2 KB | `d25420b15463d5933c6d9894d4574e22` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s3-seed0.json` | 9.2 KB | `fcb37cd304e80a55f7fcc3f2596c199a` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s3-seed1.json` | 9.2 KB | `21e397b2537e7b1584e0ad110eac4e3c` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s3-seed2.json` | 9.2 KB | `7d7acbcf032c57a7a03a8eb4a694cbf6` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s3-seed3.json` | 9.2 KB | `337653ec58c2a87ea46fa1053dc2908a` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s3-seed4.json` | 9.2 KB | `e11c22cb833106cd3b77638fde3f4f96` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s4-seed0.json` | 9.2 KB | `fa87e9099fb4a81236142e1747779924` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s4-seed1.json` | 9.2 KB | `96790fbba81088039bf29182d3b2be8c` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s4-seed2.json` | 9.2 KB | `4e64e75070ed268089808629a29b862d` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s4-seed3.json` | 9.2 KB | `4f90887f54546f93375fb364a5f375ef` | 2026-11-18 (server paths anonymized) |
| `pose/image/pose-loso-s4-seed4.json` | 9.2 KB | `b3b53c9bc7c631ae60f9f19d9ef2b802` | 2026-11-18 (server paths anonymized) |
| `pose_control/commit.txt` | 83 B | `1648df2067e2115ab72f0c81bb4c65c6` | 2026-10-19 10:08 |
| `pose_control/bodynorm/pose-8020-seed0-shuffled.json` | 9.2 KB | `b2b79a1b58c77d0f434344afc26f538d` | 2026-11-18 (server paths anonymized) |
| `pose_control/bodynorm/pose-loso-s0-seed0-shuffled.json` | 9.3 KB | `aa50d6fcf596d47faf96e18bd6fbb3cd` | 2026-11-18 (server paths anonymized) |
| `pose_control/bodynorm/pose-loso-s1-seed0-shuffled.json` | 9.2 KB | `96a4292027710fcd918e8ac80da6b589` | 2026-11-18 (server paths anonymized) |
| `pose_control/bodynorm/pose-loso-s2-seed0-shuffled.json` | 9.2 KB | `6937cefa4eba81d9e6f3daf17802d029` | 2026-11-18 (server paths anonymized) |
| `pose_control/bodynorm/pose-loso-s3-seed0-shuffled.json` | 9.2 KB | `513fecd73c16969859dd51b24315d4e6` | 2026-11-18 (server paths anonymized) |
| `pose_control/bodynorm/pose-loso-s4-seed0-shuffled.json` | 9.2 KB | `596cccb7716e8f4b121d6dee707b9bc0` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-8020-seed0-shuffled.json` | 9.2 KB | `5ff59d135ee49c3d720c8caaa9a96284` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-loso-s0-seed0-shuffled.json` | 9.2 KB | `7ec13b7afec15e81c68909a94cf6f48e` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-loso-s1-seed0-shuffled.json` | 9.2 KB | `2af586a836c5191f065a9ab8a04006eb` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-loso-s2-seed0-shuffled.json` | 9.2 KB | `5bc8b2f18c19c94602a6fa2034b6d381` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-loso-s3-seed0-shuffled.json` | 9.2 KB | `36a311294b2086fbdbb5f9e2de2af48a` | 2026-11-18 (server paths anonymized) |
| `pose_control/image/pose-loso-s4-seed0-shuffled.json` | 9.2 KB | `c7427b4d25c740a03d731423f0aea197` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-22 07:08 |
| `pose_study/runs/commit.txt` | 208 B | `4f0f6b7226e541798dec2f9d5f4f3cbe` | 2026-10-21 21:38 |
| `pose_study/runs/errors.log` | 173.9 KB | `a86b3b4b0992e5277ec36df41b94a47c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/jobs_phase1.txt` | 162.6 KB | `51da28166abda8406b380f079266946e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/jobs_phase2.txt` | 4.7 KB | `0973acf0ebb9f6cbb354c2e6a6635351` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested_selection.csv` | 373 B | `25186ce5544be3b61a6d15388494c77e` | 2026-10-22 06:31 |
| `pose_study/runs/nested_selection_grid.csv` | 3.8 KB | `10d923001e94bc70df4cb3724152142f` | 2026-10-22 06:31 |
| `pose_study/runs/run.log` | 668 B | `75a8c7db6e5e0609e9bdf9f37ce1fc55` | 2026-10-22 07:08 |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s0-seed0.json` | 9.5 KB | `4459fa51133d3a53c6a07f5f00cb3924` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s0-seed1.json` | 9.5 KB | `28becf717998cf82ef7073608558157a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s0-seed2.json` | 9.5 KB | `c04c8eab9a39fea7ba6b6096e428aca2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s0-seed3.json` | 9.5 KB | `dbb4d4f68d9efc2d9715d323b0f17c3d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s0-seed4.json` | 9.5 KB | `a4c31e20ae0bfee4e91461a86722aa2d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s1-seed0.json` | 9.5 KB | `6e04bf4e5b781aafe7ae52e475f7fd80` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s1-seed1.json` | 9.5 KB | `d446c4270b6cb4751e0304d3845f91a5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s1-seed2.json` | 9.5 KB | `0b68d6d84f6fe290733181bd7ad33286` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s1-seed3.json` | 9.5 KB | `67381492239cab609a87f0bfa72ad815` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s1-seed4.json` | 9.5 KB | `7c9718c7d2ec463a3dbb3874f8ca1974` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s2-seed0.json` | 9.5 KB | `0fd446995749e1b5638f0547fa53f177` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s2-seed1.json` | 9.5 KB | `9d9befbff3f9b6f2f1bc1fdd7d5685d1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s2-seed2.json` | 9.5 KB | `ee821c75a58384a6d5461282dc01e245` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s2-seed3.json` | 9.5 KB | `73ad16e78c0fba6d9260fbcf1264ad24` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s2-seed4.json` | 9.5 KB | `a10fd8c73d7c927352933d881295219c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s3-seed0.json` | 9.5 KB | `7a904c397b1f3eed0d85c4c3b1525480` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s3-seed1.json` | 9.5 KB | `53526ada83aa70d602a278eae437ceab` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s3-seed2.json` | 9.5 KB | `90aef5dbc6a19fd133a11a74bc54e12c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s3-seed3.json` | 9.5 KB | `31b26d30b72e9c7fcf37bfa50feb4adf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s3-seed4.json` | 9.5 KB | `6bd1872a79f6f485a3420f584ac70ae7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s4-seed0.json` | 9.5 KB | `3440323d441416c69d8aa85bd2f84944` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s4-seed1.json` | 9.5 KB | `c9bd6badde4f11806c5f2bb5bfdeeafe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s4-seed2.json` | 9.5 KB | `5b06fb9c44c5863b6d24fb89f239dad9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s4-seed3.json` | 9.5 KB | `1617eea5e0feb4a5f49d5428b68a95bf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A1_no_augmentation/pose-loso-s4-seed4.json` | 9.5 KB | `fcee1047155d63605f7c8da8b3b702fe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s0-seed0.json` | 9.8 KB | `7ef92c702310837708d5e0e1e8b44828` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s0-seed1.json` | 9.8 KB | `4d22aa3ed3fd93c99a8bb3b520e35565` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s0-seed2.json` | 9.8 KB | `29734afa547244fa7323828878c71c23` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s0-seed3.json` | 9.8 KB | `a8dab287827c502e6ae1813b7060edb1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s0-seed4.json` | 9.8 KB | `c816a9db8f54e43ac1d72c2ae81f5d20` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s1-seed0.json` | 9.8 KB | `e9f39c04732d80073086092dd07ed45c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s1-seed1.json` | 9.8 KB | `85c09a600465863c24c615205a0c03b0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s1-seed2.json` | 9.8 KB | `d693be19a985189ed418776deaf4b384` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s1-seed3.json` | 9.8 KB | `92371e4c911688068ab714c2ea0855d1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s1-seed4.json` | 9.8 KB | `5214487e36cef5990524a7ff76404515` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s2-seed0.json` | 9.8 KB | `07be00d91d87212b3126ad5165db9384` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s2-seed1.json` | 9.8 KB | `0b9ef40324b026f4636594464413b59a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s2-seed2.json` | 9.8 KB | `35c8f787b8a85f62bc4f7253e43c172c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s2-seed3.json` | 9.8 KB | `a35a2fb603e3071517c3ca3ebf7a2b2f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s2-seed4.json` | 9.8 KB | `47a0c48f3a0ed50485147ffce2789862` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s3-seed0.json` | 9.8 KB | `56cdf1e26e43833389ee7e8c88ad9658` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s3-seed1.json` | 9.8 KB | `39589744ae3aadb5361c4b142542d340` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s3-seed2.json` | 9.8 KB | `41de96f8ecd286507632b5326986e6d2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s3-seed3.json` | 9.8 KB | `34b7a2879c62cf4dc56ec74d5b59019d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s3-seed4.json` | 9.8 KB | `3491be7182bb17f8fc0c8147460eb0e6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s4-seed0.json` | 9.8 KB | `08187d860a193d9ab394df2505e188ca` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s4-seed1.json` | 9.8 KB | `d66be24935c1d735e0a33c5026236c6f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s4-seed2.json` | 9.8 KB | `d98d52e128ab97c2009163b3fef806fd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s4-seed3.json` | 9.8 KB | `1eb0157d98e75e528593be96fb5e24cc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A2_no_label_smoothing/pose-loso-s4-seed4.json` | 9.8 KB | `ea03cd016c5b16f54512c4d04ce30b91` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s0-seed0.json` | 9.9 KB | `7cb7947ef995764e451200620beee6f9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s0-seed1.json` | 9.9 KB | `c89fe331d69722fb7a670c901ac02e59` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s0-seed2.json` | 9.9 KB | `17e8e7e9516eebf5d7d5e08930fe18db` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s0-seed3.json` | 9.9 KB | `f7ce22e2b0cc912a628e28bf7be65e5e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s0-seed4.json` | 9.9 KB | `3b27e400bcf2185100c6b674f0b79412` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s1-seed0.json` | 9.9 KB | `eb9c20bd74e1d66199433652809948dd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s1-seed1.json` | 9.9 KB | `2429828843daf7ad3036c59085772ce9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s1-seed2.json` | 9.9 KB | `d509d076355d10949cd509317ceb4e7d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s1-seed3.json` | 9.9 KB | `94da198f14533526937a90d8ec32427a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s1-seed4.json` | 9.9 KB | `cf5375e5965604c813925079c279ac9d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s2-seed0.json` | 9.9 KB | `c64114738f586454267b297fdf35622a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s2-seed1.json` | 9.9 KB | `70a4889847d7e25123c225cd190c8840` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s2-seed2.json` | 9.9 KB | `acfadb64963c4bb3a4cd565d24401ac4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s2-seed3.json` | 9.8 KB | `318ea30e0b5497c445bb2913f7f18f89` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s2-seed4.json` | 9.8 KB | `3cf03631ef8855aea4cdeb935d1ce614` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s3-seed0.json` | 9.8 KB | `4677837c4690995c3134c5a1290eea1b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s3-seed1.json` | 9.8 KB | `09e5b7c7c5b0194c0297a332f6e31db4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s3-seed2.json` | 9.8 KB | `be6a52592fae1dad1d5727824c8e6ce6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s3-seed3.json` | 9.8 KB | `808a851392a7d7b68409bb2f8121fe16` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s3-seed4.json` | 9.8 KB | `d82794e0b00ccad651dda406db45e72d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s4-seed0.json` | 9.8 KB | `75def91ca36e14573901a45704254213` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s4-seed1.json` | 9.8 KB | `f84a58785af2582014c47ec88e73e491` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s4-seed2.json` | 9.8 KB | `aea48ed9bae458fa04fedba5876a2aa3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s4-seed3.json` | 9.8 KB | `09e36675bb0fadb6bf47dc670b872d42` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A3_plain_recipe/pose-loso-s4-seed4.json` | 9.8 KB | `d0a3402ef764ccc2c2fb2dbdcae105a3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s0-seed0.json` | 9.5 KB | `425c12956776f009482fac95bce03c26` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s0-seed1.json` | 9.5 KB | `84a0a484af1db33f4806c10d80699cb1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s0-seed2.json` | 9.5 KB | `5a5fe9fd0b874ac7572be7c88659b2a8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s0-seed3.json` | 9.5 KB | `c67cbf6936db92e976d75b239b25b53e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s0-seed4.json` | 9.5 KB | `1a6d56d3b30e6382d6cc104c1dc961f6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s1-seed0.json` | 9.5 KB | `56e122a7ce58410dbd6f91c717ae6379` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s1-seed1.json` | 9.5 KB | `ea6d3d3da299c44c28f51b2f63e444fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s1-seed2.json` | 9.5 KB | `0ebc0024590e6b61a9d62f25bec1bb76` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s1-seed3.json` | 9.5 KB | `53c2078e6e93177ab13d3e2388ab36bd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s1-seed4.json` | 9.5 KB | `c6ca9f648a603cb0fc3d15938c04ea4b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s2-seed0.json` | 9.5 KB | `0762a6486287608e40dacea1a57eabde` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s2-seed1.json` | 9.5 KB | `121dc7c64dbf0cf186fbc6d50d161b95` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s2-seed2.json` | 9.5 KB | `55db5600a3ce85885d0a256af3ebd4c8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s2-seed3.json` | 9.5 KB | `467a5605031337367ac34254805ef332` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s2-seed4.json` | 9.5 KB | `e7992f3297eac04d57048d2e4ea25590` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s3-seed0.json` | 9.5 KB | `3c355707b9eb191daf27eed19d680864` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s3-seed1.json` | 9.5 KB | `45ae7c09213f49c6d41dcdac2aa19b30` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s3-seed2.json` | 9.5 KB | `a5619048454593e374f71803f90b4c51` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s3-seed3.json` | 9.5 KB | `484c64d72c4e4e88eada53bf24e5669e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s3-seed4.json` | 9.5 KB | `f3eddbf2d53f37dbaffefd56fc943314` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s4-seed0.json` | 9.5 KB | `ea9549f5c2e2659d2bd74ac5e9dc0e5d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s4-seed1.json` | 9.5 KB | `19dac317d10c99255d787f80743c8a53` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s4-seed2.json` | 9.5 KB | `42feb585e843835ba0d8bb5897442ad1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s4-seed3.json` | 9.5 KB | `4b9e30410dd4a244be2efa24433a3139` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A4_mean_pooling/pose-loso-s4-seed4.json` | 9.5 KB | `58ae51d495ec977f2ec8e08912a6e00b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s0-seed0.json` | 9.5 KB | `6cd0c740908d99d05ccd9f1e993cf836` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s0-seed1.json` | 9.5 KB | `241460cedb72177b511ce247ff3f503a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s0-seed2.json` | 9.5 KB | `953a84a9758d5e13554fc79b444f205f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s0-seed3.json` | 9.5 KB | `02ea97c3e9902cf5f94d8496d4f2123c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s0-seed4.json` | 9.5 KB | `8b4c6f0801a9ba25863e0712f4e690c2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s1-seed0.json` | 9.5 KB | `cc9a7d419ef6cf49f98e2e478dd595e8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s1-seed1.json` | 9.5 KB | `9bbdac856538d760f68be6492d297730` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s1-seed2.json` | 9.5 KB | `e9848225d0fe9be3f539c20401a67512` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s1-seed3.json` | 9.5 KB | `50f64f6177399bc26b1c653e18c7f2e0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s1-seed4.json` | 9.5 KB | `408b6f86ca53e2c4e8feccf8d498995d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s2-seed0.json` | 9.5 KB | `430a000258e5d17d34e2a59f5f7c1962` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s2-seed1.json` | 9.5 KB | `ad1b8b0b957f9f23a8bb092ea9d2e06e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s2-seed2.json` | 9.5 KB | `52bb668e0783a70e3d058c60ff423812` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s2-seed3.json` | 9.5 KB | `7bd66b4521bf3b8dc36eb0a1445f2f2b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s2-seed4.json` | 9.5 KB | `a241aedd671b8a1946e61d3bd22338e8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s3-seed0.json` | 9.5 KB | `aeecf0329d403ac8b648e111a3b47e17` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s3-seed1.json` | 9.5 KB | `8519f63b6aec3d378d83d8520cee09fe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s3-seed2.json` | 9.5 KB | `2cc4d571a3fd2f1b2765d465555ace23` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s3-seed3.json` | 9.5 KB | `a3c284d931d6e5f150b6118c8e451b21` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s3-seed4.json` | 9.5 KB | `4a4dd266cbe8428ff4e35dd780aee48a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s4-seed0.json` | 9.5 KB | `f96ffabfc6f7589d84f4b5580ff43802` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s4-seed1.json` | 9.5 KB | `59f2010e2e47bdc8d65eb2a915caaeaf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s4-seed2.json` | 9.5 KB | `17f1bd78932ccb5d4d8eb3bdfc86e3b5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s4-seed3.json` | 9.5 KB | `db790846170078157a28f85c152ce415` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A5_hands_only/pose-loso-s4-seed4.json` | 9.5 KB | `b1ca166b443e1c44e889dea1d639ddba` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s0-seed0.json` | 9.4 KB | `8ae3b934b70d97313c073cbb9996ce71` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s0-seed1.json` | 9.5 KB | `9721a81021f41a6961213443ddfba97a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s0-seed2.json` | 9.5 KB | `b59e7fe74270be334be3f79c33ee9054` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s0-seed3.json` | 9.5 KB | `7d703dd5085e85c06a3694381e05ca21` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s0-seed4.json` | 9.5 KB | `f0a4ee13d2b4438ed69186c99816569d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s1-seed0.json` | 9.5 KB | `7f85497dc7d021a579cbc90e4be96671` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s1-seed1.json` | 9.5 KB | `4f88c1813f33853f5d38c367a3baadb9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s1-seed2.json` | 9.5 KB | `223fefb8378233c994a7d642bc702798` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s1-seed3.json` | 9.5 KB | `165c6ff0c9a4f637e4c0754bdbda1602` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s1-seed4.json` | 9.5 KB | `4c1820cf8cf2465a195149dc3cc653c9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s2-seed0.json` | 9.5 KB | `cdfad5022bbd25af1b3a4bc1e562a113` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s2-seed1.json` | 9.5 KB | `d9f5b88f55f50ada8f1e0680464ddbcd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s2-seed2.json` | 9.5 KB | `c40782c304d700e1a6b91b2463db5212` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s2-seed3.json` | 9.5 KB | `e0c02f2b9ffd8420a88aeed3a9ab42bf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s2-seed4.json` | 9.5 KB | `b2d902f626c06b371397214567f914c9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s3-seed0.json` | 9.5 KB | `c4af750a374962dcffb19007b9f3b60c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s3-seed1.json` | 9.5 KB | `2deeef508233209a2e45da49ffb30ea0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s3-seed2.json` | 9.5 KB | `832277900e8f9d0d4a1cf9dd3bb1d9bd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s3-seed3.json` | 9.5 KB | `d1379345a0a76dbaa80f98de2cd1fc71` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s3-seed4.json` | 9.5 KB | `4f4c1033fd300bc92c7c44164cebc670` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s4-seed0.json` | 9.5 KB | `1ac45a8ad6ad958bf035a3d6e375dbfd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s4-seed1.json` | 9.5 KB | `95ae3b7e5bc084265d1762fc4dbb2409` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s4-seed2.json` | 9.5 KB | `9fd487ce49c14ebc1000c56771bec869` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s4-seed3.json` | 9.5 KB | `bdeac47698b52f07687b6422a3d7bda6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A6_body_only/pose-loso-s4-seed4.json` | 9.5 KB | `e7c36a7155f117971d8e18396e4d5a30` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed0.json` | 9.5 KB | `6349e796134339c379b17a3e78714278` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed1.json` | 9.5 KB | `dd2f6c9cfcca0c4645e693d860962205` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed2.json` | 9.5 KB | `631b2acfd8ef03c0ec492d242d61cecc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed3.json` | 9.5 KB | `167a2a9af52cd9989f475b16fdecff7f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s0-seed4.json` | 9.5 KB | `d15cfa399c60c74e658d6de62d73550a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed0.json` | 9.5 KB | `b594e9813418c8c74d47a9df29d1b95c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed1.json` | 9.5 KB | `56673b4eebb9a2585a9f693432cd2a57` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed2.json` | 9.5 KB | `6601556d0bd017897c6dfb22eee11d1a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed3.json` | 9.5 KB | `c6a2d59315f3aa10db71b2ac12be26f0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s1-seed4.json` | 9.5 KB | `09c83e6d88e49b0dd308830b5e49f6f3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed0.json` | 9.5 KB | `e983a5f31e2ffb8e1a97b065a2c99b04` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed1.json` | 9.5 KB | `a169ed204f815f4060137942df17dd75` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed2.json` | 9.5 KB | `5d1a95c68e10e227a915448ea8163250` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed3.json` | 9.5 KB | `4cec5456d3f5ea4ac8c49c4e5156782c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s2-seed4.json` | 9.5 KB | `6535ef80d34f9ced43108b6ae7ea97b1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed0.json` | 9.5 KB | `2a262b98d062803990acdf9b620251e9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed1.json` | 9.5 KB | `5e60729dea6aad17ecb4987457fbfba1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed2.json` | 9.5 KB | `5fbd468c72b182fcd96a0ee0a686db93` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed3.json` | 9.5 KB | `45982fc22b6f84564d97fd5e30186b97` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s3-seed4.json` | 9.5 KB | `f89762ef7ae0a49cdf3ae37e649ca180` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed0.json` | 9.5 KB | `5d8c0101d78cc84a4efdca6a7eaeb038` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed1.json` | 9.5 KB | `a80d2d64914894cfd48ca23ee2bc4331` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed2.json` | 9.5 KB | `985b06bc6ce3f25cea0c364c1cb51e6b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed3.json` | 9.5 KB | `b4e06e81ac3b4578e65ca777f7499722` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/ablation/A7_image_rotation_about_shoulders/pose-loso-s4-seed4.json` | 9.5 KB | `606999d5990df75c10155c29cec1c95a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s0-train1.json` | 9.5 KB | `f8d68a689ba086f99287ed371474933f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s0-train2.json` | 9.5 KB | `9fb6ed53bb86cd065ca7b599e4665405` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s0-train3.json` | 9.5 KB | `8209d8910b8f6bc09bb88d9db30f74b0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s0-train4.json` | 9.5 KB | `3c78753787e4dcf46cacbb8c375d0f72` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s1-train0.json` | 9.5 KB | `ee04e0961bdac018b9b7b4187b03e503` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s1-train2.json` | 9.5 KB | `0c78cade3ed833defb569fd63617cc1b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s1-train3.json` | 9.5 KB | `41a3c05e5329839fc95206953c3c2bb0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s1-train4.json` | 9.5 KB | `92f93d35192775707156f882da4e6cfc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s2-train0.json` | 9.5 KB | `c7836fe63b097f7784db5419cd0b896c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s2-train1.json` | 9.5 KB | `2f59b836b3de7de48e8923d19574b87a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s2-train3.json` | 9.5 KB | `28bfae5cef9da075b02f1057a37a7db7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s2-train4.json` | 9.5 KB | `8ed426937ecaab573f9c771c658e502f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s3-train0.json` | 9.5 KB | `6a5c01a8c379ed464c2339d2fc3be985` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s3-train1.json` | 9.5 KB | `82f0265765f10ea7e1802f1fefc9f559` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s3-train2.json` | 9.5 KB | `ce84bd4babbc4a7dc850a386eadf1876` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s3-train4.json` | 9.5 KB | `82edf0ef8f45dbb47f4befb4b9b93774` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s4-train0.json` | 9.5 KB | `8e105f49594ac40c6bcf112030fafa11` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s4-train1.json` | 9.5 KB | `2daa01fd87a0a4086f5e9fe0a1d53f5c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s4-train2.json` | 9.5 KB | `30cacd47129f6ff546f2abb3f764ad92` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k1-s4-train3.json` | 9.5 KB | `37b5baf5e852dbf9c43dcd8cc960af0a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train12.json` | 9.5 KB | `196de253281c431c8583b5fb6a58a1a7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train13.json` | 9.5 KB | `1a5744fc0da223d29aeef23a5291e8d5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train14.json` | 9.5 KB | `13b489d1e96d18e293172a47ec19d4fc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train23.json` | 9.5 KB | `73c4f9b4d641e0a0c7e5ea9cc970534a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train24.json` | 9.5 KB | `200de560962a442d057f81e850a5adfa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s0-train34.json` | 9.5 KB | `184a168c1cd12499898978953f0c4679` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train02.json` | 9.5 KB | `2d0bea39e8a7bb7fb0b31d71da9d01d8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train03.json` | 9.5 KB | `7c028511b2aebe6c6e1e606a5c3ab741` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train04.json` | 9.5 KB | `b285f0ae9b25bdf684ad3a82367ae4be` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train23.json` | 9.5 KB | `e2c75970e062daff21af7bf33b8576b4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train24.json` | 9.5 KB | `71a348038f08fccb06820f779313fbb6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s1-train34.json` | 9.5 KB | `a95aa720b873c61f5aa9e39859c8d541` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train01.json` | 9.5 KB | `36642c9668a9e47e0ef7c35bdaf79aea` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train03.json` | 9.5 KB | `8a0be706731c596176209c54a53f1ba7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train04.json` | 9.5 KB | `4b06aed1ce27fc493e336ca16f904c3b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train13.json` | 9.5 KB | `8785a45477572d196983c40de0175ce3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train14.json` | 9.5 KB | `6b4b784a4f6f01c7ac603677fd98800c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s2-train34.json` | 9.5 KB | `d790674349152e4c9a0d0ce53e83b2bf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train01.json` | 9.5 KB | `b4e543579898086b0b547fe5a2c3544d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train02.json` | 9.5 KB | `9d50b3bd189e47212b61d0feb88f33fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train04.json` | 9.5 KB | `49630d718ceffd2fdb7c952fe342d641` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train12.json` | 9.5 KB | `b8f61b0664c662c4f46c1500f8e5cfc7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train14.json` | 9.5 KB | `d9db7dcd966de89f8d8734eeaf8c1cfc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s3-train24.json` | 9.5 KB | `d5e73715b94545946e8e38ca5f4a6c2a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train01.json` | 9.5 KB | `7497857d1362fbee46789aa6884970c7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train02.json` | 9.5 KB | `f0522ecfe0ba11b08d4693d680910556` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train03.json` | 9.5 KB | `4fa82de878d219fc5c14eae2ac11d0ff` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train12.json` | 9.5 KB | `74e93d5947b85d1d34073ab4aac7f847` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train13.json` | 9.5 KB | `981a0bc91b433df1aa73fff3a9241585` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k2-s4-train23.json` | 9.5 KB | `d9215378140f4656a5775de6aa62743f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s0-train123.json` | 9.5 KB | `3acc71a9d196a641ef2f910a9d79f0ad` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s0-train124.json` | 9.5 KB | `b1c83729eb2f7f6bc1af38fe3a53f338` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s0-train134.json` | 9.5 KB | `aa86dccc4cc5bc2a68f4f3af68c9b8f2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s0-train234.json` | 9.5 KB | `b1735389d30275d853cb0eecdca93237` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s1-train023.json` | 9.5 KB | `392ed4c78b66f6275b81ef351ff0c8d5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s1-train024.json` | 9.5 KB | `78100e098817df76a22dc9d73f143d51` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s1-train034.json` | 9.5 KB | `e8619dad0151e010286d0e173e2a5ea7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s1-train234.json` | 9.5 KB | `8e21dd1d026d341ef7caf051dc14de69` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s2-train013.json` | 9.5 KB | `993a867b6236930154e4520de8af8b8a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s2-train014.json` | 9.5 KB | `0a7eb43185d015c50748223075bff875` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s2-train034.json` | 9.5 KB | `f186c74f6bee98c307f25e600d22e097` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s2-train134.json` | 9.5 KB | `15adf9b44e71711850fc2c0027a8ba6c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s3-train012.json` | 9.5 KB | `14dbf9dd3e56189862bb14662db8db85` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s3-train014.json` | 9.5 KB | `7a503cff802401480d43b1320ce67692` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s3-train024.json` | 9.5 KB | `c085ebc0c5e6485f0bd9e0abc4d1c103` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s3-train124.json` | 9.5 KB | `88aacbd0f0cfce176d7024d8a6575fd8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s4-train012.json` | 9.5 KB | `4f1834980c0c039179e2e4273bfb6ea9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s4-train013.json` | 9.5 KB | `8d143d2c3a784d592b83c763bf33ec33` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s4-train023.json` | 9.5 KB | `ecfcaa21a439217bc02756f16c52e733` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/curve/k3-s4-train123.json` | 9.5 KB | `14395565ea72c6eba0bd8f0bd2cfc2ce` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s0-seed0.json` | 9.5 KB | `6ed9e94aacd6d37feb212216d408d5ef` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s0-seed1.json` | 9.5 KB | `f1d993d5e7c99a43675b8dd02b2400fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s0-seed2.json` | 9.5 KB | `1cf6f872edd6cc43977f3d675c38311f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s0-seed3.json` | 9.5 KB | `32a680a08fa16fe6729d5d4fac9d2633` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s0-seed4.json` | 9.5 KB | `b2bfa00cbb4d403dd996b055dbfb682c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s1-seed0.json` | 9.5 KB | `2a3264db5f63dfc4c07f72873c8b16a1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s1-seed1.json` | 9.5 KB | `680917897e8f53202fdf6174815db2b5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s1-seed2.json` | 9.5 KB | `267c07d458c5d09aad6cbf98a7a8b862` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s1-seed3.json` | 9.5 KB | `c15aa8f366fe377ff90be6d52906e560` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s1-seed4.json` | 9.5 KB | `bedecb3306791b6cd8d23d332eee6daf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s2-seed0.json` | 9.5 KB | `8a380dfefea312336c0456cad7fc21bf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s2-seed1.json` | 9.5 KB | `577c60b1fc4ea23febb16e65824f245f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s2-seed2.json` | 9.5 KB | `32ae7f595c7ff7679fdfe47d54a27cf3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s2-seed3.json` | 9.5 KB | `be126c2951729823e74a477382037d3e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s2-seed4.json` | 9.5 KB | `15aaae439cb7b849c8589406a4468c91` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s3-seed0.json` | 9.5 KB | `42d73ddd566d87130e322ca057faa71c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s3-seed1.json` | 9.5 KB | `79e2b5621d23eec231c862f6efc1f845` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s3-seed2.json` | 9.5 KB | `260353a0e337e49704211f719d094c3a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s3-seed3.json` | 9.5 KB | `921bb793110adedc304b54de88ee0b5f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s3-seed4.json` | 9.5 KB | `1a93c24e7f701cc639885241e3676946` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s4-seed0.json` | 9.5 KB | `5235ed269e5a0a9504bfd0b2beace254` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s4-seed1.json` | 9.5 KB | `8b4415b7b9b5376668bdcc5a8082eb77` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s4-seed2.json` | 9.5 KB | `c8659c0f19d92f109f9e30d401ab2072` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s4-seed3.json` | 9.5 KB | `d2a8886520b2daf5751f72450e975fb7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f16/pose-loso-s4-seed4.json` | 9.5 KB | `93c16b2734b0dbbb973307589e2131ad` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s0-seed0.json` | 9.5 KB | `a517aaaef6bf69f52fecd00eda62dba2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s0-seed1.json` | 9.5 KB | `13d47e7c7272aaa73cc45613a146d604` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s0-seed2.json` | 9.5 KB | `f2dd9ec0a7b190f312ee764fddb0ab68` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s0-seed3.json` | 9.5 KB | `59da94d052dc8d2deddd65aa290f2142` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s0-seed4.json` | 9.5 KB | `11b41e80f7e9207683845c4b5a08b2fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s1-seed0.json` | 9.5 KB | `e876a218d72016718568f9c49bef12d7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s1-seed1.json` | 9.5 KB | `2a4ef2eaef9bab3d007697f931a779ab` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s1-seed2.json` | 9.5 KB | `c55829e3020040162dcb419f274d6693` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s1-seed3.json` | 9.5 KB | `0c912a715cfa22f31af767968ba880c6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s1-seed4.json` | 9.5 KB | `168c151507031656544a7238da986b08` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s2-seed0.json` | 9.5 KB | `481e791cf50cc764130bb0d12355bdfa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s2-seed1.json` | 9.5 KB | `d52d8649c9e619eaed216d76514234b1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s2-seed2.json` | 9.5 KB | `25aa3851f406cf66c4ec743f51cdd650` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s2-seed3.json` | 9.5 KB | `91cb4206d62ae63b08c4af572dce3a05` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s2-seed4.json` | 9.5 KB | `1463db29d5fda923ee0d74ee0980ce13` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s3-seed0.json` | 9.5 KB | `d8ced2c73c29dd2220dbfc57498be0a1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s3-seed1.json` | 9.5 KB | `8e106e189d5380c484847d683e4c4c37` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s3-seed2.json` | 9.5 KB | `332ac6d6bed2ebea11eecc8c4bded17e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s3-seed3.json` | 9.5 KB | `08c9c8e855179b5734c7f9cb59b2d29a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s3-seed4.json` | 9.5 KB | `13992778451412f25fc68bbc6db94780` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s4-seed0.json` | 9.5 KB | `9b6d58253b01a4a32384ccd8dea1e45e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s4-seed1.json` | 9.5 KB | `81e6ce37e1ab0b83cb63536c982ccd04` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s4-seed2.json` | 9.5 KB | `da9166449d45a762089bbf90673d1d17` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s4-seed3.json` | 9.5 KB | `c0a633be3b02adba1d3cc68b54750281` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f32/pose-loso-s4-seed4.json` | 9.5 KB | `206a9a30f9f7948e623275741beca76f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s0-seed0.json` | 9.5 KB | `6cfe89d4504fc7f8c061595ecac417cc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s0-seed1.json` | 9.5 KB | `aab88d500e6ddbe35b3c2828f1267c1d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s0-seed2.json` | 9.5 KB | `bd53d27fb25d88cc181e89e30e058386` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s0-seed3.json` | 9.5 KB | `ee31b0d65fdb1091a6efed44c28569fe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s0-seed4.json` | 9.5 KB | `3ac46c10892bea6a62201dfa47fe1148` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s1-seed0.json` | 9.5 KB | `d6c33cdaa7361666d3114edb260e20c6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s1-seed1.json` | 9.5 KB | `82de3a670c77111eb1edb51f11150205` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s1-seed2.json` | 9.5 KB | `420b26b79158026bae372b12956ebf6b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s1-seed3.json` | 9.5 KB | `7cd0ef852848d38073947070be4f2d48` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s1-seed4.json` | 9.5 KB | `5a9cb3ed4b9cfd7b8fcef2836435e10b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s2-seed0.json` | 9.5 KB | `a4ee3685bd71cddd441592315995dd0a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s2-seed1.json` | 9.5 KB | `4690178c7233252a54c55630d4709f77` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s2-seed2.json` | 9.5 KB | `a7f81fcacf503e0d89fd5983b8e4d051` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s2-seed3.json` | 9.5 KB | `eaec8d5c927ed428b3b3db2f3a146971` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s2-seed4.json` | 9.5 KB | `32242641d57a26eb90254b0476edad5a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s3-seed0.json` | 9.5 KB | `50ec84890c9f1abefcf5000d81b75e6b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s3-seed1.json` | 9.5 KB | `1417b249455479c5b8315e5a872b4831` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s3-seed2.json` | 9.5 KB | `3a24aaca18fbcca639a93197c913728a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s3-seed3.json` | 9.5 KB | `db3a902d4e07c1e4299f3bc873ec8e6d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s3-seed4.json` | 9.5 KB | `a8c2c5f7d9c907cf8b0364b6c8c63f60` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s4-seed0.json` | 9.5 KB | `1cb87d7014289da12cb0eb594af179e7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s4-seed1.json` | 9.5 KB | `8c7ea4e13654a61b0e63f94d06f75e2c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s4-seed2.json` | 9.5 KB | `f1fc51419825214c21c77e9cd100c456` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s4-seed3.json` | 9.5 KB | `07974e9c3abe60becf928ecc09f34406` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/frames/f48/pose-loso-s4-seed4.json` | 9.5 KB | `bf6d7c737ad6486e449923e994399096` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out0-val1.json` | 9.5 KB | `3a1ffb2e87dc50c0444a3c8f990295f8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out0-val2.json` | 9.5 KB | `c9d79b4bea8033abba4dfdb197b0f01e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out0-val3.json` | 9.5 KB | `d15bef3f7c20192e231eb5d6e701d9dd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out0-val4.json` | 9.5 KB | `f9696593c710527ca8e121a558031cc7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out1-val0.json` | 9.5 KB | `f0f2098a3ec4065f2a64406f3c50cc56` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out1-val2.json` | 9.5 KB | `0565e32f49a8d711b48e15713c23c541` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out1-val3.json` | 9.5 KB | `53b466ac487b3c1019b4b55f9437bed0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out1-val4.json` | 9.5 KB | `6405631859d811dbdc14d2eaa7f81160` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out2-val0.json` | 9.5 KB | `2f2abe9601aeebfe6d77a0840f15e7bf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out2-val1.json` | 9.5 KB | `b319ff412ce678d81b1141976828ed98` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out2-val3.json` | 9.5 KB | `427899a708b4298a0c6e8f839b6a5832` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out2-val4.json` | 9.5 KB | `a9e14bb902fd0aca01741de81f097e8b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out3-val0.json` | 9.5 KB | `bee48759c9c448ac24e78ffcd4db2503` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out3-val1.json` | 9.5 KB | `3596c827e8e4db820ed37a325e39dfa8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out3-val2.json` | 9.5 KB | `c72329eac66ffc9e50e5a73fc1a95f0a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out3-val4.json` | 9.5 KB | `419d769f0960aa0df323ba6c2096767c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out4-val0.json` | 9.5 KB | `bd187d78b03732d42e2ad4135e54f293` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out4-val1.json` | 9.5 KB | `8c097d68370bf21cc5c18a6148fbf6ea` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out4-val2.json` | 9.5 KB | `16318bd85df6617c9a2d9c0cb72c0047` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr1e-3-out4-val3.json` | 9.5 KB | `5e3ea5e1f83cf148784db949696732a1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out0-val1.json` | 9.5 KB | `6033da89fa527d81c0d93cd3e108f3d7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out0-val2.json` | 9.5 KB | `1427a81ea23ec64020bfa63915aa2648` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out0-val3.json` | 9.5 KB | `cd78a9640db4fd4c1cb43deb65cfa950` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out0-val4.json` | 9.5 KB | `6f991e0c3e28270428312d5446654b5a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out1-val0.json` | 9.5 KB | `5f7d86737f4bda768a93e888784ebb2e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out1-val2.json` | 9.5 KB | `20231c35f7c4156ee49d579a5cc04b27` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out1-val3.json` | 9.5 KB | `8d5b7f3432951b898fcce0390d2fd7b8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out1-val4.json` | 9.5 KB | `6ecc3af80e55e05f8afbbd5d9a31e1f3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out2-val0.json` | 9.5 KB | `44ff6bb111318e3b80d494ad79e6315a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out2-val1.json` | 9.5 KB | `efd839e5c3444e1efef2bea05cc86787` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out2-val3.json` | 9.5 KB | `16c7374c46109d63abcbcb316b6b281c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out2-val4.json` | 9.5 KB | `5df096bcb1810410cd8cec01c1f6add4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out3-val0.json` | 9.5 KB | `744cacc98ecbd69622e63432e6a3c8ab` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out3-val1.json` | 9.5 KB | `3d2cf535bfc753febf8f5f8c49432ffa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out3-val2.json` | 9.5 KB | `b599bca9668b08f24c81675b658cfc4f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out3-val4.json` | 9.5 KB | `0fd1da19121bb45b9ecc808d3e6101cf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out4-val0.json` | 9.5 KB | `5c49c29aa40d57503bcc506897710b19` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out4-val1.json` | 9.5 KB | `847701ddfaf063c8982a6d328fb72055` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out4-val2.json` | 9.5 KB | `cbfbbe2df4932c4e0698ed205e5f6949` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L2-lr5e-4-out4-val3.json` | 9.5 KB | `751e4359d64e6872a028d7d232102770` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out0-val1.json` | 9.5 KB | `f9c1bcdb71a4a8b563be9387ce4a51ad` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out0-val2.json` | 9.5 KB | `789d4036f392ce60a71cbaf1dccf2c1d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out0-val3.json` | 9.5 KB | `a7cfa623248db9b6e99e9ac0c4534765` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out0-val4.json` | 9.5 KB | `596a1ae3a7b563bd75c1afe751f8b288` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out1-val0.json` | 9.5 KB | `dc067a04201188116d567589e39b7e1b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out1-val2.json` | 9.5 KB | `7c7d6e33c6fab4a96f721619ab7dfba2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out1-val3.json` | 9.5 KB | `2a4a570ef857e00533e014dc09e34c6d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out1-val4.json` | 9.5 KB | `696a7ef5173cfedbfd67b82c892e385e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out2-val0.json` | 9.5 KB | `11e12b9473cbd57ba49c97cb51582e75` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out2-val1.json` | 9.5 KB | `d2f45fe49d7291dfd84921c812dbef70` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out2-val3.json` | 9.5 KB | `506bdc1df99b12456e97904a6bbada47` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out2-val4.json` | 9.5 KB | `86eee820f567611d57687901501f986e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out3-val0.json` | 9.5 KB | `7d080792838eed78ca8d3d672fbac0b4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out3-val1.json` | 9.5 KB | `49c8d57c96e8875bae68870011082488` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out3-val2.json` | 9.5 KB | `dc0c6bbc4212b079342d480996afba19` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out3-val4.json` | 9.5 KB | `1c1d2910d99d61e87b393300c3130dc3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out4-val0.json` | 9.5 KB | `1c305346b99b6ad6bbb752560f6ee1d3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out4-val1.json` | 9.6 KB | `e0793ade306c815cbe071a3fd0f0fc8e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out4-val2.json` | 9.5 KB | `f3f50e7c529e41b31a17091c2226199b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr1e-3-out4-val3.json` | 9.5 KB | `02afb85bdc58207aba85a2f08c4c6848` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out0-val1.json` | 9.5 KB | `2eb8bf93fbf72b28a40250a400cc9690` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out0-val2.json` | 9.5 KB | `8cb79b043fffa4c740d948cd501fd79f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out0-val3.json` | 9.5 KB | `3d1ca78cb75ce01fd9c5f2828f8606e6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out0-val4.json` | 9.5 KB | `d8f1520f17f0fa9884fff66eef748038` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out1-val0.json` | 9.5 KB | `2d20c15c96b09a35cc48f3d8ea7338c7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out1-val2.json` | 9.5 KB | `39118912a1f80b46834347d0fbbc8b08` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out1-val3.json` | 9.5 KB | `5997e079f8b379db2310cbd83c13acbc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out1-val4.json` | 9.5 KB | `f37ddf2ace722eb1166a86035fccfff0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out2-val0.json` | 9.5 KB | `425a02277168d397a09c121d89778070` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out2-val1.json` | 9.5 KB | `5af53255c532a3cc9660bb850f27286d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out2-val3.json` | 9.5 KB | `7cbdf096fe1a1d72fc44cf155c4e5553` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out2-val4.json` | 9.5 KB | `57be488b55074a482bbb2d7d9f68958f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out3-val0.json` | 9.5 KB | `c98c2e7e1a3bcae5141f40b04b520bf8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out3-val1.json` | 9.5 KB | `72f5a98e7771982dbde2250a62b26123` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out3-val2.json` | 9.5 KB | `5098c9f9be4b8769ce71f8368f64281d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out3-val4.json` | 9.5 KB | `7137eb0ee5c57932ea29eb6025a1e36a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out4-val0.json` | 9.5 KB | `81536303a979829f42a4df7181cee999` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out4-val1.json` | 9.5 KB | `9498177515879a261ceb3f4b38f45035` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out4-val2.json` | 9.5 KB | `4b6a2a15e92be0578cfc96dc774e585f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L3-lr5e-4-out4-val3.json` | 9.5 KB | `a997e0e12c1cc607b0e8dac7195dd1a0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out0-val1.json` | 9.5 KB | `ea488166ff683109c38f2a5a031a0776` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out0-val2.json` | 9.5 KB | `cdca1dcced41be901e1e68ffbde880af` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out0-val3.json` | 9.5 KB | `e727b8b4bc1b100b106a6c6caae655b6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out0-val4.json` | 9.5 KB | `ac8fbd7dd59e6c2c613a4ee41f9476bc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out1-val0.json` | 9.5 KB | `526fc9f89418aa84cbdc5b844b371acd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out1-val2.json` | 9.5 KB | `4782c62ec030e89a443e62bbc133085a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out1-val3.json` | 9.5 KB | `b284f8d757ac5628734e8b5a5000ab47` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out1-val4.json` | 9.5 KB | `9ae8bba43c18e052ce1bb3379cf32176` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out2-val0.json` | 9.5 KB | `6e6799c0519af6be5dd9b3808f7ed1c4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out2-val1.json` | 9.5 KB | `c248e905133f5d6af2f19b3ee9bd6cae` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out2-val3.json` | 9.5 KB | `fa7c6d35802093f6e399433c150d6f44` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out2-val4.json` | 9.5 KB | `a088bd9672578b693a0233a49866b2ee` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out3-val0.json` | 9.5 KB | `cb83623c425b06eca6b7549cbd8da862` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out3-val1.json` | 9.5 KB | `85396f55997046729b0cf39faed12b3c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out3-val2.json` | 9.5 KB | `140008093b856fd76b17ae1cf80ada2b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out3-val4.json` | 9.5 KB | `153d40cb0b9cc52999db329287b25542` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out4-val0.json` | 9.5 KB | `c1a3e277f1b9a42c246f30b8fd43f866` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out4-val1.json` | 9.5 KB | `3010ebaf7d2218ee716d3e427d8903e0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out4-val2.json` | 9.5 KB | `88c553267bdfddb4274c9802e4a0b740` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr1e-3-out4-val3.json` | 9.5 KB | `59379acf4c851c7f8d78ac30f0569404` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out0-val1.json` | 9.5 KB | `4ecb7227827f5dbfa771ddf425f08019` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out0-val2.json` | 9.5 KB | `ccb0c654f1b3842d11fb42a37d34843b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out0-val3.json` | 9.5 KB | `c4039f100a82064342bb5b994d3047b5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out0-val4.json` | 9.5 KB | `cb036512b9c06961665eedf16dd4fdbd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out1-val0.json` | 9.5 KB | `2f98b0ba19e5ea2d3abd1accb58d908d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out1-val2.json` | 9.5 KB | `c6da885506f87e785c0b843ce71f4d01` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out1-val3.json` | 9.5 KB | `3f86f466501182170a30b86c8580f98e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out1-val4.json` | 9.5 KB | `333eb3c33a18a143f59f488c3b0ff34d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out2-val0.json` | 9.5 KB | `e4c4cdbce62e3a000951a26894b9719b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out2-val1.json` | 9.5 KB | `16f06f5302fb04cefa88f665b57786fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out2-val3.json` | 9.5 KB | `8d5fe8bfbf951ab37749963c31e92ff2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out2-val4.json` | 9.5 KB | `b1584e643b63a27f06a43d1d58ab5bf1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out3-val0.json` | 9.5 KB | `7dfd6a02c39355e3de5764a75e6f0386` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out3-val1.json` | 9.5 KB | `bf10171dda3ff15ba28b40a9c4e0d4a3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out3-val2.json` | 9.5 KB | `d3f1a8dae36b5a32b040e79b9ed3a1fb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out3-val4.json` | 9.5 KB | `6641c46226b22c88eb99082bb7056c77` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out4-val0.json` | 9.5 KB | `ef3ab0d1f087c1c20f45e2a69f51dc3e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out4-val1.json` | 9.5 KB | `3d1d79d890232391fec39efc3df0fd15` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out4-val2.json` | 9.5 KB | `fda496c0294eef4944e7fc03e4969a40` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d128-L4-lr5e-4-out4-val3.json` | 9.5 KB | `f94ef4ef57425fb993b046dd8a33bbb0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out0-val1.json` | 9.5 KB | `6a6ed4a075595f22a59dcaef7b23092e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out0-val2.json` | 9.5 KB | `0f5f7b6a261f2d47f725bba026a08024` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out0-val3.json` | 9.5 KB | `7f51a4c1b2250e21cb5e03a86161353d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out0-val4.json` | 9.5 KB | `3dfe9d96c197870233d0a51b1fe5211b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out1-val0.json` | 9.5 KB | `57eb03b404282abaa4f27ed91f74c8b9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out1-val2.json` | 9.5 KB | `77b98242189c7bf12cb92e1c74c08a8d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out1-val3.json` | 9.5 KB | `a8482e123debe5ae22f8f30f50e366c2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out1-val4.json` | 9.5 KB | `49a4d9946391ac0ca47ae7104c48d8e6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out2-val0.json` | 9.5 KB | `e3ac43dc2526b89f774fa4d6a43a5101` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out2-val1.json` | 9.5 KB | `b6fc9af7610a1f0d4a023a8f10b07f30` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out2-val3.json` | 9.5 KB | `49077393b536fa5319637e946367b034` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out2-val4.json` | 9.5 KB | `167017d34cf7ab08700167194b8d1361` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out3-val0.json` | 9.5 KB | `8634ea7455f54b9272af6f15efc8d250` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out3-val1.json` | 9.5 KB | `5346cbf19e9c7673b83829773fdd71f2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out3-val2.json` | 9.5 KB | `76a3ec798a078f60eac55cc56d711941` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out3-val4.json` | 9.5 KB | `afc797416a3f26104d325648eeff014a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out4-val0.json` | 9.5 KB | `e4f21a48fff6b457d9bff96fefb51a02` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out4-val1.json` | 9.5 KB | `0610dc974ef7512a75b85f2e01f77660` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out4-val2.json` | 9.5 KB | `cc724e19ffb19889e5399cf39bce2bc7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr1e-3-out4-val3.json` | 9.5 KB | `b4c672dde61553f4863af6406864cc87` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out0-val1.json` | 9.5 KB | `427a6232f97677af9ee4c6e27622acb2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out0-val2.json` | 9.5 KB | `00e749fd6632f5fbd3610d515fc76d02` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out0-val3.json` | 9.5 KB | `f13e38dac522f06814c6da13fb891867` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out0-val4.json` | 9.5 KB | `910455e5538cc175cb98680a02c60995` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out1-val0.json` | 9.5 KB | `270f8676d54f8985c997888a767ff248` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out1-val2.json` | 9.5 KB | `849932b222fe3d91be3e94997d50b4da` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out1-val3.json` | 9.5 KB | `1c0b1bc72eadf4ce675a5f27e184479d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out1-val4.json` | 9.5 KB | `0062d78bd5dc8841fa332cc8c601040d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out2-val0.json` | 9.5 KB | `ce08da7305f806fe72d1d26f34fcf18e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out2-val1.json` | 9.5 KB | `362b40e5c830423ac4ca2b9923760211` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out2-val3.json` | 9.5 KB | `cea56d161d5a27badac0c292eece81a3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out2-val4.json` | 9.5 KB | `070601ff29b9a2051b0339de47b91f69` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out3-val0.json` | 9.5 KB | `6e3e9f8397f1890b1b56edcb698b46d6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out3-val1.json` | 9.5 KB | `02139b763b65f37c6e51a24fba32e920` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out3-val2.json` | 9.5 KB | `193f407d01d492f5cd4f24f58c9d60b6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out3-val4.json` | 9.5 KB | `25bf69a0a0b822bf5b7e9a8a092acfe3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out4-val0.json` | 9.5 KB | `f3e047054ecb4c72f31f2939919e993f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out4-val1.json` | 9.5 KB | `b71df2f1b42d5d901e009df6ea5c90a0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out4-val2.json` | 9.5 KB | `eab3a2fd53fdb5b9324296556e615d6b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L2-lr5e-4-out4-val3.json` | 9.5 KB | `5d6ba9d6d63e364edfdedfaadb586aff` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out0-val1.json` | 9.5 KB | `ef698993cb962b1c80414bd089d693ca` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out0-val2.json` | 9.5 KB | `84c6d93b6a5777bad4470c6a852e0ac3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out0-val3.json` | 9.5 KB | `56ba1356f76bcdfe9e2c306ca48112dd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out0-val4.json` | 9.5 KB | `c93f31fd880022eed5d0532e517099ed` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out1-val0.json` | 9.5 KB | `6c85bd8a9d7718cf9c9f379c2be7d9f6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out1-val2.json` | 9.5 KB | `4930c4267de8c5d1a37dfc5e2e6ad58e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out1-val3.json` | 9.5 KB | `1d17fdf61c58fa1d1068c09b7ebf06e4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out1-val4.json` | 9.5 KB | `c7fec625170a15b4e50f977e1bfcf3b7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out2-val0.json` | 9.5 KB | `136376cbd70d280f0eabba52ca85784a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out2-val1.json` | 9.5 KB | `78cd59532c07ada168acc8230a0e55f8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out2-val3.json` | 9.5 KB | `f18e7af3dcf6cc61ca206bad6a8f6a4b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out2-val4.json` | 9.5 KB | `3a83134c104a94d7b2a32e6806727c3c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out3-val0.json` | 9.5 KB | `78d5ae9b63d96ee4c170a5ae5aeffd23` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out3-val1.json` | 9.5 KB | `29ae1821cab3830341d1390b62dfe86b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out3-val2.json` | 9.5 KB | `cc79030236f05c8761b4df956e028335` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out3-val4.json` | 9.5 KB | `b4be925e9c5e4eb3aecc449dd22b44c6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out4-val0.json` | 9.5 KB | `6e869c6ece213a3e654d5f66238d6757` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out4-val1.json` | 9.5 KB | `17e595f238495fa3f79bb94512882f9c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out4-val2.json` | 9.5 KB | `5869bcfc74c118bdacd2e26e2c6092cf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr1e-3-out4-val3.json` | 9.5 KB | `b7fb3bc0ed376b27d29c33b77f2f622d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out0-val1.json` | 9.5 KB | `71d3307078da77e7c573fbab1f5f1ef3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out0-val2.json` | 9.5 KB | `0e0977ae28cf21021118f5cb96230466` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out0-val3.json` | 9.5 KB | `3c2a95a4e3acbcdf92a5769cc0f68dcd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out0-val4.json` | 9.5 KB | `0244e578907dc3154c71f127ee6ec7e3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out1-val0.json` | 9.5 KB | `3fa3e922a12905627fff66af24327148` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out1-val2.json` | 9.5 KB | `db51ca4f1d3266f2f6e50ba05a42bf30` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out1-val3.json` | 9.5 KB | `6c9afa7cad8d423fa07973d14a940158` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out1-val4.json` | 9.5 KB | `faf6090bd9ede86a73b6701e49324cf9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out2-val0.json` | 9.5 KB | `1eccf7ddc30459a42215f191f4265781` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out2-val1.json` | 9.5 KB | `9b8a7ef0349611f6736435e0a1e4d1d3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out2-val3.json` | 9.5 KB | `0abf98332f74dbf9c2fd13a4d3c21fd4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out2-val4.json` | 9.5 KB | `ee3a25bf5ec972729b4c6ce61fc2ce9a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out3-val0.json` | 9.5 KB | `55f402b9d9a4aed85c15189832fbb605` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out3-val1.json` | 9.5 KB | `1dea123b2a10876ca893d1dcaddcc30b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out3-val2.json` | 9.5 KB | `d95e9ce391586ead6a060f5edb6aec15` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out3-val4.json` | 9.5 KB | `c3e82cb4115e7d6dc49794a0c323e6c2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out4-val0.json` | 9.5 KB | `d8d350a92ecfc70ae434bd856a8c48b0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out4-val1.json` | 9.5 KB | `e01e7b9c223d028e2b93a96407419621` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out4-val2.json` | 9.5 KB | `0c0603a775f8c62c48e85938c1e985e8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L3-lr5e-4-out4-val3.json` | 9.5 KB | `3b6699e233511e2f6d6a000e70f32795` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out0-val1.json` | 9.5 KB | `1203b23a8ce76a91ebd1b01b0d53c9ba` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out0-val2.json` | 9.5 KB | `5cddca8821e585d7aad72e315eea391d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out0-val3.json` | 9.5 KB | `4effd86b7ab6c236e0cb51594bd6ff78` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out0-val4.json` | 9.5 KB | `fba9ad62f93bdf725fa39079c8989242` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out1-val0.json` | 9.5 KB | `eb20f1b7614e19097632eadda9bbd775` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out1-val2.json` | 9.5 KB | `5420c0e9c44f2914bc6f338e26409fad` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out1-val3.json` | 9.5 KB | `cb43333850982ac37921c5fdb8bb2a3f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out1-val4.json` | 9.5 KB | `f5b8c879284bfc483fbc5b17accf05b2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out2-val0.json` | 9.5 KB | `ca6b1b81ad81b6bdd7c8ff6e82644fa1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out2-val1.json` | 9.5 KB | `85228175a2084a57f7f1db6b0d551db3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out2-val3.json` | 9.5 KB | `e89226ff74c006a1f89f54b5bbeab118` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out2-val4.json` | 9.5 KB | `967de21889baeb69f1ecd0cf0fae48ea` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out3-val0.json` | 9.5 KB | `228bef1bd792ebd736cdd316a9393026` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out3-val1.json` | 9.5 KB | `d1e3acc49f956632369393c83ecd1602` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out3-val2.json` | 9.5 KB | `bbe1174d69108db8bbe7d415bccd6ede` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out3-val4.json` | 9.5 KB | `dc8d2be28db893bea3331827cad6c29f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out4-val0.json` | 9.5 KB | `e76b3c0763b85ebf0728537140f5dd71` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out4-val1.json` | 9.5 KB | `f65224cfe478e3d42aad5f2effc4cd6b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out4-val2.json` | 9.5 KB | `49564a0244690efbdeb8409989f4f757` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr1e-3-out4-val3.json` | 9.5 KB | `d32342738bab74f95f171304374a51f4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out0-val1.json` | 9.5 KB | `0eee72888720be938407ee2c945e0fc1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out0-val2.json` | 9.5 KB | `81be47125b6e10539377ff064f501cef` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out0-val3.json` | 9.5 KB | `ef1925c20c2b92733a2a3cacf604bf3f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out0-val4.json` | 9.5 KB | `bfdff832b4cb92d701c51f717bcdbe4c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out1-val0.json` | 9.5 KB | `7428d37d9d292822422f56ba3a69294b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out1-val2.json` | 9.5 KB | `271390d46c2c8aec95d3485f18791c1d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out1-val3.json` | 9.5 KB | `dd03e8500f1de943d897e433a84a7ca9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out1-val4.json` | 9.5 KB | `eba5ab0995b309e4e33fbd1706b6a173` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out2-val0.json` | 9.5 KB | `dbc76a4f0c1010946e8cacbe65dbb059` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out2-val1.json` | 9.5 KB | `9babd5f52838215a09cb59d2f69788ce` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out2-val3.json` | 9.5 KB | `665e827e5e48a15119cfa3c23ebefc36` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out2-val4.json` | 9.5 KB | `a00b468d32b5c1f64a6b32a152b9177e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out3-val0.json` | 9.5 KB | `6e82273eae30060058bc3f346bafb232` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out3-val1.json` | 9.5 KB | `f09ad2a1e31b097ceba7dbae5128afca` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out3-val2.json` | 9.5 KB | `7371e4efbf8b5e42a0279d095437b2e1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out3-val4.json` | 9.5 KB | `057d13236778d61353840ac471415e1a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out4-val0.json` | 9.5 KB | `34c8f5ad314dd7cd3f03a881544d7a83` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out4-val1.json` | 9.5 KB | `1ba9fa94c0c37da456248a26a056549d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out4-val2.json` | 9.5 KB | `65a92cf0cff0f6a758fc827044ddbacf` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d256-L4-lr5e-4-out4-val3.json` | 9.5 KB | `d1224c86d107693f0c89168a1aa2a4e5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out0-val1.json` | 9.5 KB | `2ab75721643117a7aa443c621a071604` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out0-val2.json` | 9.5 KB | `afb30e7e038b6923e1e77da8a26956e2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out0-val3.json` | 9.5 KB | `d03c16af24b2dc45be79c5599c98d11f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out0-val4.json` | 9.5 KB | `94381971c53c3a96d478bcaad81adb83` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out1-val0.json` | 9.5 KB | `3415ee0b01d6216fa0508fa7c33902ea` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out1-val2.json` | 9.5 KB | `5ff09e326c413cfebe56425a2312d349` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out1-val3.json` | 9.5 KB | `7b1d2f8275602dbf684874e796881e89` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out1-val4.json` | 9.5 KB | `7754afa0f712535a3aadee47687b8ec0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out2-val0.json` | 9.5 KB | `454cb0fa370aa7add65bbb5aef449651` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out2-val1.json` | 9.5 KB | `d963ece6de0d09aa5010f75381dbde3e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out2-val3.json` | 9.5 KB | `f1de755fd551c47571baf2acf815e2b9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out2-val4.json` | 9.5 KB | `c634bc4aa9e98c05a5540a60b4dad4fd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out3-val0.json` | 9.5 KB | `8b5c140ecdcf1b583c5785fd6dc3cecc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out3-val1.json` | 9.5 KB | `9abd2e8b06deea617f27403de9466b1d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out3-val2.json` | 9.5 KB | `f2ce7e7cfb22d02502b0822aff9f3023` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out3-val4.json` | 9.5 KB | `0e6ee029135c26794ccabac7f9f14f25` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out4-val0.json` | 9.5 KB | `2d8fe862b5ae1eae9821801c832e9779` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out4-val1.json` | 9.5 KB | `dd2b616e63da390f551a9d3113b2f2c1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out4-val2.json` | 9.5 KB | `601da1f96483b87bac297141333adf85` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr1e-3-out4-val3.json` | 9.5 KB | `34c1891ddf2d628311d74871ee1e9c69` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out0-val1.json` | 9.5 KB | `0fe8627661338fc1f36f09d624ccb18c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out0-val2.json` | 9.5 KB | `6ec7de81d19665cc087bb85e5df9fd16` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out0-val3.json` | 9.5 KB | `995db79d9c569123f9ae726697dcf1fa` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out0-val4.json` | 9.5 KB | `946937101ae38714f80f3f12e775422b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out1-val0.json` | 9.5 KB | `84d891580c06db77d203df1bafb867f8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out1-val2.json` | 9.5 KB | `504b76e17cca612f3bc28ca18ca07940` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out1-val3.json` | 9.5 KB | `0d8127231a74abd426b9f659fc5c6422` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out1-val4.json` | 9.5 KB | `190d29406869f21db31559bf71f090e6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out2-val0.json` | 9.5 KB | `57004c95f027c977804d9c22637fc321` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out2-val1.json` | 9.5 KB | `a483b7a7bedf827de3bb3bbdf38a2eef` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out2-val3.json` | 9.5 KB | `68207527a96c0e9f8b13974b7e32db48` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out2-val4.json` | 9.5 KB | `1beb5683370da7e0a44b6ecd1556a9b2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out3-val0.json` | 9.5 KB | `892ab5295aed84e6f0bde1f20eb82803` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out3-val1.json` | 9.5 KB | `bfed1d6af230ea13fe4ad551e3eebcfd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out3-val2.json` | 9.5 KB | `45e79e343db1c65620e41e548ee74a5d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out3-val4.json` | 9.5 KB | `20c7bd00ddb63fb31511be6fd098cc15` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out4-val0.json` | 9.5 KB | `ae9e16809b619a726dccf13fd5f9eaf5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out4-val1.json` | 9.5 KB | `b21036f151674ab482c7fc663be7b218` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out4-val2.json` | 9.5 KB | `81fb5b1e4dc56ea04bf2164425fb431d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L2-lr5e-4-out4-val3.json` | 9.5 KB | `f0619c33f3fa5a16a64c4784efed5bb6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out0-val1.json` | 9.5 KB | `81c788759250e497c91eabff14602d0f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out0-val2.json` | 9.5 KB | `e1bfad97161f7d6c66b029a97f7a284c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out0-val3.json` | 9.5 KB | `2d447e5673274ff31360291d8869d95c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out0-val4.json` | 9.5 KB | `d08289433d9165d0137eac23813f1991` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out1-val0.json` | 9.5 KB | `98595fd8aee94c0155f50af6ef342bd8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out1-val2.json` | 9.5 KB | `9ba54bee755f812e5f0a2598da1e471f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out1-val3.json` | 9.5 KB | `2aa3faa6b7a45f9e952a795d78c902ac` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out1-val4.json` | 9.5 KB | `fea42107a1d8f74844b1bd526becb8dc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out2-val0.json` | 9.5 KB | `d99b12c63e4a9b171749cc9dd98f96a9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out2-val1.json` | 9.5 KB | `f323c278e28f55661a3e64a5aa840f7b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out2-val3.json` | 9.5 KB | `d2b6fb924200fa8ac95dd16f74f92613` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out2-val4.json` | 9.5 KB | `5024585d99a447ad98b90020afa9b421` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out3-val0.json` | 9.5 KB | `11b98eadd9ece489c83b11364ff132b3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out3-val1.json` | 9.5 KB | `a32597305f56a3a211b8965ce560047c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out3-val2.json` | 9.5 KB | `a9cd7dcc3885ef4f14708363e737ccda` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out3-val4.json` | 9.5 KB | `750d8e584ff09c166cedd388c98c5ded` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out4-val0.json` | 9.5 KB | `e339e76f4d7550df727a0f40f3a4c98c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out4-val1.json` | 9.5 KB | `3609fedb989764821ebe4efc60196983` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out4-val2.json` | 9.5 KB | `2c01c661610103ac8f9b98ce3c8a2f4e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr1e-3-out4-val3.json` | 9.5 KB | `4570704b5decea702c90e6b56a8dffa0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out0-val1.json` | 9.5 KB | `bfd98289fc826f6dc946bce5c81f1c8b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out0-val2.json` | 9.5 KB | `74902731368cb5da782dbc0d14783ebe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out0-val3.json` | 9.5 KB | `f10ad189538a3c0d51223ccd31ba1ec5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out0-val4.json` | 9.5 KB | `4b59428481c2d7ed9af508737e09c098` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out1-val0.json` | 9.5 KB | `f8c9a44d9c3275539732a0a084b2ea89` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out1-val2.json` | 9.5 KB | `6759ce0eef7c1692daf7af47f556dd3e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out1-val3.json` | 9.5 KB | `a9f7bbc8c366b6e86195a3c769a330a3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out1-val4.json` | 9.5 KB | `a26e10b34642a37afc6a76048b8e44c7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out2-val0.json` | 9.5 KB | `f93b8371c5f969b5aa2fe084d8126f7f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out2-val1.json` | 9.5 KB | `91cd9cc829f92d48539b821d70241f96` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out2-val3.json` | 9.5 KB | `4070151210918d2c50c1bb8660a68595` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out2-val4.json` | 9.5 KB | `0e634db5d5662d15c5b5600c0805aad4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out3-val0.json` | 9.5 KB | `348c7c45abb873da6dba25547f2c5d7e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out3-val1.json` | 9.5 KB | `88225a2c38d34565a450f12c7cd6eaa0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out3-val2.json` | 9.5 KB | `e134bd3cbc926575db7e622c7190e766` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out3-val4.json` | 9.5 KB | `c8c22d1d91c90587494866388fe6bb72` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out4-val0.json` | 9.5 KB | `c0732d5557325e351ff6434340d4fcb9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out4-val1.json` | 9.5 KB | `e4544d4b4c58248906a616de4b69fa3a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out4-val2.json` | 9.5 KB | `f220c5039c30b96b6521ebe2cab8cf4b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L3-lr5e-4-out4-val3.json` | 9.5 KB | `172fa89e74f0b95974de70724ed82bc4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out0-val1.json` | 9.5 KB | `85b585c6bbd2634acda2ad5ac4b4f697` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out0-val2.json` | 9.5 KB | `8fe2252e1a347f72dcca48108be5e2c2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out0-val3.json` | 9.5 KB | `8ff6192bdeecbc7ffc8c6e8679af91ec` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out0-val4.json` | 9.5 KB | `d4d98e1d5c2d22e216fa398cc6ab24ba` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out1-val0.json` | 9.5 KB | `cdfb1d3248dfcc2be69cfebc65474169` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out1-val2.json` | 9.5 KB | `be6652a81cbe3d8bcf13f3b2e93318d2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out1-val3.json` | 9.5 KB | `375b3e375e7b5c0837a5cc9814fcd67f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out1-val4.json` | 9.5 KB | `83c0050b994b8d96418ecd5fe318cb4f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out2-val0.json` | 9.5 KB | `6b1e50bc9355b5a11488715849ef85d4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out2-val1.json` | 9.5 KB | `7582ecf22ebebd093644960f70673214` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out2-val3.json` | 9.5 KB | `73d4fc48d03335fc8ba930d9c62159ef` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out2-val4.json` | 9.5 KB | `024acf2294dd8a6b6ab36281b0cf5b5b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out3-val0.json` | 9.5 KB | `288d764b23de4ba1403433e7b88656e2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out3-val1.json` | 9.5 KB | `5ff25fb9606eede3cd88062167cf17d4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out3-val2.json` | 9.5 KB | `54b6f4a047593395cc085d6e189f30e4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out3-val4.json` | 9.5 KB | `5a38d5538a19d1a5d544bcc42335dc12` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out4-val0.json` | 9.5 KB | `6eee4d0bfdc67a1d27f0a05797c127e5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out4-val1.json` | 9.5 KB | `7527c83c4df727119609ef069c014964` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out4-val2.json` | 9.5 KB | `d56c79eaa2cfb7696a7408de22eb91f9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr1e-3-out4-val3.json` | 9.5 KB | `3df6d616adf343ed20ea33d27824eb82` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out0-val1.json` | 9.5 KB | `baf67935bcdb06cb32f8411615fd1679` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out0-val2.json` | 9.5 KB | `dcf8bf1a8e9cead698ceb5264388459d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out0-val3.json` | 9.5 KB | `88df975a603fdbc96efd1d7e3262cee8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out0-val4.json` | 9.5 KB | `a77ac0ee70311d624a40eec1da2440a8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out1-val0.json` | 9.5 KB | `b62837ffc4382099cf57b9d1f3a4a00c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out1-val2.json` | 9.5 KB | `50d51159ac27e1f3cad95ba19302de47` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out1-val3.json` | 9.5 KB | `cb3867d9575386525169ff4ade8acf5c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out1-val4.json` | 9.5 KB | `285b70b75ba4ace755b2cda42db52715` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out2-val0.json` | 9.5 KB | `fb3ab2bfb66c19d5d47ea5cd9f81042f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out2-val1.json` | 9.5 KB | `ba94f67532d2dba5270c680cfd1f530e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out2-val3.json` | 9.5 KB | `7a3912d26c1c7131522bcb51f1a53ba8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out2-val4.json` | 9.5 KB | `4b955c4f15134073be83818f7a325b98` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out3-val0.json` | 9.5 KB | `19dc6b51748e839fa2be7b5333673af7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out3-val1.json` | 9.5 KB | `d2d92269caaf15373910fefcc8cd6349` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out3-val2.json` | 9.5 KB | `8ce70ec60ab91430bed681e165ea3485` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out3-val4.json` | 9.5 KB | `99b52f625943d729b7c7db46857853fc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out4-val0.json` | 9.5 KB | `a12b8c32644a9a9c28fc676f7e50df13` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out4-val1.json` | 9.5 KB | `2932fca4404c23df0a40a02ecbb7eafe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out4-val2.json` | 9.5 KB | `5800a6c77e5c9ba9c275809eb598820b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/inner/d64-L4-lr5e-4-out4-val3.json` | 9.5 KB | `c7e5e9d4cfe9fb5245febe790d91570f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s0-seed0.json` | 9.5 KB | `659d1b2d4a5e809b742e005653986801` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s0-seed1.json` | 9.5 KB | `55eca94e8220dd540508678af16170b8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s0-seed2.json` | 9.5 KB | `cfb0be11ee4d8911020e4845dd6c9f1b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s0-seed3.json` | 9.5 KB | `e3ff6e8dc778a0806aca79f6112cdfb7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s0-seed4.json` | 9.5 KB | `4eb63f82df72cde1ce0c427df162cda1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s1-seed0.json` | 9.5 KB | `f23130c6b39fc0c368bdaeb703f457fb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s1-seed1.json` | 9.5 KB | `066ab2a60e083dfb8e137e7c5cfa9d18` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s1-seed2.json` | 9.5 KB | `8f13f95c18daa5007bcea8cae4e43887` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s1-seed3.json` | 9.5 KB | `42d81b27d2ac69f85d97027ee369cb06` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s1-seed4.json` | 9.5 KB | `f3737f39c834ccc95286291674cf4b7e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s2-seed0.json` | 9.5 KB | `79d7c4ec846d2fe23ca74cbcef829935` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s2-seed1.json` | 9.5 KB | `9b1853e805962e37f58cedd007ffd06c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s2-seed2.json` | 9.5 KB | `3f98e868b07a2d163992a3856b306789` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s2-seed3.json` | 9.5 KB | `5cb505f6157e799f93abeeb5bde5c480` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s2-seed4.json` | 9.5 KB | `1a3856496b6bb4e4606e48e7b5a68dd2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s3-seed0.json` | 9.5 KB | `509db054238dad2e2fc2f17ca4dc5cd6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s3-seed1.json` | 9.5 KB | `b0a50316866e4e478ddd9c05139eca76` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s3-seed2.json` | 9.5 KB | `a06c4921af4bf97ea631a367bc88ad0b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s3-seed3.json` | 9.5 KB | `1694bd5d4fa3d8e2b2df225348d74373` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s3-seed4.json` | 9.5 KB | `f7bb548b5b158b6218d4329c42043c32` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s4-seed0.json` | 9.5 KB | `8bea9185997a227b2f23d9d755184148` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s4-seed1.json` | 9.5 KB | `df1fcf0725e53a4c35ae5e922e8e71b5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s4-seed2.json` | 9.5 KB | `ad1d50bd422973a98ecbf070fba60ca3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s4-seed3.json` | 9.5 KB | `ebfdd431b99df672f7769bf26ad9251d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/nested/pose-loso-s4-seed4.json` | 9.5 KB | `e142bd7a6389da6f5861ce16046ef81d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr1e-3-s0.json` | 9.5 KB | `3b30f0625b59a7b42c37f64365fee16f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr1e-3-s1.json` | 9.5 KB | `7927378afc6bae1c01a71f1201c37014` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr1e-3-s2.json` | 9.5 KB | `b29db15443312561acad07d5e92125e7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr1e-3-s3.json` | 9.5 KB | `89cbcde01875239f45e701201646bfa8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr1e-3-s4.json` | 9.5 KB | `94b9ca9fc6c791122edc9b3a13653dbe` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr5e-4-s0.json` | 9.5 KB | `6d760fd5f0325a1a360823e683dd314e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr5e-4-s1.json` | 9.5 KB | `48676a6a3693410ae1c9b2c6276bcbfb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr5e-4-s2.json` | 9.5 KB | `9acabf608fde2e1105ac823afa0aa886` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr5e-4-s3.json` | 9.5 KB | `88c0265a0476fb4331d584ea608d6761` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L2-lr5e-4-s4.json` | 9.5 KB | `a5ddf95da6a56f7de24de142018b2968` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr1e-3-s0.json` | 9.5 KB | `90c3124152bb6bd303e6f8f2c2658878` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr1e-3-s1.json` | 9.5 KB | `5139ad9ff11fa4ff1ff00327e9294b2e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr1e-3-s2.json` | 9.5 KB | `554d75707e52bd3dc9b266bcd6f7bf21` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr1e-3-s3.json` | 9.5 KB | `a81c96c887b93534221a7d8bffd226db` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr1e-3-s4.json` | 9.5 KB | `adfbce6313cebd8d3b968b7292441b68` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr5e-4-s0.json` | 9.5 KB | `548ce848edef762f38e9868440417f43` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr5e-4-s1.json` | 9.5 KB | `6500f6fd6bf5cb6d10b36749f5455d9d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr5e-4-s2.json` | 9.5 KB | `d62353ac8f097e08cbf368d05ffd85e1` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr5e-4-s3.json` | 9.5 KB | `1f9e38bccd81e4e4f147bf0fc0b1db25` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L3-lr5e-4-s4.json` | 9.5 KB | `9ef42c8f6200d7c84063f0a47e20450f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr1e-3-s0.json` | 9.5 KB | `c6536be17e21ca74a26206d208d3c42f` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr1e-3-s1.json` | 9.5 KB | `c31ffd9719dee78394527294a02b6bbd` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr1e-3-s2.json` | 9.5 KB | `d12688e28b6d379df60f58a3053093d7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr1e-3-s3.json` | 9.5 KB | `9994aed1398edbb7a5c99c42a6d5cff0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr1e-3-s4.json` | 9.5 KB | `f40601e79ca6188f5ee6eb21e6050918` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr5e-4-s0.json` | 9.5 KB | `979f186a2259389b2cbb7d9d270ab24e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr5e-4-s1.json` | 9.5 KB | `2d7993f469b15ce71e9e5cd0b90b63e3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr5e-4-s2.json` | 9.5 KB | `bb4c0a79bf1bbd299a793b9bc1e3cf87` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr5e-4-s3.json` | 9.5 KB | `f59fda00dd6a839ad3551d53cb4095c2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d128-L4-lr5e-4-s4.json` | 9.5 KB | `62120ac626e31d83dde176c847263277` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr1e-3-s0.json` | 9.5 KB | `a03d72a7833773ee311e7f59a655a11b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr1e-3-s1.json` | 9.5 KB | `d5255ce3e4c820f869d7ad67903f51ef` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr1e-3-s2.json` | 9.5 KB | `a019a1a2acf586648435b24f7f137865` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr1e-3-s3.json` | 9.5 KB | `f3d945f8bf011c85e80e1be2d76248c6` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr1e-3-s4.json` | 9.5 KB | `02ec9035014a8adb4955a741524ae98c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr5e-4-s0.json` | 9.5 KB | `ef7a959591e757db8a8f37ad2a700ee3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr5e-4-s1.json` | 9.5 KB | `c0134376d7e2f473799589a95327c745` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr5e-4-s2.json` | 9.5 KB | `25f94bf52caad55274e7db810401ac03` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr5e-4-s3.json` | 9.5 KB | `880041a517996dc3fcf04766e175148d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L2-lr5e-4-s4.json` | 9.5 KB | `5215aeaab5fb071414c5edb08f96141a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr1e-3-s0.json` | 9.5 KB | `e4a74f68e878cc4d0301e49537b10b52` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr1e-3-s1.json` | 9.5 KB | `33d3c900cf4613aed319ad3b9b6ea389` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr1e-3-s2.json` | 9.5 KB | `ea7e3756d474dfec13b9446f451bb915` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr1e-3-s3.json` | 9.5 KB | `4d656b545c770cbc1353454ec0869995` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr1e-3-s4.json` | 9.5 KB | `3d0556889e1b6913fa8940e2c43bc616` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr5e-4-s0.json` | 9.5 KB | `6c25ef38c058ab4b41b9ed5903e35fd7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr5e-4-s1.json` | 9.5 KB | `8feb2f0ddff8dfda9c032c64d15e7fd2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr5e-4-s2.json` | 9.5 KB | `2189b215319fc4b5000fa6eb3eb25083` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr5e-4-s3.json` | 9.5 KB | `136c563ffc0c0e04954d7d77716ed9af` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L3-lr5e-4-s4.json` | 9.5 KB | `c336560d9a629da3167668476b248a0e` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr1e-3-s0.json` | 9.5 KB | `da2d3311688f88fce748a832060b7a04` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr1e-3-s1.json` | 9.5 KB | `c95018baf9feae3735986692bd0cdf96` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr1e-3-s2.json` | 9.5 KB | `80da5eccdff41e5cc7aef65e2f997730` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr1e-3-s3.json` | 9.5 KB | `4e4b754af8733e6656d54b5236f3d830` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr1e-3-s4.json` | 9.5 KB | `0fc7cc79761cc6c0427bb940e69fa100` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr5e-4-s0.json` | 9.5 KB | `fb4ff8c45a9bfe7c642ff814c4db74d4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr5e-4-s1.json` | 9.5 KB | `de63122219bcf38f09747bee05f62062` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr5e-4-s2.json` | 9.5 KB | `1ce281e8fccea7b0697660b610d049d9` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr5e-4-s3.json` | 9.5 KB | `e8d92a601e55ead1f564c46909f5661b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d256-L4-lr5e-4-s4.json` | 9.5 KB | `bcbe4f43b6cf871af0bad6b8508c09b8` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr1e-3-s0.json` | 9.5 KB | `85c5abd98c7179c4dc1f7d06a073bc56` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr1e-3-s1.json` | 9.5 KB | `de99b4a1341b5ac99c35c31ce0ea04eb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr1e-3-s2.json` | 9.5 KB | `eb06b517dfadc4e1af6ef95926993b24` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr1e-3-s3.json` | 9.5 KB | `519d3ff394baabd2e660fbcf6987d0be` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr1e-3-s4.json` | 9.5 KB | `a481fb3e86f8f69ecc714501c1ebbde4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr5e-4-s0.json` | 9.5 KB | `17f7c9882bb9fd1ed42cdddae300e604` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr5e-4-s1.json` | 9.5 KB | `abe77d95c963fb29a5b77d67956c9372` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr5e-4-s2.json` | 9.5 KB | `9db67b04190740a93fde7826b9d395bb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr5e-4-s3.json` | 9.5 KB | `1ca75f41d03a6d2d384913fc74cb4f20` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L2-lr5e-4-s4.json` | 9.5 KB | `3044d4254bde561f16d6bcbec0f0d3a0` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr1e-3-s0.json` | 9.5 KB | `a5d86209e4e68bb92b72e5d302d91685` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr1e-3-s1.json` | 9.5 KB | `a6a09ad4ab517659991e0272d4b624ad` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr1e-3-s2.json` | 9.5 KB | `e1f93609d85c115f22aedbcff3f69fae` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr1e-3-s3.json` | 9.5 KB | `28d7b402a731cb213e4c15a2442d7b80` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr1e-3-s4.json` | 9.5 KB | `ffa372cc09862b687646f8b356e521b7` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr5e-4-s0.json` | 9.5 KB | `00c83dff9416a0dc3495cbd2548ebf8b` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr5e-4-s1.json` | 9.5 KB | `cde5a9049220b0aad4ffec3d23aa92fb` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr5e-4-s2.json` | 9.5 KB | `a7d80c3deb49f32ee96972d5ec3883e5` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr5e-4-s3.json` | 9.5 KB | `8b463f5fce986189469b61f3f1a9cce4` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L3-lr5e-4-s4.json` | 9.5 KB | `88c5aba69cf21d0ef36dd8364101e1b3` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr1e-3-s0.json` | 9.5 KB | `7275c80c54d71413d6a4408f0f18b918` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr1e-3-s1.json` | 9.5 KB | `db968ad57af47809a2b9f02785613c45` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr1e-3-s2.json` | 9.5 KB | `64ccc047f4e8c38578f28e9487355a0c` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr1e-3-s3.json` | 9.5 KB | `f00e16fcb2ecab97d277c050614198d2` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr1e-3-s4.json` | 9.5 KB | `85c4b0b99936cac3475bb57cdf96ee23` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr5e-4-s0.json` | 9.5 KB | `80603b448f11d3bd9637733ae1602b81` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr5e-4-s1.json` | 9.5 KB | `e794ff5adaf3a56b301dace530cc608a` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr5e-4-s2.json` | 9.5 KB | `72dc2f427ae16c69994a829b44c619bc` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr5e-4-s3.json` | 9.5 KB | `0570f9e2a07cc813c0a6c3dcb1f97e8d` | 2026-11-18 (server paths anonymized) |
| `pose_study/runs/sensitivity/d64-L4-lr5e-4-s4.json` | 9.5 KB | `42a70e2cb630cbecb9caeff47ee27440` | 2026-11-18 (server paths anonymized) |
| `pose_study/stats/ci_ablations.csv` | 2.2 KB | `9018692b129f7d71357fed32bd3adab9` | 2026-10-23 09:07 |
| `pose_study/stats/ci_ablations.log` | 3.0 KB | `d74d7989eef48dcb9ad0f38210c0030b` | 2026-10-23 09:07 |
| `pose_study/stats/ci_frames.csv` | 1023 B | `fbc1a9998acf4825e96051f13f7a0f5b` | 2026-10-23 09:13 |
| `pose_study/stats/ci_frames.log` | 1.3 KB | `adfab8985c3579fd68a9f2403d403a53` | 2026-10-23 09:13 |
| `pose_study/stats/ci_nested.csv` | 576 B | `b0d14b8846cea9731aa4a4dc04363398` | 2026-10-23 08:56 |
| `pose_study/stats/ci_nested.log` | 690 B | `0df994f28043632cbfec44896854264c` | 2026-10-23 08:56 |
| `pose_study/stats/commit.txt` | 66 B | `faa751df186ea7c783b2f7e0456d1659` | 2026-10-23 08:53 |
| `pose_study/stats/pairs_ablations.csv` | 2.0 KB | `5594711438b322073636e8b822c11c42` | 2026-10-23 09:07 |
| `pose_study/stats/pairs_frames.csv` | 935 B | `b63527b61dc9e5a5425422bfbee2003e` | 2026-10-23 09:13 |
| `pose_study/stats/pairs_nested.csv` | 418 B | `a7c8fd3433560bd3e7a0bacc3536c027` | 2026-10-23 08:56 |
| `pose_study/stats/s1_nested.csv` | 499 B | `1b33d2b06d02224622b1f8ca26b9e00b` | 2026-10-23 08:53 |
| `pose_study/stats/s1_selected_configs.csv` | 371 B | `d4290680e456a7e86693d9ab85a10311` | 2026-10-23 08:53 |
| `pose_study/stats/s2_sensitivity.csv` | 2.4 KB | `4996298e53b87e892e921eadb97de17d` | 2026-10-23 08:53 |
| `pose_study/stats/s3_s4_variants.csv` | 2.5 KB | `13386698a4958231ad7efb462d643136` | 2026-10-23 08:53 |
| `pose_study/stats/s5_learning_curve.csv` | 604 B | `fdf917dcab2da49d0cf3535ae7fa2229` | 2026-10-23 08:53 |
| `pose_study/stats/summary.log` | 3.1 KB | `51df27fb0ae1857ff3815ebd9acc8cfd` | 2026-10-23 08:53 |
| `prediction_metrics/command.txt` | 2.5 KB | `ed5b0ea348ce05e991a59d6a58f3bbf6` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/commit.txt` | 223 B | `f58576222c63e9704d167fff986c39b6` | 2026-10-28 18:46 |
| `prediction_metrics/confusion_landmarks_tsfel_body_relative_rf_8020.csv` | 10.4 KB | `65b2c2a9b6cba3213274f88180b4a157` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_landmarks_tsfel_body_relative_rf_loso.csv` | 10.6 KB | `82be82fd2bd4bdb64c0cd7824b055344` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_late_fusion_slowfast_spoter_8020.csv` | 8.6 KB | `bae005ec8d759aba95baddd2ba207c3a` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_late_fusion_slowfast_spoter_loso.csv` | 12.0 KB | `1f095dec448fbf7b14bef77588e5d645` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_official_spoter_8020.csv` | 9.5 KB | `fc5704678b7f6565f0be8d152d58e561` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_official_spoter_loso.csv` | 10.6 KB | `abb7413c3f036aefe2fc6d3c1260179e` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_slowfast_r50_8020.csv` | 10.1 KB | `cc06ac6ce31287f1f0af135f7f9fd823` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/confusion_slowfast_r50_loso.csv` | 12.0 KB | `cf9eca94f0272301e588ac5d9a9e0067` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/metrics_runs.csv` | 115.4 KB | `2d2314a6d3031085391ad97f5b0fc3a9` | 2026-10-28 18:46 |
| `prediction_metrics/metrics_summary.csv` | 38.6 KB | `3d81f071b1868c8f4e903fac18eb1e16` | 2026-10-28 18:46 |
| `prediction_metrics/per_sign_f1.csv` | 32.0 KB | `36d27f1b6f54374ab7b617325f033779` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/prediction_metrics.log` | 7.6 KB | `96be7c01d5107a28173e187695ad35cb` | 2026-10-28 18:46 |
| `prediction_metrics/sign_names.json` | 843 B | `5989f9fd7c415d3015e2c927e04b5f19` | 2026-11-18 (server paths anonymized) |
| `prediction_metrics/top_confusions_loso.csv` | 3.6 KB | `aa3d3a839a21ab40b18d726a7b4fbae8` | 2026-11-18 (server paths anonymized) |
| `signer_ci/command.txt` | 2.3 KB | `3355a435327bd8aa8e541dccec652c9c` | 2026-11-18 (server paths anonymized) |
| `signer_ci/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-21 10:09 |
| `signer_ci/signer_ci.csv` | 5.9 KB | `27970ac949edfc01af37775d48f02136` | 2026-10-21 10:37 |
| `signer_ci/signer_ci.log` | 6.0 KB | `258630af024221775652638f77cd6548` | 2026-10-21 10:37 |
| `signer_ci/signer_pairs.csv` | 2.6 KB | `56c0446e33e2d8784d6fd0e4740d57e5` | 2026-10-21 10:37 |
| `signer_ci_final/command.txt` | 2.8 KB | `248dd33b13f5a262498cbc4ddc7a5a18` | 2026-11-18 (server paths anonymized) |
| `signer_ci_final/commit.txt` | 222 B | `94019ddb51d2044bbc69aa9f4f17b916` | 2026-10-27 13:35 |
| `signer_ci_final/signer_ci.csv` | 6.8 KB | `cb97f91cbd41e0c0935ad08df10133d0` | 2026-10-27 14:06 |
| `signer_ci_final/signer_ci.log` | 7.4 KB | `1b98f3f19df6b87dc9644af62a6b945c` | 2026-10-27 14:06 |
| `signer_ci_final/signer_pairs.csv` | 3.7 KB | `74a2bd21f68768dbda8fd921dc9df782` | 2026-10-27 14:06 |
| `signer_ci_v3/command.txt` | 2.3 KB | `b822abf9be2ab398221f4f665f9841c0` | 2026-11-18 (server paths anonymized) |
| `signer_ci_v3/commit.txt` | 184 B | `dc762a89f7e465c5ff6cfa06bf97d8c3` | 2026-10-21 21:03 |
| `signer_ci_v3/signer_ci.csv` | 5.9 KB | `111e8067ef9f2837de927b8d36932c88` | 2026-10-21 21:31 |
| `signer_ci_v3/signer_ci.log` | 6.0 KB | `d5841d4aca54cbfd22d90fef45d3af2f` | 2026-10-21 21:31 |
| `signer_ci_v3/signer_pairs.csv` | 2.6 KB | `462c363512b7a15a066732a2150ecf0e` | 2026-10-21 21:31 |
| `slowfast/meta.csv` | 25.2 KB | `ab648abc3d7275ba7ba4a1b02fabd373` | 2026-10-19 21:14 |
| `slowfast/run_slowfast.log` | 3.0 KB | `c0febe8302d9017ec0e3194d2f24455a` | 2026-10-22 18:12 |
| `slowfast/results/slowfast-8020-seed0-shuffled.json` | 4.3 KB | `46f39ff1445e36bc17554bc2b9177ea7` | 2026-10-22 18:12 |
| `slowfast/results/slowfast-8020-seed0.json` | 4.3 KB | `d27a523e8441362fef1627888c0c2b48` | 2026-10-22 09:57 |
| `slowfast/results/slowfast-8020-seed1.json` | 3.7 KB | `e052803584045da8ca3809c9116e017b` | 2026-10-22 13:48 |
| `slowfast/results/slowfast-8020-seed2.json` | 4.3 KB | `c28d5ed75b4b29ef21cf3f927b326318` | 2026-10-22 16:08 |
| `slowfast/results/slowfast-loso-s0-seed0-shuffled.json` | 4.3 KB | `f97da629cff3f2196427a4692cf436e6` | 2026-10-22 17:26 |
| `slowfast/results/slowfast-loso-s0-seed0.json` | 4.3 KB | `6bbbb6d8a4fe46bf194ebad8efc784bc` | 2026-10-22 04:56 |
| `slowfast/results/slowfast-loso-s0-seed1.json` | 4.3 KB | `de79ba332141c2c37ab1a18c085e9e48` | 2026-10-22 10:48 |
| `slowfast/results/slowfast-loso-s0-seed2.json` | 3.8 KB | `c90587d2dac5af7fdb617cfea9ac189e` | 2026-10-22 13:41 |
| `slowfast/results/slowfast-loso-s1-seed0.json` | 4.3 KB | `928810182f39c1fb53b17d24afac931d` | 2026-10-22 06:59 |
| `slowfast/results/slowfast-loso-s1-seed1.json` | 4.3 KB | `02303aebdfc59fa1e225ad84c50c9370` | 2026-10-22 10:32 |
| `slowfast/results/slowfast-loso-s1-seed2.json` | 4.3 KB | `cf274044eb9f663275825581140774c0` | 2026-10-22 14:16 |
| `slowfast/results/slowfast-loso-s2-seed0.json` | 4.3 KB | `3b1441cbca2f577ffaac6d31d70851da` | 2026-10-22 06:48 |
| `slowfast/results/slowfast-loso-s2-seed1.json` | 4.3 KB | `9411c03212a5e907aa897533f202952b` | 2026-10-22 11:21 |
| `slowfast/results/slowfast-loso-s2-seed2.json` | 3.7 KB | `36fe7102c09efdaa9dde246038f5b0b6` | 2026-10-22 15:13 |
| `slowfast/results/slowfast-loso-s3-seed0.json` | 3.7 KB | `5f48bbb5e3e202f37f6bfcf59e9345ee` | 2026-10-22 08:40 |
| `slowfast/results/slowfast-loso-s3-seed1.json` | 4.3 KB | `4458e47076c584bb0b99c726d02b11ae` | 2026-10-22 12:29 |
| `slowfast/results/slowfast-loso-s3-seed2.json` | 4.3 KB | `172baec29617cedead002c6484912c69` | 2026-10-22 15:58 |
| `slowfast/results/slowfast-loso-s4-seed0.json` | 3.7 KB | `4b38fba129af6996b130dc135647d957` | 2026-10-22 09:09 |
| `slowfast/results/slowfast-loso-s4-seed1.json` | 4.2 KB | `f2ed67126675bfd2335a73b94c41d01b` | 2026-10-22 12:24 |
| `slowfast/results/slowfast-loso-s4-seed2.json` | 4.3 KB | `5c2833f1649ac82b903237c9ba2ebca3` | 2026-10-22 16:36 |
| `slowfast_v2/commit.txt` | 361 B | `a1a0026d35257b9a8aaa2cf4094700c9` | 2026-10-23 09:23 |
| `slowfast_v2/final_jobs.txt` | 2.0 KB | `f4a9af2f87d1004198c003cd0a347ca9` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/run.log` | 4.7 KB | `99a77c8c11ca687101009e1d83fd8efa` | 2026-10-24 06:09 |
| `slowfast_v2/selected_lr.txt` | 6 B | `5f9b5d6e0cded1fa997ce119dfea1b70` | 2026-10-23 20:36 |
| `slowfast_v2/selection_jobs.txt` | 2.2 KB | `9a769ce24341b2ec68c0fe35b1a6edea` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/logs/slowfast-8020-seed0-shuffled.log` | 1.2 KB | `8e9d2b6d4f6db28ccad85b3c4f975fa0` | 2026-10-24 06:09 |
| `slowfast_v2/logs/slowfast-8020-seed0.log` | 1.2 KB | `e74e1acc5c719e7aff387147e217b2e0` | 2026-10-24 00:25 |
| `slowfast_v2/logs/slowfast-8020-seed1.log` | 1.2 KB | `93426371c0facb4bab92679757ec9b05` | 2026-10-24 02:20 |
| `slowfast_v2/logs/slowfast-8020-seed2.log` | 1.2 KB | `844344dcdaea93a86ee226194eb159a4` | 2026-10-24 06:06 |
| `slowfast_v2/logs/slowfast-loso-s0-seed0-shuffled.log` | 1.2 KB | `2daca1307cc6c473387d3ab4d6a51b3f` | 2026-10-24 06:08 |
| `slowfast_v2/logs/slowfast-loso-s0-seed0-val1-lr0.001.log` | 1.2 KB | `7e383e3cc0fe916764e9a732ec96c417` | 2026-10-23 14:05 |
| `slowfast_v2/logs/slowfast-loso-s0-seed0-val1-lr0.003.log` | 1.2 KB | `400eefef82ab9f016906d723c1117bf4` | 2026-10-23 12:18 |
| `slowfast_v2/logs/slowfast-loso-s0-seed0-val1-lr0.01.log` | 399 B | `397c58f04e57ef0090598125be80d8b1` | 2026-10-23 09:44 |
| `slowfast_v2/logs/slowfast-loso-s0-seed0.log` | 1.2 KB | `e19458d8d19cdddbf158210c950357ad` | 2026-10-23 22:28 |
| `slowfast_v2/logs/slowfast-loso-s0-seed1.log` | 1.2 KB | `807eca10a5d3fe9053e0808c6473f5af` | 2026-10-24 00:25 |
| `slowfast_v2/logs/slowfast-loso-s0-seed2.log` | 1.2 KB | `27005f35016565115fbe06a475126853` | 2026-10-24 04:06 |
| `slowfast_v2/logs/slowfast-loso-s1-seed0-val2-lr0.001.log` | 1.2 KB | `c8dddf6eef21b7c4cf7b857dc6f10dcf` | 2026-10-23 15:10 |
| `slowfast_v2/logs/slowfast-loso-s1-seed0-val2-lr0.003.log` | 1.2 KB | `0700f1257044a67355b6e94ee9bd204d` | 2026-10-23 12:31 |
| `slowfast_v2/logs/slowfast-loso-s1-seed0-val2-lr0.01.log` | 285 B | `bfe7963de837310e67447d2cbf004fe5` | 2026-10-23 09:36 |
| `slowfast_v2/logs/slowfast-loso-s1-seed0.log` | 1.2 KB | `0f6cf788f5cf26223da764149768a50a` | 2026-10-23 22:31 |
| `slowfast_v2/logs/slowfast-loso-s1-seed1.log` | 1.2 KB | `a595589e1e7f39e0feb8720163124516` | 2026-10-24 00:26 |
| `slowfast_v2/logs/slowfast-loso-s1-seed2.log` | 1.2 KB | `3924772cce8ee07385c54aba9b788e87` | 2026-10-24 04:12 |
| `slowfast_v2/logs/slowfast-loso-s2-seed0-val3-lr0.001.log` | 1.2 KB | `0f3f477276c088a7554e8b3107c03103` | 2026-10-23 15:23 |
| `slowfast_v2/logs/slowfast-loso-s2-seed0-val3-lr0.003.log` | 1.2 KB | `9f1a669c6eb799bfc2b3e55d3f8b4aa0` | 2026-10-23 12:39 |
| `slowfast_v2/logs/slowfast-loso-s2-seed0-val3-lr0.01.log` | 1.2 KB | `7f204ba8e702c19a41dfaa2fc391902b` | 2026-10-23 10:50 |
| `slowfast_v2/logs/slowfast-loso-s2-seed0.log` | 1.2 KB | `5c1d3af9cfa9f84c260a812304bd8b6c` | 2026-10-23 22:31 |
| `slowfast_v2/logs/slowfast-loso-s2-seed1.log` | 1.2 KB | `6a6143c251d3052e1e3fb8954592d35b` | 2026-10-24 02:14 |
| `slowfast_v2/logs/slowfast-loso-s2-seed2.log` | 1.2 KB | `7378c3e6e103a1c6d531054202bc7c8e` | 2026-10-24 04:14 |
| `slowfast_v2/logs/slowfast-loso-s3-seed0-val4-lr0.001.log` | 1.2 KB | `b8fc4a515c29dcfbe827315aae7415cb` | 2026-10-23 15:31 |
| `slowfast_v2/logs/slowfast-loso-s3-seed0-val4-lr0.003.log` | 1.2 KB | `1ff39d8cfabc67d251544432cf2249ef` | 2026-10-23 13:44 |
| `slowfast_v2/logs/slowfast-loso-s3-seed0-val4-lr0.01.log` | 1.2 KB | `de1b44cc223e1850d8667bbe24f845c5` | 2026-10-23 11:02 |
| `slowfast_v2/logs/slowfast-loso-s3-seed0.log` | 1.2 KB | `79c16d252cb9b601107b3a204c00152d` | 2026-10-23 22:31 |
| `slowfast_v2/logs/slowfast-loso-s3-seed1.log` | 1.2 KB | `6483f0db70cbddbc93a00c5ed1427694` | 2026-10-24 02:18 |
| `slowfast_v2/logs/slowfast-loso-s3-seed2.log` | 1.2 KB | `4c457bd9f25ca2b48d0045dd84b8c337` | 2026-10-24 04:14 |
| `slowfast_v2/logs/slowfast-loso-s4-seed0-val0-lr0.001.log` | 1.2 KB | `83b5b5dbf1f4cd87e75a70010b53a85c` | 2026-10-23 16:35 |
| `slowfast_v2/logs/slowfast-loso-s4-seed0-val0-lr0.003.log` | 1.2 KB | `3e6ff4cae265004e00cdc86fb49e7e54` | 2026-10-23 13:57 |
| `slowfast_v2/logs/slowfast-loso-s4-seed0-val0-lr0.01.log` | 1.2 KB | `60a251a3e16e9555ce1a9d35d75b8e80` | 2026-10-23 11:10 |
| `slowfast_v2/logs/slowfast-loso-s4-seed0.log` | 1.2 KB | `593df7d3c8821f3595edd8699c702e0d` | 2026-10-24 00:21 |
| `slowfast_v2/logs/slowfast-loso-s4-seed1.log` | 1.2 KB | `8867845ebbfd0dfa0d56ed4fbe3e18c9` | 2026-10-24 02:19 |
| `slowfast_v2/logs/slowfast-loso-s4-seed2.log` | 1.2 KB | `90fcd0e56ca214bdf13e6bf516ec8a47` | 2026-10-24 05:59 |
| `slowfast_v2/results/slowfast-8020-seed0-shuffled.json` | 4.5 KB | `6a66b094c88f1cd46ba0b4c219d3912b` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-8020-seed0.json` | 4.5 KB | `f290fa0ba8df6ead43c9368451bf421b` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-8020-seed1.json` | 4.5 KB | `4ba1e2de5d84092101d0439a78a07425` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-8020-seed2.json` | 4.5 KB | `1fe9ee1c837fcc691bf47c1f6e52555b` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s0-seed0-shuffled.json` | 4.4 KB | `aa8848aca6aa229db7fb090695d9b348` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s0-seed0.json` | 4.5 KB | `d271b5358aa65567586e0675ec704632` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s0-seed1.json` | 4.5 KB | `412b9efb84e9ebab9de8a5b548a98c11` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s0-seed2.json` | 4.5 KB | `aeb96506cdee01eabb793ee389e55d10` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s1-seed0.json` | 4.5 KB | `3de44e536d11c1d0f8913b5940d86cbf` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s1-seed1.json` | 4.5 KB | `a776fbbf86b277e415c26c7082eb21a2` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s1-seed2.json` | 4.5 KB | `bf7565b308aef347c1bd590b5ac73c0b` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s2-seed0.json` | 4.5 KB | `635dc9b41f9b5321c58df200fc9f9236` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s2-seed1.json` | 4.5 KB | `93fb7586ae2c0a7f1772624555455acf` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s2-seed2.json` | 4.5 KB | `8e7d6fe053a264f86d3860352df70c24` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s3-seed0.json` | 4.5 KB | `43b297e62ae3ac3f99b889245aa94d8c` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s3-seed1.json` | 4.5 KB | `657287739b26badc58bfb2e04907903f` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s3-seed2.json` | 4.5 KB | `0f6f089bee0a621ba76181cdc52a33b6` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s4-seed0.json` | 4.5 KB | `46dce31a35aa32c11ba9fae925518cef` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s4-seed1.json` | 4.5 KB | `d8b4ab703ec986e6a6b0d2189f9551cb` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/results/slowfast-loso-s4-seed2.json` | 4.5 KB | `51faf0b8b9bbe3c80ac8bf292c6869ea` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s0-seed0-val1-lr0.001.json` | 4.5 KB | `15a798d523c35bb3298c0b971e8e7cce` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s0-seed0-val1-lr0.003.json` | 4.5 KB | `61265ef2284c410ae006fb26922c4824` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s0-seed0-val1-lr0.01.json` | 2.6 KB | `6e47eabd981e10223d7e0beb1c706ae7` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s1-seed0-val2-lr0.001.json` | 4.5 KB | `3504fdfcd676d72ebc0d9db28baba722` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s1-seed0-val2-lr0.003.json` | 4.5 KB | `850671c5b46e70e8fce5eaf75c07d1e7` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s1-seed0-val2-lr0.01.json` | 2.3 KB | `f5e8f3f796f247f336ae5089dfb79d34` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s2-seed0-val3-lr0.001.json` | 4.5 KB | `1213e569d77b0bc12651819876386774` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s2-seed0-val3-lr0.003.json` | 4.5 KB | `19939c0483b85005f98d6cd388ccba97` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s2-seed0-val3-lr0.01.json` | 4.4 KB | `cf61c7e6d3eab77ea34151968fe9b0c8` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s3-seed0-val4-lr0.001.json` | 4.5 KB | `039f5ab831ffd04ee6870407fed306be` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s3-seed0-val4-lr0.003.json` | 4.5 KB | `2447595a3175b0c8ea4e30974d20ed6c` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s3-seed0-val4-lr0.01.json` | 4.5 KB | `eb661f711e0ca0bc1138e3887a96bae8` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s4-seed0-val0-lr0.001.json` | 4.5 KB | `539952c171b254daeb078cce804658fd` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s4-seed0-val0-lr0.003.json` | 4.5 KB | `620738154a9d0591ec1bab718daa5f5b` | 2026-11-18 (server paths anonymized) |
| `slowfast_v2/selection/slowfast-loso-s4-seed0-val0-lr0.01.json` | 4.4 KB | `5eb651db79ad0ebdaa7942969346ce04` | 2026-11-18 (server paths anonymized) |
| `spoter/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-23 20:58 |
| `spoter/commit.txt` | 238 B | `af80507922454a0c2ce2e2e36371c861` | 2026-10-23 09:11 |
| `spoter/jobs.txt` | 1.2 KB | `320e9a74720df5a206ea27f9c3fbe334` | 2026-10-23 09:11 |
| `spoter/run.log` | 3.7 KB | `79f4febc0a80616c1c6cb4716c8d5daa` | 2026-10-23 20:58 |
| `spoter/spoter-8020-seed0-shuffled.json` | 11.1 KB | `1fb17b728439d015c2650a29428a8d80` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-8020-seed0.json` | 11.1 KB | `d010580d43445b3c121ad236ce611ac5` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-8020-seed1.json` | 11.0 KB | `c30fa8ec12cbe7808c64093e8cdfa2f1` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-8020-seed2.json` | 10.7 KB | `b5f2a173b1e43785805d134fcbba3667` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-8020-seed3.json` | 11.0 KB | `f5a4bc665f28e7ddfe797791c66d634a` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-8020-seed4.json` | 11.0 KB | `94f7a709471e53b06f7652b6459bb8a6` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed0-shuffled.json` | 11.1 KB | `6eabfb4ccc820410dc1612c1f07d62f6` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed0.json` | 11.1 KB | `625a3822cee97bc6a658dad2b948b297` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed1.json` | 11.1 KB | `9c76fad20b5a9ec048b76aea95164cb2` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed2.json` | 11.1 KB | `3a618c0cc7b378b779d36ef9d1867014` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed3.json` | 11.0 KB | `c62a7d5613f0fc27e0f15ef05f7d75e6` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s0-seed4.json` | 11.1 KB | `d6250a55453d296345cc4426f5b4676b` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed0-shuffled.json` | 11.0 KB | `a3acb3e3f9e4cb4aa31de913f335aad4` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed0.json` | 11.1 KB | `416aa66a76b02d21d9c706d93983a291` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed1.json` | 11.1 KB | `0c86b0b9b60ae386b5b8fe59fb4ea45e` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed2.json` | 11.1 KB | `43dbeb358a9e217c011d7bda98a440f8` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed3.json` | 11.1 KB | `3b0d41bb7f0817313b819c48f4bc3c16` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s1-seed4.json` | 11.1 KB | `d877b6e8270a2b6cf6570446c17b60c2` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed0-shuffled.json` | 11.0 KB | `4714838de37b0e4858ac5408fb0e4cfd` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed0.json` | 11.1 KB | `f870219c6fdf84451b5cbe66bb95555b` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed1.json` | 11.1 KB | `c37cfbe030ff7750ba6f42f7bc7fdb16` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed2.json` | 11.0 KB | `a44f792500ab8e036eecf37df16223b8` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed3.json` | 11.1 KB | `d591311f6a43a1eeeef3cf0660a95151` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s2-seed4.json` | 10.9 KB | `0fbc601ddaeb2659f4a9137739d728a0` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed0-shuffled.json` | 11.1 KB | `748bccbce50412ddd8765bb85ead6c3a` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed0.json` | 10.7 KB | `d06ff00bcf828969ac0112f7fb562aa3` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed1.json` | 10.6 KB | `ba2298954cc07cbf8ccdb805de60773d` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed2.json` | 10.5 KB | `892eee1635a2730566caa5718e13edba` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed3.json` | 10.6 KB | `e88f3ef938c9de137ad5bb712eb99593` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s3-seed4.json` | 10.7 KB | `496eba25da5a3c7e22f9362687c6baaf` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed0-shuffled.json` | 11.1 KB | `ff62d46b9154192ec6df3089a1686337` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed0.json` | 11.1 KB | `d9dbd2f3cc49d532e4a61119fe0898ef` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed1.json` | 11.1 KB | `9e8a57eeb9472a5384ee3aad365882b0` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed2.json` | 11.1 KB | `07640c9911bbb42f1343bf5db3d0c6b7` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed3.json` | 11.1 KB | `c28edc3310d79ae3c4fc43f68f046a6d` | 2026-11-18 (server paths anonymized) |
| `spoter/spoter-loso-s4-seed4.json` | 11.1 KB | `70ec58f3d635cd734c1377a3bc97a625` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/STOPPED` | 95 B | `36330fd3ae0c87651175e79dc5404dfe` | 2026-10-20 10:24 |
| `stgcn_ntu_epochs/commit.txt` | 154 B | `bf8c4ccbb5e0d0c30e0b77536d2c017f` | 2026-10-19 19:43 |
| `stgcn_ntu_epochs/run.log` | 4.3 KB | `013fb173d6f502e337a93df2c8735cc6` | 2026-10-20 10:00 |
| `stgcn_ntu_epochs/bodynorm/stgcn-loso-s0-seed0.json` | 7.9 KB | `a39217213d4f4121cb939fe4a14ba57b` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/bodynorm/stgcn-loso-s1-seed0.json` | 7.9 KB | `4f789211948e8a302903c8ea1e1dbf4c` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/bodynorm/stgcn-loso-s2-seed0.json` | 7.9 KB | `91704c96cba9352f3f8783ee598a521f` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/bodynorm/stgcn-loso-s3-seed0.json` | 7.9 KB | `2b866a88f1f705a79842e7133ae8eeb4` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-8020-seed0.json` | 7.9 KB | `46e3bcbee1f55a34d3f218faa741f708` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-8020-seed1.json` | 7.8 KB | `a243b29510c5e3980fb3db3fa41e590e` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-8020-seed2.json` | 7.9 KB | `811d82d3e17184dd9f0e0db361befc99` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-8020-seed3.json` | 7.9 KB | `64ef81e53fb04535835376c83319c396` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-8020-seed4.json` | 7.8 KB | `2796ab0375bd20a9f5412844cb4fc868` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s0-seed0.json` | 7.8 KB | `991cf5b82ffd0aff2f0d7db77f8d95c9` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s0-seed1.json` | 7.9 KB | `df7785021f0c4546d41cb339b38624dc` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s0-seed2.json` | 7.8 KB | `e96c05d7c32d8e50ec18fcda92f98e93` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s0-seed3.json` | 7.9 KB | `a7f8c722a44b2f4558f19c335c3a1604` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s0-seed4.json` | 7.9 KB | `e6bbc94382647bcbf3cdd86623ae21b6` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s1-seed0.json` | 7.9 KB | `ce659f86faf5903c8367531f2869db3b` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s1-seed1.json` | 7.9 KB | `d9acb4bb9c51cbd75fcc2f5200043338` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s1-seed2.json` | 7.9 KB | `02189b00476a9fa1df409d51d427fdc8` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s1-seed3.json` | 7.9 KB | `0f115af64919c6bac2890e1ad3d1e5be` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s1-seed4.json` | 7.9 KB | `96e889b5bd48a61d2c536a6173c5671a` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s2-seed0.json` | 7.9 KB | `de5050418c173e92867f1bbb8574007b` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s2-seed1.json` | 7.9 KB | `dd2226ce89f0cf95dc069949ab5c6764` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s2-seed2.json` | 7.8 KB | `ef2af053a72819ec75e7592faf745a70` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s2-seed3.json` | 7.9 KB | `78015d1e4b5512fba512dd91b909bcfb` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s2-seed4.json` | 7.9 KB | `5c2663bc83a1f493dac6cd36763d220b` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s3-seed0.json` | 7.9 KB | `deb096a1163aa2931a7dc465e74fe451` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s3-seed1.json` | 7.8 KB | `864316eefe114a11d6d97fbaec1fbc01` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s3-seed2.json` | 7.9 KB | `d1fe414868dbde16b3a6e342f6c94b51` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s3-seed3.json` | 7.9 KB | `8fbc1ed0d62c7737d6d61f0d13086e81` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s3-seed4.json` | 7.9 KB | `d392444a085acaf9fbc89bcfa147f02f` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s4-seed0.json` | 7.8 KB | `9819a62aa5c64f69d73eb435fa29eb2a` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s4-seed1.json` | 7.8 KB | `37ce90eb18f62649c13f598acc006696` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s4-seed2.json` | 7.9 KB | `133d9b41cb067e7c3734561cb1337a9a` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s4-seed3.json` | 7.8 KB | `5597ce6f48d12d2700441dce972213c7` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image/stgcn-loso-s4-seed4.json` | 7.9 KB | `710fbbe09c24e5e45a894465d4e6e562` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-8020-seed0-shuffled.json` | 7.9 KB | `110fe97d34f785364c3d03bc11a812e4` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-loso-s0-seed0-shuffled.json` | 7.8 KB | `26eb2789d4304f4f6cbf47dda59d218d` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-loso-s1-seed0-shuffled.json` | 7.9 KB | `64d58fb75528ed82cd315e4c55d284ec` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-loso-s2-seed0-shuffled.json` | 7.8 KB | `0ea4c80e2ecfdf2234b6472117d2ea80` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-loso-s3-seed0-shuffled.json` | 7.8 KB | `cf76bb311c52af8056eafb9da49f106b` | 2026-11-18 (server paths anonymized) |
| `stgcn_ntu_epochs/image_control/stgcn-loso-s4-seed0-shuffled.json` | 7.9 KB | `220915a5544815663a6ed20ba3a04ec3` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/DONE` | 5 B | `678e5e019a79526d0fcca5e29f6e5f78` | 2026-10-20 19:44 |
| `stgcn_v2/commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-20 11:54 |
| `stgcn_v2/final_jobs.txt` | 11.6 KB | `6c1b780c46ebb41d78d9a7d5700a6bef` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/run.log` | 11.5 KB | `8b7f87c40da4f2dd8a8ef313a96b0e82` | 2026-10-20 19:44 |
| `stgcn_v2/selected_lr_bodynorm.txt` | 5 B | `14673621d9ed27dfa4fd8c2f42a43cd4` | 2026-10-20 13:01 |
| `stgcn_v2/selected_lr_image.txt` | 6 B | `976c55a570010b297cf125d68ac00451` | 2026-10-20 13:01 |
| `stgcn_v2/selection_jobs.txt` | 6.3 KB | `e151bd79401b377fb5e6e90bbbd58023` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-8020-seed0.json` | 17.2 KB | `7867edfd0489ec67fd02e1754b44f08c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-8020-seed1.json` | 17.1 KB | `c0d4d3666012577fb197b693201b0752` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-8020-seed2.json` | 17.1 KB | `4ec34be7fce9195bd9e777c75a5e3c7e` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-8020-seed3.json` | 17.2 KB | `911097c5ad3404c54ddb6b002fa06f6c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-8020-seed4.json` | 17.2 KB | `fd23b7a93ffdf81964c8fa1bd60f0dd1` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed0.json` | 17.1 KB | `d5a4bd7345747059c35dc1c9d4dc9e63` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed1.json` | 17.1 KB | `22d8e12f303d48e82d15c99973db9d2a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed2.json` | 17.1 KB | `eff3df95b7d6f60248599d94e88f82ec` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed3.json` | 17.2 KB | `ea920c177f20eb50398c3ee2b457ed18` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s0-seed4.json` | 17.1 KB | `20315871bed420c6599527f00089edee` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed0.json` | 17.2 KB | `136efc13f1d68137da1b87c240e9d5d6` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed1.json` | 17.2 KB | `a7649c257dd1d46fae4d55481f2a63bb` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed2.json` | 17.2 KB | `23bc09184b04973e20e088cb556139e0` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed3.json` | 17.2 KB | `c8b379f34a9d6e34b1fe93f04b91e991` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s1-seed4.json` | 17.2 KB | `50d0bfe6ef7a681d68770563352d8abe` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed0.json` | 17.2 KB | `f12c853e44b9426868a8e220865f9a9b` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed1.json` | 17.2 KB | `30cbce2aa3ee2de8e8ab51b8472d4cce` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed2.json` | 17.2 KB | `e5e78740b678274d192c7ceb9689a67a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed3.json` | 17.1 KB | `44f2d0039ba860d3f22447a4282e11d9` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s2-seed4.json` | 17.1 KB | `9ae3e072a79e2f41daaf90593a7d0828` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed0.json` | 17.2 KB | `4f6b5a83462d202088e4b88e7c99b4bc` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed1.json` | 17.1 KB | `a023fff940807d6363b3911296844ba6` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed2.json` | 17.1 KB | `40b0f48a5eaf09b90f21ca47831b2b28` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed3.json` | 17.2 KB | `8c2d95cccd2ee157407790a9fc5ae542` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s3-seed4.json` | 17.1 KB | `7afd27c0eb55b2adc0b881f0f41ac051` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed0.json` | 17.2 KB | `536e9ead232f8491b1cd7d3381084c5c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed1.json` | 17.1 KB | `626d035b86e7ce9c90b5404fc9e41991` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed2.json` | 17.1 KB | `1c5246bfbf9e943514ab1a67f24f9724` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed3.json` | 17.2 KB | `e41b132c57ab451e1cd17c3160151780` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm/stgcn-loso-s4-seed4.json` | 17.2 KB | `cb3eea8743220b4143ed32cde204ff2b` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-8020-seed0-shuffled.json` | 17.0 KB | `6aeecf891b3fbdf064753ca83d6a6ab7` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-loso-s0-seed0-shuffled.json` | 17.1 KB | `3ef9495f8e015027e5d5a1fe006f3dc4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-loso-s1-seed0-shuffled.json` | 17.0 KB | `4f4e3c06a8181398837090671b1a6dc8` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-loso-s2-seed0-shuffled.json` | 17.1 KB | `0b33534e8bb14f358102d98bd0febc1c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-loso-s3-seed0-shuffled.json` | 17.0 KB | `590e7d3c0c274d4e73f79ffdc8a5f442` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/bodynorm_control/stgcn-loso-s4-seed0-shuffled.json` | 17.0 KB | `6972c686e74bb6f2f9e27f0c36924294` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-8020-seed0.json` | 17.3 KB | `cff4d35076b5153af80fb2d49a5a5ad2` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-8020-seed1.json` | 17.3 KB | `bfe029879ec8758a2141467b0e4813ca` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-8020-seed2.json` | 17.3 KB | `4bfe841465a04ff1cbb2f19bff4e60ff` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-8020-seed3.json` | 17.3 KB | `3f68eba2c6bf414b54c046354117b201` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-8020-seed4.json` | 17.3 KB | `25aea1429375892625c6d3dd68950358` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s0-seed0.json` | 17.3 KB | `e9c9d4a2c0ebbeadb4af604ab8ede1a8` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s0-seed1.json` | 17.3 KB | `6f86c9052b66ae0ee1c7c1c815d179c6` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s0-seed2.json` | 17.3 KB | `629e008837d49ae4e2ebef489b95232a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s0-seed3.json` | 17.3 KB | `359d4e22e030a900e7a698fab55a2ea2` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s0-seed4.json` | 17.3 KB | `00ec23c8327cb83c82ae1ba14dfd09ce` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s1-seed0.json` | 17.4 KB | `74b1e6a57c7b8aa0f98269fd2a6cddcf` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s1-seed1.json` | 17.3 KB | `7cd3c66a279c166bc99a17d8b4e1feb3` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s1-seed2.json` | 17.3 KB | `5665d1aed3c7f113d282e3d6b1941756` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s1-seed3.json` | 17.3 KB | `70461ae7089a010c77d06757235a772c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s1-seed4.json` | 17.3 KB | `4e9877063511dd71b4e3754206dd5bca` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s2-seed0.json` | 17.3 KB | `1f8d06a46eae7c1a2ae1b292ee2f2bed` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s2-seed1.json` | 17.3 KB | `cbc73955e70c7d17d1fe426049c0e7f4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s2-seed2.json` | 17.3 KB | `eb03b32b5c5276c982ef70e60c4150ad` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s2-seed3.json` | 17.3 KB | `9401a527f82ed87cce3b79006500af0a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s2-seed4.json` | 17.3 KB | `fd62ef1eea9ac03dfd11df24fed8f76c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s3-seed0.json` | 17.3 KB | `6c53c99bb03f571f0033be99f5d96ad9` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s3-seed1.json` | 17.3 KB | `b85b403cda2e3771bc62a6bf4884b365` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s3-seed2.json` | 17.3 KB | `10e858f50a6ecc3aa9c898fde1b4e67b` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s3-seed3.json` | 17.3 KB | `637e0af65babc9b5537ecc8fe1dc65b7` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s3-seed4.json` | 17.3 KB | `eab84e33a7859aac7b1a87baa73c5f76` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s4-seed0.json` | 17.3 KB | `cd6d75f8c1681f3a806823f06f5ea86c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s4-seed1.json` | 17.3 KB | `45ee7617f046c2f0f2218b3911a8a754` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s4-seed2.json` | 17.3 KB | `9bfceb4d71641d37624017c565924ec4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s4-seed3.json` | 17.3 KB | `aea87006bdcab9553f06df2c83073111` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image/stgcn-loso-s4-seed4.json` | 17.3 KB | `9ce60aa9e2226d2d14bc8da00883eadb` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-8020-seed0-shuffled.json` | 17.2 KB | `dafbc80d4df240bc78c2e5f5d66c30fa` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-loso-s0-seed0-shuffled.json` | 17.2 KB | `0c44f3f6751a0e27720c5a467ea2dcf0` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-loso-s1-seed0-shuffled.json` | 17.2 KB | `fa0e2ce9639ddc1f83ce7f56b833b628` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-loso-s2-seed0-shuffled.json` | 17.2 KB | `4d5363d95df268add8a249936917f43b` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-loso-s3-seed0-shuffled.json` | 17.2 KB | `d632fd036f0064640c42e59344c72907` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/image_control/stgcn-loso-s4-seed0-shuffled.json` | 17.2 KB | `23a149c2a6707271b646b24b84dac82a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/logs/stgcn-8020-seed0-shuffled.log` | 128 B | `58ecb2b39fedd7ed3e01b4be98587050` | 2026-10-20 19:44 |
| `stgcn_v2/logs/stgcn-8020-seed0.log` | 119 B | `884eeb5bc1f26c748782a94c14f4cb75` | 2026-10-20 17:03 |
| `stgcn_v2/logs/stgcn-8020-seed1.log` | 119 B | `720dacf3a560b6a8a5716e6da3e318df` | 2026-10-20 17:30 |
| `stgcn_v2/logs/stgcn-8020-seed2.log` | 119 B | `5f2f85ffb0292cb437a2e696c789bc91` | 2026-10-20 18:08 |
| `stgcn_v2/logs/stgcn-8020-seed3.log` | 119 B | `76747e934f1b2bc0cddef5222ed02302` | 2026-10-20 18:37 |
| `stgcn_v2/logs/stgcn-8020-seed4.log` | 119 B | `ff4b64e263251f0ac3ed175d34c15b90` | 2026-10-20 19:13 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-shuffled.log` | 131 B | `915f834b689caeaca5bd1d42cadb562f` | 2026-10-20 19:19 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.01.log` | 134 B | `5f296951bafd93aa9750225e09978ea5` | 2026-10-20 12:45 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.025.log` | 135 B | `154451b51ca9023952868a5bf476e15e` | 2026-10-20 12:27 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0-val1-lr0.05.log` | 134 B | `97f6c0165a54e4d078853d65d94e6695` | 2026-10-20 12:10 |
| `stgcn_v2/logs/stgcn-loso-s0-seed0.log` | 122 B | `c6f415bd09fd3251e2cd5ba7e19456ab` | 2026-10-20 16:38 |
| `stgcn_v2/logs/stgcn-loso-s0-seed1.log` | 122 B | `4b8eddc302c97133c86014ae79f3aca2` | 2026-10-20 17:06 |
| `stgcn_v2/logs/stgcn-loso-s0-seed2.log` | 122 B | `917b2a80efea60ecb6ea2f37b88069b1` | 2026-10-20 17:42 |
| `stgcn_v2/logs/stgcn-loso-s0-seed3.log` | 122 B | `b71c59afa56bef401de3ab59efa90cb8` | 2026-10-20 18:13 |
| `stgcn_v2/logs/stgcn-loso-s0-seed4.log` | 122 B | `9b039fb4db09f5ad805b361cb6690a33` | 2026-10-20 18:47 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-shuffled.log` | 131 B | `e195e25b88d0ba060759c4197367281f` | 2026-10-20 19:22 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.01.log` | 134 B | `8c769b531017f25d16009ef0867037ca` | 2026-10-20 12:45 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.025.log` | 135 B | `34c168a1e05774c229326c469bff11ce` | 2026-10-20 12:28 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0-val2-lr0.05.log` | 134 B | `c9977bb45d700949368e6974bbd56aec` | 2026-10-20 12:11 |
| `stgcn_v2/logs/stgcn-loso-s1-seed0.log` | 122 B | `3a491f90bbd7a9446d7cc627ce1f4848` | 2026-10-20 16:41 |
| `stgcn_v2/logs/stgcn-loso-s1-seed1.log` | 122 B | `0e8484d8aa13bec09d6bee2e4ea71fef` | 2026-10-20 17:08 |
| `stgcn_v2/logs/stgcn-loso-s1-seed2.log` | 122 B | `5439ea59ee81af19f0f27bfcae2b48d2` | 2026-10-20 17:46 |
| `stgcn_v2/logs/stgcn-loso-s1-seed3.log` | 122 B | `f978b6c04b5de884712d31bca2025b29` | 2026-10-20 18:15 |
| `stgcn_v2/logs/stgcn-loso-s1-seed4.log` | 122 B | `5c67d2bccd620d47b3070aed88df5ff2` | 2026-10-20 18:51 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-shuffled.log` | 131 B | `af39e15f9c2ff4442ffcfe922cb5e052` | 2026-10-20 19:29 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.01.log` | 134 B | `f220580d4421106e19404698cdd4634d` | 2026-10-20 12:59 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.025.log` | 135 B | `70b79cb1a5e0490b04ee02cee62f0730` | 2026-10-20 12:28 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0-val3-lr0.05.log` | 134 B | `81d2fcd16c2382d7f1c527030671b5ee` | 2026-10-20 12:11 |
| `stgcn_v2/logs/stgcn-loso-s2-seed0.log` | 122 B | `94a71690363473cc7f98f911624df770` | 2026-10-20 16:44 |
| `stgcn_v2/logs/stgcn-loso-s2-seed1.log` | 122 B | `e1ff6aaab826c95f9fe449f9ecb7176d` | 2026-10-20 17:21 |
| `stgcn_v2/logs/stgcn-loso-s2-seed2.log` | 122 B | `f8fdd1865a152e3da18b9bcdcc07433c` | 2026-10-20 17:50 |
| `stgcn_v2/logs/stgcn-loso-s2-seed3.log` | 122 B | `5489f602931ca0b4e43c9b61b8eaa57e` | 2026-10-20 18:25 |
| `stgcn_v2/logs/stgcn-loso-s2-seed4.log` | 122 B | `98e0eecd85b52aaddb3f7ec32fa13b27` | 2026-10-20 18:57 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-shuffled.log` | 131 B | `7329d96d88afc15f1c22f845e9509422` | 2026-10-20 19:35 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.01.log` | 134 B | `ba3815a7d0bdd3bf08b636011b97a18a` | 2026-10-20 13:01 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.025.log` | 135 B | `ab1f9b14c43243649ac934b89a5a10e5` | 2026-10-20 12:42 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0-val4-lr0.05.log` | 134 B | `5a1599e713a3e752980b89615c7e3b66` | 2026-10-20 12:11 |
| `stgcn_v2/logs/stgcn-loso-s3-seed0.log` | 122 B | `0d677ed34894af830f73cb2adc753598` | 2026-10-20 16:46 |
| `stgcn_v2/logs/stgcn-loso-s3-seed1.log` | 122 B | `8195caabc80c12b0764b6c1d36ae1e2c` | 2026-10-20 17:25 |
| `stgcn_v2/logs/stgcn-loso-s3-seed2.log` | 122 B | `ee3d84ab4e5ca4c37eecbd897784537f` | 2026-10-20 17:53 |
| `stgcn_v2/logs/stgcn-loso-s3-seed3.log` | 122 B | `56547a191a755800d19bca6b57db934d` | 2026-10-20 18:30 |
| `stgcn_v2/logs/stgcn-loso-s3-seed4.log` | 122 B | `b57f83f09f5e762ba3e271b491bc7485` | 2026-10-20 18:59 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-shuffled.log` | 131 B | `968d0be49fe16c5d1919d083b923f853` | 2026-10-20 19:41 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.01.log` | 134 B | `91849c406efabeeb97b1b1bf70782c55` | 2026-10-20 13:01 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.025.log` | 135 B | `544750cc4d0d8e0da7c30cdc9262e946` | 2026-10-20 12:44 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0-val0-lr0.05.log` | 134 B | `6b1d3d447b8623cb1f6369650250ec5c` | 2026-10-20 12:26 |
| `stgcn_v2/logs/stgcn-loso-s4-seed0.log` | 122 B | `9b599eb18a5a6fb0c1a4fbba2e303962` | 2026-10-20 16:59 |
| `stgcn_v2/logs/stgcn-loso-s4-seed1.log` | 122 B | `04d11ba5562dcf0b25017cc5c31b434c` | 2026-10-20 17:28 |
| `stgcn_v2/logs/stgcn-loso-s4-seed2.log` | 122 B | `76e3b813018c5387a9a1198c772840f5` | 2026-10-20 18:04 |
| `stgcn_v2/logs/stgcn-loso-s4-seed3.log` | 122 B | `c6f60604a4dbb5e65c075bacdd645cae` | 2026-10-20 18:35 |
| `stgcn_v2/logs/stgcn-loso-s4-seed4.log` | 122 B | `cb296672f6835dbe522d2f8a38c6cbd1` | 2026-10-20 19:08 |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.01.json` | 15.7 KB | `8170255ad2d5c4cbdbaaa298843d90e4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.025.json` | 17.3 KB | `64123009bcb24af3e51d1936c3006442` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s0-seed0-val1-lr0.05.json` | 17.2 KB | `e872acace30f700d4fe4e27a8f9b9a2a` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.01.json` | 15.7 KB | `20914f2929d7623a68d158479e93f6c3` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.025.json` | 17.4 KB | `568b4d93a472b758574d986c330757e4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s1-seed0-val2-lr0.05.json` | 17.1 KB | `1548953ed195d31821cc7ac1c5557d46` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.01.json` | 15.7 KB | `828bee3faa342b692b36616cd6cc93f5` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.025.json` | 17.3 KB | `114e5d69a7ce9cc556282df1ec464b12` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s2-seed0-val3-lr0.05.json` | 17.1 KB | `43ab43ce746fd7a4651e0de065d5936c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.01.json` | 15.7 KB | `7a26821aa482dda03e93d98193f2aba6` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.025.json` | 17.3 KB | `6cedb351284f872284d6d594176788c8` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s3-seed0-val4-lr0.05.json` | 17.2 KB | `293d938442f340a7a33202d5e646be53` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.01.json` | 15.6 KB | `67cb81edfb065b483bfb7fd3be3c86f4` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.025.json` | 17.3 KB | `0c01a93c24ec998ca4a233701d1e5f5c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/bodynorm/stgcn-loso-s4-seed0-val0-lr0.05.json` | 17.1 KB | `50f22e4efd456597e2d9192f0324bca5` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.01.json` | 15.7 KB | `428c2fc1eedb3c713f81eb3b545fe6a8` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.025.json` | 17.3 KB | `c5d9f96e8a452255915844a8d64466fa` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s0-seed0-val1-lr0.05.json` | 17.1 KB | `74d6a94c585c723575fd9d3e7f1bf15c` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.01.json` | 15.7 KB | `d6f83999409cdfedc9fec29b87d488f5` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.025.json` | 17.3 KB | `666e8b8316f24f586974df2184414afa` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s1-seed0-val2-lr0.05.json` | 17.1 KB | `2aa822301e91b6452526f90772b06680` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.01.json` | 15.6 KB | `9fa79f76f7078334b13c2c352baa7180` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.025.json` | 17.3 KB | `75a635269ab1aaa2065257ff7cf3ca48` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s2-seed0-val3-lr0.05.json` | 17.1 KB | `3340a6d942d91a5234f5a3f8e899abc9` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.01.json` | 15.7 KB | `ecebebb65faeca04e9b0033be680f5c5` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.025.json` | 17.3 KB | `fe23cce7c5e2e580eb7e7d59ba720c6f` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s3-seed0-val4-lr0.05.json` | 17.1 KB | `233d26e75e3668f1f2fbb50e327a97b2` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.01.json` | 15.6 KB | `6d1a308f527a5cac10622e4fed0ffdb5` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.025.json` | 17.3 KB | `d2d3805ebe87deb888a489ad27c9fb1e` | 2026-11-18 (server paths anonymized) |
| `stgcn_v2/selection/image/stgcn-loso-s4-seed0-val0-lr0.05.json` | 17.1 KB | `bbd34ff6149210bf22b77b198d3fb6ba` | 2026-11-18 (server paths anonymized) |
| `summaries/pose_transformer_runs.commit.txt` | 100 B | `2b395677b84c03713d21edba7edbfe9a` | 2026-10-20 11:18 |
| `summaries/pose_transformer_runs.csv` | 12.2 KB | `adafc7f2ed8362081072fa5c98f605d2` | 2026-10-20 11:18 |
| `summaries/pose_transformer_runs_summary.csv` | 1.7 KB | `aecdf3f553372169f4b806d0b6e0c623` | 2026-10-20 11:18 |
| `summaries/slowfast_runs.commit.txt` | 238 B | `af80507922454a0c2ce2e2e36371c861` | 2026-10-23 09:12 |
| `summaries/slowfast_runs.csv` | 3.1 KB | `3ca42ca612b1e63ad831751764672355` | 2026-10-23 09:12 |
| `summaries/slowfast_runs_summary.csv` | 790 B | `3c9267c4ea261fc22a6d2887973fdf4a` | 2026-10-23 09:12 |
| `summaries/slowfast_v2_runs.commit.txt` | 221 B | `94689a97a575d3b16876d1aef4aa973e` | 2026-10-27 13:46 |
| `summaries/slowfast_v2_runs.csv` | 3.3 KB | `33a832c8a9a127da70bffc367fec13b0` | 2026-10-27 13:46 |
| `summaries/slowfast_v2_runs_summary.csv` | 791 B | `204495163f23b67ce1878aee2a3ca5ed` | 2026-10-27 13:46 |
| `summaries/spoter_runs.commit.txt` | 221 B | `94689a97a575d3b16876d1aef4aa973e` | 2026-10-27 13:46 |
| `summaries/spoter_runs.csv` | 6.1 KB | `e3b82678661df61148714ecf7fed7c30` | 2026-10-27 13:46 |
| `summaries/spoter_runs_summary.csv` | 980 B | `a8f98af15087a3d3b3522198a30b6736` | 2026-10-27 13:46 |
| `summaries/stgcn_ntu_epochs_runs.commit.txt` | 100 B | `2b395677b84c03713d21edba7edbfe9a` | 2026-10-20 11:18 |
| `summaries/stgcn_ntu_epochs_runs.csv` | 7.5 KB | `d311d5d04ccb488eacf67aa35d075e4e` | 2026-10-20 11:18 |
| `summaries/stgcn_ntu_epochs_runs_summary.csv` | 1.3 KB | `aaf88410fbf4ec0ae2c7eda0d1a4a98b` | 2026-10-20 11:18 |
| `summaries/stgcn_v2_runs.commit.txt` | 148 B | `0e164445f4f4da38c6485c089eafcbae` | 2026-10-21 10:09 |
| `summaries/stgcn_v2_runs.csv` | 13.2 KB | `f2248b6a3cf0d518fa11c0b26a235c37` | 2026-10-21 10:09 |
| `summaries/stgcn_v2_runs_summary.csv` | 1.9 KB | `bf2dfeae0e3370559c14ceb5ac49b271` | 2026-10-21 10:09 |
| `vivit/run_vivit.log` | 13.8 KB | `1d179c4035fd65afab0fdb07198fb8af` | 2026-10-23 08:52 |
| `vivit/vivit-8020-seed0/log_history.csv` | 2.5 KB | `58a57193da1d98d5350a4ec21a136a3b` | 2026-10-18 06:26 |
| `vivit/vivit-8020-seed0/results.json` | 2.7 KB | `97a6976490364c935138c3b565348c57` | 2026-10-18 06:27 |
| `vivit/vivit-8020-seed1/log_history.csv` | 2.5 KB | `b1ad1bb2d1cd212f0538a1371c5240b3` | 2026-10-19 08:01 |
| `vivit/vivit-8020-seed1/results.json` | 2.7 KB | `38a96517cfc0ca6a637a2c1ccc817cc6` | 2026-10-19 08:02 |
| `vivit/vivit-8020-seed2/log_history.csv` | 2.5 KB | `cda8d4523bf3585f902d6527bd400491` | 2026-10-20 12:18 |
| `vivit/vivit-8020-seed2/results.json` | 2.7 KB | `db712f27342ecd4fac6c0d74448c9751` | 2026-10-20 12:20 |
| `vivit/vivit-B-s0-seed0/log_history.csv` | 2.1 KB | `12ff9aecb90bf733ae0cd4586fdf3b3b` | 2026-10-18 23:38 |
| `vivit/vivit-B-s0-seed0/results.json` | 2.7 KB | `101e982f6523e32494174939e71052dd` | 2026-10-18 23:38 |
| `vivit/vivit-B-s0-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 03:02 |
| `vivit/vivit-B-s0-seed0-shuffled/log_history.csv` | 2.1 KB | `1bdbcb3acede453327abd69af5e327a6` | 2026-10-22 03:02 |
| `vivit/vivit-B-s0-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 03:02 |
| `vivit/vivit-B-s0-seed0-shuffled/results.json` | 2.8 KB | `a14a73ca6be259e250f9173af3611aaf` | 2026-10-22 03:03 |
| `vivit/vivit-B-s0-seed1/log_history.csv` | 2.1 KB | `a1f99579cbe207fe71130cfc1a67419a` | 2026-10-19 19:00 |
| `vivit/vivit-B-s0-seed1/results.json` | 2.7 KB | `a4147aed4a11a77427b8f31ae2fd15d4` | 2026-10-19 19:00 |
| `vivit/vivit-B-s0-seed2/log_history.csv` | 2.1 KB | `c31662d1c2d4da440901731c08de844b` | 2026-10-21 03:52 |
| `vivit/vivit-B-s0-seed2/results.json` | 2.8 KB | `3cfe65e43cf95f27d6f4aad338485ace` | 2026-10-21 03:53 |
| `vivit/vivit-B-s1-seed0/log_history.csv` | 2.1 KB | `0c1563c6c31131ad7526a5a2e81f705f` | 2026-10-19 03:23 |
| `vivit/vivit-B-s1-seed0/results.json` | 2.7 KB | `01a93470acb2e42a697fc0d15fd33ec5` | 2026-10-19 03:23 |
| `vivit/vivit-B-s1-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 07:44 |
| `vivit/vivit-B-s1-seed0-shuffled/log_history.csv` | 2.1 KB | `cf77bfeba615ad17a67371d7709e81e6` | 2026-10-22 07:44 |
| `vivit/vivit-B-s1-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 07:44 |
| `vivit/vivit-B-s1-seed0-shuffled/results.json` | 2.7 KB | `5b066f4ccd6962ff4cd1cb6d5359b7bb` | 2026-10-22 07:45 |
| `vivit/vivit-B-s1-seed1/log_history.csv` | 2.1 KB | `dff05332689ecf145483fee82d209a6e` | 2026-10-19 19:47 |
| `vivit/vivit-B-s1-seed1/results.json` | 2.7 KB | `e25bd4ef293077f92f3c8c0388064411` | 2026-10-19 19:47 |
| `vivit/vivit-B-s1-seed2/log_history.csv` | 2.1 KB | `4269f5dc1ed45da72608653c53006151` | 2026-10-21 03:32 |
| `vivit/vivit-B-s1-seed2/results.json` | 2.7 KB | `7a579a1c404a24fe5721053410636fe2` | 2026-10-21 03:33 |
| `vivit/vivit-B-s2-seed0/log_history.csv` | 2.1 KB | `cb03fd49df1276665b2758c8d26b04a7` | 2026-10-19 07:17 |
| `vivit/vivit-B-s2-seed0/results.json` | 2.8 KB | `c7ec08f80003e02ad1e4051259de6397` | 2026-10-19 07:18 |
| `vivit/vivit-B-s2-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 07:44 |
| `vivit/vivit-B-s2-seed0-shuffled/log_history.csv` | 2.1 KB | `f350d02ea20fbcc2077d018bd5e5b3d4` | 2026-10-22 07:44 |
| `vivit/vivit-B-s2-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 07:44 |
| `vivit/vivit-B-s2-seed0-shuffled/results.json` | 2.8 KB | `6049307dbd6ab288c79794d9cb0bc399` | 2026-10-22 07:46 |
| `vivit/vivit-B-s2-seed1/log_history.csv` | 2.1 KB | `391a533a95de75a3c1000a47c2729acc` | 2026-10-19 20:37 |
| `vivit/vivit-B-s2-seed1/results.json` | 2.7 KB | `b71455817992cee4714f865ffc886155` | 2026-10-19 20:38 |
| `vivit/vivit-B-s2-seed2/log_history.csv` | 2.1 KB | `8e74f8f6f3c0508f1a4fa4fdb8344d31` | 2026-10-21 09:20 |
| `vivit/vivit-B-s2-seed2/results.json` | 2.8 KB | `f5502ce96d320f35447e9788e2da7ca4` | 2026-10-21 09:21 |
| `vivit/vivit-B-s3-seed0/log_history.csv` | 2.1 KB | `b709ff956e09524746d4b9d0f5f3d918` | 2026-10-19 08:29 |
| `vivit/vivit-B-s3-seed0/results.json` | 2.7 KB | `bce0f7d829d7eba3ea21b8f243d491aa` | 2026-10-19 08:30 |
| `vivit/vivit-B-s3-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-22 04:51 |
| `vivit/vivit-B-s3-seed0-shuffled/log_history.csv` | 2.1 KB | `ce51e3eafe7123e196e2bc2bd6a9f33b` | 2026-10-22 04:51 |
| `vivit/vivit-B-s3-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-22 04:51 |
| `vivit/vivit-B-s3-seed0-shuffled/results.json` | 2.8 KB | `58ec7738bf2a681a14104007516021aa` | 2026-10-22 04:52 |
| `vivit/vivit-B-s3-seed1/log_history.csv` | 2.1 KB | `84a7ca42b8f30b5831ecf98e9a79fc5c` | 2026-10-20 00:07 |
| `vivit/vivit-B-s3-seed1/results.json` | 2.7 KB | `c8dc7e3b8e02b3b4ec527f4d07e7ab86` | 2026-10-20 00:08 |
| `vivit/vivit-B-s3-seed2/log_history.csv` | 2.1 KB | `b2335eecda9d80fff03d8fa850b7a33d` | 2026-10-21 11:23 |
| `vivit/vivit-B-s3-seed2/results.json` | 2.7 KB | `b955329718257522ecd7877968f31e8c` | 2026-10-21 11:25 |
| `vivit/vivit-B-s4-seed0/log_history.csv` | 2.1 KB | `2778beba94debb9519c54e2ea63d291b` | 2026-10-19 11:49 |
| `vivit/vivit-B-s4-seed0/results.json` | 2.7 KB | `1ddc187ec8a6be0d42101fdfe59844ce` | 2026-10-19 11:50 |
| `vivit/vivit-B-s4-seed0-shuffled/config.json` | 2.7 KB | `afbb7700120e9401f854f6a83b2d9783` | 2026-10-23 20:35 |
| `vivit/vivit-B-s4-seed0-shuffled/log_history.csv` | 2.1 KB | `b76a0fa693cc9d9a45d1383fe7b937d0` | 2026-10-23 20:35 |
| `vivit/vivit-B-s4-seed0-shuffled/preprocessor_config.json` | 418 B | `53e7bdfde61a3dd9bdf9c60419b339b4` | 2026-10-23 20:35 |
| `vivit/vivit-B-s4-seed0-shuffled/results.json` | 2.8 KB | `5b766eb23d4edd09712c04c8adc060f6` | 2026-10-23 20:36 |
| `vivit/vivit-B-s4-seed1/log_history.csv` | 2.1 KB | `a71dbb5396518431b2c2b8f512f72327` | 2026-10-20 06:54 |
| `vivit/vivit-B-s4-seed1/results.json` | 2.7 KB | `a6124c5e4fc97a1ca397eb0b0a794b89` | 2026-10-20 06:55 |
| `vivit/vivit-B-s4-seed2/log_history.csv` | 2.1 KB | `3f3d55c7d372ec5f9ba1081bc681573a` | 2026-10-21 15:10 |
| `vivit/vivit-B-s4-seed2/results.json` | 2.7 KB | `d5b62b5ca65f094e8b6afde53de04b82` | 2026-10-21 15:11 |
| `vivit/vivit-s0-seed0/log_history.csv` | 5.4 KB | `78cd3c022a1665bdf151f4f29870c750` | 2026-10-18 01:36 |
| `vivit/vivit-s0-seed0/results.json` | 2.8 KB | `a0a48781e0a22a6df1e31d59d430c942` | 2026-10-18 01:37 |
| `vivit/vivit-s0-seed1/log_history.csv` | 5.5 KB | `b1e43b6230ca163d35bb41be63989604` | 2026-10-18 11:08 |
| `vivit/vivit-s0-seed1/results.json` | 2.8 KB | `7112e07bbf03665b427c9fbfeee7a832` | 2026-10-18 11:08 |
| `vivit/vivit-s0-seed2/log_history.csv` | 5.4 KB | `d7b24b79e805d22d0cb99fda7c14f846` | 2026-10-20 05:02 |
| `vivit/vivit-s0-seed2/results.json` | 2.8 KB | `4e2a65e2f9271003cbf79ae29c7b3117` | 2026-10-20 05:03 |
| `vivit/vivit-s1-seed0/log_history.csv` | 5.4 KB | `a2e5734ddd9e3b2b8fa03158e223da56` | 2026-10-18 02:01 |
| `vivit/vivit-s1-seed0/results.json` | 2.8 KB | `5e59b6cf85080123e4e4ab7ac1af9910` | 2026-10-18 02:02 |
| `vivit/vivit-s1-seed1/log_history.csv` | 5.4 KB | `5e61a7b6140f4a1b7c23225804881845` | 2026-10-18 11:24 |
| `vivit/vivit-s1-seed1/results.json` | 2.8 KB | `5d718aa89a90949e3042b73631531201` | 2026-10-18 11:25 |
| `vivit/vivit-s1-seed2/log_history.csv` | 5.4 KB | `a088b741f3cd4d9cd6f028fedb978729` | 2026-10-20 06:09 |
| `vivit/vivit-s1-seed2/results.json` | 2.8 KB | `fbf6444e3137b524cdb6393d8edc46fa` | 2026-10-20 06:10 |
| `vivit/vivit-s2-seed0/log_history.csv` | 5.4 KB | `c2f7a5c32a3bd514811fbf1691b2f458` | 2026-10-18 01:53 |
| `vivit/vivit-s2-seed0/results.json` | 2.8 KB | `b850f99899a725866c6d2c580bdb908b` | 2026-10-18 01:54 |
| `vivit/vivit-s2-seed1/log_history.csv` | 5.4 KB | `260a715309e05bc5bd6eaf1073080014` | 2026-10-18 15:32 |
| `vivit/vivit-s2-seed1/results.json` | 2.7 KB | `3913a4dba9c34558e69eb53976957d1a` | 2026-10-18 15:33 |
| `vivit/vivit-s2-seed2/log_history.csv` | 5.4 KB | `38286330982bc1d84148584c1bdab32e` | 2026-10-20 09:49 |
| `vivit/vivit-s2-seed2/results.json` | 2.8 KB | `f1f16e7604950a295cefd352d3fd60e6` | 2026-10-20 09:49 |
| `vivit/vivit-s3-seed0/log_history.csv` | 5.4 KB | `b4c7966a1362403f8aea42bfbdc3a1ee` | 2026-10-18 01:48 |
| `vivit/vivit-s3-seed0/results.json` | 2.8 KB | `695107916ca15ff8143de8f1ca7bff8f` | 2026-10-18 01:48 |
| `vivit/vivit-s3-seed1/log_history.csv` | 5.4 KB | `a0dc3801ea5c1416b9ea6a3d57d08381` | 2026-10-18 19:37 |
| `vivit/vivit-s3-seed1/results.json` | 2.8 KB | `28d9914f70525469a5f36e05378a7103` | 2026-10-18 19:38 |
| `vivit/vivit-s3-seed2/log_history.csv` | 5.5 KB | `d6a5548aa8ec4dc72f4164e5cf29cd3f` | 2026-10-20 17:52 |
| `vivit/vivit-s3-seed2/results.json` | 2.8 KB | `3455065ae08c00a302aef0f51d2091c3` | 2026-10-20 17:53 |
| `vivit/vivit-s4-seed0/log_history.csv` | 5.5 KB | `8749c84aff5c4b2f8f668077f17b8431` | 2026-10-18 10:36 |
| `vivit/vivit-s4-seed0/results.json` | 2.8 KB | `57ce9fd9aaf81eb23c12778267dba9aa` | 2026-10-18 10:37 |
| `vivit/vivit-s4-seed1/log_history.csv` | 5.4 KB | `d4db56232a10766310b839da9933b5fc` | 2026-10-18 20:23 |
| `vivit/vivit-s4-seed1/results.json` | 2.8 KB | `5150fbe0721d2c572dc5a5be21f6cb8a` | 2026-10-18 20:23 |
| `vivit/vivit-s4-seed2/log_history.csv` | 5.4 KB | `1611bdeabb675ae57270c2f0f862beb1` | 2026-10-20 20:08 |
| `vivit/vivit-s4-seed2/results.json` | 2.8 KB | `c4b8fcc985fb70bc09fa675aa6e2f530` | 2026-10-20 20:09 |

### Repository figures (PNG): `docs/figures`

Generated 2026-10-28 18:52. 8 files listed; 0 bulk groups summarized.

| File | Size | MD5 | Modified |
|------|------|-----|----------|
| `fig_confusion_fusion.png` | 287.1 KB | `31194dd8d1d8c71ced86308cf65f0e0b` | 2026-10-28 18:46 |
| `fig_dtw_matrix.png` | 95.7 KB | `f155b5e84f99df75ab29db108261f629` | 2026-10-27 14:06 |
| `fig_importance.png` | 163.3 KB | `b2d96fb7abd5d042186c9c72f193c79d` | 2026-10-27 14:06 |
| `fig_importance_pose.png` | 65.9 KB | `ff24d3ed778af14ac94c91f30f5427d1` | 2026-10-27 14:06 |
| `fig_learning_curves.png` | 245.8 KB | `36021dc939a0d4de314c25510ef51ac9` | 2026-10-27 14:06 |
| `fig_loso_models.png` | 488.9 KB | `ad9110d11780f4b0ca4d2353810b987f` | 2026-10-27 14:06 |
| `fig_loso_per_signer.png` | 96.6 KB | `a681080b512c29393e6f8aaa5378905d` | 2026-10-27 14:06 |
| `fig_per_sign_f1.png` | 255.9 KB | `e0ddf95113ac0ef5e14342dcbae358db` | 2026-10-28 18:46 |
