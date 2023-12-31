import subprocess
from typing import NamedTuple
import logging
import os
import constants as c
import argparse

CONFIG_BIG_VIDEO = [
    '-x',
    '--no-overwrites',
]


class MusicInfo(NamedTuple):
    title: str
    url: str
    end_time: str
    timestamps: str


def path_friendly(path: str) -> str:
    to_remove = '/:*?"<>|'
    for ch in to_remove:
        path = path.replace(ch, '')
    return path


music = [
    MusicInfo(
        path_friendly('Peaceful Jeremy Soule #1'),
        'https://www.youtube.com/watch?v=cbqxazYJp_U',
        '3:50:38',
        """
            The Streets of Whiterun (Skyrim) 0:00:00
            Awake (Skyrim) 0:04:01
            From Past to Present (Skyrim) 0:05:33
            Unbroken Road (Skyrim) 0:10:37
            Ancient Stones (Skyrim) 0:17:00
            The City Gates (Skyrim) 0:21:44
            Dragonsreach (Skyrim) 0:25:30
            Under an Ancient Sun (Skyrim) 0:27:51
            Masser (Skyrim) 0:31:31
            Distant Horizons (Skyrim) 0:37:35
            Dawn (Skyrim) 0:41:28
            The Jerall Mountains (Skyrim) 0:45:25
            Secunda (Skyrim) 0:48:41
            Imperial Throne (Skyrim) 0:50:44
            Frostfall (Skyrim) 0:53:00
            Kyne's Peace (Skyrim) 0:56:24
            Unbound (Skyrim) 1:00:13
            Far Horizons (Skyrim) 1:01:46
            A Winter's Tale (Skyrim) 1:07:16
            The Bannered Mare (Skyrim) 1:10:36
            The White River (Skyrim) 1:13:04
            Standing Stones (Skyrim) 1:16:33
            Tundra (Skyrim) 1:23:09
            Journey's End (Skyrim) 1:26:56
            Before the Storm (Skyrim) 1:31:03
            A Chance Meeting (Skyrim) 1:32:08
            Out of the Cold (Skyrim) 1:35:18
            Around the Fire (Skyrim) 1:38:18
            Aurora (Skyrim) 1:41:27
            Solitude (Skyrim) 1:48:46
            The Gathering Storm (Skyrim) 1:50:56
            Sky Above, Voice Within (Skyrim) 1:53:48
            Wind Guide You (Skyrim) 1:57:45
            Through the Valleys (Oblivion) 2:06:48
            Harvest Dawn (Oblivion) 2:11:07
            King and Country (Oblivion) 2:13:58
            Wings of Kynareth (Oblivion) 2:18:03
            All's Well (Oblivion) 2:21:33
            Watchman's Ease (Oblivion) 2:23:58
            Glory of Cyrodiil (Oblivion) 2:26:03
            Minstrel's Lament (Oblivion) 2:28:31
            Auriel's Ascension (Oblivion) 2:33:13
            Sunrise of Flutes (Oblivion) 2:36:18
            Dusk At the Market (Oblivion) 2:39:14
            Peace of Akatosh (Oblivion) 2:41:25
            Nerevar Rises (Morrowind) 2:45:36
            Peaceful Waters (Morrowind) 2:46:35
            Over the Next Hill (Morrowind) 2:49:41
            The Road Most Travelled (Morrowind) 2:52:46
            Blessing of Vivec (Morrowind) 2:56:01
            Shed Your Travails (Morrowind) 2:59:17
            Caprice (Morrowind) 3:02:30
            Darkened Depths (Morrowind) 3:05:58
            The Prophecy Fulfilled (Morrowind) 3:06:49
            Skyrim Atmospheres (Skyrim) 3:08:01 """
    ),
    MusicInfo(
        path_friendly('Hotline Miami Soundtrack'),
        'https://www.youtube.com/watch?v=oKD-MVfC9Ag',
        '1:31:33',
        """
            00:00    1. Sun Araw - Horse Steppin
            10:10    2. M O O N - Hydrogen
            14:59    3. M O O N - Paris
            19:02    4. M O O N - Crystals
            23:59    5. Sun Araw - Deep Cover
            32:12    6. Jasper Byrne - Miami
            35:32    7. Jasper Byrne - Hotline
            38:44    8. Scattle - Knock Knock
            42:48    9. Elliott Berlin - Musikk per automatikk
            45:38   10. Perturbator - Miami Disco
            50:09   11. M O O N - Release
            56:11   12. Eirik Suhrke - A New Morning
            58:40   13. Scattle - Flatline
            1:00:54 14. Coconuts - Silver Lights
            1:07:30 15. El Huervo feat. Shelby Cinca - Daisuke
            1:10:03 16. El Huervo - Turf Intro
            1:11:23 17. El Huervo - Turf Main
            1:14:15 18. El Huervo - Crush
            1:16:55 19. Perturbator - Electric Dreams
            1:21:40 20. Scattle - Inner Animal
            1:25:21 21. Scattle - Its Safe Now
            1:28:05 22. Hotline Miami - Static (Bonus)
            1:30:03 23. Scattle - To The Top   (Bonus)
            """
    ),
    MusicInfo(
        path_friendly('Castlevania SOTN + Songs Saturn'),
        'https://www.youtube.com/watch?v=eRmpU0RZOdU',
        '1:44:23',
        """
            01. Metamorphosis 0:00
            02. Prologue 1:02
            03. Dance of Illusions 2:29
            04. Moonlight Nocturne 3:49
            05. Prayer 5:34
            06. Dracula's Castle 6:31
            07. Dance of Gold 8:24
            08. Marble Gallery 10:16
            09. Tower of Mist 11:40
            10. Nocturne 14:27
            11. Wood Carving Partita 16:47
            12. Door of Holy Spirits 19:31
            13. Festival of Servants 20:59
            14. Land of Benediction 22:50
            15. Requiem For the Gods 23:08
            16. Crystal Teardrops 25:17
            17. Abandoned Pit 27:19
            18. Rainbow Cemetery 29:32
            19. Silence 32:18
            20. Lost Painting 32:36
            21. Dance of Pales 34:17
            22. Curse Zone 36:48
            23. Enchanted Banquet 38:04
            24. Wandering Ghosts 40:12
            25. The Tragic Prince 43:03
            26. The Door to the Abyss 47:08
            27. Heavenly Doorway 48:54
            28. Death Ballad 50:45
            29. Blood Relations 52:26
            30. Metamorphosis II 54:00
            31. Final Toccata 54:37
            32. Black Banquet 59:48
            33. Metamorphosis III 1:02:41
            34. I am the Wind [Cynthia Harrell] 1:03:28
            35. Bonus Track 1:08:04
            36. The Master Librarian 1:12:16
            37. Chaconne C Moll [Saturn] 1:13:52
            38. Vampire Killer Rock [Saturn] 1:18:37
            39. Vampire Killer Techno-goth [Saturn] 1:22:02
            40. Beginning Techno-goth [Saturn] 1:24:52
            41. Beginning Jazz [Saturn] 1:30:01
            42. Bloody Tears Hard Rock Version A [Saturn] 1:35:08
            43. Bloody Tears Hard Rock Version B [Saturn] 1:37:46
            44. Guardian [Saturn] 1:42:04
            """
    ),
    MusicInfo(
        path_friendly('Baba is You OST'),
        'https://www.youtube.com/watch?v=dVyd_hAq6G4',
        '1:27:11',
        """
            0:00:00 1. Baba is You
            0:03:45 2. on the island
            0:06:41 3. Wall is Stop ...for Starting Off
            0:10:38 4. Water is Sink... for The Lake
            0:14:46 5. Cog is Push... for Solitary Isle
            0:18:44 6. Leaf is Move... for Forest of Fall
            0:22:20 7. Bos has Key... for Temple Ruins
            0:26:57 8. Tree is Shift... for Deep Forest
            0:30:50 9. Rocket is Dust... for Space
            0:37:06 10. Fruit on Grass... for The Garden
            0:42:44 11. Lava is Hot... for The Cavern
            0:49:08 12. Bird is Float... for The Mountain
            0:54:06 13. Crystal is Still... for Crystal Cave
            0:57:44 14. Reed is Sad... for The Rain
            1:03:31 15. Baba Fear Ghost... for Haunted Field
            1:09:47 16. Cursor is Select... for the Level Editor
            1:20:08 17. Keke is Party... for the Jamming
            1:24:44 18. Flag is Win... Ending Theme
        """
    ),
    MusicInfo(
        path_friendly('TNT: Evilution - MUSIC COVER'),
        'https://www.youtube.com/watch?v=He3F4CQFZVY',
        '37:42',
        """
            00:00 - Ruined World
            00:19 - Sadistic
            04:31 - Smells Like Burning Corpse
            08:28 - Death's Bells
            11:15 - More
            13:10 - Agony Rhapsody
            15:07 - Soldier of Chaos
            17:00 - Into the Beast's Belly
            19:34 - Infinite
            22:45 - Let's Kill at Will
            25:07 - Cold Subtleness
            27:51 - Blood Jungle
            31:23 - Horizon
            33:11 - AimShootKill
            34:43 - Legion of the Lost
    """
    ),
    MusicInfo(
        path_friendly('Castlevania 3 Soundtrack Remastered'),
        'https://www.youtube.com/watch?v=UwIQ3nBZ4Dw',
        '32:25',
        """
            01. 00:00 Prelude
            02. 01:42 Epitaph
            03. 02:30 Prayer
            04. 02:42 Beginning
            05. 04:39 BOSS FIGHT
            06. 05:47 Stage Clear
            07. 05:53 Destiny
            08. 06:26 Clockwork
            09. 07:55 Mad Forest
            10. 09:28 Anxiety
            11. 11:39 Rising
            12. 13:25 Stream
            13. 14:43 Dead Beat
            14. 16:16 Nightmare
            15. 17:50 Encounter
            16. 18:32 Aquarius
            17. 20:03 Demon Seed
            18. 21:35 Deja Vu (Vampire Killer)
            19. 22:38 Riddle
            20. 24:07 Pressure
            21. 24:45 Overture
            22. 26:49 Big Battle
            23. 28:09 Bigger Battle
            24. 29:26 All Clear!
            25. 29:36 Evergreen
            26. 30:43 Flashback
            27. 31:56 Ooooops!
            28. 32:00 Game Over
     """
    ),
    MusicInfo(
        path_friendly('Quake Champions: Doom Edition'),
        'https://www.youtube.com/watch?v=ne6_AsTRZd4',
        '1:56:00',
        """
            00:00 Slipgate
            02:16 Augmented
            05:37 Inferno
            09:30 Dune
            13:38 Phobos (Doom Cover)
            16:23 Conflagration
            19:22 The Abyss
            23:18 Geist
            28:18 Quad Machine (Quake 2 Cover)
            31:57 Infuscomus (Blood Cover)
            35:03 Xenomorph
            38:08 Shodan
            41:51 Devil
            45:33 Descent into Cerberon (Quake 2 Cover)
            48:53 Deimos
            53:15 Grabbag (Duke Nukem Cover)
            55:28 Durandal (Marathon 2 Cover)
            58:59 G M G
            01:02:06 Wraith
            01:06:00 Vyper
            01:09:04 Wolfenstein Metal Remix
            01:12:52 Doomed
            01:15:26 Crusade
            01:20:04 For the Makron
            01:25:04 Nightmare
            01:30:24 Ballet
            01:34:52 Eternal
            01:40:56 Bull Rush
            01:45:33 Incendimus
            01:51:51 Punk's Not Dead
     """
    ),
    MusicInfo(
        path_friendly('The Elder Scrolls II: Daggerfall OST'),
        'https://www.youtube.com/watch?v=CqUCz7E1s90',
        '2:34:40',
        """
            0:00:00 01 - Intro Cinematic
            0:02:01 02 - Day Theme 1 - A Beautiful Day in the City - 29
            0:03:07 03 - Day Theme 2 - Day
            0:05:17 04 - Day Theme 3 - Sunny Day
            0:06:05 05 - Day Theme 4 - Sunny Day 2
            0:06:56 06 - Day Theme 5 - Swimming
            0:08:21 07 - Day Theme 6 - 02
            0:09:44 08 - Day Theme 7 - 03
            0:11:24 09 - Day Theme 8 - 12
            0:12:26 10 - Day Theme 9 - 13
            0:13:37 11 - Day Theme 10 - 22
            0:15:28 12 - Night Theme 1 - Daggerfall Nights - 11
            0:17:23 13 - Night Theme 2 - Curse
            0:19:11 14 - Night Theme 3 - Eerie
            0:20:48 15 - Night Theme 4 - Ruins
            0:22:34 16 - Night Theme 5 - On the Ship - 18
            0:24:07 17 - Night Theme 6 - 10
            0:27:07 18 - Night Theme 7 - 21
            0:28:36 19 - Rain Theme 1 - Overcast
            0:29:22 20 - Rain Theme 2 - Overcast (Long version)
            0:31:03 21 - Rain Theme 3 - Raining
            0:32:21 22 - Rain Theme 4 - 08
            0:33:42 23 - Snow Theme 1 - Snow Over Northmoor
            0:35:16 24 - Snow Theme 2 - Snowing
            0:36:42 25 - Snow Theme 3 - Oversnow
            0:38:06 26 - Snow Theme 4 - 20
            0:39:21 27 - Interior Theme - Fireplace - 23
            0:40:25 28 - Mage's Guild Theme 1 - Mage
            0:41:33 29 - Mage's Guild Theme 2 - Magic
            0:43:01 30 - Shop Theme - General Shop
            0:44:14 31 - Tavern Theme 1 - Folk 1
            0:44:44 32 - Tavern Theme 2 - Folk 2
            0:45:20 33 - Tavern Theme 3 - Folk 3
            0:45:50 34 - Tavern Theme 4 - Square
            0:46:24 35 - Tavern Theme 5 - Tavern
            0:46:58 36 - Temple Theme 1 - Bad
            0:48:36 37 - Temple Theme 2 - Good
            0:50:07 38 - Temple Theme 3 - Neutral
            0:51:12 39 - Castle Theme - Palace
            0:52:50 40 - Palace Theme - 06
            0:54:21 41 - Dungeon Theme 1 - Privateer's Hold
            0:58:04 42 - Dungeon Theme 2 - The Mantellan Crux - 04
            0:59:32 43 - Dungeon Theme 3 - 05
            1:05:08 44 - Dungeon Theme 4 - Dungeon 4
            1:08:11 45 - Dungeon Theme 5 - Dungeon 5
            1:10:11 46 - Dungeon Theme 6 - Dungeon 6
            1:12:11 47 - Dungeon Theme 7 - Dungeon 7
            1:14:11 48 - Dungeon Theme 8 - Dungeon 8
            1:18:56 49 - Dungeon Theme 9 - Dungeon 9
            1:20:55 50 - Dungeon Theme 10 - Dungeon 10
            1:23:21 51 - Dungeon Theme 11 - Dungeon 11
            1:25:27 52 - Dungeon Theme 12 - GDUNGN9
            1:27:49 53 - Dungeon Theme 13 - 07
            1:29:55 54 - Dungeon Theme 14 - Castle Dungeon - 15
            1:31:03 55 - Dungeon Theme 15 - 28
            1:32:39 56 - Unused Dungeon Theme - D1
            1:36:16 57 - Unused Dungeon Theme - D2
            1:40:09 58 - Unused Dungeon Theme - D3
            1:43:40 59 - Unused Dungeon Theme - D4
            1:47:34 60 - Unused Dungeon Theme - D5
            1:53:17 61 - Unused Dungeon Theme - D6
            1:58:01 62 - Unused Dungeon Theme - D7
            2:01:12 63 - Unused Dungeon Theme - D8
            2:05:15 64 - Unused Dungeon Theme - D9
            2:10:51 65 - Unused Dungeon Theme - D10
            2:14:15 66 - Unused Sneaking Theme 1 - Sneaking
            2:15:36 67 - Unused Sneaking Theme 2 - Sneaking 2
            2:16:49 68 - Unused Sneaking Theme 3 - Sneaking 3
            2:19:06 69 - Unused Sneaking Theme 4 - At Home - 16
            2:20:11 70 - Unused Sneaking Theme 5 - 09
            2:21:13 71 - Unused Sneaking Theme 6 - 25
            2:22:24 72 - Unused Sneaking Theme 7 - 30
            2:24:06 73 - Unused Theme - 17
            2:25:12 74 - Daggerfall Demo Theme (Bonus) - DAG_3
            2:26:41 75 - Website Midi Release Track 1 (Bonus) - DAG_2
            2:27:45 76 - Website Midi Release Track 2 (Bonus) - DAG_6
            2:28:42 77 - Website Midi Release Track 3 (Bonus) - DAG_7
            2:30:51 78 - Website Midi Release Track 4 (Bonus) - DAG_10
            2:32:09 79 - Website Midi Release Track 5 (Bonus) - DAG_12
            2:33:48 80 - Music Test
     """
    ),
    MusicInfo(
        path_friendly('Mega Drive - 198XAD'),
        'https://www.youtube.com/watch?v=l3NoYyNKSXQ',
        '1:09:44',
        """
            1. Infiltrate 0:00
            2. Acid Spit 1:20
            3. NARC 6:02
            4. Memory Dealer 10:45
            5. Osaka Sewers 15:47
            6. Exoskeleton 20:07
            7. Murderlize 'em 25:44
            8. Haunted (Hunted) 30:27
            9. Edge of Reality 33:59
            10. Video Stalker 39:27
            11. The Reducer 43:14
            12. Slum Lord 47:45
            13. Zero Point Non-Response 52:45
            14. Only One 58:15
     """
    ),
    MusicInfo(
        path_friendly('Mega Drive - 199XAD'),
        'https://www.youtube.com/watch?v=k40GsYoQgNo',
        '57:20',
        """
            00:00  Operator
            02:12  Gun Hag
            06:55  NARC
            12:44  Crypt Dive
            17:38  Nikita
            22:30  Orbital Strike
            26:54  SKULjammer
            32:11  H exe
            35:28  Streets of Fire
            41:04  Terror Eyes
            46:16  Source Code
            51:10  Active Denial System
     """
    ),
    MusicInfo(
        path_friendly('Mega Drive - Seas Of Infinity'),
        'https://www.youtube.com/watch?v=CrHRv11O9Cg',
        '53:41',
        """
            01. Seas Of Infinity 0:00
            02. Godspeed Us To The Stars 2:07
            03. Biohacker 6:43
            04. Junkhead 11:54
            05. No Fate 16:04
            06. Initializing 21:49
            07. Off/World 22:07
            08. Run The Code 26:39
            09. Cesaro Totality 32:23
            10. Visceral Grit ’92 33:22
            11. In Dreams 38:52
     """
    ),
    MusicInfo(
        path_friendly('КОРОЛЬ И ШУТ'),
        'https://www.youtube.com/watch?v=0-C0lCPFTj8',
        '2:53:11',
        """
            01. Лесник 00:00
            02. Прыгну со скалы 03:09
            03. Ели мясо мужики 06:21
            04. Ром 08:36
            05. Кукла колдуна 11:17
            06. Проклятый старый дом 14:40
            07. Гимн шута 18:59
            08. Воспоминания о былой любви 24:01
            09. Мертвый Анархист 28:51
            10. Танец злобного гения 32:57
            11. Дурак и молния 36:55
            12. Камнем по голове 38:48
            13. Месть Гарри 41:24
            14. Марионетки 44:32
            15. Фред 48:10
            16. Северный флот 51:32
            17. Любовь и пропеллер 53:43
            18. Внезапная голова 56:37
            19. Отражение 59:02
            20. Хардкор по-русски 01:04:34
            21. От женщин кругом голова 01:07:27
            22. Маска 01:08:56
            23. Два вора и монета 01:13:40
            24. Жаль, нет Ружья! 01:15:54
            25. Медведь 01:19:33
            26. Волосокрад 01:23:04
            27. Тайна хозяйки старинных часов 01:27:31
            28. Рогатый 01:31:03
            29. Смельчак и ветер 01:34:19
            30. Мария 01:37:17
            31. Некромант 01:41:21
            32. Девушка и Граф 01:44:04
            33. Охотник 01:48:36
            34. Валет и Дама 01:51:09
            35. Мастер приглашает в гости 01:54:38
            36. Невеста палача 01:57:51
            37. Помнят с горечью древляне 02:02:11
            38. Блуждают тени 02:06:04
            39. Возвращение колдуна 02:08:14
            40. Парень и леший 02:11:30
            41. Утопленник 02:15:42
            42. Вдова и Горбун 02:19:44
            43. Идол 02:22:54
            44. Гробовщик 02:25:55
            45. Дочь вурдалака 02:29:47
            46. Писатель Гудвин 02:33:56
            47. Джокер 02:37:03
            48. Дагон 02:40:20
            49. Двое против всех 02:45:24
            50. Фокусник 02:49:18
     """
    ),
    MusicInfo(
        path_friendly('TheGreatKingKukuiYumeNikki'),
        c.NO_URL,
        '3:00:58',
        """
            Nikki Title Screen 0:00
            Working Please Wait 2:27
            Dream Room 4:54
            Dark World 7:08
            Martian Underground 9:42
            Shield-Folk World 12:24
            Snow World 14:55
            Barracks Settlement 17:36
            Flue Player 20:11
            Windmill World 22:48
            Dense Woods B 25:08
            The Pink Sea 27:46
            Checkered Tile Path 30:34
            Poniko's Room (Lights on) 33:13
            Poniko's Room (Lights off) 35:54
            Sky Garden 38:40
            Witch Flight 41:28
            Mars 44:06
            FC Locations 46:50
            FC Dungeon 49:28
            The End 52:07
            2kki Title Screen 54:50
            Computer (Default) 55:55
            Black Building 57:04
            Seagull 58:06
            Snowy Pipe Organ 59:32
            Sewers 01:00:41
            Hand Hub 01:02:03
            Garden World 01:05:30
            Space 01:06:26
            Tapir-San 01:07:57
            Shinto Shrine 01:09:18
            Scenic Outlook 01:10:19
            Heart Room 01:11:28
            Blue Forest 01:12:28
            Mosenite 01:13:36
            qs0UrDFJ-bgm041 01:14:42
            Library 01:15:42
            Bug effect room 01:16:51
            Sky Kingdom 01:17:55
            Overgrown City (deeper section) 01:19:08
            Pink Tanuki Road 01:20:07
            Mask Shop 01:21:11
            Dressing Room 01:22:30
            Pastel Blue House 01:23:36
            Kura Puzzle Complete! 01:24:40
            Bug Maze 01:25:39
            Gakuran 01:26:39
            Sugar World (Purple) 01:27:50
            Underwater Amusement Park (Brown Eye Floor Area) 01:28:58
            The Ceiling 01:29:57
            Lotus Waters 01:31:02
            The Deciding Street 01:32:20
            bgm6 01:33:41
            Cosmic World 01:34:50
            Rainbow Silhoutte World 01:36:18
            Fairy Tale Path 01:37:10
            Galactic Park 01:38:11
            Grey Road 01:39:20
            Sunken City 01:40:24
            Fairy Tale Woods (Apple House)/Bridged Swamp Islands 01:41:14
            Green Neon World 01:42:13
            Grass World (Pond room) 01:43:14
            Forest Pier 01:44:14
            Grass World Studio 01:45:13
            Cog Maze 01:46:13
            Circus in the Forest 01:47:09
            Grass World (Vine Corridor) 01:48:10
            Alley Robot World 01:49:07
            Coffeeman 01:50:18
            Forest 01:51:24
            Ocean Floor 01:52:25
            Black Cat 01:53:33
            Jigsaw Puzzle World (Night Sky) 01:54:43
            Bleak Future (Prelude) 01:55:27
            Helmet Girl's Apartment 01:56:26
            Prismatic Tent 01:58:24
            Hidden Shoal 01:59:24
            Sea Sponge Path 02:00:35
            Cocktail Lounge 02:01:26
            Broken City 02:02:24
            Abandoned Apartments (Lower Apartments) 02:03:28
            Green Butterfly Area 02:04:31
            Neon Candle World 02:05:27
            Ending #3 (Fall) 02:06:18
            Underwater 02:06:48
            Way to Rainbow Maze 02:07:50
            Overgrown Islands 02:08:51
            The Sewers 02:09:54
            Sugar Hole (Back Rooms) 02:10:56
            Starry Pier (Oreko) 02:11:55
            Microscopic World (Gas) 02:12:55
            Microscopic World (Clear Gas) 02:13:57
            Sugar Hole 02:14:49
            Alleyway Hospital 02:15:49
            Industrial Snow World 02:16:47
            Deep Plant Labyrinth (Past) 02:17:47
            Plant Labyrinth (Past) 02:18:56
            Bound by Flesh 02:20:05
            FC Overworld 02:21:35
            A Small White Room 02:23:00
            Monochrome World 02:24:03
            Apartments 02:25:23
            Teleporters 02:26:50
            Ghost Garden to Underwater Path 02:28:29
            Downtown 02:30:01
            Endless 02:31:31
            Plant_A 02:32:57
            Lost 02:33:53
            Water 02:34:58
            Drop 02:35:54
            Sky 02:36:59
            Wind_A 02:37:59
            Drop_A 02:38:58
            Save 02:39:56
            Mist 02:40:56
            Snow 02:42:02
            Wind Chimes 02:43:11
            Underwater Lab 02:44:11
            Unanswered Prayer 02:45:07
            Thunderstorm 02:46:07
            Spirit Town 02:47:02
            Snowy 02:48:09
            Recollection 02:49:17
            Rain Indoors 02:50:21
            Ocean Depths 02:51:21
            Ocean 02:52:25
            Lotus 02:53:28
            Hollow Place 02:54:26
            Forest Loop 02:55:28
            Colors 02:56:32
            Cicadas 02:57:28
            Chimiko 02:58:08
            AP-Echonio 02:59:00
            Rain Indoors w Thunder 02:59:57
     """
    ),
    MusicInfo(
        path_friendly('Yume Nikki 2kki Sleep Mix Naked flames'),
        'https://youtu.be/4XPBqvUfHwo',
        '1:20:04',
        """
            0:00 - Green Neon World - Yume 2kki
            1:53 - Forest Carnival - Yume 2kki
            3:21 - Forest Carnival (Lantern & Ladders) - Yume 2kki
            5:06 - Snow World - Yume Nikki
            6:13 - Depths - Yume 2kki
            7:22 - Madotsuki's Dream Room - Yume Nikki
            7:54 - The Wilderness - Yume Nikki
            8:42 - Forest Pier - Yume 2kki
            9:26 - Shield-Folk World - Yume Nikki
            10:10 - The Mall (Stairwell) - Yume Nikki
            11:13 - Red Rock Caves - Yume 2kki
            12:42 - Dense Woods B - Yume Nikki
            13:29 - The Wilderness (Stairway to the Sky) - Yume Nikki
            14:56 - Fairy Tale Woods (Apple House) - Yume 2kki
            16:30 - Bug Maze - Yume 2kki
            17:35 - The Ceiling (Reversed) - Yume 2kki
            19:28 - Blue Forest - Yume 2kki
            20:17 - Magnet Room - Yume 2kki
            21:16 - The Sky Garden - Yume Nikki
            22:09 - Pink Sea (Poniko's Room, lights on) - Yume Nikki
            23:05 - Pink Sea (Poniko's Room, lights out) - Yume Nikki
            24:02 - Track 335 A* - Yume 2kki
            25:19 - Industrial Towers - Yume 2kki
            26:45 - Realistic Beach - Yume 2kki
            28:38 - Barracks Settlement - Yume Nikki
            29:45 - The Ghost World - Yume Nikki
            31:22 - The Underground World - Yume Nikki
            32:30 - Windmill World - Yume Nikki
            33:04 - The Underground World (Blazing Corridor) - Yume Nikki
            33:46 - Lotus Waters - Yume 2kki
            36:10 - GALAXY Town (The Balcony) - Yume 2kki (0.105f and older)
            37:22 - Grass World (Vine Corridor) - Yume 2kki
            38:53 - Mushroom World - Yume 2kki
            40:23 - Forest World - Yume Nikki
            42:30 - Puddle World - Yume Nikki
            43:23 - Main Menu - Yume Nikki
            44:23 - White Fern World - Yume 2kki
            46:00 - Apartments - Yume 2kki
            47:13 - Dark Room - Yume 2kki
            47:57 - Dark World - Yume Nikki
            48:53 - Mars - Yume Nikki
            50:41 - The Deciding Street - Yume 2kki
            52:13 - Pink Sea - Yume Nikki
            53:17 - Sand Desert Land - Yume 2kki
            54:15 - Window Room - Yume 2kki
            55:45 - Rainbow Silhouette World - Yume 2kki
            56:56 - Highway - Yume 2kki
            58:31 - Forest World - Yume 2kki
            1:00:31 - The Hand Hub - Yume 2kki
            1:01:56 - Block World (Bed Event) - Yume Nikki (0.06)
            1:03:03 - Botanical Garden - Yume 2kki
            1:04:23 - Mars (Martian Underground) - Yume Nikki
            1:05:25 - Number World - Yume Nikki
            1:07:15 - Dense Woods A - Yume Nikki
            1:08:18 - Candle World - Yume Nikki
            1:09:29 - The Checkered Tile Path - Yume Nikki
            1:10:14 - Witch Island - Yume Nikki
            1:12:33 - Ending - Yume Nikki
            1:15:52 - Save Theme - Yume Nikki
            1:19:22 - White Desert - Yume Nikki
    """
    ),
    MusicInfo(
        path_friendly('Yume Nikki Fangames Sleep Mix Naked Flames'),
        'https://www.youtube.com/watch?v=hnKpn7iPW6Y',
        '1:01:54',
        """
            0:00 midnight_90BPM (Broken Bottles)
            2:30 drop (yume graffiti)
            4:06 green (yume graffiti)
            5:35 lake_a (yume graffiti)
            7:52 water (yume graffiti)
            10:10 strange plants world (yume 2kki)
            12:05 loop6 (yume nyaki)
            14:09 Colored Tree Area (Me)
            15:29 spookiebox (yume nyaki)
            17:20 joshua (presence of music)
            19:58 vacant eyes (presence of music)
            21:55 outlander_1 (yume nyaki)
            23:46 soundtest (yume graffiti)
            25:25 back / underground facility (yuque)
            26:57 concave / sewers A (yuque)
            27:30 depth / pool (yuque)
            29:15 iced (yuque)
            31:35 mint / apartment complex (yuque)
            32:40 dream room (yuque)
            33:50 pattern_4 (yume nyaki)
            36:05 monochrome spirals / red bathroom (yuque)
            37:30 sandbar world (yuque)
            39:40 station / metro station (yuque)
            43:35 save theme (yuque)
            45:03 quicksand world (yuque)
            53:29 title theme (yuque)
            56:50 BGM003_Fror / Flooring world (.B.P.)
            01:00:51 loop3 (yume nyaki)
     """
    ),
    MusicInfo(
        path_friendly('yume 2kki ost - sleep mix lavender hearts'),
        'https://www.youtube.com/watch?v=ChaoIMuN_9g',
        '1:19:28',
        """
            0:00 red sky cliff
            5:35 depths
            13:07 the ceiling (reversed)
            23:48 decrepit dwellings (hidden forest)
            29:47 chaotic buildings
            38:01 butterfly forest (green butterfly)
            42:26 dream planet (mars)
            48:55 overgrown city (deeper section)
            54:56 circus in the forest
            1:01:15 rainbow silhouette world
            1:05:45 aquarium (overgrown city)
            1:08:04 blue forest
            1:11:35 antiquated resthouse
     """
    ),
    MusicInfo(
        path_friendly('Yume 2kki ~ Dream Exploration'),
        'https://www.youtube.com/watch?v=-gtQuKQVknk',
        '3:38:49',
        """
            0:00 - Lotus Waters
            6:51 - The Ceiling (Reversed)
            12:06 - The Ceiling
            14:58 - Bleak Future (Prelude)
            15:45 - Bleak Future
            17:38 - Mosenite
            18:36 - Radiant Ruins
            21:48 - Grass World Studio
            24:43 - Grass World
            26:47 - Dark Forest
            27:45 - Forest Pier
            30:16 - Grass World (Pond)
            32:00 - Forgotten Megalopolis (Lower Section)
            42:00 - Piano Alley
            45:25 - Dark Museum
            47:13 - Baddies Bar
            48:13 - Abandoned Apartments
            51:07 - Depths (Ocean Floor)
            54:51 - Dream of Roses (Rose Path Event)
            56:38 - Aquarium (Overgrown City)
            1:01:05 - Pinwheel Bridge (+ Alt. ver.)
            1:05:00 - Ocean Floor
            1:06:50 - Cog Maze
            1:08:34 - Cocktail Lounge
            1:14:21 - Lotus Park
            1:16:04 - Lavender Waters
            1:20:05 - Meri- Library
            1:22:07 - Save Theme
            1:24:21 - Botanical Garden
            1:26:27 - Floating Catacombs (Mushroom Room)
            1:28:27 - Pink Tanuki Road
            1:29:30 - Piano Flourish
            1:32:24 - Splash Streetway
            1:33:34 - Red Cliff
            1:34:59 - Galactic Park Bridge
            1:37:54 - Graffiti Maze (Tree)
            1:38:45 - Flying Fish World
            1:40:25 - Evergreen Woods
            1:42:19 - Grass World (Vine Corridor)
            1:43:59 - Green Neon World
            1:47:08 - Red Lily Lake
            1:49:18 - Star Ocean
            1:51:31 - Lotus Waters (again)
            1:55:48 - Lavender Waters (again, I love these songs)
            1:59:50 - Rooftop
            2:03:40 - Overgrown City (Deeper Section)
            2:05:24 - Ether Caverns
            2:07:25 - Deserted Pier
            2:09:11 - Depths
            2:11:43 - Depths (Ocean Floor)
            2:15:12 - Snowy Village (Uninhabited House)
            2:17:22 - Day & Night Towers
            2:18:46 - Cloud Tops (Night)
            2:21:04 - Forgotten Megalopolis (Lower Section)
            2:23:13 - Alley Robot Room
            2:26:09 - Black Building
            2:27:15 - Black Cat
            2:28:53 - End/Save Theme (Music Box)
            2:31:03 - Bottom Garden
            2:33:07 - Jade Sky Hamlet
            2:35:10 - Blue Forest
            2:37:06 - Carnival Town (Victorian Drains)
            2:38:55 - Chaotic Buildings
            2:40:38 - Hidden Shoal
            2:42:10 - Starry Night Event
            2:43:04 - Starfield Garden
            2:43:52 - Blue Cactus Islands
            2:45:39 - Rainbow Silhouette World
            2:47:24 - Bridged Swamp Islands
            2:49:17 - Cutlery World
            2:51:31 - Green Butterfly Forest
            2:54:19 - Dojo (Space)
            2:56:30 - City Limits
            3:00:17 - Tree of Life
            3:02:15 - White Tree from Pencil World
            3:04:29 - Sea Sponge Path
            3:05:53 - Grey Road
            3:07:49 - Highway (Limits)
            3:11:06 - Seagull
            3:13:39 - Overgrown City (House Section)
            3:15:18 - Portrait Purgatory
            3:16:02 - Farm World
            3:16:48 - Broken City Playground
            3:17:47 - Abandoned Apartments (Lower Section)
            3:20:42 - Tomb of Velleties
            3:26:15 - Nocturnal Grove
            3:31:23 - Tomb of Velleties (Lunar Sanctuary)
     """
    ),
    MusicInfo(
        path_friendly('Deus Ex 2000 Full OST'),
        'https://www.youtube.com/watch?v=JhjkBE3d3Uw',
        '5:06:35',
        """
            0:00 Main Title
            2:25 Intro Sequence
            4:43 Training Room
            6:48 Liberty Island
            11:24 Liberty Island Conversation
            13:37 Liberty Island Action
            16:14 Liberty Island Death
            17:35 UNATCO
            20:03 UNATCO Conversation
            22:31 UNATCO Action
            25:49 UNATCO Death
            26:16 Leaving Liberty Island
            27:14 Battery Park
            30:44 Battery Park Conversation
            32:56 Battery Park Action
            35:17 Battery Park Death
            36:29 NYC Streets
            41:05 NYC Conversation
            43:18 NYC Action
            45:17 NYC Death
            45:40 Underworld Tavern
            51:01 Underworld Tavern Action
            51:24 Lebedev's Airfield
            54:24 Airfield Conversation
            55:37 Airfield Action
            57:31 Airfield Death
            58:02 Leaving Lebedev's Airfield
            58:40 Gunther Hermann Arrests JC
            59:14 Majestic 12 Labs
            1:02:44 Majestic 12 Conversation
            1:04:54 Majestic 12 Action
            1:07:39 Majestic 12 Death
            1:08:10 Enemy Within (UNATCO Escape)
            1:12:02 UNATCO Escape Conversation
            1:14:15 UNATCO Escape Action
            1:17:20 UNATCO Escape Death
            1:17:45 Hong Kong Helipad
            1:20:20 Helipad Action
            1:22:37 Helipad Death
            1:23:08 The Synapse (Hong Kong Streets)
            1:27:31 Hong Kong Conversation
            1:29:34 Hong Kong Action
            1:31:34 Hong Kong Death
            1:32:02 Desolation (Hong Kong Canal)
            1:34:25 Hong Kong Canal Conversation
            1:35:36 Hong Kong Canal Action
            1:37:19 Hong Kong Canal Death
            1:37:42 Lucky Money Club 1
            1:40:10 Lucky Money Club Action 1
            1:40:31 Lucky Money Club 2
            1:43:38 Lucky Money Club Action 2
            1:43:58 VersaLife
            1:47:04 VersaLife Conversation
            1:49:34 VersaLife Action
            1:51:57 VersaLife Death
            1:52:24 Leaving Hong Kong
            1:52:51 Return to NYC
            1:56:03 NYC Return Conversation
            1:56:56 NYC Return Action
            1:58:15 NYC Return Death
            1:58:34 To The Naval Base
            1:59:31 Naval Base
            2:03:05 Naval Base Conversation
            2:05:37 Naval Base Action
            2:06:47 Naval Base Death
            2:07:22 Paris Streets
            2:08:41 La Porte de l'Enfer 1
            2:11:41 La Porte de l'Enfer Action 1
            2:11:56 La Porte de l'Enfer 2
            2:16:38 La Porte de l'Enfer Action 2
            2:17:00 Evading Gunther Herman
            2:18:20 DuClare Château
            2:21:21 Château Conversation
            2:22:40 Château Action
            2:25:30 Château Death
            2:26:01 Paris Cathedral
            2:29:47 Paris Cathedral Conversation
            2:30:42 Paris Cathedral Action
            2:33:17 Paris Cathedral Death
            2:34:22 Vandenberg
            2:37:31 Vandenberg Conversation
            2:39:39 Vandenberg Action
            2:41:37 Vandenberg Death
            2:42:04 The Nothing (Tunnel)
            2:45:24 Tunnel Action
            2:47:32 Tunnel Death
            2:48:08 Leaving Vandenberg
            2:48:39 Nauticus (Oceanlab)
            2:51:48 Ocean Conversation
            2:53:46 Ocean Action
            2:56:34 Ocean Death
            2:56:54 Oceanlab Complex
            3:00:34 Ocean Complex Conversation
            3:02:01 Ocean Complex Action
            3:04:10 Ocean Complex Death
            3:05:22 Leaving the Oceanlab
            3:05:45 Begin the End (Bunker)
            3:09:33 Bunker Conversation
            3:10:16 Bunker Action
            3:12:53 Bunker Death
            3:13:19 Area 51
            3:17:46 Area 51 Conversation
            3:19:36 Area 51 Action
            3:21:37 Area 51 Death
            3:22:04 Dark Age Ending
            3:23:22 Helios Ending
            3:24:43 Illuminati Ending
            3:26:35 The Illuminati
            3:29:14 DX Club Mix
            3:32:15 Conspiravision
            3:38:03 Main Title (Album Version)
            3:40:30 UNATCO Conversation (Intro)
            3:41:10 UNATCO Conversation (Extended)
            3:45:10 Battery Park Conversation (Extended)
            3:48:17 Underworld Tavern (Alternate)
            3:50:32 Majestic 12 Labs (Unused)
            3:52:45 UNATCO Escape (Unused)
            3:53:24 Helipad Conversation (Unused)
            3:55:37 Naval Base (Unused)
            3:57:49 Tunnel Conversation (Unused)
            3:59:42 Area 51 (Unused)
            4:01:14 Dark Age Ending (Album Version)
            4:02:29 Main Title (Conspiracy Version)
            4:04:56 The God Machine [Vig]
            4:11:19 Distortion HQ [Nutritious]
            4:14:42 The Search for Ambrosia [zircon & Jillian Aversa]
            4:19:44 Neonature [nervous_testpilot]
            4:25:44 MachiNation [Alexander Brandon]
            4:28:20 Sadevakio [Eino Keskitalo]
            4:33:47 Human Soldier [halc]
            4:37:48 Augmented UNATCO [VideoGameManiac]
            4:46:01 UNATCO (Jared Burgin Remix)
            4:49:07 UNATCO Theme (Vieon Remix)
            4:52:32 Siren Synapse [Alexander Brandon & Jimmy Hinson]
            4:56:56 Endless Night [Technomancer]
            5:01:45 Ma Chérie Nicolette [Alexander Brandon & Jimmy Hinson]
     """
    ),
]

