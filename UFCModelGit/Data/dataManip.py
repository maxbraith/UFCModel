#imports
import pandas as pd
import csv

#create dataframes
df = pd.read_csv('tapology_scrape.csv')
df2 = pd.read_csv('ufc_history_fight_statistics.csv')

#history/df2 does not include UFC 1 so it will be removed from tap/df
df = df[df['event'] != 'UFC 1: The Beginning']

#match event names between dataframes
df['event'] = df['event'].replace('UFC Fight Night 5: Leben vs. Silva', 'UFC Fight Night 5', regex=True)
df['event'] = df['event'].replace('UFC Fight Night 6: Sanchez vs Parisyan', 'UFC Fight Night 6', regex=True)
df['event'] = df['event'].replace('UFC Fight Night 25: Battle on the Bayou', 'UFC Fight Night: Shields vs Ellenberger', regex=True)
df['event'] = df['event'].replace('UFC Fight Night: Holloway vs. Korean Zombie', 'UFC Fight Night: Holloway vs. The Korean Zombie', regex=True)
df['event'] = df['event'].replace('UFC on FX 6: Sotiropoulos vs. Pearson', 'UFC on FX: Sotiropoulos vs Pearson', regex=True)
df['event'] = df['event'].replace('UFC Fight Night 67: Condit vs. Alves', 'UFC Fight Night: Condit vs Alves', regex=True)
df['event'] = df['event'].replace('The Ultimate Fighter 23 Finale', 'The Ultimate Fighter: Team Joanna vs. Team Cláudia Finale', regex=True)
df['event'] = df['event'].replace("UFC 270: N'Gannou vs. Gane", 'UFC 270: Ngannou vs. Gane', regex=True)
df['event'] = df['event'].replace("UFC Fight Night 141: Blaydes vs. N'Gannou 2", 'UFC Fight Night: Blaydes vs. Ngannou 2', regex=True)
df['event'] = df['event'].replace('UFC on FUEL TV 3: Korean Zombie vs. Poirier', 'UFC on FUEL TV: Korean Zombie vs Poirier', regex=True)
df['event'] = df['event'].replace('UFC on ESPN+ 22: Blachowicz vs. Jacare', 'UFC Fight Night: Blachowicz vs. Jacare', regex=True)
df['event'] = df['event'].replace('UFC on FOX 5: Henderson vs. Diaz', 'UFC on FOX: Henderson vs Diaz', regex=True)
df['event'] = df['event'].replace('UFC Fight Night 40: Brown vs. Silva', 'UFC Fight Night: Brown vs Silva', regex=True)
df['event'] = df['event'].replace('UFC 257: Poirier vs. McGregor 2', 'UFC 257: Poirier vs. McGregor', regex=True)
df['event'] = df['event'].replace('UFC on FX 5: Browne vs. Silva', 'UFC on FX: Browne vs Bigfoot', regex=True)
df['event'] = df['event'].replace("UFC Fight Night 58: Machida vs. Dollaway", "UFC Fight Night: Machida vs Dollaway", regex=True)
df['event'] = df['event'].replace("UFC on FOX 27: Jacare vs. Brunson 2", "UFC Fight Night: Jacare vs. Brunson 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 77: Belfort vs. Henderson 3", "UFC Fight Night: Belfort vs Henderson 3", regex=True)
df['event'] = df['event'].replace("UFC 273: Volkanovski vs. Korean Zombie", "UFC 273: Volkanovski vs. The Korean Zombie", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 18: Condit vs. Kampmann", "UFC Fight Night: Condit vs Kampmann", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 95: Cyborg vs. Lansberg", "UFC Fight Night: Cyborg vs. Lansberg", regex=True)
df['event'] = df['event'].replace("UFC 295: Procházka vs. Pereira", "UFC 295: Prochazka vs. Pereira", regex=True)
df['event'] = df['event'].replace("UFC 121: Lesnar vs. Velasquez", "UFC 121: Lesnar vs Velasquez", regex=True)
df['event'] = df['event'].replace("UFC 66: Liddell vs. Ortiz 2", "UFC 66: Liddell vs Ortiz 2", regex=True)
df['event'] = df['event'].replace("UFC 183: Silva vs. Diaz", "UFC 183: Silva vs Diaz", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 5: Struve vs. Miocic", "UFC on FUEL TV: Struve vs Miocic", regex=True)
df['event'] = df['event'].replace("UFC 187: Johnson vs. Cormier", "UFC 187: Johnson vs Cormier", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 19: Diaz vs. Guillard", "UFC Fight Night: Diaz vs Guillard", regex=True)
df['event'] = df['event'].replace("UFC 142: Aldo vs. Mendes", "UFC 142: Aldo vs Mendes", regex=True)
df['event'] = df['event'].replace("UFC on ABC 5: Emmett vs. Topuria", "UFC Fight Night: Emmett vs. Topuria", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Luque vs. Muhammad 2", "UFC Fight Night: Luque vs. Muhammad", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 34: Saffiedine vs. Lim", "UFC Fight Night: Saffiedine vs Lim", regex=True)
df['event'] = df['event'].replace("UFC on FOX 24: Johnson vs. Reis", "UFC on FOX: Johnson vs. Reis", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Song vs. Simón", "UFC Fight Night: Song vs. Simon", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 9: Stevenson vs Guillard", "UFC Fight Night: Stevenson vs Guillard", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 83: Cowboy vs. Cowboy", "UFC Fight Night: Cowboy vs Cowboy", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 32: Belfort vs. Henderson 2", "UFC Fight Night: Belfort vs Henderson 2", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 17 Finale", "The Ultimate Fighter: Team Jones vs. Team Sonnen Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 131: Rivera vs. Moraes", "UFC Fight Night: Rivera vs. Moraes", regex=True)
df['event'] = df['event'].replace("UFC 87: Seek and Destroy", "UFC 87: Seek And Destroy", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 39: Nogueira vs. Nelson", "UFC Fight Night: Minotauro vs Nelson", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 5: Till vs. Masvidal", "UFC Fight Night: Till vs. Masvidal", regex=True)
df['event'] = df['event'].replace("UFC 267: Błachowicz vs. Teixeira", "UFC 267: Blachowicz vs. Teixeira", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 105: Lewis vs. Browne", "UFC Fight Night: Lewis vs. Browne", regex=True)
df['event'] = df['event'].replace("UFC 184: Rousey vs. Zingano", "UFC 184: Rousey vs Zingano", regex=True)
df['event'] = df['event'].replace("UFC on Versus 1: Vera vs Jones", "UFC Live: Vera vs Jones", regex=True)
df['event'] = df['event'].replace("UFC on Versus 3: Sanchez vs Kampmann", "UFC Live: Sanchez vs Kampmann", regex=True)
df['event'] = df['event'].replace("UFC on FX 7: Belfort vs. Bisping", "UFC on FX: Belfort vs Bisping", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 6: Reyes vs. Weidman", "UFC Fight Night: Reyes vs. Weidman", regex=True)
df['event'] = df['event'].replace("UFC on FX 2: Alves vs. Kampmann", "UFC on FX: Alves vs Kampmann", regex=True)
df['event'] = df['event'].replace("UFC 140: Jones vs. Machida", "UFC 140: Jones vs Machida", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 71: Mir vs. Duffee", "UFC Fight Night: Mir vs Duffee", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 99: Mousasi vs. Hall 2", "UFC Fight Night: Mousasi vs. Hall 2", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 8: Silva vs. Stann", "UFC on FUEL TV: Silva vs. Stann", regex=True)
df['event'] = df['event'].replace("UFC 197: Jones vs. Saint Preux", "UFC 197: Jones vs Saint Preux", regex=True)
df['event'] = df['event'].replace("UFC 110: Nogueira vs. Velasquez", "UFC 110: Nogueira vs Velasquez", regex=True)
df['event'] = df['event'].replace("UFC on FOX 7: Henderson vs. Melendez", "UFC on FOX: Henderson vs Melendez", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 48: Bisping vs. Le", "UFC Fight Night: Bisping vs Le", regex=True)
df['event'] = df['event'].replace("UFC 83: Serra vs. St. Pierre 2", "UFC 83: Serra vs St-Pierre 2", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 20: Maia vs. Askren", "UFC Fight Night: Maia vs. Askren", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 128: Barboza vs. Lee", "UFC Fight Night: Barboza vs. Lee", regex=True)
df['event'] = df['event'].replace("UFC 129: St. Pierre vs. Shields", "UFC 129: St-Pierre vs Shields", regex=True)
df['event'] = df['event'].replace("UFC on FOX 16: Dillashaw vs. Barao 2", "UFC on FOX: Dillashaw vs. Barao II", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 15 Finale", "The Ultimate Fighter: Live Finale", regex=True)
df['event'] = df['event'].replace("UFC 200: Tate vs. Nunes", "UFC 200: Tate vs Nunes", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 21 Finale", "The Ultimate Fighter: American Top Team vs. Blackzilians Finale", regex=True)
df['event'] = df['event'].replace("UFC on FX 8: Belfort vs. Rockhold", "UFC on FX: Belfort vs. Rockhold", regex=True)
df['event'] = df['event'].replace("UFC 143: Diaz vs. Condit", "UFC 143: Diaz vs Condit", regex=True)
df['event'] = df['event'].replace("UFC 217: Bisping vs. St. Pierre", "UFC 217: Bisping vs. St-Pierre", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 106: Belfort vs. Gastelum", "UFC Fight Night: Belfort vs. Gastelum", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 84: Silva vs. Bisping", "UFC Fight Night: Silva vs Bisping", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 62: Maia vs. LaFlare", "UFC Fight Night: Maia vs LaFlare", regex=True)
df['event'] = df['event'].replace("UFC 107: Penn vs. Sanchez", "UFC 107: Penn vs Sanchez", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 9: Mousasi vs. Latifi", "UFC on FUEL TV: Mousasi vs Latifi", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 113: Nelson vs. Ponzinibbio", "UFC Fight Night: Nelson vs. Ponzinibbio", regex=True)
df['event'] = df['event'].replace("UFC 139: Shogun vs. Henderson", "UFC 139: Shogun vs Henderson", regex=True)
df['event'] = df['event'].replace("UFC 220: Miocic vs. N'Gannou", "UFC 220: Miocic vs. Ngannou", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 12: Swick vs. Burkman", "UFC Fight Night: Swick vs Burkman", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 22: Marquardt vs. Palhares", "UFC Fight Night: Marquardt vs Palhares", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Nzechukwu vs. Cuțelaba", "UFC Fight Night: Nzechukwu vs. Cutelaba", regex=True)
df['event'] = df['event'].replace("UFC 122: Marquardt vs. Okami", "UFC 122: Marquardt vs Okami", regex=True)
df['event'] = df['event'].replace("UFC on FOX 4: Shogun vs. Vera", "UFC on FOX: Shogun vs Vera", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 47: Bader vs. St. Preux", "UFC Fight Night: Bader vs Saint Preux", regex=True)
df['event'] = df['event'].replace("UFC on Versus 2: Jones vs. Matyushenko", "UFC Live: Jones vs Matyushenko", regex=True)
df['event'] = df['event'].replace("UFC on Versus 6: Cruz vs. Johnson", "UFC Live: Cruz vs Johnson", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 10: Dos Anjos vs. Lee", "UFC Fight Night: Dos Anjos vs. Lee", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 69: Jędrzejczyk vs. Penne", "UFC Fight Night: Jedrzejczyk vs Penne", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 43: Te Huna vs. Marquardt", "UFC Fight Night: Te Huna vs Marquardt", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 10: Nogueira vs. Werdum 2", "UFC on FUEL TV: Nogueira vs. Werdum", regex=True)
df['event'] = df['event'].replace("UFC 95: Sanchez vs. Stevenson", "UFC 95: Sanchez vs Stevenson", regex=True)
df['event'] = df['event'].replace("UFC 192: Cormier vs. Gustafsson", "UFC 192: Cormier vs Gustafsson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 38: Shogun vs. Henderson 2", "UFC Fight Night: Shogun vs Henderson 2", regex=True)
df['event'] = df['event'].replace("UFC 152: Jones vs. Belfort", "UFC 152: Jones vs Belfort", regex=True)
df['event'] = df['event'].replace("UFC 282: Błachowicz vs. Ankalaev", "UFC 282: Blachowicz vs. Ankalaev", regex=True)
df['event'] = df['event'].replace("UFC 137: Penn vs. Diaz", "UFC 137: Penn vs Diaz", regex=True)
df['event'] = df['event'].replace("UFC 182: Jones vs. Cormier", "UFC 182: Jones vs Cormier", regex=True)
df['event'] = df['event'].replace("UFC 146: Dos Santos vs. Mir", "UFC 146: Dos Santos vs Mir", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 115: Volkov vs. Struve", "UFC Fight Night: Volkov vs. Struve", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 135: Gaethje vs. Vick", "UFC Fight Night: Gaethje vs. Vick", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 7: Overeem vs. Rozenstruik", "UFC Fight Night: Overeem vs. Rozenstruik", regex=True)
df['event'] = df['event'].replace("UFC 168: Weidman vs. Silva 2", "UFC 168: Weidman vs Silva 2", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 6 Finale", "The Ultimate Fighter: Team Hughes vs. Team Serra Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 119: Machida vs. Brunson", "UFC Fight Night: Brunson vs. Machida", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 21: Magomedsharipov vs. Kattar", "UFC Fight Night: Zabit vs. Kattar", regex=True)
df['event'] = df['event'].replace("UFC 154: St. Pierre vs. Condit", "UFC 154: St-Pierre vs Condit", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 3 Finale", "The Ultimate Fighter: Team Ortiz vs. Team Shamrock Finale", regex=True)
df['event'] = df['event'].replace("UFC 188: Velasquez vs. Werdum", "UFC 188: Velasquez vs Werdum", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 7: Barao vs. McDonald", "UFC on FUEL TV: Barao vs McDonald", regex=True)
df['event'] = df['event'].replace("UFC on FOX 2: Evans vs. Davis", "UFC on FOX: Evans vs Davis", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 85: Hunt vs. Mir", "UFC Fight Night: Hunt vs Mir", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 138: Volkan vs. Smith", "UFC Fight Night: Oezdemir vs. Smith", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 29: Maia vs. Shields", "UFC Fight Night: Maia vs Shields", regex=True)
df['event'] = df['event'].replace("UFC on FOX 31: Lee vs. Iaquinta 2", "UFC Fight Night: Lee vs. Iaquinta", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 15: Diaz vs. Neer", "UFC Fight Night: Diaz vs Neer", regex=True)
df['event'] = df['event'].replace("UFC 123: Rampage vs. Machida", "UFC 123: Rampage vs Machida", regex=True)
df['event'] = df['event'].replace("UFC 204: Bisping vs. Henderson 2", "UFC 204: Bisping vs. Henderson", regex=True)
df['event'] = df['event'].replace("UFC 198: Werdum vs. Miocic", "UFC 198: Werdum vs Miocic", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 3: N'Gannou vs. Dos Santos", "UFC Fight Night: Ngannou vs. Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC on ABC 3: Ortega vs. Rodriguez", "UFC Fight Night: Ortega vs. Rodriguez", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 2: Assunção vs. Moraes 2", "UFC Fight Night: Assuncao vs. Moraes 2", regex=True)
df['event'] = df['event'].replace("UFC 287: Pereira vs Adesanya 2", "UFC 287: Pereira vs. Adesanya 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 36: Machida vs. Mousasi", "UFC Fight Night: Machida vs Mousasi", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 120: Poirier vs. Pettis", "UFC Fight Night: Poirier vs. Pettis", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 122: Bisping vs. Gastelum", "UFC Fight Night: Bisping vs. Gastelum", regex=True)
df['event'] = df['event'].replace("UFC 211: Miocic vs. Dos Santos 2", "UFC 211: Miocic vs. Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 25: Anderson vs. Błachowicz 2", "UFC Fight Night: Anderson vs. Blachowicz", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 25 Finale", "The Ultimate Fighter: Redemption Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 109: Gustafsson vs. Teixeira", "UFC Fight Night: Gustafsson vs. Teixeira", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 53: Nelson vs. Story", "UFC Fight Night: Nelson vs Story", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 44: Swanson vs. Stephens", "UFC Fight Night: Swanson vs Stephens", regex=True)
df['event'] = df['event'].replace("UFC on FOX 6: Johnson vs. Dodson", "UFC on FOX: Johnson vs Dodson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 130: Thompson vs. Till", "UFC Fight Night: Thompson vs. Till", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 4: Munoz vs. Weidman", "UFC on FUEL TV: Munoz vs Weidman", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 20: Maynard vs Diaz", "UFC Fight Night: Maynard vs Diaz", regex=True)
df['event'] = df['event'].replace("UFC 158: St. Pierre vs. Diaz", "UFC 158: St-Pierre vs Diaz", regex=True)
df['event'] = df['event'].replace("UFC 52: Couture vs. Liddell 2", "UFC 52: Couture vs Liddell 2", regex=True)
df['event'] = df['event'].replace("UFC on FOX 9: Johnson vs. Benavidez 2", "UFC on FOX: Johnson vs. Benavidez 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 87: Overeem vs. Arlovski", "UFC Fight Night: Overeem vs Arlovski", regex=True)
df['event'] = df['event'].replace("UFC 172: Jones vs. Teixeira", "UFC 172: Jones vs Teixeira", regex=True)
df['event'] = df['event'].replace("UFC on FOX 22: VanZant vs. Waterson", "UFC on FOX: VanZant vs. Waterson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 55: Rockhold vs. Bisping", "UFC Fight Night: Rockhold vs Bisping", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 11: Gustafsson vs. Smith", "UFC Fight Night: Gustafsson vs. Smith", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 74: Holloway vs. Oliveira", "UFC Fight Night: Holloway vs Oliveira", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 51: Bigfoot vs. Arlovski 2", "UFC Fight Night: Bigfoot vs Arlovski", regex=True)
df['event'] = df['event'].replace("UFC on FOX 18: Johnson vs. Bader", "UFC on FOX: Johnson vs. Bader", regex=True)
df['event'] = df['event'].replace("UFC on FOX 10: Henderson vs. Thomson", "UFC on FOX: Henderson vs Thomson", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 2: Barboza vs. Gaethje", "UFC Fight Night: Barboza vs. Gaethje", regex=True)
df['event'] = df['event'].replace("UFC on FOX 14: Gustafsson vs. Johnson", "UFC on FOX: Gustafsson vs Johnson", regex=True)
df['event'] = df['event'].replace("UFC 131: Carwin vs. Dos Santos", "UFC 131: Dos Santos vs Carwin", regex=True)
df['event'] = df['event'].replace("UFC 124: St. Pierre vs. Koscheck 2", "UFC 124: St-Pierre vs Koscheck 2", regex=True)
df['event'] = df['event'].replace("UFC on FOX 15: Machida vs. Rockhold", "UFC on FOX: Machida vs Rockhold", regex=True)
df['event'] = df['event'].replace("UFC 134: Silva vs. Okami", "UFC 134: Silva vs Okami", regex=True)
df['event'] = df['event'].replace("UFC 98: Evans vs. Machida", "UFC 98: Evans vs Machida", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 8: Jacare vs. Hermansson", "UFC Fight Night: Jacare vs. Hermansson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 89: MacDonald vs. Thompson", "UFC Fight Night: MacDonald vs Thompson", regex=True)
df['event'] = df['event'].replace("UFC on FOX 21: Maia vs. Condit", "UFC on FOX: Maia vs. Condit", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 4: Lewis vs. Dos Santos", "UFC Fight Night: Lewis vs. Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC on FOX 13: Dos Santos vs. Miocic", "UFC on FOX: Dos Santos vs Miocic", regex=True)
df['event'] = df['event'].replace("UFC on FX 1: Guillard vs. Miller", "UFC on FX: Guillard vs Miller", regex=True)
df['event'] = df['event'].replace("UFC 148: Silva vs. Sonnen 2", "UFC 148: Silva vs Sonnen 2", regex=True)
df['event'] = df['event'].replace("UFC 190: Rousey vs. Correia", "UFC 190: Rousey vs Correia", regex=True)
df['event'] = df['event'].replace("UFC 167: St. Pierre vs. Hendricks", "UFC 167: St-Pierre vs Hendricks", regex=True)
df['event'] = df['event'].replace("UFC 260: Miocic vs. N'Gannou 2", "UFC 260: Miocic vs. Ngannou", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 140: Magny vs. Ponzinibbio", "UFC Fight Night: Magny vs. Ponzinibbio", regex=True)
df['event'] = df['event'].replace("UFC 180: Werdum vs. Hunt", "UFC 180: Werdum vs Hunt", regex=True)
df['event'] = df['event'].replace("UFC 160: Velasquez vs. Silva 2", "UFC 160: Velasquez vs Silva 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 17: Lauzon vs. Stephens", "UFC Fight Night: Lauzon vs Stephens", regex=True)
df['event'] = df['event'].replace("UFC 169: Barao vs. Faber 2", "UFC 169: Barao vs Faber 2", regex=True)
df['event'] = df['event'].replace("UFC 277: Peña vs. Nunes 2", "UFC 277: Pena vs. Nunes 2", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 27 Finale", "The Ultimate Fighter: Undefeated Finale", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 1: Cejudo vs. Dillashaw", "UFC Fight Night: Cejudo vs. Dillashaw", regex=True)
df['event'] = df['event'].replace("UFC 126: Silva vs. Belfort", "UFC 126: Silva vs Belfort", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 101: Whittaker vs. Brunson", "UFC Fight Night: Whittaker vs. Brunson", regex=True)
df['event'] = df['event'].replace("UFC 135: Jones vs. Rampage", "UFC 135: Jones vs Rampage", regex=True)
df['event'] = df['event'].replace("UFC 175: Weidman vs. Machida", "UFC 175: Weidman vs Machida", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Błachowicz vs. Rakić", "UFC Fight Night: Blachowicz vs. Rakic", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 2: Silva vs. Gustafsson", "UFC on FUEL TV: Gustafsson vs Silva", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 1: Ellenberger vs. Sanchez", "UFC on FUEL TV: Sanchez vs Ellenberger", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 14: Silva vs. Irvin", "UFC: Silva vs Irvin", regex=True)
df['event'] = df['event'].replace("UFC on FOX 11: Werdum vs. Browne", "UFC on FOX: Werdum vs Browne", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 116: Rockhold vs. Branch", "UFC Fight Night: Rockhold vs. Branch", regex=True)
df['event'] = df['event'].replace("UFC 174: Johnson vs. Bagautinov", "UFC 174: Johnson vs Bagautinov", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 88: Almeida vs. Garbrandt", "UFC Fight Night: Almeida vs Garbrandt", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 72: Bisping vs. Leites", "UFC Fight Night: Bisping vs Leites", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 28: Lee vs. Oliveira", "UFC Fight Night: Lee vs. Oliveira", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 1: N'Gannou vs. Velasquez", "UFC Fight Night: Ngannou vs. Velasquez", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 24: Blaydes vs. Dos Santos", "UFC Fight Night: Blaydes vs. Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 94: Poirier vs. Johnson", "UFC Fight Night: Poirier vs. Johnson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 70: Machida vs. Romero", "UFC Fight Night: Machida vs Romero", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 121: Werdum vs. Tybura", "UFC Fight Night: Werdum vs. Tybura", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 5: Covington vs. Lawler", "UFC Fight Night: Covington vs. Lawler", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 90: Dos Anjos vs. Alvarez", "UFC Fight Night: Dos Anjos vs. Alvarez", regex=True)
df['event'] = df['event'].replace("UFC 181: Hendricks vs. Lawler 2", "UFC 181: Hendricks vs Lawler II", regex=True)
df['event'] = df['event'].replace("UFC 50: The War of '04", "UFC 50: The War Of '04", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 96: Lineker vs. Dodson", "UFC Fight Night: Lineker vs. Dodson", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 12: Moicano vs. Korean Zombie", "UFC Fight Night: Moicano vs. The Korean Zombie", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 75: Barnett vs. Nelson", "UFC Fight Night: Barnett vs Nelson", regex=True)
df['event'] = df['event'].replace("UFC on FOX 20: Holm vs. Shevchenko", "UFC on FOX: Holm vs. Shevchenko", regex=True)
df['event'] = df['event'].replace("UFC on ABC 1: Holloway vs. Kattar", "UFC Fight Night: Holloway vs. Kattar", regex=True)
df['event'] = df['event'].replace("UFC The Final Chapter: Ortiz vs Shamrock 3", "Ortiz vs Shamrock 3: The Final Chapter", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 127: Werdum vs. Volkov", "UFC Fight Night: Werdum vs. Volkov", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 20 Finale", "The Ultimate Fighter: A Champion Will Be Crowned Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 60: Henderson vs. Thatch", "UFC Fight Night: Henderson vs Thatch", regex=True)
df['event'] = df['event'].replace("UFC 162: Silva vs. Weidman", "UFC 162: Silva vs Weidman", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 123: Swanson vs. Ortega", "UFC Fight Night: Swanson vs. Ortega", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 125: Machida vs. Anders", "UFC Fight Night: Machida vs. Anders", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 111: Holm vs. Correia", "UFC Fight Night: Holm vs. Correia", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 73: Teixeira vs. St. Preux", "UFC Fight Night: Teixeira vs Saint Preux", regex=True)
df['event'] = df['event'].replace("UFC 161: Evans vs. Henderson", "UFC 161: Evans vs Henderson", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 8 Finale", "The Ultimate Fighter: Team Nogueira vs. Team Mir Finale", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 16: Cowboy vs. Gaethje", "UFC Fight Night: Cowboy vs. Gaethje", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 80: Namajunas vs. VanZant", "UFC Fight Night: Namajunas vs. VanZant", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 57: Edgar vs. Swanson", "UFC Fight Night: Edgar vs Swanson", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 14 Finale", "The Ultimate Fighter: Team Bisping vs Team Miller Finale", regex=True)
df['event'] = df['event'].replace("UFC 185: Pettis vs. Dos Anjos", "UFC 185: Pettis vs Dos Anjos", regex=True)
df['event'] = df['event'].replace("UFC on Versus 5: Hardy vs. Lytle", "UFC Live: Hardy vs Lytle", regex=True)
df['event'] = df['event'].replace("UFC 7.5: Ultimate Ultimate 1995", "UFC - Ultimate Ultimate '95", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 124: Stephens vs. Choi", "UFC Fight Night: Stephens vs. Choi", regex=True)
df['event'] = df['event'].replace("UFC 166: Velasquez vs. Dos Santos 3", "UFC 166: Velasquez vs Dos Santos 3", regex=True)
df['event'] = df['event'].replace("UFC on FOX 12: Lawler vs. Brown", "UFC on FOX: Lawler vs Brown", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 28 Finale", "The Ultimate Fighter: Heavy Hitters Finale", regex=True)
df['event'] = df['event'].replace("UFC 120: Bisping vs. Akiyama", "UFC 120: Bisping vs Akiyama", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 15: Andrade vs. Zhang", "UFC Fight Night: Andrade vs. Zhang", regex=True)
df['event'] = df['event'].replace("UFC on FOX 29: Poirier vs. Gaethje", "UFC Fight Night: Poirier vs. Gaethje", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 134: Shogun vs. Smith", "UFC Fight Night: Shogun vs. Smith", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 114: Pettis vs. Moreno", "UFC Fight Night: Pettis vs. Moreno", regex=True)
df['event'] = df['event'].replace("UFC on FOX 1: Velasquez vs. Dos Santos", "UFC on FOX: Velasquez vs Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC 138: Leben vs. Munoz", "UFC 138: Leben vs Munoz", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 16: Fight for the Troops", "UFC Fight Night - Fight for the Troops", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 64: Gonzaga vs. Cro Cop 2", "UFC Fight Night: Gonzaga vs Cro Cop 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 13: Florian vs. Lauzon", "UFC Fight Night: Florian vs Lauzon", regex=True)
df['event'] = df['event'].replace("UFC 259: Błachowicz vs. Adesanya", "UFC 259: Blachowicz vs. Adesanya", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 6: Thompson vs. Pettis", "UFC Fight Night: Thompson vs. Pettis", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 27: Condit vs. Kampmann 2", "UFC Fight Night: Condit vs Kampmann 2", regex=True)
df['event'] = df['event'].replace("UFC 170: Rousey vs. McMann", "UFC 170: Rousey vs McMann", regex=True)
df['event'] = df['event'].replace("UFC 102: Couture vs. Nogueira", "UFC 102: Couture vs Nogueira", regex=True)
df['event'] = df['event'].replace("UFC on FOX 17: Dos Anjos vs. Cowboy 2", "UFC on FOX: Dos Anjos vs. Cowboy 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Bisping vs. Kennedy", "UFC Fight Night: Bisping vs Kennedy", regex=True)
df['event'] = df['event'].replace("UFC on FOX 19: Teixeira vs. Evans", "UFC on FOX: Teixeira vs Evans", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 52: Hunt vs. Nelson", "UFC Fight Night: Hunt vs Nelson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 103: Rodriguez vs. Penn", "UFC Fight Night: Rodriguez vs. Penn", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 78: Magny vs. Gastelum", "UFC Fight Night: Magny vs Gastelum", regex=True)
df['event'] = df['event'].replace("UFC 178: Johnson vs. Cariaso", "UFC 178: Johnson vs Cariaso", regex=True)
df['event'] = df['event'].replace("UFC 179: Aldo vs. Mendes 2", "UFC 179: Aldo vs Mendes 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 68: Boetsch vs. Henderson", "UFC Fight Night: Boetsch vs Henderson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 35: Rockhold vs. Philippou", "UFC Fight Night: Rockhold vs Philippou", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 28: Teixeira vs. Bader", "UFC Fight Night: Teixeira vs Bader", regex=True)
df['event'] = df['event'].replace("UFC on FOX 23: Shevchenko vs. Peña", "UFC on FOX: Shevchenko vs. Pena", regex=True)
df['event'] = df['event'].replace("UFC 94: St-Pierre vs. Penn 2", "UFC 94: St-Pierre vs Penn 2", regex=True)
df['event'] = df['event'].replace("UFC 246: McGregor vs. Cerrone", "UFC 246: McGregor vs. Cowboy", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 26: Shogun vs. Sonnen", "UFC Fight Night: Shogun vs Sonnen", regex=True)
df['event'] = df['event'].replace("UFC on FX 4: Guida vs. Maynard", "UFC on FX: Maynard vs Guida", regex=True)
df['event'] = df['event'].replace("UFC 17.5: Ultimate Brazil", "UFC - Ultimate Brazil", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 126: Cowboy vs. Medeiros", "UFC Fight Night: Cerrone vs. Medeiros", regex=True)
df['event'] = df['event'].replace("UFC 163: Aldo vs. Korean Zombie", "UFC 163: Aldo vs Jung", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 129: Maia vs. Usman", "UFC Fight Night: Maia vs. Usman", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 92: Caceres vs. Rodriguez", "UFC Fight Night: Rodriguez vs. Caceres", regex=True)
df['event'] = df['event'].replace("UFC 147: Silva vs. Franklin 2", "UFC 147: Silva vs Franklin 2", regex=True)
df['event'] = df['event'].replace("UFC 15.5: Ultimate Japan", "UFC - Ultimate Japan", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 139: Korean Zombie vs. Rodriguez", "UFC Fight Night: Korean Zombie vs. Rodriguez", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 132: Cowboy vs. Edwards", "UFC Fight Night: Cowboy vs. Edwards", regex=True)
df['event'] = df['event'].replace("UFC 68: Uprising", "UFC 68: The Uprising", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 37: Gustafsson vs. Manuwa", "UFC Fight Night: Gustafsson vs Manuwa", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 118: Cowboy vs. Till", "UFC Fight Night: Cerrone vs. Till", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 102: Lewis vs. Abdurakhimov", "UFC Fight Night: Lewis vs. Abdurakhimov", regex=True)
df['event'] = df['event'].replace("UFC 150: Henderson vs. Edgar 2", "UFC 150: Henderson vs Edgar II", regex=True)
df['event'] = df['event'].replace("UFC on FOX 3: Diaz vs. Miller", "UFC on FOX: Diaz vs Miller", regex=True)
df['event'] = df['event'].replace("UFC on ABC 4: Rozenstruik vs. Almeida", "UFC Fight Night: Rozenstruik vs. Almeida", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 79: Henderson vs. Masvidal", "UFC Fight Night: Henderson vs Masvidal", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 93: Arlovski vs. Barnett", "UFC Fight Night: Arlovski vs. Barnett", regex=True)
df['event'] = df['event'].replace("UFC 155: Dos Santos vs. Velasquez 2", "UFC 155: Dos Santos vs Velasquez II", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 18: Hermansson vs. Cannonier", "UFC Fight Night: Hermansson vs. Cannonier", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 7 Finale", "The Ultimate Fighter: Team Rampage vs Team Forrest Finale", regex=True)
df['event'] = df['event'].replace("UFC on ABC 2: Vettori vs. Holland", "UFC Fight Night: Vettori vs. Holland", regex=True)
df['event'] = df['event'].replace("UFC 165: Jones vs. Gustafsson", "UFC 165: Jones vs Gustafsson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 76: Holohan vs. Smolka", "UFC Fight Night: Holohan vs Smolka", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 61: Bigfoot vs. Mir", "UFC Fight Night: Bigfoot vs Mir", regex=True)
df['event'] = df['event'].replace("UFC 195: Lawler vs. Condit", "UFC 195: Lawler vs Condit", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 13 Finale", "The Ultimate Fighter: Team Lesnar vs Team dos Santos Finale", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 11 Finale", "The Ultimate Fighter: Team Liddell vs Team Ortiz Finale", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 26 Finale", "The Ultimate Fighter: A New World Champion Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 54: MacDonald vs. Saffiedine", "UFC Fight Night: MacDonald vs Saffiedine", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 82: Hendricks vs. Thompson", "UFC Fight Night: Hendricks vs Thompson", regex=True)
df['event'] = df['event'].replace("UFC 114: Jackson vs Evans", "UFC 114: Rampage vs Evans", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 12 Finale", "The Ultimate Fighter: Team GSP vs Team Koscheck Finale", regex=True)
df['event'] = df['event'].replace("UFC 186: Johnson vs. Horiguchi", "UFC 186: Johnson vs Horiguchi", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 117: St. Preux vs. Okami", "UFC Fight Night: Saint Preux vs. Okami", regex=True)
df['event'] = df['event'].replace("UFC on FOX 30: Alvarez vs. Poirier 2", "UFC Fight Night: Alvarez vs. Poirier 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 65: Miocic vs. Hunt", "UFC Fight Night: Miocic vs Hunt", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 14: Shevchenko vs. Carmouche 2", "UFC Fight Night: Shevchenko vs. Carmouche 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 50: Jacare vs. Mousasi 2", "UFC Fight Night: Jacare vs Mousasi", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 27: Benavidez vs. Figueiredo", "UFC Fight Night: Benavidez vs. Figueiredo", regex=True)
df['event'] = df['event'].replace("UFC 177: Dillashaw vs. Soto", "UFC 177: Dillashaw vs Soto", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 11: Thomas vs Florian", "UFC Fight Night: Thomas vs Florian", regex=True)
df['event'] = df['event'].replace("UFC 145: Jones vs. Evans", "UFC 145: Jones vs Evans", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 133: Dos Santos vs. Ivanov", "UFC Fight Night: Dos Santos vs. Ivanov", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 98: Dos Anjos vs. Ferguson", "UFC Fight Night: Dos Anjos vs. Ferguson", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 10 Finale", "The Ultimate Fighter: Heavyweights Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 31: Fight for the Troops 3", "UFC Fight Night: Fight for the Troops 3", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 136: Hunt vs. Oleinik", "UFC Fight Night: Hunt vs. Oleinik", regex=True)
df['event'] = df['event'].replace("UFC 159: Jones vs. Sonnen", "UFC 159: Jones vs Sonnen", regex=True)
df['event'] = df['event'].replace("UFC 86: Jackson vs. Griffin", "UFC 86: Jackson vs Griffin", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Makhachev vs. Moisés", "UFC Fight Night: Makhachev vs. Moises", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 86: Rothwell vs. Dos Santos", "UFC Fight Night: Rothwell vs Dos Santos", regex=True)
df['event'] = df['event'].replace("UFC 278: Usman vs. Edwards 2", "UFC 278: Usman vs. Edwards", regex=True)
df['event'] = df['event'].replace("UFC 157: Rousey vs. Carmouche", "UFC 157: Rousey vs Carmouche", regex=True)
df['event'] = df['event'].replace("UFC on FOX 28: Emmett vs. Stephens", "UFC Fight Night: Emmett vs. Stephens", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 33: Hunt vs. Bigfoot", "UFC Fight Night: Hunt vs Bigfoot", regex=True)
df['event'] = df['event'].replace("UFC 57: Liddell vs. Couture 3", "UFC 57: Liddell vs Couture 3", regex=True)
df['event'] = df['event'].replace("UFC 144: Edgar vs. Henderson", "UFC 144: Edgar vs Henderson", regex=True)
df['event'] = df['event'].replace("UFC 194: Aldo vs. McGregor", "UFC 194: Aldo vs McGregor", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 17: Rodriguez vs. Stephens", "UFC Fight Night: Rodriguez vs. Stephens", regex=True)
df['event'] = df['event'].replace("UFC 205: Alvarez vs. McGregor", "UFC 205: Alvarez vs McGregor", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 13: De Randamie vs. Ladd", "UFC Fight Night: De Randamie vs. Ladd", regex=True)
df['event'] = df['event'].replace("UFC 141: Lesnar vs. Overeem", "UFC 141: Lesnar vs Overeem", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 21: Florian vs Gomi", "UFC Fight Night: Florian vs Gomi", regex=True)
df['event'] = df['event'].replace("UFC 164: Henderson vs. Pettis 2", "UFC 164: Henderson vs Pettis 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 59: McGregor vs. Siver", "UFC Fight Night: McGregor vs Siver", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 5 Finale", "The Ultimate Fighter: Team Pulver vs. Team Penn Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 49: Henderson vs. dos Anjos", "UFC Fight Night: Henderson vs Dos Anjos", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 24: Nogueira vs. Davis", "UFC Fight Night: Nogueira vs Davis", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 81: Dillashaw vs. Cruz", "UFC Fight Night: Dillashaw vs Cruz", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 9: Iaquinta vs. Cowboy", "UFC Fight Night: Iaquinta vs. Cowboy", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 91: McDonald vs. Lineker", "UFC Fight Night: McDonald vs. Lineker", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 41: Munoz vs. Mousasi", "UFC Fight Night: Munoz vs Mousasi", regex=True)
df['event'] = df['event'].replace("UFC 208: Holm vs. de Randamie", "UFC 208: Holm vs. De Randamie", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 63: Mendes vs. Lamas", "UFC Fight Night: Mendes vs Lamas", regex=True)
df['event'] = df['event'].replace("UFC on FOX 8: Johnson vs. Moraga", "UFC on FOX: Johnson vs Moraga", regex=True)
df['event'] = df['event'].replace("UFC 103: Franklin vs. Belfort", "UFC 103: Franklin vs Belfort", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Ortega vs. Korean Zombie", "UFC Fight Night: Ortega vs. The Korean Zombie", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 19: Joanna vs. Waterson", "UFC Fight Night: Joanna vs. Waterson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 107: Manuwa vs. Anderson", "UFC Fight Night: Manuwa vs. Anderson", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 30: Machida vs. Munoz", "UFC Fight Night: Machida vs Munoz", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 16 Finale", "The Ultimate Fighter: Team Carwin vs. Team Nelson Finale", regex=True)
df['event'] = df['event'].replace("UFC 5: Return of the Beast", "UFC 5: The Return of the Beast", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 2 Finale", "The Ultimate Fighter: Team Hughes vs. Team Franklin Finale", regex=True)
df['event'] = df['event'].replace("UFC 215: Nunes vs. Shevchenko 2", "UFC 215: Nunes vs Shevchenko 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 10: Stout vs Fisher", "UFC Fight Night: Stout vs Fisher", regex=True)
df['event'] = df['event'].replace("UFC on ESPN 4: Dos Anjos vs. Edwards", "UFC Fight Night: Dos Anjos vs. Edwards", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 104: Bermudez vs. Korean Zombie", "UFC Fight Night: Bermudez vs. The Korean Zombie", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 66: Edgar vs. Faber", "UFC Fight Night: Edgar vs Faber", regex=True)
df['event'] = df['event'].replace("UFC on FOX 25: Weidman vs. Gastelum", "UFC Fight Night: Weidman vs. Gastelum", regex=True)
df['event'] = df['event'].replace("UFC 93: Franklin vs. Henderson", "UFC 93: Franklin vs Henderson", regex=True)
df['event'] = df['event'].replace("UFC 196: McGregor vs. Diaz", "UFC 196: McGregor vs Diaz", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 8: Evans vs Salmon", "UFC Fight Night: Evans vs Salmon", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 9 Finale", "The Ultimate Fighter: United States vs. United Kingdom Finale", regex=True)
df['event'] = df['event'].replace("UFC on FOX 26: Lawler vs. Dos Anjos", "UFC Fight Night: Lawler vs. Dos Anjos", regex=True)
df['event'] = df['event'].replace("UFC 156: Aldo vs. Edgar", "UFC 156: Aldo vs Edgar", regex=True)
df['event'] = df['event'].replace("UFC 191: Johnson vs. Dodson 2", "UFC 191: Johnson vs Dodson 2", regex=True)
df['event'] = df['event'].replace("UFC 275: Teixeira vs. Procházka", "UFC 275: Teixeira vs. Prochazka", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 23: Fight for the Troops 2", "UFC Fight Night: Fight for the Troops 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 56: Shogun vs. St. Preux", "UFC Fight Night 56: Shogun vs Saint Preux", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 46: McGregor vs. Brandao", "UFC Fight Night: McGregor vs Brandao", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 22 Finale", "The Ultimate Fighter: Team McGregor vs. Team Faber Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 110: Lewis vs. Hunt", "UFC Fight Night: Lewis vs. Hunt", regex=True)
df['event'] = df['event'].replace("UFC 13: Ultimate Force", "UFC 13: The Ultimate Force", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 3: Błachowicz vs. Santos", "UFC Fight Night: Blachowicz vs. Santos", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 1 Finale", "The Ultimate Fighter: Team Couture vs. Team Liddell Finale", regex=True)
df['event'] = df['event'].replace("UFC 193: Rousey vs. Holm", "UFC 193: Rousey vs Holm", regex=True)
df['event'] = df['event'].replace("UFC 153: Silva vs. Bonnar", "UFC 153: Silva vs Bonnar", regex=True)
df['event'] = df['event'].replace("UFC 118: Edgar vs. Penn 2", "UFC 118: Edgar vs Penn 2", regex=True)
df['event'] = df['event'].replace("UFC 189: Mendes vs. McGregor", "UFC 189: Mendes vs McGregor", regex=True)
df['event'] = df['event'].replace("UFC on Versus 4: Barry vs. Kongo", "UFC Live: Kongo vs Barry", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Miocic vs. Maldonado", "UFC Fight Night: Miocic vs Maldonado", regex=True)
df['event'] = df['event'].replace("UFC 173: Barao vs. Dillashaw", "UFC 173: Barao vs Dillashaw", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Kim vs. Hathaway", "UFC Fight Night: Kim vs Hathaway", regex=True)
df['event'] = df['event'].replace("UFC on FX 3: Johnson vs. McCall", "UFC on FX: Johnson vs McCall", regex=True)
df['event'] = df['event'].replace("UFC 149: Faber vs. Barao", "UFC 149: Faber vs Barao", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 7: Overeem vs. Oleinik", "UFC Fight Night: Overeem vs. Oleinik", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 24 Finale", "The Ultimate Fighter: Tournament of Champions Finale", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 19 Finale", "The Ultimate Fighter: Team Edgar vs. Team Penn Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 100: Bader vs. Nogueira 2", "UFC Fight Night: Bader vs. Nogueira", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 7: Sanchez vs Riggs", "UFC Fight Night: Sanchez vs Riggs", regex=True)
df['event'] = df['event'].replace("UFC on FUEL TV 6: Franklin vs. Le", "UFC Macao: Franklin vs Le", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 18 Finale", "The Ultimate Fighter: Team Rousey vs. Team Tate Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 45: Cerrone vs. Miller", "UFC Fight Night: Cowboy vs Miller", regex=True)
df['event'] = df['event'].replace("UFC 132: Cruz vs Faber II", "UFC 132: Cruz vs Faber", regex=True)
df['event'] = df['event'].replace("UFC 133: Evans vs. Ortiz 2", "UFC 133: Evans vs Ortiz 2", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 108: Swanson vs. Lobov", "UFC Fight Night: Swanson vs. Lobov", regex=True)
df['event'] = df['event'].replace("UFC 96: Jackson vs. Jardine", "UFC 96: Jackson vs Jardine", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 26: Felder vs. Hooker", "UFC Fight Night: Felder vs. Hooker", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 142: Dos Santos vs. Tuivasa", "UFC Fight Night: Dos Santos vs. Tuivasa", regex=True)
df['event'] = df['event'].replace("UFC 26: Ultimate Field of Dreams", "UFC 26: Ultimate Field Of Dreams", regex=True)
df['event'] = df['event'].replace("UFC on ESPN+ 23: Edgar vs. Korean Zombie", "UFC Fight Night: Edgar vs. The Korean Zombie", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Reyes vs. Procházka", "UFC Fight Night: Reyes vs. Prochazka", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 42: Henderson vs. Khabilov", "UFC Fight Night: Henderson vs Khabilov", regex=True)
df['event'] = df['event'].replace("UFC 171: Hendricks vs. Lawler", "UFC 171: Hendricks vs Lawler", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 112: Chiesa vs. Lee", "UFC Fight Night: Chiesa vs. Lee", regex=True)
df['event'] = df['event'].replace("The Ultimate Fighter 4 Finale", "The Ultimate Fighter: The Comeback Finale", regex=True)
df['event'] = df['event'].replace("UFC Fight Night 137: Santos vs. Anders", "UFC Fight Night: Marreta vs. Anders", regex=True)
df['event'] = df['event'].replace("UFC 11.5: Ultimate Ultimate 1996", "UFC - Ultimate Ultimate '96", regex=True)
df['event'] = df['event'].replace("UFC Fight Night: Korean Zombie vs. Ige", "UFC Fight Night: Jung vs. Ige", regex=True)


#match events for rows presented issues
for index, row in df.iterrows():
    if row['event'] == 'UFC on ESPN+ 5: Till vs. Masvidal':
        df.loc[index, 'event'] = 'UFC Fight Night: Till vs. Masvidal'
    if row['event'] == 'UFC on ESPN+ 20: Maia vs. Askren':
        df.loc[index, 'event'] = 'UFC Fight Night: Maia vs. Askren'
    if row['event'] == 'UFC on ESPN+ 10: Dos Anjos vs. Lee':
        df.loc[index, 'event'] = 'UFC Fight Night: Dos Anjos vs. Lee'
    if row['event'] == 'UFC on ESPN+ 21: Magomedsharipov vs. Kattar':
        df.loc[index, 'event'] = 'UFC Fight Night: Zabit vs. Kattar'
    if row['event'] == 'UFC on ESPN+ 2: Assunção vs. Moraes 2':
        df.loc[index, 'event'] = 'UFC Fight Night: Assuncao vs. Moraes 2'
    if row['event'] == 'UFC on ESPN+ 25: Anderson vs. Błachowicz 2':
        df.loc[index, 'event'] = 'UFC Fight Night: Anderson vs. Blachowicz'
    if row['event'] == 'UFC on ESPN+ 11: Gustafsson vs. Smith':
        df.loc[index, 'event'] = 'UFC Fight Night: Gustafsson vs. Smith'
    if row['event'] == 'UFC on ESPN+ 8: Jacare vs. Hermansson':
        df.loc[index, 'event'] = 'UFC Fight Night: Jacare vs. Hermansson'
    if row['event'] == 'UFC on ESPN+ 4: Lewis vs. Dos Santos':
        df.loc[index, 'event'] = 'UFC Fight Night: Lewis vs. Dos Santos'
    if row['event'] == 'UFC on ESPN+ 1: Cejudo vs. Dillashaw':
        df.loc[index, 'event'] = 'UFC Fight Night: Cejudo vs. Dillashaw'
    if row['event'] == 'UFC on ESPN+ 28: Lee vs. Oliveira':
        df.loc[index, 'event'] = 'UFC Fight Night: Lee vs. Oliveira'
    if row['event'] == 'UFC on ESPN+ 24: Blaydes vs. Dos Santos':
        df.loc[index, 'event'] = 'UFC Fight Night: Blaydes vs. Dos Santos'
    if row['event'] == 'UFC on ESPN+ 12: Moicano vs. Korean Zombie':
        df.loc[index, 'event'] = 'UFC Fight Night: Moicano vs. The Korean Zombie'
    if row['event'] == 'UFC on ESPN+ 16: Cowboy vs. Gaethje':
        df.loc[index, 'event'] = 'UFC Fight Night: Cowboy vs. Gaethje'
    if row['event'] == 'UFC on ESPN+ 15: Andrade vs. Zhang':
        df.loc[index, 'event'] = 'UFC Fight Night: Andrade vs. Zhang'
    if row['event'] == 'UFC on ESPN+ 6: Thompson vs. Pettis':
        df.loc[index, 'event'] = 'UFC Fight Night: Thompson vs. Pettis'
    if row['event'] == 'UFC on ESPN+ 18: Hermansson vs. Cannonier':
        df.loc[index, 'event'] = 'UFC Fight Night: Hermansson vs. Cannonier'
    if row['event'] == 'UFC on ESPN+ 14: Shevchenko vs. Carmouche 2':
        df.loc[index, 'event'] = 'UFC Fight Night: Shevchenko vs. Carmouche 2'
    if row['event'] == 'UFC on ESPN+ 27: Benavidez vs. Figueiredo':
        df.loc[index, 'event'] = 'UFC Fight Night: Benavidez vs. Figueiredo'
    if row['event'] == 'UFC on ESPN+ 17: Rodriguez vs. Stephens':
        df.loc[index, 'event'] = 'UFC Fight Night: Rodriguez vs. Stephens'
    if row['event'] == 'UFC on ESPN+ 13: De Randamie vs. Ladd':
        df.loc[index, 'event'] = 'UFC Fight Night: De Randamie vs. Ladd'
    if row['event'] == 'UFC on ESPN+ 9: Iaquinta vs. Cowboy':
        df.loc[index, 'event'] = 'UFC Fight Night: Iaquinta vs. Cowboy'
    if row['event'] == 'UFC on ESPN+ 19: Joanna vs. Waterson':
        df.loc[index, 'event'] = 'UFC Fight Night: Joanna vs. Waterson'
    if row['event'] == 'UFC on ESPN+ 3: Błachowicz vs. Santos':
        df.loc[index, 'event'] = 'UFC Fight Night: Blachowicz vs. Santos'
    if row['event'] == 'UFC on ESPN+ 7: Overeem vs. Oleinik':
        df.loc[index, 'event'] = 'UFC Fight Night: Overeem vs. Oleinik'
    if row['event'] == 'UFC on ESPN+ 26: Felder vs. Hooker':
        df.loc[index, 'event'] = 'UFC Fight Night: Felder vs. Hooker'
    if row['event'] == 'UFC on ESPN+ 23: Edgar vs. Korean Zombie':
        df.loc[index, 'event'] = 'UFC Fight Night: Edgar vs. The Korean Zombie'
    if row['event'] == 'UFC on ESPN+ 22: Blachowicz vs. Jacare':
        df.loc[index, 'event'] = 'UFC Fight Night: Blachowicz vs. Jacare'


#clean winners, losers, fights
for i in range(5):
    for index, row in df.iterrows():
        winner = row['winner']
        loser = row['loser']
        fight = row['fight']
        if(isinstance(winner, str)):
            if('ć' in winner):
                df.loc[index, 'winner'] = winner.replace('ć', 'c')
            if('ê' in winner):
                df.loc[index, 'winner'] = winner.replace('ê', 'e')
            if('Á' in winner):
                df.loc[index, 'winner'] = winner.replace('Á', 'A')
            if('Ł' in winner):
                df.loc[index, 'winner'] = winner.replace('Ł', 'L')
            if('č' in winner):
                df.loc[index, 'winner'] = winner.replace('č', 'c')
            if('ă' in winner):
                df.loc[index, 'winner'] = winner.replace('ă', 'a')
            if('á' in winner):
                df.loc[index, 'winner'] = winner.replace('á', 'a')
            if('ä' in winner):
                df.loc[index, 'winner'] = winner.replace('ä', 'a')
            if('ú' in winner):
                df.loc[index, 'winner'] = winner.replace('ú', 'u')
            if('ę' in winner):
                df.loc[index, 'winner'] = winner.replace('ę', 'e')
            if('ã' in winner):
                df.loc[index, 'winner'] = winner.replace('ã', 'a')
            if('.' in winner):
                df.loc[index, 'winner'] = winner.replace('.', '')
            if('é' in winner): 
                df.loc[index, 'winner'] = winner.replace('é', 'e')
            if('ô' in winner):
                df.loc[index, 'winner'] = winner.replace('ô', 'o')
            if("'" in winner):
                df.loc[index, 'winner'] = winner.replace("'", '')
            if('ö' in winner):
                df.loc[index, 'winner'] = winner.replace('ö', 'o')
            if('í' in winner):
                df.loc[index, 'winner'] = winner.replace('í', 'i')
            if('ř' in winner):
                df.loc[index, 'winner'] = winner.replace('ř', 'r')
            if('-' in winner):
                df.loc[index, 'winner'] = winner.replace('-', ' ')
            if('â' in winner):
                df.loc[index, 'winner'] = winner.replace('â', 'a')
            if('Ľ' in winner):
                df.loc[index, 'winner'] = winner.replace('Ľ', 'L')
            if('ţ' in winner):
                df.loc[index, 'winner'] = winner.replace('ţ', 't')
            if('ł' in winner):
                df.loc[index, 'winner'] = winner.replace('ł', 'l')
            if('õ' in winner):
                df.loc[index, 'winner'] = winner.replace('õ', 'o')
            if('š' in winner):
                df.loc[index, 'winner'] = winner.replace('š', 's')
            if('ó' in winner):
                df.loc[index, 'winner'] = winner.replace('ó', 'o')
            if('ç' in winner):
                df.loc[index, 'winner'] = winner.replace('ç', 'c')
            if('ń' in winner):
                df.loc[index, 'winner'] = winner.replace('ń', 'n')
            if('ñ' in winner):
                df.loc[index, 'winner'] = winner.replace('ñ', 'n')
            if('ž' in winner):
                df.loc[index, 'winner'] = winner.replace('ž', 'z')
        if(isinstance(loser, str)):
            if('ć' in loser):
                df.loc[index, 'loser'] = loser.replace('ć', 'c')
            if('ê' in loser):
                df.loc[index, 'loser'] = loser.replace('ê', 'e')
            if('Á' in loser):
                df.loc[index, 'loser'] = loser.replace('Á', 'A')
            if('Ł' in loser):
                df.loc[index, 'loser'] = loser.replace('Ł', 'L')
            if('č' in loser):
                df.loc[index, 'loser'] = loser.replace('č', 'c')
            if('ă' in loser):
                df.loc[index, 'loser'] = loser.replace('ă', 'a')
            if('á' in loser):
                df.loc[index, 'loser'] = loser.replace('á', 'a')
            if('ä' in loser):
                df.loc[index, 'loser'] = loser.replace('ä', 'a')
            if('ú' in loser):
                df.loc[index, 'loser'] = loser.replace('ú', 'u')
            if('ę' in loser):
                df.loc[index, 'loser'] = loser.replace('ę', 'e')
            if('ã' in loser):
                df.loc[index, 'loser'] = loser.replace('ã', 'a')
            if('.' in loser):
                df.loc[index, 'loser'] = loser.replace('.', '')
            if('é' in loser): 
                df.loc[index, 'loser'] = loser.replace('é', 'e')
            if('ô' in loser):
                df.loc[index, 'loser'] = loser.replace('ô', 'o')
            if("'" in loser):
                df.loc[index, 'loser'] = loser.replace("'", '')
            if('ö' in loser):
                df.loc[index, 'loser'] = loser.replace('ö', 'o')
            if('í' in loser):
                df.loc[index, 'loser'] = loser.replace('í', 'i')
            if('ř' in loser):
                df.loc[index, 'loser'] = loser.replace('ř', 'r')
            if('-' in loser):
                df.loc[index, 'loser'] = loser.replace('-', ' ')
            if('â' in loser):
                df.loc[index, 'loser'] = loser.replace('â', 'a')
            if('Ľ' in loser):
                df.loc[index, 'loser'] = loser.replace('Ľ', 'L')
            if('ţ' in loser):
                df.loc[index, 'loser'] = loser.replace('ţ', 't')
            if('ł' in loser):
                df.loc[index, 'loser'] = loser.replace('ł', 'l')
            if('õ' in loser):
                df.loc[index, 'loser'] = loser.replace('õ', 'o')
            if('š' in loser):
                df.loc[index, 'loser'] = loser.replace('š', 's')
            if('ó' in loser):
                df.loc[index, 'loser'] = loser.replace('ó', 'o')
            if('ç' in loser):
                df.loc[index, 'loser'] = loser.replace('ç', 'c')
            if('ń' in loser):
                df.loc[index, 'loser'] = loser.replace('ń', 'n')
            if('ñ' in loser):
                df.loc[index, 'loser'] = loser.replace('ñ', 'n')
            if('ž' in loser):
                df.loc[index, 'loser'] = loser.replace('ž', 'z')
        if(isinstance(fight, str)):
            if('ć' in fight):
                df.loc[index, 'fight'] = fight.replace('ć', 'c')
            if('ê' in fight):
                df.loc[index, 'fight'] = fight.replace('ê', 'e')
            if('Á' in fight):
                df.loc[index, 'fight'] = fight.replace('Á', 'A')
            if('Ł' in fight):
                df.loc[index, 'fight'] = fight.replace('Ł', 'L')
            if('č' in fight):
                df.loc[index, 'fight'] = fight.replace('č', 'c')
            if('ă' in fight):
                df.loc[index, 'fight'] = fight.replace('ă', 'a')
            if('á' in fight):
                df.loc[index, 'fight'] = fight.replace('á', 'a')
            if('ä' in fight):
                df.loc[index, 'fight'] = fight.replace('ä', 'a')
            if('ú' in fight):
                df.loc[index, 'fight'] = fight.replace('ú', 'u')
            if('ę' in fight):
                df.loc[index, 'fight'] = fight.replace('ę', 'e')
            if('ã' in fight):
                df.loc[index, 'fight'] = fight.replace('ã', 'a')
            if('.' in fight):
                df.loc[index, 'fight'] = fight.replace('.', '')
            if('é' in fight): 
                df.loc[index, 'fight'] = fight.replace('é', 'e')
            if('ô' in fight):
                df.loc[index, 'fight'] = fight.replace('ô', 'o')
            if("'" in fight):
                df.loc[index, 'fight'] = fight.replace("'", '')
            if('ö' in fight):
                df.loc[index, 'fight'] = fight.replace('ö', 'o')
            if('í' in fight):
                df.loc[index, 'fight'] = fight.replace('í', 'i')
            if('ř' in fight):
                df.loc[index, 'fight'] = fight.replace('ř', 'r')
            if('-' in fight):
                df.loc[index, 'fight'] = fight.replace('-', ' ')
            if('â' in fight):
                df.loc[index, 'fight'] = fight.replace('â', 'a')
            if('Ľ' in fight):
                df.loc[index, 'fight'] = fight.replace('Ľ', 'L')
            if('ţ' in fight):
                df.loc[index, 'fight'] = fight.replace('ţ', 't')
            if('ł' in fight):
                df.loc[index, 'fight'] = fight.replace('ł', 'l')
            if('õ' in fight):
                df.loc[index, 'fight'] = fight.replace('õ', 'o')
            if('š' in fight):
                df.loc[index, 'fight'] = fight.replace('š', 's')
            if('ó' in fight):
                df.loc[index, 'fight'] = fight.replace('ó', 'o')
            if('ç' in fight):
                df.loc[index, 'fight'] = fight.replace('ç', 'c')
            if('ń' in fight):
                df.loc[index, 'fight'] = fight.replace('ń', 'n')
            if('ñ' in fight):
                df.loc[index, 'fight'] = fight.replace('ñ', 'n')
            if('ž' in fight):
                df.loc[index, 'fight'] = fight.replace('ž', 'z')
            
#clean redCorner, blueCorner, winner
for index, row in df2.iterrows():
    redCorner = row['redCorner']
    blueCorner = row['blueCorner']
    winner = row
    if(isinstance(redCorner, str)):
        if("'" in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace("'", '')
        if('.' in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace('.', '')
        if('-' in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace('-', ' ')
    if(isinstance(blueCorner, str)):
        if("'" in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace("'", '')
        if('.' in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace('.', '')
        if('-' in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace('-', ' ')
    if(isinstance(winner, str)):
        if("'" in winner):
            df2.loc[index, 'winner'] = winner.replace("'", '')
        if('.' in winner):
            df2.loc[index, 'winner'] = winner.replace('.', '')
        if('-' in winner):
            df2.loc[index, 'winner'] = winner.replace('-', ' ')
    

#define headers
column_headers = [
    'fight', 'redCorner', 'blueCorner', 'winner', 'event', 'referee', 'method_of_victory',
    'date', 'venue', 'title_fight', 'billing', 'redCorner_wins', 'blueCorner_wins',
    'redCorner_losses', 'blueCorner_losses', 'redCorner_draws', 'blueCorner_draws',
    'redCorner_age', 'blueCorner_age', 'redCorner_nation', 'blueCorner_nation',
    'redCorner_fan', 'blueCorner_fan', 'redCorner_knockdowns', 'blueCorner_knockdowns',
    'redCorner_sig_str', 'blueCorner_sig_str', 'redCorner_sig_str_percentage',
    'blueCorner_sig_str_percentage', 'redCorner_total_str', 'blueCorner_total_str',
    'redCorner_takedowns', 'blueCorner_takedowns', 'redCorner_takedown_percentage',
    'blueCorner_takedown_percentage', 'redCorner_subs_attempted', 'blueCorner_subs_attempted'
]

#create dataframe using headers
dfNew = pd.DataFrame(columns=column_headers)

#fix some inconsistencies
df2['redCorner'] = df2['redCorner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)
df2['winner'] = df2['winner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)
df2['winner'] = df2['winner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)

#fight overturned - only shown in one df
index = (df['fight'] == 'Miles Johns vs Dan Argueta') & (df['date'] == '09.23.2023')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df2['redCorner'] = df2['redCorner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)
df2['winner'] = df2['winner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)

df['fight'] = df['fight'].replace('Ian Machado Garry', 'Ian Garry', regex=True)
df['winner'] = df['winner'].replace('Ian Machado Garry', 'Ian Garry', regex=True)
df['loser'] = df['loser'].replace('Ian Machado Garry', 'Ian Garry', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)
df2['winner'] = df2['winner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)

df['fight'] = df['fight'].replace('Carl Deaton III', 'Carl Deaton', regex=True)
df['winner'] = df['winner'].replace('Carl Deaton III', 'Carl Deaton', regex=True)
df['loser'] = df['loser'].replace('Carl Deaton III', 'Carl Deaton', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)
df2['winner'] = df2['winner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)

df['fight'] = df['fight'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)
df['winner'] = df['winner'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)
df['loser'] = df['loser'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Katlyn Cerminara', 'Katlyn Chookagian', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Katlyn Cerminara', 'Katlyn Chookagian', regex=True)
df2['winner'] = df2['winner'].replace('Katlyn Cerminara', 'Katlyn Chookagian', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)
df2['winner'] = df2['winner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)
df2['winner'] = df2['winner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)
df2['winner'] = df2['winner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)
df2['winner'] = df2['winner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)

df['fight'] = df['fight'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)
df['winner'] = df['winner'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)
df['loser'] = df['loser'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)
df2['winner'] = df2['winner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)
df2['winner'] = df2['winner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)

df['fight'] = df['fight'].replace('Yanan Wu', 'Wu Yanan', regex=True)
df['winner'] = df['winner'].replace('Yanan Wu', 'Wu Yanan', regex=True)
df['loser'] = df['loser'].replace('Yanan Wu', 'Wu Yanan', regex=True)

df['fight'] = df['fight'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)
df['winner'] = df['winner'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)
df['loser'] = df['loser'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)
df2['winner'] = df2['winner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)

df['fight'] = df['fight'].replace('Des Green', 'Desmond Green', regex=True)
df['winner'] = df['winner'].replace('Des Green', 'Desmond Green', regex=True)
df['loser'] = df['loser'].replace('Des Green', 'Desmond Green', regex=True)

df['fight'] = df['fight'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)
df['winner'] = df['winner'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)
df['loser'] = df['loser'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)

df['fight'] = df['fight'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)
df['winner'] = df['winner'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)
df['loser'] = df['loser'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)

df['fight'] = df['fight'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)
df['winner'] = df['winner'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)
df['loser'] = df['loser'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)

df['fight'] = df['fight'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)
df['winner'] = df['winner'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)
df['loser'] = df['loser'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)
df2['winner'] = df2['winner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)

df['fight'] = df['fight'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)
df['winner'] = df['winner'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)
df['loser'] = df['loser'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)

df['fight'] = df['fight'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)
df['winner'] = df['winner'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)
df['loser'] = df['loser'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)

df['fight'] = df['fight'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)
df['winner'] = df['winner'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)
df['loser'] = df['loser'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)

#fight overturned
index = (df['fight'] == 'Alex Morono vs Niko Price') & (df['date'] == '02.04.2017')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df2['redCorner'] = df2['redCorner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)
df2['winner'] = df2['winner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)
df2['winner'] = df2['winner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)

df['fight'] = df['fight'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)
df['winner'] = df['winner'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)
df['loser'] = df['loser'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)

df['fight'] = df['fight'].replace('Mike Graves', 'Michael Graves', regex=True)
df['winner'] = df['winner'].replace('Mike Graves', 'Michael Graves', regex=True)
df['loser'] = df['loser'].replace('Mike Graves', 'Michael Graves', regex=True)

df['fight'] = df['fight'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)
df['winner'] = df['winner'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)
df['loser'] = df['loser'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)

df['fight'] = df['fight'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)
df['winner'] = df['winner'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)
df['loser'] = df['loser'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)

df['fight'] = df['fight'].replace('Ronald Stallings', 'Ron Stallings', regex=True)
df['winner'] = df['winner'].replace('Ronald Stallings', 'Ron Stallings', regex=True)
df['loser'] = df['loser'].replace('Ronald Stallings', 'Ron Stallings', regex=True)

df['fight'] = df['fight'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)
df['winner'] = df['winner'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)
df['loser'] = df['loser'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)

df['fight'] = df['fight'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)
df['winner'] = df['winner'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)
df['loser'] = df['loser'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)

df['fight'] = df['fight'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)
df['winner'] = df['winner'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)
df['loser'] = df['loser'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)

df['fight'] = df['fight'].replace('Robbie Peralta', 'Robert Peralta', regex=True)
df['winner'] = df['winner'].replace('Robbie Peralta', 'Robert Peralta', regex=True)
df['loser'] = df['loser'].replace('Robbie Peralta', 'Robert Peralta', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)
df2['winner'] = df2['winner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)

#fight overturned
index = (df['fight'] == 'Norifumi Yamamoto vs Roman Salazar') & (df['date'] == '02.28.2015')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df['fight'] = df['fight'].replace('Alexander Torres', 'Alex Torres', regex=True)
df['winner'] = df['winner'].replace('Alexander Torres', 'Alex Torres', regex=True)
df['loser'] = df['loser'].replace('Alexander Torres', 'Alex Torres', regex=True)

df['fight'] = df['fight'].replace('Pat Walsh', 'Patrick Walsh', regex=True)
df['winner'] = df['winner'].replace('Pat Walsh', 'Patrick Walsh', regex=True)
df['loser'] = df['loser'].replace('Pat Walsh', 'Patrick Walsh', regex=True)

df['fight'] = df['fight'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)
df['winner'] = df['winner'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)
df['loser'] = df['loser'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)

df['fight'] = df['fight'].replace('Dan Spohn', 'Daniel Spohn', regex=True)
df['winner'] = df['winner'].replace('Dan Spohn', 'Daniel Spohn', regex=True)
df['loser'] = df['loser'].replace('Dan Spohn', 'Daniel Spohn', regex=True)

df['fight'] = df['fight'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)
df['winner'] = df['winner'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)
df['loser'] = df['loser'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)

df['fight'] = df['fight'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)
df['winner'] = df['winner'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)
df['loser'] = df['loser'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)

#fight overturned
index = (df['fight'] == 'Louis Gaudinot vs Phil Harris') & (df['date'] == '03.08.2014')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df['fight'] = df['fight'].replace('Benny Alloway', 'Ben Alloway', regex=True)
df['winner'] = df['winner'].replace('Benny Alloway', 'Ben Alloway', regex=True)
df['loser'] = df['loser'].replace('Benny Alloway', 'Ben Alloway', regex=True)

df['fight'] = df['fight'].replace('Phil De Fries', 'Philip De Fries', regex=True)
df['winner'] = df['winner'].replace('Phil De Fries', 'Philip De Fries', regex=True)
df['loser'] = df['loser'].replace('Phil De Fries', 'Philip De Fries', regex=True)

df['fight'] = df['fight'].replace('Matt Riddle', 'Matthew Riddle', regex=True)
df['winner'] = df['winner'].replace('Matt Riddle', 'Matthew Riddle', regex=True)
df['loser'] = df['loser'].replace('Matt Riddle', 'Matthew Riddle', regex=True)

df['fight'] = df['fight'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)
df['winner'] = df['winner'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)
df['loser'] = df['loser'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)

df['fight'] = df['fight'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)
df['winner'] = df['winner'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)
df['loser'] = df['loser'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)

df['fight'] = df['fight'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)
df['winner'] = df['winner'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)
df['loser'] = df['loser'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)

df['fight'] = df['fight'].replace('Roli Delgado', 'Rolando Delgado', regex=True)
df['winner'] = df['winner'].replace('Roli Delgado', 'Rolando Delgado', regex=True)
df['loser'] = df['loser'].replace('Roli Delgado', 'Rolando Delgado', regex=True)

df['fight'] = df['fight'].replace('Dave Kaplan', 'David Kaplan', regex=True)
df['winner'] = df['winner'].replace('Dave Kaplan', 'David Kaplan', regex=True)
df['loser'] = df['loser'].replace('Dave Kaplan', 'David Kaplan', regex=True)

df['fight'] = df['fight'].replace('Mike Patt', 'Michael Patt', regex=True)
df['winner'] = df['winner'].replace('Mike Patt', 'Michael Patt', regex=True)
df['loser'] = df['loser'].replace('Mike Patt', 'Michael Patt', regex=True)

df['fight'] = df['fight'].replace('Thomas Speer', 'Tommy Speer', regex=True)
df['winner'] = df['winner'].replace('Thomas Speer', 'Tommy Speer', regex=True)
df['loser'] = df['loser'].replace('Thomas Speer', 'Tommy Speer', regex=True)

df['fight'] = df['fight'].replace('Douglas Evans', 'Doug Evans', regex=True)
df['winner'] = df['winner'].replace('Douglas Evans', 'Doug Evans', regex=True)
df['loser'] = df['loser'].replace('Douglas Evans', 'Doug Evans', regex=True)

df['fight'] = df['fight'].replace('Daniel Barrera', 'Dan Barrera', regex=True)
df['winner'] = df['winner'].replace('Daniel Barrera', 'Dan Barrera', regex=True)
df['loser'] = df['loser'].replace('Daniel Barrera', 'Dan Barrera', regex=True)

df['fight'] = df['fight'].replace('Allen Berubie', 'Allen Berube', regex=True)
df['winner'] = df['winner'].replace('Allen Berubie', 'Allen Berube', regex=True)
df['loser'] = df['loser'].replace('Allen Berubie', 'Allen Berube', regex=True)

df['fight'] = df['fight'].replace('Yoshitomi Mishima', 'Dokonjonosuke Mishima', regex=True)
df['winner'] = df['winner'].replace('Yoshitomi Mashima', 'Dokonjonosuke Mashima', regex=True)
df['loser'] = df['loser'].replace('Yoshitomi Mashima', 'Dokonjonosuke Mashima', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Steve Lynch', 'Steven Lynch', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Steve Lynch', 'Steven Lynch', regex=True)
df2['winner'] = df2['winner'].replace('Steve Lynch', 'Steven Lynch', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)
df2['winner'] = df2['winner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)

df['fight'] = df['fight'].replace('Josh Schockman', 'Josh Shockman', regex=True)
df['winner'] = df['winner'].replace('Josh Schockman', 'Josh Shockman', regex=True)
df['loser'] = df['loser'].replace('Josh Schockman', 'Josh Shockman', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)
df2['winner'] = df2['winner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)

df['fight'] = df['fight'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)
df['winner'] = df['winner'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)
df['loser'] = df['loser'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)

df['fight'] = df['fight'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)
df['winner'] = df['winner'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)
df['loser'] = df['loser'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)

df['fight'] = df['fight'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)
df['winner'] = df['winner'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)
df['loser'] = df['loser'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)

df['fight'] = df['fight'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)
df['winner'] = df['winner'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)
df['loser'] = df['loser'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)
df2['winner'] = df2['winner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)

df['fight'] = df['fight'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)
df['winner'] = df['winner'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)
df['loser'] = df['loser'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)

df['fight'] = df['fight'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)
df['winner'] = df['winner'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)
df['loser'] = df['loser'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)
df2['winner'] = df2['winner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)

df['fight'] = df['fight'].replace('John Campatella', 'John Campetella', regex=True)
df['winner'] = df['winner'].replace('John Campatella', 'John Campetella', regex=True)
df['loser'] = df['loser'].replace('John Campatella', 'John Campetella', regex=True)

df['fight'] = df['fight'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)
df['winner'] = df['winner'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)
df['loser'] = df['loser'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)

df['fight'] = df['fight'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)
df['winner'] = df['winner'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)
df['loser'] = df['loser'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)

#move row to be consistent with df2
row2move = df.loc[6663]
df = df.drop(6663)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:6671], pd.DataFrame([row2move]), df.iloc[6671:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7233]
df = df.drop(7233)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7239], pd.DataFrame([row2move]), df.iloc[7239:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7238]
df = df.drop(7238)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7235], pd.DataFrame([row2move]), df.iloc[7235:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7294]
df = df.drop(7294)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7300], pd.DataFrame([row2move]), df.iloc[7300:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7299]
df = df.drop(7299)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7296], pd.DataFrame([row2move]), df.iloc[7296:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7319]
df = df.drop(7319)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7320], pd.DataFrame([row2move]), df.iloc[7320:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7337]
df = df.drop(7337)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7338], pd.DataFrame([row2move]), df.iloc[7338:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7349]
df = df.drop(7349)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7347], pd.DataFrame([row2move]), df.iloc[7347:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7352]
df = df.drop(7352)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7350], pd.DataFrame([row2move]), df.iloc[7350:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7352]
df = df.drop(7352)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7351], pd.DataFrame([row2move]), df.iloc[7351:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7387]
df = df.drop(7387)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7388], pd.DataFrame([row2move]), df.iloc[7388:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7389]
df = df.drop(7389)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7392], pd.DataFrame([row2move]), df.iloc[7392:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7391]
df = df.drop(7391)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7389], pd.DataFrame([row2move]), df.iloc[7389:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7391]
df = df.drop(7391)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7390], pd.DataFrame([row2move]), df.iloc[7390:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7402]
df = df.drop(7402)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7401], pd.DataFrame([row2move]), df.iloc[7401:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7424]
df = df.drop(7424)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7425], pd.DataFrame([row2move]), df.iloc[7425:]], ignore_index=True)

#move row to be consistent with df2
row2move = df.loc[7427]
df = df.drop(7427)
#shift indices below row removed up one
df.reset_index(drop=True, inplace=True)
#place row where it needs to be
df = pd.concat([df.iloc[:7433], pd.DataFrame([row2move]), df.iloc[7433:]], ignore_index=True)



for (index, row), (index2, row2) in zip(df.iterrows(), df2.iterrows()):
    if(row['event'] == row2['event']):
        fight = row['fight'].split(' vs ')
        fighter1 = ''.join(sorted(str(fight[0]).replace(" ", "").lower()))
        fighter2 = ''.join(sorted(str(fight[1]).replace(" ", "").lower()))
        redCorner = ''.join(sorted(str(row2['redCorner']).replace(" ", "").lower()))
        blueCorner = ''.join(sorted(str(row2['blueCorner']).replace(" ", "").lower()))
        winner1 = ''.join(sorted(str(row['winner']).replace(" ", "").lower()))
        winner2 = ''.join(sorted(str(row2['winner']).replace(" ", "").lower()))
        if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
            if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                if(winner1 in winner2 or winner2 in winner1):
                    fight = row['fight']
                    redCorner = row2['redCorner']
                    blueCorner = row2['blueCorner']
                    winner = row2['winner']
                    event = row2['event']
                    referee = row2['referee']
                    method_of_vic = row2['method_of_victory']
                    date = row['date']
                    venue = row['venue']
                    title_fight = row['title_fight']
                    billing = row['billing']
                    if(winner1 in redCorner or redCorner in winner1):
                        redCorner_wins = row['winner_wins']
                        redCorner_losses = row['winner_losses']
                        redCorner_draws = row['winner_draws']
                        redCorner_age = row['winner_age']
                        redCorner_nation = row['winner_nationality']
                        redCorner_fan = row['winner_fan ']
                        blueCorner_wins = row['loser_wins']
                        blueCorner_losses = row['loser_losses']
                        blueCorner_draws = row['loser_draws']
                        blueCorner_age = row['loser_age']
                        blueCorner_nation = row['loser_nationality']
                        blueCorner_fan = row['loser_fan']
                    elif(winner1 in blueCorner or blueCorner in winner1):
                        blueCorner_wins = row['winner_wins']
                        blueCorner_losses = row['winner_losses']
                        blueCorner_draws = row['winner_draws']
                        blueCorner_age = row['winner_age']
                        blueCorner_nation = row['winner_nationality']
                        blueCorner_fan = row['winner_fan ']
                        redCorner_wins = row['loser_wins']
                        redCorner_losses = row['loser_losses']
                        redCorner_draws = row['loser_draws']
                        redCorner_age = row['loser_age']
                        redCorner_nation = row['loser_nationality']
                        redCorner_fan = row['loser_fan']
                    else:
                        if(fight[0] in redCorner or redCorner in fight[0]):
                            redCorner_wins = row['winner_wins']
                            redCorner_losses = row['winner_losses']
                            redCorner_draws = row['winner_draws']
                            redCorner_age = row['winner_age']
                            redCorner_nation = row['winner_nationality']
                            redCorner_fan = row['winner_fan ']
                            blueCorner_wins = row['loser_wins']
                            blueCorner_losses = row['loser_losses']
                            blueCorner_draws = row['loser_draws']
                            blueCorner_age = row['loser_age']
                            blueCorner_nation = row['loser_nationality']
                            blueCorner_fan = row['loser_fan']
                        if(fight[0] in blueCorner or blueCorner in fight[0]):
                            blueCorner_wins = row['winner_wins']
                            blueCorner_losses = row['winner_losses']
                            blueCorner_draws = row['winner_draws']
                            blueCorner_age = row['winner_age']
                            blueCorner_nation = row['winner_nationality']
                            blueCorner_fan = row['winner_fan ']
                            redCorner_wins = row['loser_wins']
                            redCorner_losses = row['loser_losses']
                            redCorner_draws = row['loser_draws']
                            redCorner_age = row['loser_age']
                            redCorner_nation = row['loser_nationality']
                            redCorner_fan = row['loser_fan']
                    redCorner_knockdowns = row2['red_Knockdowns']
                    blueCorner_knockdowns = row2['blue_Knockdowns']
                    redCorner_sig_str = row2['red_sig_str']
                    blueCorner_sig_str = row2['blue_sig_str']
                    redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                    blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                    redCorner_total_str = row2['red_total_strikes']
                    blueCorner_total_str = row2['blue_total_strikes']
                    redCorner_takedowns = row2['red_takedowns']
                    blueCorner_takedowns = row2['blue_takedowns']
                    redCorner_takedown_percentage = row2['red_takedown_percentage']
                    blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                    redCorner_subs_attempted = row2['red_subs_attempted']
                    blueCorner_subs_attempted = row2['blue_subs_attempted']      
            else:
                fight = row['fight'].split(' vs ')
                fighter1 = str(fight[0]).replace(" ", "").lower()
                fighter2 = str(fight[1]).replace(" ", "").lower()
                redCorner = str(row2['redCorner']).replace(" ", "").lower()
                blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                winner1 = str(row['winner']).replace(" ", "").lower()
                winner2 = str(row2['winner']).replace(" ", "").lower()
                if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                    if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                        if(winner1 in winner2 or winner2 in winner1):
                            fight = row['fight']
                            redCorner = row2['redCorner']
                            blueCorner = row2['blueCorner']
                            winner = row2['winner']
                            event = row2['event']
                            referee = row2['referee']
                            method_of_vic = row2['method_of_victory']
                            date = row['date']
                            venue = row['venue']
                            title_fight = row['title_fight']
                            billing = row['billing']
                            if(winner1 in redCorner or redCorner in winner1):
                                redCorner_wins = row['winner_wins']
                                redCorner_losses = row['winner_losses']
                                redCorner_draws = row['winner_draws']
                                redCorner_age = row['winner_age']
                                redCorner_nation = row['winner_nationality']
                                redCorner_fan = row['winner_fan ']
                                blueCorner_wins = row['loser_wins']
                                blueCorner_losses = row['loser_losses']
                                blueCorner_draws = row['loser_draws']
                                blueCorner_age = row['loser_age']
                                blueCorner_nation = row['loser_nationality']
                                blueCorner_fan = row['loser_fan']
                            elif(winner1 in blueCorner or blueCorner in winner1):
                                blueCorner_wins = row['winner_wins']
                                blueCorner_losses = row['winner_losses']
                                blueCorner_draws = row['winner_draws']
                                blueCorner_age = row['winner_age']
                                blueCorner_nation = row['winner_nationality']
                                blueCorner_fan = row['winner_fan ']
                                redCorner_wins = row['loser_wins']
                                redCorner_losses = row['loser_losses']
                                redCorner_draws = row['loser_draws']
                                redCorner_age = row['loser_age']
                                redCorner_nation = row['loser_nationality']
                                redCorner_fan = row['loser_fan']
                            else:
                                if(fight[0] in redCorner or redCorner in fight[0]):
                                    redCorner_wins = row['winner_wins']
                                    redCorner_losses = row['winner_losses']
                                    redCorner_draws = row['winner_draws']
                                    redCorner_age = row['winner_age']
                                    redCorner_nation = row['winner_nationality']
                                    redCorner_fan = row['winner_fan ']
                                    blueCorner_wins = row['loser_wins']
                                    blueCorner_losses = row['loser_losses']
                                    blueCorner_draws = row['loser_draws']
                                    blueCorner_age = row['loser_age']
                                    blueCorner_nation = row['loser_nationality']
                                    blueCorner_fan = row['loser_fan']
                                if(fight[0] in blueCorner or blueCorner in fight[0]):
                                    blueCorner_wins = row['winner_wins']
                                    blueCorner_losses = row['winner_losses']
                                    blueCorner_draws = row['winner_draws']
                                    blueCorner_age = row['winner_age']
                                    blueCorner_nation = row['winner_nationality']
                                    blueCorner_fan = row['winner_fan ']
                                    redCorner_wins = row['loser_wins']
                                    redCorner_losses = row['loser_losses']
                                    redCorner_draws = row['loser_draws']
                                    redCorner_age = row['loser_age']
                                    redCorner_nation = row['loser_nationality']
                                    redCorner_fan = row['loser_fan']
                            redCorner_knockdowns = row2['red_Knockdowns']
                            blueCorner_knockdowns = row2['blue_Knockdowns']
                            redCorner_sig_str = row2['red_sig_str']
                            blueCorner_sig_str = row2['blue_sig_str']
                            redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                            blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                            redCorner_total_str = row2['red_total_strikes']
                            blueCorner_total_str = row2['blue_total_strikes']
                            redCorner_takedowns = row2['red_takedowns']
                            blueCorner_takedowns = row2['blue_takedowns']
                            redCorner_takedown_percentage = row2['red_takedown_percentage']
                            blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                            redCorner_subs_attempted = row2['red_subs_attempted']
                            blueCorner_subs_attempted = row2['blue_subs_attempted'] 
        else:
            fight = row['fight'].split(' vs ')
            fighter1 = str(fight[0]).replace(" ", "").lower()
            fighter2 = str(fight[1]).replace(" ", "").lower()
            redCorner = str(row2['redCorner']).replace(" ", "").lower()
            blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
            winner1 = str(row['winner']).replace(" ", "").lower()
            winner2 = str(row2['winner']).replace(" ", "").lower()
            if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                    if(winner1 in winner2 or winner2 in winner1):
                        fight = row['fight']
                        redCorner = row2['redCorner']
                        blueCorner = row2['blueCorner']
                        winner = row2['winner']
                        event = row2['event']
                        referee = row2['referee']
                        method_of_vic = row2['method_of_victory']
                        date = row['date']
                        venue = row['venue']
                        title_fight = row['title_fight']
                        billing = row['billing']
                        if(winner1 in redCorner or redCorner in winner1):
                            redCorner_wins = row['winner_wins']
                            redCorner_losses = row['winner_losses']
                            redCorner_draws = row['winner_draws']
                            redCorner_age = row['winner_age']
                            redCorner_nation = row['winner_nationality']
                            redCorner_fan = row['winner_fan ']
                            blueCorner_wins = row['loser_wins']
                            blueCorner_losses = row['loser_losses']
                            blueCorner_draws = row['loser_draws']
                            blueCorner_age = row['loser_age']
                            blueCorner_nation = row['loser_nationality']
                            blueCorner_fan = row['loser_fan']
                        elif(winner1 in blueCorner or blueCorner in winner1):
                            blueCorner_wins = row['winner_wins']
                            blueCorner_losses = row['winner_losses']
                            blueCorner_draws = row['winner_draws']
                            blueCorner_age = row['winner_age']
                            blueCorner_nation = row['winner_nationality']
                            blueCorner_fan = row['winner_fan ']
                            redCorner_wins = row['loser_wins']
                            redCorner_losses = row['loser_losses']
                            redCorner_draws = row['loser_draws']
                            redCorner_age = row['loser_age']
                            redCorner_nation = row['loser_nationality']
                            redCorner_fan = row['loser_fan']
                        else:
                            if(fight[0] in redCorner or redCorner in fight[0]):
                                redCorner_wins = row['winner_wins']
                                redCorner_losses = row['winner_losses']
                                redCorner_draws = row['winner_draws']
                                redCorner_age = row['winner_age']
                                redCorner_nation = row['winner_nationality']
                                redCorner_fan = row['winner_fan ']
                                blueCorner_wins = row['loser_wins']
                                blueCorner_losses = row['loser_losses']
                                blueCorner_draws = row['loser_draws']
                                blueCorner_age = row['loser_age']
                                blueCorner_nation = row['loser_nationality']
                                blueCorner_fan = row['loser_fan']
                            if(fight[0] in blueCorner or blueCorner in fight[0]):
                                blueCorner_wins = row['winner_wins']
                                blueCorner_losses = row['winner_losses']
                                blueCorner_draws = row['winner_draws']
                                blueCorner_age = row['winner_age']
                                blueCorner_nation = row['winner_nationality']
                                blueCorner_fan = row['winner_fan ']
                                redCorner_wins = row['loser_wins']
                                redCorner_losses = row['loser_losses']
                                redCorner_draws = row['loser_draws']
                                redCorner_age = row['loser_age']
                                redCorner_nation = row['loser_nationality']
                                redCorner_fan = row['loser_fan']
                        redCorner_knockdowns = row2['red_Knockdowns']
                        blueCorner_knockdowns = row2['blue_Knockdowns']
                        redCorner_sig_str = row2['red_sig_str']
                        blueCorner_sig_str = row2['blue_sig_str']
                        redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                        blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                        redCorner_total_str = row2['red_total_strikes']
                        blueCorner_total_str = row2['blue_total_strikes']
                        redCorner_takedowns = row2['red_takedowns']
                        blueCorner_takedowns = row2['blue_takedowns']
                        redCorner_takedown_percentage = row2['red_takedown_percentage']
                        blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                        redCorner_subs_attempted = row2['red_subs_attempted']
                        blueCorner_subs_attempted = row2['blue_subs_attempted'] 
    column_vals = {
        'fight': fight,
        'redCorner': redCorner,
        'blueCorner': blueCorner,
        'winner': winner,
        'event': event,
        'referee': referee,
        'method_of_victory': method_of_vic,
        'date': date,
        'venue': venue,
        'title_fight': title_fight,
        'billing': billing,
        'redCorner_wins': redCorner_wins,
        'blueCorner_wins': blueCorner_wins,
        'redCorner_losses': redCorner_losses,
        'blueCorner_losses': blueCorner_losses,
        'redCorner_draws': redCorner_draws,
        'blueCorner_draws': blueCorner_draws,
        'redCorner_age': redCorner_age,
        'blueCorner_age': blueCorner_age,
        'redCorner_nation': redCorner_nation,
        'blueCorner_nation': blueCorner_nation,
        'redCorner_fan': redCorner_fan,
        'blueCorner_fan': blueCorner_fan,
        'redCorner_knockdowns': redCorner_knockdowns,
        'blueCorner_knockdowns': blueCorner_knockdowns,
        'redCorner_sig_str': redCorner_sig_str,
        'blueCorner_sig_str': blueCorner_sig_str,
        'redCorner_sig_str_percentage': redCorner_sig_str_percentage,
        'blueCorner_sig_str_percentage': blueCorner_sig_str_percentage,
        'redCorner_total_str': redCorner_total_str,
        'blueCorner_total_str': blueCorner_total_str,
        'redCorner_takedowns': redCorner_takedowns,
        'blueCorner_takedowns': blueCorner_takedowns,
        'redCorner_takedown_percentage': redCorner_takedown_percentage,
        'blueCorner_takedown_percentage': blueCorner_takedown_percentage,
        'redCorner_subs_attempted': redCorner_subs_attempted,
        'blueCorner_subs_attempted': blueCorner_subs_attempted
    }
    dfNew.loc[len(dfNew)] = column_vals



dfNew.to_csv('database.csv', index=False)



