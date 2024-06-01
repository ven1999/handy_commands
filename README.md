- Отрезать 30 секунд видео
```bash
ffmpeg -i !.! -ss 00:00:00 -t 00:00:30 -c copy !_first_30_sec.mp4
```

- Вшить soft субтитры
```bash
ffmpeg -i "!.!" -i "!.srt" -c:s mov_text -metadata:s:s:0 language=eng "!_srt.mp4"
```

- Вшить hard субтитры
```bash
ffmpeg -i "!.!" -vf subtitles="!.srt" "!_srt.mp4"
```

- Порезать видео кусками по 900 секунд
```bash
ffmpeg -i "!.!" -f segment -segment_time 900 -acodec libmp3lame -ar 44100 -ab 128k -vn -y "!_%03d.mp3"
```
