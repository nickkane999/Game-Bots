import easyocr



reader = easyocr.Reader(['en'], gpu=False)
reader.readtext('test.png')
#easyocr -l ch_sim en -f firestone_progress_temp.png --detail=1 --gpu=True
