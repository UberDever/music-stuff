import subprocess
from typing import NamedTuple
import logging
import os
import constants as c

CONFIG_BIG_VIDEO = [
    '-x',
    '--no-overwrites',
]


class MusicInfo(NamedTuple):
    title: str
    url: str
    end_time: str
    timestamps: str


music = [
    MusicInfo(
        'Peaceful Jeremy Soule #1',
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
        'Hotline Miami Soundtrack',
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
    )
]


class TrackInfo(NamedTuple):
    name: str
    start: str
    end: str


def parse_timestamps(timestamps: str, end_time: str) -> list[TrackInfo]:

    def looks_like_time(s: str) -> bool:
        import re
        regex = r'^(?:(?:[0-9]|1[0-9]|2[0-3]):)?(?:[0-5]?[0-9]):(?:[0-5]?[0-9])$'
        return re.match(regex, s)

    forbidden_parts = ['.']
    times = []
    titles = []
    lines = timestamps.strip().splitlines()
    for line in lines:
        parts = line.strip().split()
        time = list(filter(lambda x: looks_like_time(x), parts))
        assert len(time) == 1, line
        time = time[0]
        parts.remove(time)
        parts = list(filter(lambda x: not any(
            p in x for p in forbidden_parts), parts))

        titles.append(' '.join(parts))
        times.append(time)

    assert (len(times) +
            1) % 2 == 0, f'Non even number of timestamps {len(times)}'
    time_pairs = zip(titles, times, (times + [end_time])[1:])
    return [TrackInfo(title, start, end) for title, start, end in time_pairs]


def downloader_cmd(config: list[str], out_path: str, url: str) -> list[str]:
    return ['./yt-dlp', *config, '-o', out_path, url]


def ffmpeg_cmd(in_name: str,
               from_time: str,
               to_time: str,
               out_name: str) -> list[str]:
    return ['ffmpeg', '-i', in_name, '-ss', from_time, '-to', to_time, out_name]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for track in music:
        track_path = c.TMP_DIR + os.sep + track.title + '.opus'
        out_dir = c.OUT_DIR + os.sep + track.title
        if not os.path.exists(track_path) and not os.path.exists(out_dir):
            subprocess.run(downloader_cmd(
                CONFIG_BIG_VIDEO, c.TMP_DIR + os.sep + track.title, track.url))
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
            for track_info in parse_timestamps(track.timestamps, track.end_time):
                subprocess.run(ffmpeg_cmd(
                    track_path,
                    track_info.start,
                    track_info.end,
                    out_dir + os.sep + track_info.name + '.opus',
                ))
            os.remove(track_path)
        logging.debug(f'Skipping {track.title}')
