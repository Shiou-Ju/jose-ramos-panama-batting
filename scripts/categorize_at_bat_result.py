def categorize_at_bat_result(result):
    if '_' in result :
        return '安打'
    elif result in ['DB', 'BB']:
        return '保送'
    elif result.endswith('F'):
        return '飛球'
    elif result.endswith('G'):
        return '滾地球'
    elif 'K' in result:
        return '三振'
    else:
        return '其他'
