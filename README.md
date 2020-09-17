## Usage

記録開始時

`-s タスク名 見積もり時間[分]`

```
$ python3 logger.py -s 朝ごはんを食べる 40
```

記録終了

```
$ python3 logger.py -e
```

## Log

ログはlog.csvに記録されます．

|列名|説明|
|---|---|
|`time`| 開始・終了時刻|
|`est-real`| 見積もり時間[分] か 作業時間[分]|
|`event`| `start` か `end`|
|`title`| 作業内容をかいてね |


## その他

csvが文字化けするかもしれないのでGoogle Spreadsheet使ったりしほうが良いかも

---


~~pythonなんもわからん~~