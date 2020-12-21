config = { 'rank':'123', 'dilation_rate': '456', 'other':'678'}

rank_del = False
dilation_del = False
for key in config.keys():
    if key == 'rank':
        rank_del = True
    elif key == 'dilation_rate':
        dilation_del = True

if rank_del == True:
    config.pop('rank')

if dilation_del == True:
    config.pop('dilation_rate')

print(config)