# MusicInfo(
# path_friendly(    ''),
#     '',
#     '',
#     """
#
#     """
# ),


class TrackInfo(NamedTuple):
    name: str
    start: str
    end: str


def parse_timestamps(timestamps: str, end_time: str) -> list[TrackInfo]:

    def looks_like_time(s: str) -> bool:
        import re
        regex = r'^(?:[0-9]+:)?(?:[0-5]?[0-9]):(?:[0-5]?[0-9])$'
        return re.match(regex, s)

    forbidden_parts = ['.']
    times = []
    titles = []
    lines = timestamps.strip().splitlines()
    number = 0
    for line in lines:
        parts = line.strip().split()
        time = list(filter(lambda x: looks_like_time(x), parts))
        assert len(time) == 1, print(time, line)
        time = time[0]
        parts.remove(time)
        parts = list(filter(lambda x: not any(
            p in x for p in forbidden_parts), parts))

        assert len(parts) != 0, line
        n = "{:03d}".format(number)
        number += 1
        titles.append(n + ' ' + ' '.join(parts))
        times.append(time)

    time_pairs = zip(titles, times, (times + [end_time])[1:])
    return [TrackInfo(path_friendly(title), start, end)
            for title, start, end in time_pairs]


def downloader_cmd(config: list[str], out_path: str, url: str) -> list[str]:
    return ['./yt-dlp', *config, '-o', out_path, url]


