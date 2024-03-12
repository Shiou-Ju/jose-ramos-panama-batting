
## 專案欄位資料

### pitches_df_cleaned.columns
```
Index(['id', 'abs_id', 'nth_pitch_ab', 'out_count', 'strike_count',
       'ball_count', 'is_rhp', 'has_stealing_attempt', 'pitch_type',
       'pitch_release', 'is_obvious_off_zone', 'is_pitch_ended_catcher_want',
       'has_swing', 'has_first_base_runner', 'has_second_base_runner',
       'has_third_base_runner', 'has_visible_shift', 'score_diffrence',
       'is_team_leading', 'has_swing_intention', 'horizontal_ending',
       'vertical_ending', 'is_swing_delayed', 'is_swing_early', 'is_whiff'],
      dtype='object')

```

### abs_df.columns
```
      Index(['abs_id', 'file_name', 'file_name_date', 'file_name_player_name',
       'file_name_pitcher_type', 'file_name_at_bat_number', 'file_name_result',
       'is_filename_result_consistent', 'inning', 'at_bat_result', 'weather',
       'game_time'],
      dtype='object')
```

      

## 打擊數據
### 滾飛比
```
{\displaystyle GO/AO={\frac {GO}{AO}}}
```
- GO：滾地球出局(Ground Outs)
- AO：飛球出局(Fly Outs)
- G：滾地球(Ground ball)
- F：飛球(Fly ball)


### AVG(或BA) 打擊率

英文：Batting Average

```

{\displaystyle \ AVG={\frac {H}{AB}}}
```


### OBP 上壘率
英文：On Base Percentage
```
�
{\displaystyle \ OBP={\frac {H+BB+HBP}{AB+BB+HBP+SF}}} 備註: IBB 早已包含在 BB 中, 切記不要重複計算
```


### TB 壘打數
英文：Total Bases On Safe Hits
 
```
{\displaystyle \ TB=1\times 1B+2\times 2B+3\times 3B+4\times HR}
```

### SLG 長打率
英文：Slugging percentage
```
{\displaystyle \ SLG={\frac {TB}{AB}}}
```