def ffmpeg_cmd(in_name: str,
               from_time: str,
               to_time: str,
               out_name: str) -> list[str]:
    return ['ffmpeg', '-i', in_name,
            '-ss', from_time, '-to', to_time,
            '-c', 'copy',
            out_name]


def create_stubs_to_ignore():
    for track in music:
        path = c.OUT_DIR + os.sep + track.title
        if not os.path.exists(path):
            os.mkdir(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="""
    Script downloads music from youtube via yt-dlp and
    splits it into pieces by provided timestamps

    Some arguments must be provided
    """
    )
    parser.add_argument(
        '-c',
        '--convert',
        help="Start convertion for files that haven't been converted yet",
        action='store_true'
    )
    parser.add_argument(
        '-d',
        '--download',
        help=f"Start track download into {c.TMP_DIR}",
        action='store_true'
    )
    parser.add_argument(
        '-s',
        '--create-stubs',
        help="Create stubs for all tracks listed in the script to skip them",
        action='store_true'
    )
    args = parser.parse_args()
    if not any(val for key, val in vars(args).items()):
        parser.print_help()
        exit(-1)

    logging.basicConfig(level=logging.DEBUG)
    if args.create_stubs:
        create_stubs_to_ignore()
    for track in music:
        title = track.title
        track_path = c.TMP_DIR + os.sep + title + '.opus'
        out_dir = c.OUT_DIR + os.sep + title

        if args.download:
            if not os.path.exists(track_path) and not os.path.exists(out_dir):
                if track.url != c.NO_URL:
                    subprocess.run(
                        downloader_cmd(
                            CONFIG_BIG_VIDEO,
                            c.TMP_DIR + os.sep + title,
                            track.url))
            else:
                logging.debug(f'Skipping for loading {title}')

        if args.convert:
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
                for track_info in parse_timestamps(
                        track.timestamps, track.end_time):
                    out = out_dir + os.sep + track_info.name + '.opus'
                    subprocess.run(ffmpeg_cmd(
                        track_path,
                        track_info.start,
                        track_info.end,
                        out,
                    ))
                os.remove(track_path)
            else:
                logging.debug(f'Skipping for convertion {title}')
